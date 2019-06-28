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
    scripts=['str-to-json/str-to-json'],
    install_requires=['pyperclip==1.7.0'],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)
