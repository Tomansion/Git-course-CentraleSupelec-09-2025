import setuptools

setuptools.setup(
    name="python_module_template",
    version="1.0.0",
    author="ToMansion",
    description="Python library template, performs basic operations",
    license="Apache 2.0",
    keywords="math calculator",
    url="https://github.com/Tomansion/Python-module-template/",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pytest",
        "sphinx",
    ],
)
