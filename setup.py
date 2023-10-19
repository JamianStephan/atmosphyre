import setuptools 
  
with open("README.md", "r") as fh: 
    description = fh.read() 
  
setuptools.setup( 
    name="atmosphyre", 
    version="0.0.3", 
    author="Jay Stephan", 
    author_email="Jay.Stephan@stfc.ac.uk", 
    packages=["atmosphyre","numpy","astropy","math","scipy","matplotlib"], 
    description="A sample test package", 
    long_description=description, 
    long_description_content_type="text/markdown", 
    license='MIT', 
    install_requires=['numpy'] 
) 


