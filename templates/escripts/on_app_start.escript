-module(on_app_start).

main(_Args) ->
  io:format("~n"),
  interprete_modules().

interprete_modules() ->
  int:ni(demo_sup),
  int:ni(demo_app),

  io:format("输入 int:interpreted(). 或者 il(). 查看模块列表~n").