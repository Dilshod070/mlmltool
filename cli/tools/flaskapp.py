from cli.tools import Tool


class Flaskapp(Tool):
    def __init__(self):
        super().__init__()

    # Deploy flaskapp didn't work

    def upload(self, host='89.223.120.79', user='dilshod070', wdir='/home/dilshod070/src/mlmltool'):
        """
        Uploads Flaskapp to host.
        Alternative to PyCharm deployment as PyCharm takes too much space on vds
        :param host: vds host for ssh connection
        :param user: vds user for ssh connection
        :param wdir: directory on vds
        :return: None
        """
        flaskapp_dir = __file__.split('mlmltool')[0] + 'mlmltool/flaskapp'
        self._run_command('scp', '-r', flaskapp_dir, f'{user}@{host}:{wdir}')
