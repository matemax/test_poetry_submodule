# -*- coding: utf-8 -*-
from setuptools import setup
from test_poetry_submodule.poetry_private_module.private_module.foo import bar
packages = \
['test_poetry_submodule']

package_data = \
{'': ['*']}


setup_kwargs = {
    'name': 'test_poetry_submodule',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'matemax',
    'author_email': 'matemaks@ya.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': [],
    'python_requires': '>=3.7,<4.0',
}

bar()
setup(**setup_kwargs)