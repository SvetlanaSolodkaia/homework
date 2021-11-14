from setuptools import setup

setup(
    name = 'test_project',
    author = 'SV',
    packages = ['Test_date'],
    install_requires = ['requests'],
    entry_points = {'new_script': ['Test_date = Test_date.test_date_code:main']},
)