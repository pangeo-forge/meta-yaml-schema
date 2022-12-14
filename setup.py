from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

setup(
    name="pangeo-forge-meta-yaml-schema",
    description="JSON Schema for Pangeo Forge meta.yaml.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Charles Stern",
    author_email="charlesisaacstern@gmail.com",
    version="0.0.0",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "jsonschema",
        "PyYAML",
    ],
)
