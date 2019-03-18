import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="gym-http-server",
    version="0.0.1",
    description="Serve gym on a webserver and receive HTTP requests to play to the game from any client",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/saravanabalagi/gym-http-server",
    author="Saravanabalagi Ramachandran",
    author_email="saravanabalagi@hotmail.com",
    license="MIT",
    classifiers=[
    	"Development Status :: 3 - Alpha",
    	"Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points = {
        'console_scripts': ['gym-http-server=gym_http_server.command_line:main'],
    },
    packages=["gym_http_server"],
    include_package_data=True,
    install_requires=["Flask==0.11.1", "numpy", "gym==0.7.4", "requests==2.11.0", "pytest"]
)