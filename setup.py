from setuptools import find_packages, setup

setup(
    name="duckephant",
    version="0.0.1",
    description="",
    url="http://github.com/medialab/duckephant",
    author="Kelly Christensen",
    keywords="database",
    license="GPL-3.0",
    python_requires=">=3.11",
    packages=find_packages(exclude=["test"]),
    install_requires=[
        "blinker==1.7.0",
        "click==8.1.7",
        "Flask==3.0.0",
        "gunicorn==21.2.0",
        "itsdangerous==2.1.2",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.3",
        "packaging==23.2",
        "python-dotenv==1.0.0",
        "Werkzeug==3.0.1",
        "flask-wtf==1.2.1",
        "wtforms==3.1.1",
        "flask-sqlalchemy==3.1.1",
        "sqlalchemy==2.0.23",
        "typing-extensions==4.8.0",
        "flask-login==0.6.3",
        "psycopg2==2.9.9",
    ],
    extra_require={
        ":python_version<'3.11'": ["typing_extensions>=4.3"],
    },
    entry_points={
        "console_scripts": ["duckephant=app.run:main"],
    },
    zip_safe=True,
)
