import io
import os.path
import setuptools
from setuptools.command.test import test as TestCommand

from code._version import __version__

__long_desc__ = io.open(os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'README.md'), encoding='utf-8').read()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--junitxml', 'tests/test-result.xml',
            '--cov-report', 'term-missing',
            '--cov-report', 'html',
            '--cov-report', 'xml']
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)


setuptools.setup(
    version=__version__,
    name='code',
    description='Leetcode exercises',
    long_description=__long_desc__,
    long_description_content_type='text/markdown',
    keywords='leet leetcode',
    author='Rich Braun',
    author_email='richb@instantlinux.net',
    url='https://github.com/instantlinux/leet',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[],
    python_requires='>=2.7.3',
    test_suite='tests',
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Topic :: System :: Archiving :: Backup',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
