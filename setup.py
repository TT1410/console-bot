from setuptools import setup


setup(
    name='console_bot',
    version='1',
    description='Консольний бот',
    url='https://github.com/TT1410/sort_folder',
    author='TT1410',
    author_email='tarplax@gmail.com',
    license='MIT',
    packages=['console_bot'],
    include_package_data=True,
    entry_points={'console_scripts': ['console-bot = console_bot:main']}
)
