import warnings

import numpy as np
import pandas as pd
from tlz import partition

from ._compat import PANDAS_GT_131

#  preserve compatibility while moving dispatch objects
from .dispatch import (  # noqa: F401
    concat,
    concat_dispatch,
    group_split_dispatch,
    hash_object_dispatch,
    is_categorical_dtype,
    is_categorical_dtype_dispatch,
    tolist,
    tolist_dispatch,
    union_categoricals,
)
from .utils import is_dataframe_like, is_index_like, is_series_like

# cuDF may try to import old dispatch functions
hash_df = hash_object_dispatch
group_split = group_split_dispatch

# ---------------------------------
# indexing
# ---------------------------------


def loc(df, iindexer, cindexer=None):
    """
    .loc for known divisions
    """
    if cindexer is None:
        return df.loc[iindexer]
    else:
        return df.loc[iindexer, cindexer]


def iloc(df, cindexer=None):
    return df.iloc[:, cindexer]


def try_loc(df, iindexer, cindexer=None):
    """
    .loc for unknown divisions
    """
    try:
        return loc(df, iindexer, cindexer)
    except KeyError:
        return df.head(0).loc[:, cindexer]


def boundary_slice(df, start, stop, right_boundary=True, left_boundary=True, kind=None):
    """Index slice start/stop. Can switch include/exclude boundaries.

    Examples
    --------
    >>> df = pd.DataFrame({'x': [10, 20, 30, 40, 50]}, index=[1, 2, 2, 3, 4])
    >>> boundary_slice(df, 2, None)
        x
    2  20
    2  30
    3  40
    4  50
    >>> boundary_slice(df, 1, 3)
        x
    1  10
    2  20
    2  30
    3  40
    >>> boundary_slice(df, 1, 3, right_boundary=False)
        x
    1  10
    2  20
    2  30

    Empty input DataFrames are returned

    >>> df_empty = pd.DataFrame()
    >>> boundary_slice(df_empty, 1, 3)
    Empty DataFrame
    Columns: []
    Index: []
    """
    if len(df.index) == 0:
        return df

    if PANDAS_GT_131:
        if kind is not None:
            warnings.warn(
                "The `kind` argument is no longer used/supported. "
                "It will be dropped in a future release.",
                category=FutureWarning,
            )
        kind_opts = {}
        kind = "loc"
    else:
        kind = kind or "loc"
        kind_opts = {"kind": kind}

    if kind == "loc" and not df.index.is_monotonic:
        # Pandas treats missing keys differently for label-slicing
        # on monotonic vs. non-monotonic indexes
        # If the index is monotonic, `df.loc[start:stop]` is fine.
        # If it's not, `df.loc[start:stop]` raises when `start` is missing
        if start is not None:
            if left_boundary:
                df = df[df.index >= start]
            else:
                df = df[df.index > start]
        if stop is not None:
            if right_boundary:
                df = df[df.index <= stop]
            else:
                df = df[df.index < stop]
        return df

    result = getattr(df, kind)[start:stop]
    if not right_boundary and stop is not None:
        right_index = result.index.get_slice_bound(stop, "left", **kind_opts)
        result = result.iloc[:right_index]
    if not left_boundary and start is not None:
        left_index = result.index.get_slice_bound(start, "right", **kind_opts)
        result = result.iloc[left_index:]
    return result


def index_count(x):
    # Workaround since Index doesn't implement `.count`
    return pd.notnull(x).sum()


def mean_aggregate(s, n):
    try:
        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            return s / n
    except ZeroDivisionError:
        return np.float64(np.nan)


def wrap_var_reduction(array_var, index):
    if isinstance(array_var, np.ndarray) or isinstance(array_var, list):
        return pd.Series(array_var, index=index)

    return array_var


def wrap_skew_reduction(array_skew, index):
    if isinstance(array_skew, np.ndarray) or isinstance(array_skew, list):
        return pd.Series(array_skew, index=index)

    return array_skew


