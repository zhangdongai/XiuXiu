@echo off
echo 准备开始同步服务端表格

echo 设置目标文件夹
set ServerTableFolder=..\..\..\..\..\cPyer\Config\
set PublicServerTablesFolder=..\..\ServerTables\

echo 转化服务器表格为UTF8格式，并拷贝


cd OtherTools\iconv
echo 工具目录设置完成

echo 开始拷贝普通资源
for /R %PublicServerTablesFolder% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f UTF-16 -t UTF-8 %PublicServerTablesFolder%%%~nxa > %ServerTableFolder%%%~nxa
	)
)




echo 成功

pause
