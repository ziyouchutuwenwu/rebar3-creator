#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

# eunit
class TestTemplateSetting:
    def __init__(self, dir_path):
        self.__module_path = dir_path

    def writeEunitTemplate(self, eunit_template_file_name):
        self.check_dir()

        moduleName = os.path.splitext(eunit_template_file_name)[0]
        content = "-module(%s).\r\n" % (moduleName)

        content += "\r\n"
        content += '-include_lib("eunit/include/eunit.hrl").\r\n'
        content += "\r\n"
        content += "simple_test() ->\r\n"
        content += "    ?assert(true)."

        full_path = os.path.join(self.__module_path, eunit_template_file_name)
        file = open(full_path, "w+")
        file.write(content)
        file.close()

    def writeCtTemplate(self, ct_template_file_name):
        self.check_dir()

        module_name = os.path.splitext(ct_template_file_name)[0]

        content = (
            "%% http://erlang.org/doc/apps/common_test/write_test_chapter.html\r\n"
        )
        content += "-module(%s).\r\n" % (module_name)

        content += "\r\n"
        content += '-include_lib("common_test/include/ct.hrl").\r\n'
        content += "\r\n"
        content += "-compile(export_all).\r\n"
        content += "\r\n"

        content += "suite() ->\r\n"
        content += "  [\r\n"
        content += "    {timetrap, {seconds, 20}},\r\n"
        content += "      {userdata,[\r\n"
        content += '        {info, "this is a common test template."}\r\n'
        content += "      ]}\r\n"
        content += "  ].\r\n"

        content += "\r\n"
        content += "groups() ->\r\n"
        content += "  [\r\n"
        content += "    {my_group,\r\n"
        content += "      %% [parallel, {repeat, 10}],\r\n"
        content += "      [],\r\n"
        content += "      [test_case1, test_case2]}\r\n"
        content += "  ].\r\n"
        content += "\r\n"
        content += "all() ->\r\n"
        content += "  [\r\n"
        content += "    {group, my_group},\r\n"
        content += "    test_case3\r\n"
        content += "  ].\r\n"
        content += "\r\n"
        content += "init_per_suite(Config) ->\r\n"
        content += '  ct:log("init_per_suite~n"),\r\n'
        content += "  Config.\r\n"
        content += "\r\n"
        content += "end_per_suite(_Config) ->\r\n"
        content += '  ct:log("end_per_suite~n"),\r\n'
        content += "  ok.\r\n"
        content += "\r\n"
        content += "init_per_group(Group, Config) ->\r\n"
        content += '  ct:log("init_per_group~p~n",[Group]),\r\n'
        content += "  Config.\r\n"
        content += "\r\n"
        content += "end_per_group(Group, Config) ->\r\n"
        content += '  ct:log("end_per_group~p~n",[Group]),\r\n'
        content += "  Config.\r\n"
        content += "\r\n"
        content += "init_per_testcase(TestCase, Config) ->\r\n"
        content += '  ct:log("init_per_testcase~p~n",[TestCase]),\r\n'
        content += "  Config.\r\n"
        content += "\r\n"
        content += "end_per_testcase(TestCase, Config) ->\r\n"
        content += '  ct:log("end_per_testcase~p~n",[TestCase]),\r\n'
        content += "  Config.\r\n"
        content += "\r\n"
        content += "%% --------------------------------------------------------\r\n"
        content += "test_case1(_Config) ->\r\n"
        content += '  ct:log("in test_case1~n"),\r\n'
        content += '  {skip, "Not implemented."}.\r\n'
        content += "\r\n"
        content += "test_case2(_Config) ->\r\n"
        content += '  ct:log("in test_case2~n"),\r\n'
        content += "  1=1.\r\n"
        content += "\r\n"
        content += "test_case3(_Config) ->\r\n"
        content += '  ct:log("in test_case3~n"),\r\n'
        content += "  1=1.\r\n"
        content += "\r\n"
        content += "test_case4(_Config) ->\r\n"
        content += '  ct:log("in test_case4~n"),\r\n'
        content += "  1=1."

        fullPath = os.path.join(self.__module_path, ct_template_file_name)
        file = open(fullPath, "w+")
        file.write(content)
        file.close()

    def check_dir(self):
        is_existed = os.path.exists(self.__module_path)
        if not is_existed:
            os.makedirs(self.__module_path)
        return