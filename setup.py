from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='py_tradetracker',
      version='0.1',
      description='Python3 Tradetracker products feed and SOAP webservices script',
      long_description=readme(),      
      url='https://bitbucket.org/tvdsluijs/py_tradetracker',
      author='Theo van der Sluijs',
      author_email='theo@vandersluijs.nl',
      license='CC BY-NC-SA 4.0',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
        ],
      keywords='trains transport train dutch ns',
      packages=['py_tradetracker'],
      install_requires=[
          'xmltodict',
          'zeep',
      ],      
      zip_safe=False)