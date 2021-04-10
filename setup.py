from setuptools import setup, find_packages
setup(
        name='AlignR',
        version='1.0.1',
        packages=find_packages(),
        url='https://github.com/JulienAlardot/AlignmentReporter',
        license='MIT',
        author='Julien Alardot',
        author_email='alardotj.pro@gmail.com',
        description='Simple Tool to track the alignments of your players',
        long_description=open('README.md').read(),
        include_package_data=True,
        classifiers=[
            "Programming Language :: Python",
            "Natural Language :: English",
            "Operating System :: Windows",
            "Programming Language :: Python :: 3.8",
            "Topic :: Roleplaying Games Tools",
        ],
        zip_safe=False,
        entry_points={
            'console_scripts': [
                'AlignR-Launch = AlignmentReporter.UI.py:launch',
            ],
        },
        install_requires=["setuptools>=40.8.0", "PySide2==5.14.1", "matplotlib>=3.3.4", "numpy==1.19.5", "pyparsing",
                          "Cython==0.29.21", "pandas<1.2", "scipy<=1.5"]
)
