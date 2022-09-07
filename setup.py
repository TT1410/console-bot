from setuptools import setup, find_namespace_packages


setup(
    name='console_bot',
    version='1',
    description='Консольний бот',
    url='https://github.com/TT1410/sort_folder',
    author='TT1410',
    author_email='tarplax@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['console-bot = console_bot:main']}
)
