@echo off
echo ׼����ʼͬ������˱��

echo ����Ŀ���ļ���
set ClientTableFolder=..\..\ClientTables\
set PublicTableFolder=..\..\PublicTables\
set ServerTableFolder=..\..\ServerTables\
set TempFolder=..\..\1\
set TempFolder2=..\..\2\
set TempFolder3=..\..\3\
md 1
md 2
md 3


cd OtherTools\iconv
echo ����Ŀ¼�������
echo %TempFolder%

pause

echo ��ʼ������ͨ��Դ
for /R %ClientTableFolder% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f GBK -t UTF-16 %ClientTableFolder%%%~nxa > %TempFolder%%%~nxa
	)
)


for /R %TempFolder% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f UTF-16BE -t UTF-16LE %TempFolder%%%~nxa > %ClientTableFolder%%%~nxa
	)
)

echo ��ʼ������ͨ��Դ
for /R %PublicTableFolder% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f GBK -t UTF-16 %PublicTableFolder%%%~nxa > %TempFolder2%%%~nxa
	)
)


for /R %TempFolder2% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f UTF-16BE -t UTF-16LE %TempFolder2%%%~nxa > %PublicTableFolder%%%~nxa
	)
)

echo ��ʼ������ͨ��Դ
for /R %ServerTableFolder% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f GBK -t UTF-16 %ServerTableFolder%%%~nxa > %TempFolder3%%%~nxa
	)
)

for /R %TempFolder3% %%s in (,*) do (
	for /f "delims=" %%a in ("%%s") do (
		iconv.exe -f UTF-16BE -t UTF-16LE %TempFolder3%%%~nxa > %ServerTableFolder%%%~nxa
	)
)


echo �ɹ�

pause
