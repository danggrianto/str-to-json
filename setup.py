import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="str-to-json",
    version="0.0.1",
    author="Daniel Anggrianto",
    author_email="d.anggrianto@gmail.com",
    description="Convert string on clipboard to JSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danggrianto/str-to-json/",
    packages=setuptools.find_packages(),
    scripts=['export_yaml/export_yaml'],
    install_requires=['pyyaml'],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
