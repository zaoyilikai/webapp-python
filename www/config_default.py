#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Bill Li'

'''
Default configurations.
'''

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'webapp',
        'password': 'password',
        'db': 'webapp'
    },
    'session': {
        'secret': 'Webapp'
    }
}
