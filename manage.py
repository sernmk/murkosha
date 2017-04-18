#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a manage file for murkosha project.
"""

import os
import sys

__author__ = 'sobolevn'


def main():
    """ Main function. """
    from django.core.management import execute_from_command_line

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'murkosha.settings')
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
