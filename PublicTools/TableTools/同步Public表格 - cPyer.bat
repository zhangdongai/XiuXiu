@echo off
echo 准备开始拷贝表格

echo 设置目标文件夹

set ServerTableFolder=..\..\Server\Config\
set ServerTableFolder_Internation=..\..\Server\Config_VN\

set ClientTableFolder=..\..\Client\Assets\BundleAssets\Tables\
set PublicTableFolder=..\PublicTables\

set ClientTableFolder_Internation=..\..\Client\International\VN\R_BundleAssets\Tables\
set PublicTableFolder_Internation=.\PublicTables\

echo 请将公用文件放入到同级PublicTables目录下

echo 拷贝客户端数据表
copy %PublicTableFolder% %ClientTableFolder%
copy %PublicTableFolder_Internation% %ClientTableFolder_Internation%
copy %PublicTableFolder_Internation% %ClientTableFolder%

echo 拷贝并转换服务器数据表 


cd ..\OtherTools\iconv
echo 工具目录设置完成

echo 开始拷贝普通资源
for /R ..\%PublicTableFolder% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f UTF-16 -t UTF-8 ..\%PublicTableFolder%%%~nxa > ..\%ServerTableFolder%%%~nxa
	)
)


echo 开始拷贝Internation资源
for /R ..\..\Tables_VN\%PublicTableFolder_Internation% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f UTF-16 -t UTF-8 ..\..\Tables_VN\%PublicTableFolder_Internation%%%~nxa > ..\..\Tables_VN\%ServerTableFolder_Internation%%%~nxa
	)
)

copy ..\..\Tables_VN\%ServerTableFolder_Internation% ..\..\Tables_VN\%ServerTableFolder%

echo 结束

pause
