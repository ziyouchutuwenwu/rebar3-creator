辅助rebar3的创建工程工具, 看需求更新

release为创建一键式app, 运行业务代码
app为app模块, 作为release的模块使用
lib为库
escript为独立运行的es脚本


idea内配置, 选项, 添加自定义工具
--------
```
name: compile
group: rebar3
Program: rebar3
parameters: compile
Working directory: $ProjectFileDir$
```

```
name: eunit
group: rebar3
Program: rebar3
parameters: eunit
Working directory: $ProjectFileDir$
```

```
name: ct
group: rebar3
Program: rebar3
parameters: ct
Working directory: $ProjectFileDir$
```

```
name: clean
group: rebar3
Program: sh
parameters: clean.sh
Working directory: $ProjectFileDir$
```

```
name: tar
group: rebar3
Program: rebar3
parameters: tar
Working directory: $ProjectFileDir$
```