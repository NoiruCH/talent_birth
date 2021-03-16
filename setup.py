
from setuptools import setup

setup(
    name="talent_birth",
    version="1.0.0",
    install_requires=['requests', 'bs4', 'click'],
    entry_points={
        'console_scripts': [
            "talent_birth=talent_birth.core:cli" # package.module: func
        ]
    }
)


