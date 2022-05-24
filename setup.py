from setuptools import setup, find_packages

VERSION = '0.0.5'
DESCRIPTION = 'abstraction for language model priming / prompt engineering'
LONG_DESCRIPTION = 'Ready made prompts for GPT3 or create your own in seconds'

setup(
    name="prompt_engineering",
    version=VERSION,
    author="Mohammed Terry-Jack",
    author_email="<mohammedterryjack@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'priming', 'prompts', 'gpt3', 'gptj'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ]
)