def wrap_kurtosis_reduction(array_kurtosis, index):
    if isinstance(array_kurtosis, np.ndarray) or isinstance(array_kurtosis, list):
        return pd.Series(array_kurtosis, index=index)

    return array_kurtosis


def var_mixed_concat(numeric_var, timedelta_var, columns):
    vars = pd.concat([numeric_var, timedelta_var])

    return vars.reindex(index=columns)


def describe_aggregate(values):
    assert len(values) > 0

    # arrange categorical and numeric stats
    names = []
    values_indexes = sorted((x.index for x in values), key=len)
    for idxnames in values_indexes:
        for name in idxnames:
            if name not in names:
                names.append(name)

    return pd.concat(values, axis=1, sort=False).reindex(names)


def describe_numeric_aggregate(
    stats, name=None, is_timedelta_col=False, is_datetime_col=False
):
    assert len(stats) == 6
    count, mean, std, min, q, max = stats

    if is_series_like(count):
        typ = type(count.to_frame())
    else:
        typ = type(q)

    if is_timedelta_col:
        mean = pd.to_timedelta(mean)
        std = pd.to_timedelta(std)
        min = pd.to_timedelta(min)
        max = pd.to_timedelta(max)
        q = q.apply(lambda x: pd.to_timedelta(x))

    if is_datetime_col:
        # mean is not implemented for datetime
        min = pd.to_datetime(min)
        max = pd.to_datetime(max)
        q = q.apply(lambda x: pd.to_datetime(x))

    if is_datetime_col:
        part1 = typ([count, min], index=["count", "min"])
    else:
        part1 = typ([count, mean, std, min], index=["count", "mean", "std", "min"])

    q.index = [f"{l * 100:g}%" for l in tolist(q.index)]
    if is_series_like(q) and typ != type(q):
        q = q.to_frame()
    part3 = typ([max], index=["max"])

    result = concat([part1, q, part3], sort=False)

    if is_series_like(result):
        result.name = name

    return result


def describe_nonnumeric_aggregate(stats, name):
    args_len = len(stats)

    is_datetime_column = args_len == 5
    is_categorical_column = args_len == 3

    assert is_datetime_column or is_categorical_column

    if is_categorical_column:
        nunique, count, top_freq = stats
    else:
        nunique, count, top_freq, min_ts, max_ts = stats

    # input was empty dataframe/series
    if len(top_freq) == 0:
        data = [0, 0]
        index = ["count", "unique"]
        dtype = None
        data.extend([None, None])
        index.extend(["top", "freq"])
        dtype = object
        result = pd.Series(data, index=index, dtype=dtype, name=name)
        return result

    top = top_freq.index[0]
    freq = top_freq.iloc[0]

    index = ["unique", "count", "top", "freq"]
    values = [nunique, count]

    if is_datetime_column:
        tz = top.tz
        top = pd.Timestamp(top)
        if top.tzinfo is not None and tz is not None:
            # Don't tz_localize(None) if key is already tz-aware
            top = top.tz_convert(tz)
        else:
            top = top.tz_localize(tz)

        first = pd.Timestamp(min_ts, tz=tz)
        last = pd.Timestamp(max_ts, tz=tz)
        index.extend(["first", "last"])
        values.extend([top, freq, first, last])
    else:
        values.extend([top, freq])

    return pd.Series(values, index=index, name=name)


def _cum_aggregate_apply(aggregate, x, y):
    """Apply aggregation function within a cumulative aggregation

    Parameters
    ----------
    aggregate: function (a, a) -> a
        The aggregation function, like add, which is used to and subsequent
        results
    x:
    y:
    """
    if y is None:
        return x
    else:
        return aggregate(x, y)


def cumsum_aggregate(x, y):
    if x is None:
        return y
    elif y is None:
        return x
    else:
        return x + y


def cumprod_aggregate(x, y):
    if x is None:
        return y
    elif y is None:
        return x
    else:
        return x * y


