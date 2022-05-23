import setuptools
    
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='forloop',
    version='0.6.1',
    author='DovaX',
    author_email='dominik@forloop.ai',
    description='Forloop.ai platform - package containing public API commands',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ForloopAI/forloop',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          
     ],
    python_requires='>=3.6',
)
    