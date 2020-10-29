#! /usr/bin/env python3

from pathlib import Path

class Site():
    '''
    site class: TODO
    '''

    def __init__(self, source, dest):
        '''

        :param source: TODO
        :param dest: TODO
        '''
        self.source = Path(self.source)
        self.dest = Path(self.dest)


    def create_dir(self, path):
        '''

        :return: TODO
        '''
        directory = self.dest.relative_to(self.source)
        Path.mkdir(directory, parents=True, exist_ok=True)