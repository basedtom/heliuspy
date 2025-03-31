from setuptools import find_packages, setup

setup(
    name="heliuspy",  # Must be unique on PyPI
    version="0.1.0",  # Start with a version number
    packages=find_packages(),  # Automatically finds your_package/
    description="A Python library for interacting with Helius endpoints",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="tom",
    author_email="0xtomv@gmail.com",
    url="https://github.com/basedtom/heliuspy",
    license="APACHE",  # Or your chosen license
    install_requires=[  # List dependencies from requirements.txt
        "requests",
    ],
    python_requires=">=3.6",  # Specify Python version compatibility
)
