"""Compute and write Sparameters using Meep in MPI."""

import multiprocessing
import pathlib
import pickle
import shlex
import subprocess
import time
from pathlib import Path
from typing import Optional

import pydantic

import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.config import logger, sparameters_path
from gdsfactory.simulation.get_sparameters_path import (
    get_sparameters_path_meep as get_sparameters_path,
)
from gdsfactory.simulation.gmeep.write_sparameters_meep import remove_simulation_kwargs
from gdsfactory.tech import LAYER_STACK, LayerStack

ncores = multiprocessing.cpu_count()

temp_dir_default = Path(sparameters_path) / "temp"


@pydantic.validate_arguments
def write_sparameters_meep_mpi(
    component: Component,
    cores: int = ncores,
    filepath: Optional[Path] = None,
    dirpath: Path = sparameters_path,
    layer_stack: LayerStack = LAYER_STACK,
    temp_dir: Path = temp_dir_default,
    temp_file_str: str = "write_sparameters_meep_mpi",
    overwrite: bool = False,
    wait_to_finish: bool = True,
    **kwargs,
) -> Path:
    """Write Sparameters using multiple cores and MPI
    and returns Sparameters CSV filepath.

    Simulates each time using a different input port (by default, all of them)
    unless you specify port_symmetries:

    port_symmetries = {"o1":
            {
                "s11": ["s22","s33","s44"],
                "s21": ["s21","s34","s43"],
                "s31": ["s13","s24","s42"],
                "s41": ["s14","s23","s32"],
            }
        }

    Args:
        component: gdsfactory Component.
        cores: number of processors.
        filepath: to store pandas Dataframe with Sparameters in CSV format.
            Defaults to dirpath/component_.csv
        dirpath: directory to store Sparameters
        layer_stack:
        temp_dir: temporary directory to hold simulation files.
        temp_file_str: names of temporary files in temp_dir.
        overwrite: overwrites stored simulation results.
        wait_to_finish:

    Keyword Args:
        resolution: in pixels/um (20: for coarse, 120: for fine)
        port_symmetries: Dict to specify port symmetries, to save number of simulations
        source_ports: list of port string names to use as sources
        dirpath: directory to store Sparameters
        layer_stack: LayerStack class
        port_margin: margin on each side of the port
        port_monitor_offset: offset between monitor GDS port and monitor MEEP port
        port_source_offset: offset between source GDS port and source MEEP port
        filepath: to store pandas Dataframe with Sparameters in CSV format.
        animate: saves a MP4 images of the simulation for inspection, and also
            outputs during computation. The name of the file is the source index
        lazy_parallelism: toggles the flag "meep.divide_parallel_processes" to
            perform the simulations with different sources in parallel
        dispersive: use dispersive models for materials (requires higher resolution)
        extend_ports_length: to extend ports beyond the PML
        layer_stack: Dict of layer number (int, int) to thickness (um)
        zmargin_top: thickness for cladding above core
        zmargin_bot: thickness for cladding below core
        tpml: PML thickness (um)
        clad_material: material for cladding
        is_3d: if True runs in 3D
        wl_min: wavelength min (um)
        wl_max: wavelength max (um)
        wl_steps: wavelength steps
        dfcen: delta frequency
        port_source_name: input port name
        port_field_monitor_name:
        port_margin: margin on each side of the port
        distance_source_to_monitors: in (um) source goes before
        port_source_offset: offset between source GDS port and source MEEP port
        port_monitor_offset: offset between monitor GDS port and monitor MEEP port

    Returns:
        filepath for sparameters CSV (wavelengths, s11a, s12m, ...)
            where `a` is the angle in radians and `m` the module
    """
    settings = remove_simulation_kwargs(kwargs)
    filepath = filepath or get_sparameters_path(
        component=component,
        dirpath=dirpath,
        layer_stack=layer_stack,
        **settings,
    )
    filepath = pathlib.Path(filepath)
    if filepath.exists() and not overwrite:
        logger.info(f"Simulation {filepath!r} already exists")
        return filepath

    # Save the component object to simulation for later retrieval
    temp_dir.mkdir(exist_ok=True, parents=True)
    tempfile = temp_dir / temp_file_str
    component_file = tempfile.with_suffix(".pkl")
    kwargs.update(filepath=str(filepath))

    with open(component_file, "wb") as outp:
        pickle.dump(component, outp, pickle.HIGHEST_PROTOCOL)

    # Write execution file
    script_lines = [
        "import pickle\n",
        "from gdsfactory.simulation.gmeep import write_sparameters_meep\n\n",
        'if __name__ == "__main__":\n\n',
        f"\twith open(\"{component_file}\", 'rb') as inp:\n",
        "\t\tcomponent = pickle.load(inp)\n\n"
        "\twrite_sparameters_meep(component = component,\n",
    ]
    for key in kwargs.keys():
        script_lines.append(f"\t\t{key} = {kwargs[key]!r},\n")

    script_lines.append("\t)")
    script_file = tempfile.with_suffix(".py")
    script_file_obj = open(script_file, "w")
    script_file_obj.writelines(script_lines)
    script_file_obj.close()

    command = f"mpirun -np {cores} python {script_file}"
    logger.info(command)
    logger.info(str(filepath))

    subprocess.Popen(
        shlex.split(command),
        shell=False,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if wait_to_finish:
        while not filepath.exists():
            time.sleep(1)

    return filepath


write_sparameters_meep_mpi_lr = gf.partial(
    write_sparameters_meep_mpi, ymargin_top=3, ymargin_bot=3
)

write_sparameters_meep_mpi_lt = gf.partial(
    write_sparameters_meep_mpi, ymargin_bot=3, xmargin_right=3
)


if __name__ == "__main__":
    c1 = gf.c.straight(length=5)
    p = 3
    c1 = gf.add_padding_container(c1, default=0, top=p, bottom=p)

    instance_dict = {
        "component": c1,
        "run": True,
        "overwrite": True,
        "lazy_parallelism": True,
        "filepath": "instance_dict.csv",
    }

    proc = write_sparameters_meep_mpi(
        instance=instance_dict,
        cores=3,
        verbosity=True,
    )
