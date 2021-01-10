from setuptools import setup

setup(
    name="strategise-api",
    packages=["api"],
    include_package_data=True,
    install_requires=[
        "fastapi",
    ],
)