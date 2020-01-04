from setuptools import setup

setup(
    name='s3tk',
    version='0.2.1',
    description='A security toolkit for Amazon S3',
    url='https://github.com/alex14324/s3tk',
    author='Dinu Reddy ',
    author_email='alex143242@gmail.com',
    license='MIT',
    packages=['s3tk'],
    scripts=['bin/s3tk'],
    install_requires=[
        'boto3>=1.4.7',
        'botocore>=1.7.43',
        'clint',
        'click',
        'joblib'
    ],
    zip_safe=False
)
