@echo off
echo 准备开始同步客户端表格

echo 设置目标文件夹
set ClientTableFolder=..\..\Client\Assets\BundleAssets\Tables\
set PublicClientFolder=..\ClientTables\

set ClientTableFolder_Internation=..\..\Client\International\VN\R_BundleAssets\Tables\
set PublicClientFolder_Internation=.\ClientTables\

echo 请将公用文件放入到同级ClientTables目录下

echo 将数据表文件拷贝到客户端运行目录

copy %PublicClientFolder% %ClientTableFolder%
copy %PublicClientFolder_Internation% %ClientTableFolder_Internation%
copy %PublicClientFolder_Internation% %ClientTableFolder%

echo 结束


pause