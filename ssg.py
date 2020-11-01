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
    Site(**config).build()

typer.run(main)
