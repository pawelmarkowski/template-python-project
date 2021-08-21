import toml
from setuptools import setup

with open("pyproject.toml", "r", encoding="utf-8") as f:
    pyproject = toml.loads(f.read())

prod = pyproject["install_requires"]
dev = pyproject["extras_require"]["dev"]


def parse_requirement(requirement_name: str, requirement_version: str):
    if requirement_version == "*":
        return requirement_name
    if requirement_version.startswith("git+ssh"):
        return f"{requirement_name} @ {requirement_version}"
    return f"{requirement_name}{requirement_version}"


setup(
    name=pyproject["project"]["name"],
    version=pyproject["project"]["version"],
    description=pyproject["project"]["description"],
    author=pyproject["project"]["authors"][0].split(" <")[0],
    author_email=pyproject["project"]["authors"][0].split(" <")[1][:-1],
    url=pyproject["project"]["homepage"],
    license=pyproject["project"]["license"],
    # packages=['distutils', 'distutils.command'],
    install_requires=[parse_requirement(x, prod[x]) for x in prod],
    extras_require={"dev": [parse_requirement(x, dev[x]) for x in dev]},
)
