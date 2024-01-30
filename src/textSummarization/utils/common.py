import os 
from box.exceptions import BoxValueError
import yaml
from textSummarization.logging import logger
from ensure import ensure_annotations   
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns
    Args:
        path_to_yaml: Path to yaml file(str)
    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file
    Returns:
        ConfigBox: ConfigBox type"""
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_dir: list, verbose = True):
    """Creates directories
    Args: path_to_dir: list of path of directories to create(str)
    ignore_log(bool, optional): ignore if multiple directories is to be created(default: False)
    """
    for path in path_to_dir:
        os.makedirs(path, exist_ok = True)
        if verbose:
            logger.info(f"directory: {path} created successfully")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path(Path): path of the file whose size is to be returned
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"