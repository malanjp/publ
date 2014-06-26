#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Publ

usage: publ [-h] <command> <params>...

option:
    -h, --help  show this help message and exit
"""

from docopt import docopt
import imp, os, sys
sys.path.append('./plugins')


class Plugin(object):
    plugin = None

    def load(self, module_name):
        try:
            file, pathname, description = imp.find_module(module_name)
        except ImportError:
            print "Failed to find module"
        try:
            self.plugin = imp.load_module(module_name, file, pathname, description)
        except ImportError:
            print "Failed to load module"


if __name__ == '__main__':
    args = docopt(__doc__)

    plugin = Plugin()
    plugin.load(args['<command>'])
    p = plugin.plugin.TestPlugin()
    print(p.run())

    for param in args['<params>']:
        print param


