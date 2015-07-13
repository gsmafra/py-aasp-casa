from setuptools import setup, find_packages

from setup_post_install import run_post_install

setup(
    name='aaspcasa',
    version='0.1.0',
    author='Gustavo Sena Mafra',
    author_email='gsenamafra@gmail.com',
    description='IEEE AASP CASA Dataset auxiliary functions',
    license='MIT',
    packages=find_packages(),
    url='https://github.com/gsmafra/py-aasp-casa',
    install_requires=['numpy', 'scipy', 'scikit-learn', 'librosa'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Machine Learning',
        ]
    )

#run_post_install()