def cummin_aggregate(x, y):
    if is_series_like(x) or is_dataframe_like(x):
        return x.where((x < y) | x.isnull(), y, axis=x.ndim - 1)
    else:  # scalar
        return x if x < y else y


def cummax_aggregate(x, y):
    if is_series_like(x) or is_dataframe_like(x):
        return x.where((x > y) | x.isnull(), y, axis=x.ndim - 1)
    else:  # scalar
        return x if x > y else y


def assign(df, *pairs):
    # Only deep copy when updating an element
    # (to avoid modifying the original)
    pairs = dict(partition(2, pairs))
    deep = bool(set(pairs) & set(df.columns))
    df = df.copy(deep=bool(deep))
    for name, val in pairs.items():
        df[name] = val
    return df


def unique(x, series_name=None):
    out = x.unique()
    # out can be either an np.ndarray or may already be a series
    # like object.  When out is an np.ndarray, it must be wrapped.
    if not (is_series_like(out) or is_index_like(out)):
        out = pd.Series(out, name=series_name)
    return out


def value_counts_combine(x, sort=True, ascending=False, **groupby_kwargs):
    # sort and ascending don't actually matter until the agg step
    return x.groupby(level=0, **groupby_kwargs).sum()


def value_counts_aggregate(
    x, sort=True, ascending=False, normalize=False, total_length=None, **groupby_kwargs
):
    out = value_counts_combine(x, **groupby_kwargs)
    if normalize:
        out /= total_length if total_length is not None else out.sum()
    if sort:
        return out.sort_values(ascending=ascending)
    return out


def nbytes(x):
    return x.nbytes


def size(x):
    return x.size


def values(df):
    return df.values


def sample(df, state, frac, replace):
    rs = np.random.RandomState(state)
    return df.sample(random_state=rs, frac=frac, replace=replace) if len(df) > 0 else df


def drop_columns(df, columns, dtype):
    df = df.drop(columns, axis=1)
    df.columns = df.columns.astype(dtype)
    return df


def fillna_check(df, method, check=True):
    out = df.fillna(method=method)
    if check and out.isnull().values.all(axis=0).any():
        raise ValueError(
            "All NaN partition encountered in `fillna`. Try "
            "using ``df.repartition`` to increase the partition "
            "size, or specify `limit` in `fillna`."
        )
    return out


# ---------------------------------
# reshape
# ---------------------------------


def pivot_agg(df):
    return df.groupby(level=0).sum()


def pivot_sum(df, index, columns, values):
    return pd.pivot_table(
        df, index=index, columns=columns, values=values, aggfunc="sum", dropna=False
    )


def pivot_count(df, index, columns, values):
    # we cannot determine dtype until concatenationg all partitions.
    # make dtype deterministic, always coerce to np.float64
    return pd.pivot_table(
        df, index=index, columns=columns, values=values, aggfunc="count", dropna=False
    ).astype(np.float64)


def assign_index(df, ind):
    df = df.copy()
    df.index = ind
    return df


def monotonic_increasing_chunk(x):
    data = x if is_index_like(x) else x.iloc
    return pd.DataFrame(
        data=[[x.is_monotonic_increasing, data[0], data[-1]]],
        columns=["monotonic", "first", "last"],
    )


def monotonic_increasing_aggregate(concatenated):
    bounds_are_monotonic = pd.Series(
        concatenated[["first", "last"]].to_numpy().ravel()
    ).is_monotonic_increasing
    return concatenated["monotonic"].all() and bounds_are_monotonic


def monotonic_decreasing_chunk(x):
    data = x if is_index_like(x) else x.iloc
    return pd.DataFrame(
        data=[[x.is_monotonic_decreasing, data[0], data[-1]]],
        columns=["monotonic", "first", "last"],
    )


def monotonic_decreasing_aggregate(concatenated):
    bounds_are_monotonic = pd.Series(
        concatenated[["first", "last"]].to_numpy().ravel()
    ).is_monotonic_decreasing
    return concatenated["monotonic"].all() and bounds_are_monotonic
