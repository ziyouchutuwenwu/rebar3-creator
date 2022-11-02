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
    def copy_debug_essentials_to_project_dir(project_dir, project_name):
        base_dir = os.path.dirname(__file__) + "/../"
        src_dir = os.path.join(base_dir, "templates", "debug")
        dist_dir = os.path.join(project_dir, "src/debug")
        shutil.copytree(src_dir, dist_dir)
        # 修改 reloading 文件内模块名
        reloading_file_name = os.path.join(dist_dir, "reloading.erl")
        cmd = "sed -i 's/XXX/%s/g' %s" % (project_name, reloading_file_name)
        os.system(cmd)

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
        dist_dir = os.path.join(project_dir, "escripts")
        shutil.copytree(src_dir, dist_dir)

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
    def copy_crypt_key_to_project_dir(project_dir):
        base_dir = os.path.dirname(__file__) + "/../"
        src_file = os.path.join(base_dir, "templates", "crypt_key", "erlang.crypt")
        dist_dir = os.path.join(project_dir, ".erlang.crypt")
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