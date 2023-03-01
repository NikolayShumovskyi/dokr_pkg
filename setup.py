import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name='dokr',
	version='0.1',
	script=['dokr'],
	author="nikolay.shumovskyi",
	author_email="nikolay.shumovskyi@gmail.com",
	description="A Docker and AWS utility package",
	long_description=long_description,
	long_secription_content_type="text/markdown",
	url="https://github.com/NikolayShumovskyi/dokr_pkg",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent", 
	],
)
