from setuptools import setup, find_packages

setup(
    name='mlmltool',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mlmltool = cli.mlmltool:main',
        ]
    }
)
