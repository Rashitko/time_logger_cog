from setuptools import setup

setup(
    name='time_logger_cog',
    version='0.1.5',
    packages=['time_logger_cog', 'time_logger_cog.modules'],
    url='https://github.com/Rashitko/time_logger_cog',
    download_url='https://github.com/Rashitko/time_logger_cog/master/tarball/',
    license='MIT',
    author='Michal Raska',
    author_email='michal.raska@gmail.com',
    description='',
    install_requires=['up', 'pyyaml', 'pyserial'],
    package_data={
        'time_logger_cog': ['registered_modules.yml']
    }
)
