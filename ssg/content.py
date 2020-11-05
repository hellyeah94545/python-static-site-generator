#! /usr/bin/env python3

import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    def __init__(self):
        """
        Init for Content
        """
        __delimiter = r"^(?:-|\+){3}\s*$"
        __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        """
        load method for Content
        :param cls:
        :param string:
        :return:
        """

        _, fm, content = cls˚.__regex.split(string, 2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)