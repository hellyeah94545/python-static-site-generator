#! /usr/bin/env python3

import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    def __init__(self):
        """
        Init for Content
        """
        __delimeter = "^(?:-|\+{3}\s*$"
        __regex = re.compile(__delimeter, re.MULTILINE)

