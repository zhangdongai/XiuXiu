@echo off
echo ׼����ʼ�������

echo ����Ŀ���ļ���

set ServerTableFolder=..\..\Server\Config\
set ServerTableFolder_Internation=..\..\Server\Config_VN\

set ClientTableFolder=..\..\Client\Assets\BundleAssets\Tables\
set PublicTableFolder=..\PublicTables\

set ClientTableFolder_Internation=..\..\Client\International\VN\R_BundleAssets\Tables\
set PublicTableFolder_Internation=.\PublicTables\

echo �뽫�����ļ����뵽ͬ��PublicTablesĿ¼��

echo �����ͻ������ݱ�
copy %PublicTableFolder% %ClientTableFolder%
copy %PublicTableFolder_Internation% %ClientTableFolder_Internation%
copy %PublicTableFolder_Internation% %ClientTableFolder%

echo ������ת�����������ݱ� 


cd ..\OtherTools\iconv
echo ����Ŀ¼�������

echo ��ʼ������ͨ��Դ
for /R ..\%PublicTableFolder% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f UTF-16 -t UTF-8 ..\%PublicTableFolder%%%~nxa > ..\%ServerTableFolder%%%~nxa
	)
)


echo ��ʼ����Internation��Դ
for /R ..\..\Tables_VN\%PublicTableFolder_Internation% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f UTF-16 -t UTF-8 ..\..\Tables_VN\%PublicTableFolder_Internation%%%~nxa > ..\..\Tables_VN\%ServerTableFolder_Internation%%%~nxa
	)
)

copy ..\..\Tables_VN\%ServerTableFolder_Internation% ..\..\Tables_VN\%ServerTableFolder%

echo ����

pause
