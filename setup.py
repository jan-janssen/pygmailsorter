"""
Setuptools based setup module
"""
from setuptools import setup, find_packages
from pathlib import Path
import versioneer


setup(
    name="gmailsorter",
    version=versioneer.get_version(),
    description="Assign labels to emails in Google Mail based on their similarity to other emails assigned to the same label.",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/jan-janssen/gmailsorter",
    author="Jan Janssen",
    author_email="jan.janssen@outlook.com",
    license="BSD",
    packages=find_packages(exclude=["*tests*"]),
    package_data={
        'gmailsorter': [
            'webapp/static/css/*.css',
            'webapp/static/fonts/poppins/*.ttf',
            'webapp/static/images/*.jpg',
            'webapp/static/images/icons/*.ico',
            'webapp/templates/*.html'
        ],
    },
    install_requires=[
        "google-api-python-client==2.135.0",
        "google-auth==2.30.0",
        "google-auth-oauthlib==1.2.0",
        "numpy==2.0.0",
        "tqdm==4.66.4",
        "pandas==2.2.2",
        "scikit-learn==1.5.0",
        "sqlalchemy==2.0.31",
    ],
    extras_require={
        "webapp": ['gunicorn==22.0.0', "flask==3.0.3", "flask-login==0.6.3"],
    },
    cmdclass=versioneer.get_cmdclass(),
    entry_points={
            "console_scripts": [
                'gmailsorter=gmailsorter.__main__:command_line_parser',
                'gmailsorter-daemon=gmailsorter.daemon.__main__:command_line_parser',
                'gmailsorter-app=gmailsorter.webapp.app:run_app'
            ]
    }
)
