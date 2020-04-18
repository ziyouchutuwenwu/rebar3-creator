#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

# different path
class PathHelper:
    @staticmethod
    def get_app_path(rel_path, project_name):
        return os.path.join(rel_path, project_name)

    @staticmethod
    def get_rebar_config_path(rel_path, project_name, rebar_config_file_name):
        return os.path.join(rel_path, project_name, rebar_config_file_name)

    @staticmethod
    def get_test_dir_path(rel_path, project_name, project_type):
        if project_type == "release":
            return os.path.join(rel_path, project_name, "apps", project_name, "test")
        else:
            return os.path.join(rel_path, project_name, "test")

    @staticmethod
    def get_example_path(rel_path, project_name, project_type):
        if project_type == "release":
            return os.path.join(
                rel_path, project_name, "apps", project_name, "src", "example"
            )
        else:
            return os.path.join(rel_path, project_name, "src", "example")