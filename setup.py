import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rwt", # Replace with your own username
    version="0.1.0",
    author="Matt Lawlor",
    author_email="matt.a.lawlor@gmail.com",
    description="utils for making custom references with additional consensus seqs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mal2017/reference-with-transposons",
    packages=setuptools.find_packages(),
        entry_points = {
        'console_scripts': ['rwt=rwt.cli:main'],
    },
    scripts=["scripts/format_repbase_fa.R","scripts/fa2gtf.R"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
