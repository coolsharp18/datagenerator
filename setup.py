from setuptools import setup

setup(
    name='datagenerator',
    version='0.0.2',
    packages=['generator', 'test'],
    entry_points={
            "console_scripts": [
                "myscript = generator.__main__:main",
            ]
    },
    url='',
    license='',
    author='Anand Kumar',
    author_email='',
    description='Utility to generate test data based on configuration'
)
