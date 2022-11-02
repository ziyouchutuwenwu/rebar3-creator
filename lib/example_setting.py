#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os


class ExampleSetting:

    @staticmethod
    def create_dir(example_dir_path):
        is_exists = os.path.exists(example_dir_path)
        if not is_exists:
            os.makedirs(example_dir_path)
        return
