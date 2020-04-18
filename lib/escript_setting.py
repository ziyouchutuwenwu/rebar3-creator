#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

# escipt
class EscriptSetting:
    def __init__(self, dir_path):
        self.__module_path = dir_path

    def writeEscriptTemplate(self, escriptFileName):

        module_name = os.path.splitext(escriptFileName)[0]
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

        fullPath = os.path.join(self.__module_path, escriptFileName)
        file = open(fullPath, "w+")
        file.write(content)
        file.close()