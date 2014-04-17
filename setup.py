from setuptools import setup
import pyquiz

setup(
    name="pyquiz",
    version = pyquiz.__version__,
    author = "Tom Ballinger",
    author_email = "thomasballinger@gmail.com",
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
