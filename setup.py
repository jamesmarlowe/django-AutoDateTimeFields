from distutils.core import setup

setup(
    name='django-AutoDateTimeFields',
    version='0.9.0',
    author='James Marlowe',
    author_email='jameskmarlowe@gmail.com',
    packages=['autodatetimefields', 'autodatetimefields.test'],
    url='http://pypi.python.org/pypi/django-AutoDateTimeFields/',
    license='LICENSE',
    description='django date time fields that do not break like auto_now and auto_now_add do',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.1.1",\
    ],
)