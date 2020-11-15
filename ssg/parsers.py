#! /usr/bin/env python3

import shutil
import sys
from typing import List
from pathlib import Path
from docutils.core import publish_parts
from markdown import markdown
from ssg.content import Content


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
        with open(full_path, 'w') as file:
            file.write(content)

    def copy(self, path, source, dest):
        '''
        copy contents
        :return: None
        '''
        shutil.copy2(path, dest / path.relative_to(source), follow_symlinks=True)


class ResourceParser(Parser):
    '''
    TODO
    '''

    def __init__(self):
        '''
        class init
        '''
        extensions = [".jpg", ".png", ".gif", ".css", ".html"]


    def parse(self, path: Path, source: Path, dest: Path):
        '''
        Base parse method for subclasses
        :param path: path of files
        :param source: source path of files
        :param dest: destination path of files
        :return: None
        '''
        self.copy(self, path, source, dest)


class MarkdownParser():
    """
    class
    """
    extensions = [".md", ".markdown"]
