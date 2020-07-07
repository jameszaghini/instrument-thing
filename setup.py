from setuptools import setup
setup(
    name = 'synth',
    version = '0.1.0',
    packages = ['synth'],
    entry_points = {
        'console_scripts': [
            'synth = synth.__main__:main'
        ]
    })
