-module(reloading).

-export([reload/0]).
-define(PROJECT_NAME, "XXX").

reload() ->
  EBinDir = "./_build/default/lib/" ++ ?PROJECT_NAME ++ "/ebin/",
  SrcFileList = filelib:fold_files("./src/", ".*.erl", true, fun(F, AccIn) -> [F | AccIn] end, []),

  lists:foreach(fun(File) ->
      ModName = filename:rootname(filename:basename(File)),
      ModAtom = list_to_atom(ModName),

      case ModAtom of
        ?MODULE -> ignore;
        _ ->
          compile:file(File, {outdir, EBinDir}),
          code:delete(ModAtom),
          code:purge(ModAtom),
          code:load_file(ModAtom)
      end
  end,
  SrcFileList).