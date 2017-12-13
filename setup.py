from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open('test_requirements.txt','r') as f:
    test_requirements = f.read().splitlines()

setup(
    name = 'aibs_sg_prototype',
    version = '0.1.0',
    description = """Provides ability to test a single sphinx-gallery example file using aibs_sphinx theme""",
    author = "Nicholas Cain",
    author_email = "nicholasc@alleninstitute.org",
    url = 'https://github.com/AllenInstitute/aibs.sg_prototype',
    packages = find_packages(),
    include_package_data=True,
    install_requires = requirements,
    entry_points={
          'console_scripts': [
              'aibs.sg_prototype = aibs.sg_prototype.__main__:main'
        ]
    },
    setup_requires=['pytest-runner'],
    tests_require = test_requirements
)
