"""
Setup configuration for SFL Translation Agent
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="sfl-translation-agent",
    version="0.1.0",
    author="Simon James Drury",
    author_email="simondrury2010@gmail.com",
    description="SFL-based translation agent with semantic fidelity and multilingual support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simon-drury/sfl-translation-agent",
    packages=find_packages(),
    py_modules=["sfl_translation"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "all": [
            "python-spacy[transformers]",
        ]
    },
    entry_points={
        "console_scripts": [
            "sfl-translate=sfl_translation:main",
        ],
    },
    keywords="translation, sfl, systemic-functional-linguistics, nlp, machine-translation, multilingual",
    project_urls={
        "Bug Reports": "https://github.com/simon-drury/sfl-translation-agent/issues",
        "Source": "https://github.com/simon-drury/sfl-translation-agent",
        "Documentation": "https://github.com/simon-drury/sfl-translation-agent/blob/main/README.md",
    },
)
