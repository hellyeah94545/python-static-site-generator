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
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)