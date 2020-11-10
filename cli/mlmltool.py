import os
import fire

from cli.tools import Tool
from cli.tools.flaskapp import Flaskapp


class MlMlTool(Tool):
    def __init__(self):
        super().__init__()
        self.flaskapp = Flaskapp()

    @staticmethod
    def hmsg(tool: str = ''):
        """
        Show inline help message about some tool.
        The same as `mlmltool <func> --help | cat`
        :param: tool - tool to show help message about
        :return:
        """
        cmd = 'mlmltool {} -- --help | cat'.format(tool)
        os.system(cmd)


def main():
    fire.Fire(MlMlTool)


if __name__ == '__main__':
    main()
