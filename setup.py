import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cl_simulator",
    version="0.0.1",
    author="Sattvik Sahai",
    author_email="sattviksahai24@gmail.com",
    description="python simulator for Collaborative Deep Learning",
    py_modules=["cl_simulator"],
    # package_dir={'':'simulator'},
    long_description="A python library to simulate Collaborative Deep Learning. It provides the flexibility to simulate various network architectures, Collaborative Learning Stratergies, and privacy invasion attacks.",
    long_description_content_type="text/markdown",
    url="https://github.com/sattviksahai/Collaborative-Learning-Simulator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)