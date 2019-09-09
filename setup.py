from setuptools import setup

import ns


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='ns-api',
      version=ns.__version__,
      description='Wrapper for the NS api',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
      ],
      keywords='api ns nederlandse spoorwegen dutch railway',
      url='http://github.com/Shiqan/ns-api',
      author='Shiqan',
      license='MIT',
      packages=['ns'],
      install_requires=[
          'aiohttp',
          'dataclasses-json',
          'requests',
      ],
      tests_require=['pytest'],
      include_package_data=True,
      zip_safe=False)
