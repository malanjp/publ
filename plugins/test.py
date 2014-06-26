#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class BasePlugin(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def before(self):
        pass

    @abstractmethod
    def after(self);
        pass

    @abstractmethod
    def run(self):
        pass


class TestPlugin(BasePlugin):
    def before(self):
        print('before')

    def after(self):
        print('after')

    def run(self):
        print('run')



