-module(reloading).

-export([reload/0]).
% -define(PROJECT_NAME, "XXX").

reload() ->
  % EBinDir = "./_build/default/lib/" ++ ?PROJECT_NAME ++ "/ebin/",
  % SrcFileList = filelib:fold_files("./src/", ".*.erl", true, fun(F, AccIn) -> [F | AccIn] end, []),
  SrcFileList = filelib:wildcard("src/**/*.erl"),

  lists:foreach(fun(SrcFile) ->
      FileName = filename:rootname(filename:basename(SrcFile)),
      ModNameAtom = list_to_existing_atom(FileName),
      case ModNameAtom of
        ?MODULE ->
          ignore;
        _ ->
          c:l(ModNameAtom)
          % case compile:file(SrcFile, {outdir, EBinDir}) of
          %   {ok, ModName} ->
          %     % code:delete(ModName),
          %     code:purge(ModName),
          %     code:load_file(ModName);
          %   _ ->
          %     io:format("模块 ~p 编译失败，请检查~n", [SrcFile])
          % end
      end
  end,
  SrcFileList).