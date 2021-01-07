import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tmax_ims",
    version="0.0.3",
    author="Changyun Lee",
    author_email="brownbearpower@gmail.com",
    description="TMAX IMS issue alert package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZeroStrength/tmax_ims",
    packages=setuptools.find_packages(),
    install_requires=['bs4', 'py-notifier', 'pandas', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)