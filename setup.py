from setuptools import setup

setup(
    name="subspider",
    version="1.0",
    description="SubSpider - Passive Subdomain & IP Discovery Tool",
    author="YasinShaikh2003",
    py_modules=["subspider"],
    install_requires=[
        "aiohttp",
        "requests",
        "dnspython",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "subspider=subspider:main"
        ]
    }
)
