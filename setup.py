try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'My Project',
    'author': 'Gabriela Bazan',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'Gabriela.L.Bazan@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
