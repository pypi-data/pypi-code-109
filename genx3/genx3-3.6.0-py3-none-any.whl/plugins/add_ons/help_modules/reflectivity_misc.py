"""
Typing support for reflectivity plugins.
Could be extended with other small helpers.
"""
from genx.data import DataList
from genx.models.lib.refl import InstrumentBase, LayerBase, SampleBase, StackBase


try:
    # noinspection PyUnresolvedReferences
    from typing import Protocol, Iterable, List, Dict, Any, Type, Union
except ImportError:
    ReflectivityModule = object
else:
    class Sample(Protocol):

        def SimSLD(self, z, item: Union[str, None], inst: InstrumentBase) -> Dict[str, Any]:
            ...

    def Sim(data:DataList) -> List[Any]:
        ...

    class ReflectivityModule(Protocol):
        """
        Defines the attributes that are expected in a python module that defines a reflectivity model.
        This is used to type check what the classes in this file use.
        """
        sample_string_choices: Dict[str, Iterable[str]]
        SampleParameters: Dict[str, Any]
        SampleGroups: Iterable
        SampleUnits: Dict[str, str]

        instrument_string_choices: Dict[str, Iterable[str]]
        InstrumentParameters: Dict[str, Any]
        InstrumentGroups: Iterable
        InstrumentUnits: Dict[str, str]

        LayerParameters: Dict[str, Any]
        LayerGroups: Iterable
        LayerUnits: Dict[str, str]

        StackParameters: Dict[str, Any]
        StackGroups: Iterable
        StackUnits: Dict[str, str]

        Instrument: Type[InstrumentBase]
        Sample: Type[SampleBase]
        Stack: Type[StackBase]
        Layer: Type[LayerBase]

        _sim: bool
        SLD: List[Dict[str, Any]]
        sample: Sample
        Sim: Sim
        inst: InstrumentBase
