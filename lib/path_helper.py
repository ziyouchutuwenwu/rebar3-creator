#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os


# different path
class PathHelper:

    @staticmethod
    def get_project_path(rel_path, project_name):
        return os.path.join(rel_path, project_name)


    @staticmethod
    def get_rebar_config_path(project_path, rebar_config_file_name):
        return os.path.join(project_path, rebar_config_file_name)


    @staticmethod
    def get_apps_basic_path(project_path, project_name, project_type):
        if project_type == "release":
            return os.path.join(project_path, "apps", project_name)
        else:
            return project_path


    @staticmethod
    def get_test_dir_path(project_path, project_name, project_type):
        return os.path.join(PathHelper.get_apps_basic_path(project_path, project_name, project_type), "test")


    @staticmethod
    def get_example_path(project_path, project_name, project_type):
        return os.path.join(PathHelper.get_apps_basic_path(project_path, project_name, project_type), "src", "example")


    @staticmethod
    def get_debug_path(project_path, project_name, project_type):
        return os.path.join(PathHelper.get_apps_basic_path(project_path, project_name, project_type), "src", "debug")