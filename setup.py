from setuptools import setup

setup(
    name="spotternetwork",
    version="0.0.1",
    description="Find positions of storm spotters from spotternetwork.org",
    url="https://github.com/cblument/spotternetwork",
    license="MIT",
    author="Chris Blumentritt",
    author_email="cblument@gmail.com",
    py_modules=["spotternetwork"],
    install_requires=["pykml==0.1.0","geojson==1.0.8"],
    classifiers=[],
)
