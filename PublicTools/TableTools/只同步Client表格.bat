@echo off
echo 准备开始同步客户端表格

echo 设置目标文件夹
set ClientTableFolder=../Client/Assets/BundleAssets/Tables/
set PublicClientFolder=./ClientTables/

set ClientTableFolder_TW=../Client/Assets/International/TW/R_BundleAssets/Tables/
set PublicClientFolder_TW=./ClientTables_TW/

echo 请将公用文件放入到同级ClientTables目录下

echo 转化客户端txt为UTF8格式，并拷贝

if %PROCESSOR_ARCHITECTURE%==x86 goto p1 else goto p2

:p2
echo x64处理中...
start ./OtherTools/TxtConvExe_64/TxtConvWin7_64.exe   %PublicClientFolder% %ClientTableFolder%
start ./OtherTools/TxtConvExe_64/TxtConvWin7_64.exe   %PublicClientFolder_TW% %ClientTableFolder_TW%
goto ep

:p1
echo x86处理中...
start ./OtherTools//TxtConvExe/TxtConv.exe  %PublicClientFolder% %ClientTableFolder%
start ./OtherTools//TxtConvExe/TxtConv.exe  %PublicClientFolder_TW% %ClientTableFolder_TW%
goto ep

:ep
echo 成功

pause