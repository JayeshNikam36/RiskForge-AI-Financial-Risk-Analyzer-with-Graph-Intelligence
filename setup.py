from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="RiskForge",
    version="0.1",
    author="RiskForge",
    packages=find_packages(),
    install_requires=requirements,
    description="RiskForge AI Financial Risk Analyzer with Graph Intelligence",
)
