#! /usr/bin/env python3

import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    '''

    :param source:
    :param dest:
    :return:
    '''
    config = {"source": source, "dest": dest}

    newSite = Site(**config)
    newSit.build()