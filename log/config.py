import os
import logging.config

import yaml


def setup_logging(
        default_path='logging.yml',
        default_level=logging.INFO,
):
    """Setup logging configuration

    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, default_path)
    try:
        with open(path, 'r') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    except IOError as error:
        logging.basicConfig(level=default_level)
