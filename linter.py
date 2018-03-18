#
# linter.py
# Linter for SublimeLinter, a code checking framework for Sublime Text 3
#
# Written by Michał Sochoń <kaszpir@gmail.com>
# Copyright (c) 2018
#
# License: MIT
#

"""This module exports the Doc8 plugin class."""

from SublimeLinter.lint import Linter, util


class Doc8(Linter):
    """Provides an interface to doc8."""

    cmd = ('doc8', '${args}', '@')
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.8.0'
    regex = (
        r'^.+?:(?P<line>\d+): '
        r'(?P<error>[D]\d+) '
        r'(?P<message>.+)'
    )
    multiline = False
    line_col_base = (1, 0)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    word_re = None

    defaults = {
        'selector': 'text.restructuredtext',
        'working_dir': '${folder:file_path}',
        'args': '-q',
    }
