from setuptools import setup

setup(
    name="trisuella-cli",
    version="3.4.0",
    author="Bhaskar Puppala (PATEL)",
    author_email="bhaskarpatel@gmail.com",
    description="OWASP TriSuElla Continuous Trust & Assurance Platform Validator CLI",
    py_modules=["trisu_validator"],
    entry_points={
        "console_scripts": [
            "trisu = trisu_validator:main",
            "trisuella = trisu_validator:main",
        ],
    },
)
