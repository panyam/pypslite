import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypslite",
    version="0.0.1",
    author="Sri Panyam",
    description="Python GRPC Bindings for pslite - A simple local pubsub queue",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/panyam/pypslite",
    project_urls={
        "Bug Tracker": "https://github.com/panyam/pypslite/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
