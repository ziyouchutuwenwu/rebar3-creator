#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os


# escipt
class EscriptSetting:
    def __init__(self, dir_path):
        self.__module_path = dir_path

    def write_escript_template(self, escript_file_name):

        module_name = os.path.splitext(escript_file_name)[0]
        content = "-module(%s).\r\n" % (module_name)

        content += "\r\n"
        content += "-export([main/1]).\r\n"
        content += "\r\n"
        content += "main(Args) ->\r\n"
        content += '  io:format("~n"),\r\n'
        content += '  io:format("*********************************************************~n"),\r\n'
        content += '  io:format("on app start~n"),\r\n'
        content += '  io:format("*********************************************************~n"),\r\n'
        content += '  io:format("~n").'

        full_path = os.path.join(self.__module_path, escript_file_name)
        file = open(full_path, "w+")
        file.write(content)
        file.close()
