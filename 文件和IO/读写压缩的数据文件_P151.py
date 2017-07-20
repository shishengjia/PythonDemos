# -*- coding: utf-8 -*-
"""
gzip
"""

import gzip

with gzip.open('file.gz', 'wt') as f:
    f.write('Hello')

with gzip.open('file.gz', 'rt') as f:
    print(f.read())

"""
bz2
"""

import bz2

with bz2.open('file.bz2', 'wt') as f:
    f.write('Hello World')

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())
