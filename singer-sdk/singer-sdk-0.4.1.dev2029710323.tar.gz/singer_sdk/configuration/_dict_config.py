"""Helpers for parsing and wrangling configuration dictionaries."""

import logging
import os
from pathlib import Path
from typing import Any, Dict, Iterable

from singer_sdk.helpers._typing import is_string_array_type
from singer_sdk.helpers._util import read_json_file

logger = logging.getLogger(__name__)


def parse_environment_config(
    config_schema: Dict[str, Any], prefix: str
) -> Dict[str, Any]:
    """Parse configuration from environment variables.

    Args:
        config_schema: A JSON Schema dictionary for the configuration.
        prefix: Prefix for environment variables..

    Raises:
        ValueError: If an un-parsable setting is found.

    Returns:
        A configuration dictionary.
    """
    result: Dict[str, Any] = {}
    for config_key in config_schema["properties"].keys():
        env_var_name = prefix + config_key.upper().replace("-", "_")
        if env_var_name in os.environ:
            env_var_value = os.environ[env_var_name]
            logger.info(
                "Parsing '%s' config from env variable '%s'.",
                config_key,
                env_var_name,
            )
            if is_string_array_type(config_schema["properties"][config_key]):
                if env_var_value[0] == "[" and env_var_value[-1] == "]":
                    raise ValueError(
                        "A bracketed list was detected in the environment variable "
                        f"'{env_var_name}'. This syntax is no longer supported. "
                        "Please remove the brackets and try again."
                    )
                result[config_key] = env_var_value.split(",")
            else:
                result[config_key] = env_var_value
    return result


def merge_config_sources(
    inputs: Iterable[str],
    config_schema: Dict[str, Any],
    env_prefix: str,
) -> Dict[str, Any]:
    """Merge configuration from multiple sources into a single dictionary.

    Args:
        inputs: A sequence of configuration sources (file paths or ENV).
        config_schema: A JSON Schema dictionary for the configuration.
        env_prefix: Prefix for environment variables.

    Raises:
        FileNotFoundError: If any of config files does not exist.

    Returns:
        A single configuration dictionary.
    """
    config: Dict[str, Any] = {}
    for config_path in inputs:
        if config_path == "ENV":
            env_config = parse_environment_config(config_schema, prefix=env_prefix)
            config.update(env_config)
            continue

        if not Path(config_path).is_file():
            raise FileNotFoundError(
                f"Could not locate config file at '{config_path}'."
                "Please check that the file exists."
            )

        config.update(read_json_file(config_path))

    return config
