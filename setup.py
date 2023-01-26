import setuptools
import sys
import os

with open("README.md", mode="r", encoding="utf-8") as f:
    long_description = f.read()

with open("."+os.sep+"src"+os.sep+"__init__.py", mode="r", encoding="utf-8") as f:
    for line in f.readlines():
        if line.startswith("__version__"):
            quotation_marks = '"' if '"' in line else "'"
            version = line.split(quotation_marks)[1]
            break
    else:
        print("Can't find version! Stop Here!")
        sys.exit()


setuptools.setup(
    name="PyClassSaver",
    version=version,
    author="xyj_curry",
    author_email="294794907@qq.com",
    maintainer="xyj_curry",
    maintainer_email="294794907@qq.com",
    license="MIT Licence",
    description="一个用来保存python类的第三方库",
    long_description=long_description,
    platforms="any",
    keywords=["class", "save"],
    long_description_content_type="PyClassSaver",
    url="https://github.com/xyj-curry/PyClassSaver",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
