#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Roman Bataev
# Copyright (c) 2015 Roman Bataev
#
# License: MIT
#

"""This module exports the Joker plugin class."""

from SublimeLinter.lint import Linter, util


class Joker(Linter):
    """Provides an interface to joker."""

    syntax = 'clojure'
    cmd = 'joker --parse --'
    executable = 'joker'
    # version_args = '--version'
    # version_re = r'(?P<version>\d+\.\d+\.\d+)'
    # version_requirement = '>= 1.0'

    # stdin:88:13: Read error: Invalid unicode escape: \uqwer
    regex = r'stdin:(?P<line>\d+):(?P<col>\d+): (?P<message>.*((?P<error>error|Exception)|(?P<warning>warning)).*)'

    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
