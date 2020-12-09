#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os


# global rebar3 config for auto compiling
class GlobalRebar3Config:
    @staticmethod
    def remove_config():
        os.system("rm -rf ~/.config/rebar3")

    @staticmethod
    def set_config():
        os.system("mkdir -p ~/.config/rebar3")
        os.system('echo  "{plugins, [rebar3_auto]}." > ~/.config/rebar3/rebar.config')
