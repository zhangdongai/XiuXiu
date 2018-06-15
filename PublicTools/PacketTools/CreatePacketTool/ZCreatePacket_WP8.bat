echo on

echo C++��CSharp��Ϣ����������V1.0

set homeford=%cd%
echo %homeford%
cd..
cd..
set workpath=%cd%
cd..
cd..
set ServerPath=%cd%
cd "%homeford%"

rem ����CppĿ���ļ���
set DstCppFolder=%ServerPath%\Server\Project\Server\Server\Server\Common\Packet

rem ����CsharpĿ���ļ���
set DstCSharpFolder=%workpath%\Client\Assets\MLDJ\Script\GameLogic\NetWork\PacketStream

rmdir /Q /S tmp

rem ����Դ�ļ��У����������ɵ�c++��csharp��Ϣ��
set SrcFolder=%homeford%\tmp

"%homeford%"\FigurePacket_WP8.exe -i:PBMessage.proto -s:0 -cpp -c#
"%homeford%"\protoc -I=./ --cpp_out=./tmp/cpp/Packet/ PBMessage.proto

"%homeford%"\CodeEngine_WP8.exe -i:PBMessage.proto -o:tmp\cs\PBMessage.cs -c:csharp
rem "%homeford%"\FigurePacket_WP8.exe -i:PBMessage.proto -s:0 -c#

copy /Y %SrcFolder%\cpp\Packet\*.* "%DstCppFolder%"\Packet\
copy /Y %SrcFolder%\cpp\PacketHandler\*.* "%DstCppFolder%"\PacketHandler\

copy /Y %SrcFolder%\cs\*.cs "%DstCSharpFolder%"\

cd "%homeford%"
echo Complete!

pause


