# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Scatter(Component):
    """A Scatter component.


Keyword arguments:

- allColOptions (optional):
    All currently available column options.

- catColOptions (optional):
    Currently available categorical options.

- config (optional):
    The config the user sets in this component.

- numColOptions (optional):
    Currently available numerical options.

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes to Dash, to make them available for callbacks."""
    @_explicitize_args
    def __init__(self, config=Component.UNDEFINED, allColOptions=Component.UNDEFINED, catColOptions=Component.UNDEFINED, numColOptions=Component.UNDEFINED, **kwargs):
        self._prop_names = ['allColOptions', 'catColOptions', 'config', 'numColOptions', 'setProps']
        self._type = 'Scatter'
        self._namespace = 'dash_express_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['allColOptions', 'catColOptions', 'config', 'numColOptions', 'setProps']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Scatter, self).__init__(**args)
