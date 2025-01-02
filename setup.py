from setuptools import setup, find_packages

setup(
    name="rohit_prat_bot",
    version="0.2.2",
    author="Rohit Prat",
    author_email="legacy.business18@gmail.com",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rp-bot/rpbot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data={
        "rohit_prat_bot": ["images/*"],
    },
    install_requires=[
        "pillow",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "rohit_prat_bot=rohit_prat_bot.main:main",
        ],
    },
)
