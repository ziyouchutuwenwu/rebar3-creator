#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import shutil


class CopyHelper:
    @staticmethod
    def copy_vscode_debug_config_to_project_dir(project_dir):
        base_dir = os.path.dirname(__file__) + "/../"
        src_dir = os.path.join(base_dir, "templates", "vscode")
        dist_dir = os.path.join(project_dir, ".vscode")
        shutil.copytree(src_dir, dist_dir)

    @staticmethod
    def copy_tools_to_project_dir(project_dir):
        base_dir = os.path.dirname(__file__) + "/../"
        src_dir = os.path.join(base_dir, "templates", "tools")
        dist_dir = os.path.join(project_dir, "tools")
        shutil.copytree(src_dir, dist_dir)

    @staticmethod
    def copy_escripts_to_project_dir(project_dir):
        base_dir = os.path.dirname(__file__) + "/../"
        src_dir = os.path.join(base_dir, "templates", "escripts")
        dist_dir = project_dir
        for root, _dirs, files in os.walk(src_dir):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, dist_dir)

    @staticmethod
    def copy_rebar_config_to_project_dir(project_dir):
        base_dir = os.path.dirname(__file__) + "/../"
        src_dir = os.path.join(base_dir, "templates", "rebar")
        dist_dir = project_dir
        for root, _dirs, files in os.walk(src_dir):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, dist_dir)

    @staticmethod
    def copy_readme_to_project_dir(project_dir):
        base_dir = os.path.dirname(__file__) + "/../"
        src_file = os.path.join(base_dir, "templates", "README.md")
        dist_dir = project_dir
        shutil.copy(src_file, dist_dir)

    @staticmethod
    def copy_tests_to_project_dir(project_dir):
        base_dir = os.path.dirname(__file__) + "/../"
        src_dir = os.path.join(base_dir, "templates", "test")
        dist_dir = os.path.join(project_dir, "test")
        shutil.copytree(src_dir, dist_dir)