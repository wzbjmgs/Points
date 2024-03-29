import os
import logging.config
import sys
import yaml


def setup_logging():
    default_path = "points/src/resources/logging.yml"
    default_level = logging.INFO
    default_log_path = "log_files"
    docs = "docs"

    logfile_path = os.path.dirname(sys.path[0]) + "/" + docs + "/" + default_log_path
    if not os.path.exists(logfile_path):
        os.makedirs(logfile_path)
    config_file = os.path.join(os.path.dirname(sys.path[0]), default_path)
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f.read())
        __update_logfile_path(logfile_path, config)
        logging.config.dictConfig(config)
    except IOError as error:
        logging.basicConfig(level=default_level)


def __update_logfile_path(root_path, config):
    handlers = config["handlers"]

    info_handlers = handlers["info_file_handler"]
    error_handlers = handlers["error_file_handler"]

    info_handlers["filename"] = root_path + "/" + info_handlers["filename"]
    error_handlers["filename"] = root_path + "/" + error_handlers["filename"]
