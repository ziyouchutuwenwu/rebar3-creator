-module(app_start).

-export([main/1]).
-export([interprete/0]).

main(_Args) ->
  io:format("~n").

interprete() ->
  % 如果有多个依赖项目，也只是在主模块里面调用一次
  int:i([M || {M, _} <- code:all_loaded(), not code:is_sticky(M), int:interpretable(M) =:= true]),
  io:format("输入 int:interpreted(). 或者 il(). 查看模块列表~n").