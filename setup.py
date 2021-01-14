import setuptools

install_requires = [
    'prefect==0.13.18',
    'splitgraph==0.2.4',
    'pandas==1.2.0',
    'sqlalchemy==1.3.22    ',
]

setuptools.setup(
    name="prefect-lime",
    version="0.0.1",
    author="leviplj",
    author_email="leviplj@gmail.com",
    description="Prefect Addons",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=install_requires
)