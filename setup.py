import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pelt-testing",
    version="0.0.1",
    author="Luis Rosario",
    author_email="luisprooc@gmail.com",
    description="This package allows us to test algorithms and generate test data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luisprooc/pelt-testing",
    project_urls={
        "Bug Tracker": "https://github.com/luisprooc/pelt-testing/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", "Environment :: Console"
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
