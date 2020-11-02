#! /usr/bin/env python3

from typing import List
from pathlib import Path


class Parser():
    '''
    TODO
    '''

    def __init__(self):
        '''
        TODO
        '''
        extensions:  List[str] = []

    def valid_extension(self, extension):
        '''
        TODO
        :return: boolean
        '''
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        '''
        Base parse method for subclasses
        :param path: path of files
        :param source: source path of files
        :param dest: destination path of files
        :return: None
        '''
        raise NotImplementedError

    def read(self, path):
        '''
        Reads files
        :return: file text
        '''

        with open(path, 'r') as file:
            return file.read()

    def write(self, path, dest, content, ext='.html'):
        '''
        writes contents to file
        :param path: path of file to write
        :return: None
        '''
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'wr') as file:
            file.write(content)
