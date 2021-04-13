from setuptools import find_packages, setup

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.1.0",
    scripts=["manage.py"],
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Operating System :: Unix",
        "Private :: Do Not Upload",
        "Programming Language :: Python",
    ],
)
