from setuptools import setup

setup(
      python_requires='>=2.7',
      name='honeycomb-beeline',
      version='0.0.1',
      description='Honeycomb library for rapid instrumentation',
      url='https://github.com/honeycombio/beeline-python',
      author='Honeycomb.io',
      author_email='feedback@honeycomb.io',
      license='Apache',
      packages=['beeline'],
      install_requires=[
          'libhoney',
      ],
      tests_require=[
        'mock',
      ],
      zip_safe=False
)