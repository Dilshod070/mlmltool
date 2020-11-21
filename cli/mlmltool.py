import os
import fire

from cli.tools import Tool
from cli.tools.flaskapp import Flaskapp


class MlMlTool(Tool):
    def __init__(self):
        super().__init__()
        self.flaskapp = Flaskapp()
        self._user = 'dilshod070'
        self._project_path = os.getenv('MLMLTOOL_PATH') or '/Users/dilshod070/PycharmProjects/mlmltool'
        self._host_project_path = os.getenv('MLMLTOOL_PATH') or '/home/dilshod070/src/mlmltool'

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

    def update_cron(self, t='user'):
        """
        Update cron script with script in `mlmltool/scripts/cron`
        :param t: any ['user', 'root']
        """
        src_file = f'{self._project_path}/scripts/cron'
        dst_file = '/var/spool/cron/crontabs'
        if t == 'user':
            src_file = f'{src_file}/cron_user.sh'
            dst_file = f'{dst_file}/{self._user}'
            self._run_command('sudo', 'cp', src_file, dst_file)
            self._run_command('crontab', '-e')
        elif t == 'root':
            src_file = f'{src_file}/cron_root.sh'
            dst_file = f'{dst_file}/root'
            self._run_command('sudo', 'cp', src_file, dst_file)
            self._run_command('sudo', 'crontab', '-e')
        else:
            raise ValueError('Unknown value for cron type')

    def upload(self, *subdirs, host='89.223.120.79', user='dilshod070'):
        """
        Uploads mlmltool subdir to host.
        Alternative to PyCharm deployment as PyCharm takes too much space on vds
        :param subdirs: list mlmltool subdirectories
        :param host: vds host for ssh connection
        :param user: vds user for ssh connection
        :return: None
        """
        for subdir in subdirs:
            tool_dir = f'{self._project_path}/{subdir}'
            path_in_host = '{}/{}'.format(self._host_project_path, '/'.join(subdir.split('/')[:-1]))
            self._run_command('scp', '-r', tool_dir, f'{user}@{host}:{path_in_host}')


def main():
    fire.Fire(MlMlTool)


if __name__ == '__main__':
    main()
