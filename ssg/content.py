#! /usr/bin/env python3

import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):

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
        _, fm, content = cls.__regex.split(string, 2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        """
        Init for Content
        """
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        if "type" in self.data.keys():
            return self.data["type"]
        else:
            return None

