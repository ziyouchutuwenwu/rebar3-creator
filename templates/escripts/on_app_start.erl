-module(on_app_start).

-export([main/1]).

main(_Args) ->
  io:format("~n"),
  io:format("请在 bash 命令行运行 ./tools/debug_enhancer~n"),
  io:format("~n").