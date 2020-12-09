#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import shutil
import os


class ProjectRebarConfig:
    def __init__(self, config_file):
        self.__config_file = config_file

    def append(self, content):
        file = open(self.__config_file, "a+")
        file.write(content)
        file.close()

    def replace(self, old_content, new_content):
        self.make_bak_file()

        bak_file = open(self.get_bak_file_name(), "r+")
        new_file = open(self.__config_file, "w+")

        for line in bak_file.readlines():
            if line.find(old_content) != -1:
                line = line.replace(old_content, new_content)
            new_file.write(line)
        bak_file.close()
        self.remove_bak_file()
        new_file.close()

    def make_bak_file(self):
        shutil.copyfile(self.__config_file, self.get_bak_file_name())

    def remove_bak_file(self):
        os.remove(self.get_bak_file_name())

    def get_bak_file_name(self):
        return self.__config_file + ".bak"
