# Template for python project

## Start Development

Change *pyproject.toml* content before you start. 

```bash
python3.8 -m venv .venv
source .venv/bin/activate
mv example_dot_env .env
source .env
pip install -e .[dev]
#https://github.com/pypa/pip/issues/8049#issuecomment-664055253
#https://martin-thoma.com/pyproject-toml/
```
to install only required requirements use `pip install -e .`

## Create docs
mkdocs

## tox

You can easily run specific environment with option `-e`

```
tox -e py39-lint
```

`tox -a` will list the available test configurations


## Manifest.in

- .gitignore
- mkdocs.yml
- pyproject.toml
- README.md
- setup.py
- tox.ini