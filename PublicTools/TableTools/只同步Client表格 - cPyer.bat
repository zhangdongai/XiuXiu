@echo off
echo ׼����ʼͬ���ͻ��˱��

echo ����Ŀ���ļ���
set ClientTableFolder=..\..\Client\Assets\BundleAssets\Tables\
set PublicClientFolder=..\ClientTables\

set ClientTableFolder_Internation=..\..\Client\International\VN\R_BundleAssets\Tables\
set PublicClientFolder_Internation=.\ClientTables\

echo �뽫�����ļ����뵽ͬ��ClientTablesĿ¼��

echo �����ݱ��ļ��������ͻ�������Ŀ¼

copy %PublicClientFolder% %ClientTableFolder%
copy %PublicClientFolder_Internation% %ClientTableFolder_Internation%
copy %PublicClientFolder_Internation% %ClientTableFolder%

echo ����


pause