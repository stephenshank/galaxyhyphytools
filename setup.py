from setuptools import setup


setup(
    name='galaxyhyphytools',
    python_requires='>3.6.6',
    version='0.0.1',
    url='https://github.com/stephenshank/galaxyhyphytools',
    download_url="https://github.com/stephenshank/galaxyhyphytools/archive/v0.0.1.tar.gz",
    description='A few bioinformatics utilities used on galaxy.hyphy.org',
    author='Stephen D. Shank',
    author_email='sshank314@gmail.com',
    maintainer='Stephen D. Shank',
    maintainer_email='sshank314@gmail.com',
    install_requires=[
        'biopython>=1.79'
    ],
    packages=['galaxyhyphytools'],
    entry_points={
        'console_scripts': [
            'ght = galaxyhyphytools.cli:command_line_interface'
        ]
    },
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
    ]
)
