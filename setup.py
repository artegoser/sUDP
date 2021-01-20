from setuptools import setup, find_packages
 
setup(name='SUDP',
      version='1.0.1',
      url='https://github.com/artegoser/sUDP',
      license='MIT',
      author='artegoser',
      author_email='artegoser@gmail.com',
      description='Safely wrapper for UDP protocol. Python library',
      packages=['SUDP'],
      long_description_content_type='text/markdown',
      long_description=open('README.md').read(),
      zip_safe=False)