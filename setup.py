from setuptools import setup

setup(
    name='Tic_Tac_Toe',
    version='0.1',
    description='Django Tic-Tac-Toe',
    author='Alan Sendgikoski',
    author_email='asendgi@gmail.com',
    install_requires=[
        'Django==1.5.1',
        'selenium',
        'mock',
        'unittest2',  # (only if using Python 2.6)
    ]
)
