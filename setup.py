import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my-server",
    version="0.0.1",
    author="MD Mehedi Hasan",
    author_email="shuvo@asl.aero",
    packages=["my_server"],
    description="A small python server package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shuvo-asl/my-server",
    license='MIT',
    python_requires='>=3.8'
)