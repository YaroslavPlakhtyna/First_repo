"""Для ініціалізації свого проекту створіть допоміжну функцію do_setup(args_dict),
яка буде викликати функцію setup з параметрами зі словника args_dict.

Структура словника для параметра args_dicts має бути наступною

{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}"""

from setuptools import setup


def do_setup(args_dict):
    name, version, description, url, author, author_email, license, packages = args_dict.values()

    setup(name=name,
        version=version,
        description=description,
        url=url,
        author=author,
        author_email=author_email,
        license=license,
        packages=packages
    )
          