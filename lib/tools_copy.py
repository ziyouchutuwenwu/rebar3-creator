#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import shutil


class ToolsCopy:

    @staticmethod
    def copy_tools_to_project_dir(project_dir):
        base_dir = os.path.dirname(__file__) + "/../"
        tools_dir = base_dir + './tools/'
        dist_dir = project_dir + "/tools/"
        shutil.copytree(tools_dir, dist_dir)
