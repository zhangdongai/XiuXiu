@echo off
echo ׼����ʼͬ������˱��

echo ����Ŀ���ļ���
set ServerTableFolder=..\..\..\..\..\cPyer\Config\
set PublicServerTablesFolder=..\..\ServerTables\

echo ת�����������ΪUTF8��ʽ��������


cd OtherTools\iconv
echo ����Ŀ¼�������

echo ��ʼ������ͨ��Դ
for /R %PublicServerTablesFolder% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f UTF-16 -t UTF-8 %PublicServerTablesFolder%%%~nxa > %ServerTableFolder%%%~nxa
	)
)




echo �ɹ�

pause
