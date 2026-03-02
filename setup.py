"""
Setup script for the Price Elasticity package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="price-elasticity",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive tool for calculating and analyzing price elasticity of demand",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/price_elasticity",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
        ],
        "analysis": [
            "pandas>=1.3.0",
            "matplotlib>=3.4.0",
        ],
        "full": [
            "pandas>=1.3.0",
            "matplotlib>=3.4.0",
            "jupyter>=1.0.0",
            "notebook>=6.4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "elasticity-calc=elasticity:main",
        ],
    },
)
