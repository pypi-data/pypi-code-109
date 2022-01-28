"""Defining the public API for any converter class."""

import abc
import typing

from mutwoext_core import constants as core_constants
from mutwoext_core import events as core_events

__all__ = ("Converter", "EventConverter", "SymmetricalEventConverter")


class Converter(abc.ABC):
    """Abstract base class for all Converter classes.

    Converter classes are defined as classes that convert data between
    two different encodings. Their only public method (besides initialisation)
    should be a `convert` method. The first argument of the convert method
    should be the data to convert.
    """

    @abc.abstractmethod
    def convert(
        self, event_or_parameter_or_file_to_convert: typing.Any, *args, **kwargs
    ) -> typing.Any:
        raise NotImplementedError


class EventConverter(Converter):
    """Abstract base class for Converter which handle mutwo core_events.

    This class helps building new classes which convert mutwo core_events
    with few general private methods (and without adding any new public
    method). Converting mutwo event often involves the same pattern:
    due to the nested structure of an Event, the converter has
    to iterate through the different layers until it reaches leaves
    (any class that inherits from :class:`mutwo.core_events.SimpleEvent`).
    This common iteration process and the different time treatment
    between :class:`mutwo.core_events.SequentialEvent` and
    :class:`mutwo.core_events.SimultaneousEvent` are implemented in
    :class:`EventConverter`.  For writing a new EventConverter class,
    one only has to override the abstract method :func:`_convert_simple_event`
    and the abstract method :func:`convert` (where one will perhaps call
    :func:`_convert_event`.).

    **Example:**

    The following example defines a dummy class for demonstrating how
    to use EventConverter.

    >>> from mutwo.converters import abc
    >>> class DurationPrintConverter(abc.EventConverter):
    >>>     def _convert_simple_event(self, event_to_convert, absolute_entry_delay):
    >>>         return "{}: {}".format(absolute_entry_delay, event_to_convert.duration),
    >>>     def convert(self, event_to_convert):
    >>>         data_per_event = self._convert_event(event_to_convert, 0)
    >>>         [print(data) for data in data_per_event]
    >>> # now test with random event
    >>> import random
    >>> from mutwo.core_events import
    >>> random.seed(100)
    >>> random_event =.SimultaneousEvent(
    >>>     [
    >>>        .SequentialEvent(
    >>>             [
    >>>                .SimpleEvent(random.uniform(0.5, 2))
    >>>                 for _ in range(random.randint(2, 5))
    >>>             ]
    >>>         )
    >>>         for _ in range(random.randint(1, 3))
    >>>     ]
    >>> )
    >>> DurationPrintConverter().convert(random_event)
    0: 1.182390506771032
    1.182390506771032: 1.6561757084885333
    2.8385662152595654: 1.558269840401042
    4.396836055660607: 1.5979384595498836
    5.994774515210491: 1.1502716523431056
    """

    @abc.abstractmethod
    def _convert_simple_event(
        self,
        event_to_convert: core_events.SimpleEvent,
        absolute_entry_delay: core_constants.DurationType,
    ) -> typing.Sequence[typing.Any]:
        """Convert instance of :class:`mutwo.core_events.SimpleEvent`."""

        raise NotImplementedError

    def _convert_simultaneous_event(
        self,
        simultaneous_event: core_events.SimultaneousEvent,
        absolute_entry_delay: core_constants.DurationType,
    ) -> typing.Sequence[typing.Any]:
        """Convert instance of :class:`mutwo.core_events.SimultaneousEvent`."""

        data_per_simple_event_list: list[tuple[typing.Any]] = []

        for event in simultaneous_event:
            data_per_simple_event_list.extend(
                self._convert_event(event, absolute_entry_delay)
            )
        return tuple(data_per_simple_event_list)

    def _convert_sequential_event(
        self,
        sequential_event: core_events.SequentialEvent,
        absolute_entry_delay: core_constants.DurationType,
    ) -> typing.Sequence[typing.Any]:
        """Convert instance of :class:`mutwo.core_events.SequentialEvent`."""

        data_per_simple_event_list: list[tuple[typing.Any]] = []
        for event_start, event in zip(
            sequential_event.absolute_time_tuple, sequential_event
        ):
            data_per_simple_event_list.extend(
                self._convert_event(event, event_start + absolute_entry_delay)
            )
        return tuple(data_per_simple_event_list)

    def _convert_event(
        self,
        event_to_convert: core_events.abc.Event,
        absolute_entry_delay: core_constants.DurationType,
    ) -> typing.Any:
        """Convert :class:`mutwo.core_events.abc.Event` of unknown type.

        The method calls different subroutines depending on whether
        the passed event either are instances from:

            1. :class:`mutwo.core_events.SimpleEvent` or
            2. :class:`mutwo.core_events.SequentialEvent` or
            3. :class:`mutwo.core_events.SimultaneousEvent`.
        """

        if isinstance(event_to_convert, core_events.SequentialEvent):
            return self._convert_sequential_event(
                event_to_convert, absolute_entry_delay
            )

        elif isinstance(
            event_to_convert,
            core_events.SimultaneousEvent,
        ):
            return self._convert_simultaneous_event(
                event_to_convert, absolute_entry_delay
            )

        elif isinstance(
            event_to_convert,
            core_events.SimpleEvent,
        ):
            return self._convert_simple_event(event_to_convert, absolute_entry_delay)

        else:
            message = (
                "Can't convert object '{}' of type '{}' with EventConverter.".format(
                    event_to_convert, type(event_to_convert)
                )
            )

            message += " Supported types only include all inherited classes "
            message += "from '{}'.".format(core_events.abc.Event)
            raise TypeError(message)


class SymmetricalEventConverter(EventConverter):
    """Abstract base class for Converter which handle mutwo core_events.

    This converter is a more specified version of the :class:`EventConverter`.
    It helps for building converters which aim to return mutwo core_events.
    """

    @abc.abstractmethod
    def _convert_simple_event(
        self,
        event_to_convert: core_events.SimpleEvent,
        absolute_entry_delay: core_constants.DurationType,
    ) -> core_events.SimpleEvent:
        """Convert instance of :class:`mutwo.core_events.SimpleEvent`."""

        raise NotImplementedError

    def _convert_simultaneous_event(
        self,
        simultaneous_event: core_events.SimultaneousEvent,
        absolute_entry_delay: core_constants.DurationType,
    ) -> core_events.SimultaneousEvent:
        """Convert instance of :class:`mutwo.core_events.SimultaneousEvent`."""

        converted_simultaneous_event: core_events.SimultaneousEvent = (
            simultaneous_event.empty_copy()
        )

        for event in simultaneous_event:
            converted_simultaneous_event.append(
                self._convert_event(event, absolute_entry_delay)
            )
        return converted_simultaneous_event

    def _convert_sequential_event(
        self,
        sequential_event: core_events.SequentialEvent,
        absolute_entry_delay: core_constants.DurationType,
    ) -> core_events.SequentialEvent:
        """Convert instance of :class:`mutwo.core_events.SequentialEvent`."""

        converted_sequential_event: core_events.SequentialEvent = (
            sequential_event.empty_copy()
        )
        for event_start, event in zip(
            sequential_event.absolute_time_tuple, sequential_event
        ):
            converted_sequential_event.append(
                self._convert_event(event, event_start + absolute_entry_delay)
            )
        return converted_sequential_event

    def _convert_event(
        self,
        event_to_convert: core_events.abc.Event,
        absolute_entry_delay: core_constants.DurationType,
    ) -> core_events.abc.ComplexEvent[core_events.abc.Event]:
        return super()._convert_event(event_to_convert, absolute_entry_delay)
