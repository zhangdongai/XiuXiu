@echo off
echo ׼����ʼͬ���ͻ��˱��

echo ����Ŀ���ļ���
set ClientTableFolder=../Client/Assets/BundleAssets/Tables/
set PublicClientFolder=./ClientTables/

set ClientTableFolder_TW=../Client/Assets/International/TW/R_BundleAssets/Tables/
set PublicClientFolder_TW=./ClientTables_TW/

echo �뽫�����ļ����뵽ͬ��ClientTablesĿ¼��

echo ת���ͻ���txtΪUTF8��ʽ��������

if %PROCESSOR_ARCHITECTURE%==x86 goto p1 else goto p2

:p2
echo x64������...
start ./OtherTools/TxtConvExe_64/TxtConvWin7_64.exe   %PublicClientFolder% %ClientTableFolder%
start ./OtherTools/TxtConvExe_64/TxtConvWin7_64.exe   %PublicClientFolder_TW% %ClientTableFolder_TW%
goto ep

:p1
echo x86������...
start ./OtherTools//TxtConvExe/TxtConv.exe  %PublicClientFolder% %ClientTableFolder%
start ./OtherTools//TxtConvExe/TxtConv.exe  %PublicClientFolder_TW% %ClientTableFolder_TW%
goto ep

:ep
echo �ɹ�

pause