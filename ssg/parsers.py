#! /usr/bin/env python3

import shutil
import sys
from typing import List
from pathlib import Path
from docutils.core import publish_parts
from markdown import markdown
from ssg.content import Content


class Parser:
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
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        '''
        Base parse method for subclasses
        :param path: path of files
        :param source: source path of files
        :param dest: destination path of files
        :return: None
        '''
        self.copy(path, source, dest)


class MarkdownParser(Parser):
    """
    class
    """
    extensions = [".md", ".markdown"]

    def parse(self, path: Path, source: Path, dest: Path):
        '''

        :param path: path of files
        :param source: source path of files
        :param dest: destination path of files
        :return: None
        '''
        content = Content.load(self.read(path))
        html = markdown(content.body)
        self.write(path, dest, html)
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n".format
                         (path.name, content))


class ReStructuredTextParser(Parser):
    """
    class
    """
    extensions = [".rst"]

    def parse(self, path: Path, source: Path, dest: Path):
        '''

        :param path: path of files
        :param source: source path of files
        :param dest: destination path of files
        :return: None
        '''
        content = Content.load(self.read(path))
        html = publish_parts(content.body, writer_name="html5")
        self.write(path, dest, html["html_body"])
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n". format
                         (path.name, content))
