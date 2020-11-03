#! /usr/bin/env python3

from pathlib import Path

class Site():
    """
    site class: TODO
    """

    def __init__(self, source, dest, parsers=None):
        """

        :param source: TODO
        :param dest: TODO
        """
        self.source = Path(self.source)
        self.dest = Path(self.dest)
        self.parsers = parsers or []


    def create_dir(self, path):
        """

        :return: TODO
        """
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        """

        :return: None
        """
        self.dest.mkdir(parents=True, exist_ok=True)

        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)

    def load_parser(self, extension):
        """
        load_parser
        :param extension:
        :return: valid parser
        """
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser
            
    def run_parser(self, path):
        """
        
        :return: None
        """
        parser = self.load_parser(path.suffix)
        if parser:
            parser.parse(path, source, dest)
        else:
            print ("Not Implemented")