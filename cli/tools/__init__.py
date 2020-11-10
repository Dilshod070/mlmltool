import os
import abc
import logging
import subprocess

LOGGING_FORMAT = '%(name)s: %(filename)s [line:%(lineno)d] %(levelname)-8s  %(message)s'
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)


class Tool:

    __metaclass__ = abc.ABCMeta

    def __init__(self, log_level=10):
        """
        Use log_level=10 for Debug and log_level=20 for info
        """
        self._logger = logging.getLogger(__class__.__name__)
        self._logger.setLevel(log_level)

    def _run_command(self, command: str, *args, wait: bool = True):
        """
        Runs shell command
        :param command: shell command
        :param args: arguments for shell command
        :param wait: whether to run sync or async
        """
        self._logger.info([command] + list(args))
        proc = subprocess.Popen([command] + list(args))
        if wait:
            proc.wait()
