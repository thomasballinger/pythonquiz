from setuptools import setup

setup(
    name="pyquiz",
    version = '0.0.2',
    author = "Tom Ballinger",
    author_email = "thomasballinger@gmail.com",
    url='https://github.com/thomasballinger/pythonquiz',
    description = "Library for writing Python language quizes",
    license = "MIT",
    install_requires = ['jinja2'],
    packages = ["pyquiz"],
    entry_points = {
        'console_scripts': [
            'pyquiz = pyquiz.render:main',
        ],
    },
)
