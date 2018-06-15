//This code create by CodeEngine

using System.IO;
 using System;
 #if UNITY_WP8 
 using UnityPortSocket; 
 #else 
 using System.Net.Sockets; 
 #endif 
 using Google.ProtocolBuffers;
public abstract class PacketDistributed
 {
 public static PacketDistributed CreatePacket(MessageID packetID)
 {
 PacketDistributed packet = null;
 switch (packetID)
 {
 case MessageID.PACKET_CG_ABANDONMISSION: { packet = new CG_ABANDONMISSION(); } break;
case MessageID.PACKET_CG_ACCEPTMISSION: { packet = new CG_ACCEPTMISSION(); } break;
case MessageID.PACKET_CG_ASK_SETCOMMONFLAG: { packet = new CG_ASK_SETCOMMONFLAG(); } break;
case MessageID.PACKET_CG_COMPLETEMISSION: { packet = new CG_COMPLETEMISSION(); } break;
case MessageID.PACKET_CG_CONNECTED_HEARTBEAT: { packet = new CG_CONNECTED_HEARTBEAT(); } break;
case MessageID.PACKET_CG_CREATEROLE: { packet = new CG_CREATEROLE(); } break;
case MessageID.PACKET_CG_ENTER_SCENE_OK: { packet = new CG_ENTER_SCENE_OK(); } break;
case MessageID.PACKET_CG_LOGIN: { packet = new CG_LOGIN(); } break;
case MessageID.PACKET_CG_MOVE: { packet = new CG_MOVE(); } break;
case MessageID.PACKET_CG_PING: { packet = new CG_PING(); } break;
case MessageID.PACKET_CG_REQ_CHANGE_SCENE: { packet = new CG_REQ_CHANGE_SCENE(); } break;
case MessageID.PACKET_CG_REQ_RANDOMNAME: { packet = new CG_REQ_RANDOMNAME(); } break;
case MessageID.PACKET_CG_SELECTROLE: { packet = new CG_SELECTROLE(); } break;
case MessageID.PACKET_CG_SYNC_POS: { packet = new CG_SYNC_POS(); } break;
case MessageID.PACKET_GC_ABANDONMISSION_RET: { packet = new GC_ABANDONMISSION_RET(); } break;
case MessageID.PACKET_GC_ACCEPTMISSION_RET: { packet = new GC_ACCEPTMISSION_RET(); } break;
case MessageID.PACKET_GC_ASK_COMMONFLAG_RET: { packet = new GC_ASK_COMMONFLAG_RET(); } break;
case MessageID.PACKET_GC_BROADCAST_ATTR: { packet = new GC_BROADCAST_ATTR(); } break;
case MessageID.PACKET_GC_COMPLETEMISSION_RET: { packet = new GC_COMPLETEMISSION_RET(); } break;
case MessageID.PACKET_GC_CONNECTED_HEARTBEAT: { packet = new GC_CONNECTED_HEARTBEAT(); } break;
case MessageID.PACKET_GC_CREATEROLE_RET: { packet = new GC_CREATEROLE_RET(); } break;
case MessageID.PACKET_GC_CREATE_PLAYER: { packet = new GC_CREATE_PLAYER(); } break;
case MessageID.PACKET_GC_DELETE_OBJ: { packet = new GC_DELETE_OBJ(); } break;
case MessageID.PACKET_GC_ENTER_SCENE: { packet = new GC_ENTER_SCENE(); } break;
case MessageID.PACKET_GC_LOGIN_QUEUE_STATUS: { packet = new GC_LOGIN_QUEUE_STATUS(); } break;
case MessageID.PACKET_GC_LOGIN_RET: { packet = new GC_LOGIN_RET(); } break;
case MessageID.PACKET_GC_MISSION_PARAM: { packet = new GC_MISSION_PARAM(); } break;
case MessageID.PACKET_GC_MISSION_STATE: { packet = new GC_MISSION_STATE(); } break;
case MessageID.PACKET_GC_MISSION_SYNC_MISSIONLIST: { packet = new GC_MISSION_SYNC_MISSIONLIST(); } break;
case MessageID.PACKET_GC_MOVE: { packet = new GC_MOVE(); } break;
case MessageID.PACKET_GC_NOTICE: { packet = new GC_NOTICE(); } break;
case MessageID.PACKET_GC_RET_PING: { packet = new GC_RET_PING(); } break;
case MessageID.PACKET_GC_RET_RANDOMNAME: { packet = new GC_RET_RANDOMNAME(); } break;
case MessageID.PACKET_GC_SELECTROLE_RET: { packet = new GC_SELECTROLE_RET(); } break;
case MessageID.PACKET_GC_STOP: { packet = new GC_STOP(); } break;
case MessageID.PACKET_GC_SYNC_COMMONDATA: { packet = new GC_SYNC_COMMONDATA(); } break;
case MessageID.PACKET_GC_SYNC_COMMONFLAG: { packet = new GC_SYNC_COMMONFLAG(); } break;
case MessageID.PACKET_GC_SYNC_POS: { packet = new GC_SYNC_POS(); } break;
case MessageID.PACKET_GC_SYN_ATTR: { packet = new GC_SYN_ATTR(); } break;
 
 }
 if (null != packet)
 {
 packet.packetID = packetID;
 }
 return packet;
 }
 public void SendPacket()
 {
 NetWorkLogic.GetMe().SendPacket(this); 
 }
 
 public PacketDistributed ParseFrom(byte[] data, int nLen)
 {
 CodedInputStream input = CodedInputStream.CreateInstance(data,0,nLen);
 PacketDistributed inst = MergeFrom(input,this);
 input.CheckLastTagWas(0);
 return inst;
 }
 
 public abstract int SerializedSize();
 public abstract void WriteTo(CodedOutputStream data);
 public abstract PacketDistributed MergeFrom(CodedInputStream input,PacketDistributed _Inst);
 public abstract bool IsInitialized();
 
 public MessageID GetPacketID() { return packetID; }
 protected MessageID packetID;
 }
