from setuptools import setup, find_packages

setup(
    name='datasets_saver',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        "typer==0.9.0",
        "datasets==2.14.6",
    ],
    entry_points={
        'console_scripts': [
            'datasets=datasets_saver.cmd:app',
        ],
    },
)
