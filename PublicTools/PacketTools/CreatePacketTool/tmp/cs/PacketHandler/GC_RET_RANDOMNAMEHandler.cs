//This code create by CodeEngine

using System;
 using Module.Log;
 using Google.ProtocolBuffers;
 using System.Collections;
namespace SPacket.SocketInstance
 {
 public class GC_RET_RANDOMNAMEHandler : Ipacket
 {
 public uint Execute(PacketDistributed ipacket)
 {
 GC_RET_RANDOMNAME packet = (GC_RET_RANDOMNAME )ipacket;
 if (null == packet) return (uint)PACKET_EXE.PACKET_EXE_ERROR;
 //enter your logic
 return (uint)PACKET_EXE.PACKET_EXE_CONTINUE;
 }
 }
 }
