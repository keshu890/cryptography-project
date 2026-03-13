"""
SimSecure Installation Setup
Professional Cybersecurity Command-Line Tool
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simsecure",
    version="1.0.0",
    author="Security Research Team",
    author_email="security@simsecure.local",
    description="Professional Cybersecurity Command-Line Tool for Ethical Security Testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/simsecure",
    project_urls={
        "Bug Tracker": "https://github.com/example/simsecure/issues",
        "Documentation": "https://github.com/example/simsecure/wiki",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "Topic :: System :: Monitoring",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "colorama>=0.4.3",
    ],
    entry_points={
        "console_scripts": [
            "simsecure=simsecure:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
