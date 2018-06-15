//This code create by CodeEngine Author:Wendy ,don't modify

namespace SPacket.SocketInstance
 {
 public class PacketFactoryManagerInstance : PacketFactoryManager
 {
 public override bool Init ()
 {
 AddFactory(new GC_RET_PING_PF());
AddFactory(new GC_LOGIN_RET_PF());
AddFactory(new GC_LOGIN_QUEUE_STATUS_PF());
AddFactory(new GC_CREATEROLE_RET_PF());
AddFactory(new GC_SELECTROLE_RET_PF());
AddFactory(new GC_RET_RANDOMNAME_PF());
AddFactory(new GC_ENTER_SCENE_PF());
AddFactory(new GC_CONNECTED_HEARTBEAT_PF());
AddFactory(new GC_NOTICE_PF());
AddFactory(new GC_MISSION_SYNC_MISSIONLIST_PF());
AddFactory(new GC_ACCEPTMISSION_RET_PF());
AddFactory(new GC_COMPLETEMISSION_RET_PF());
AddFactory(new GC_ABANDONMISSION_RET_PF());
AddFactory(new GC_MISSION_STATE_PF());
AddFactory(new GC_MISSION_PARAM_PF());
AddFactory(new GC_CREATE_PLAYER_PF());
AddFactory(new GC_DELETE_OBJ_PF());
AddFactory(new GC_SYNC_POS_PF());
AddFactory(new GC_MOVE_PF());
AddFactory(new GC_STOP_PF());
AddFactory(new GC_BROADCAST_ATTR_PF());
AddFactory(new GC_SYN_ATTR_PF());
AddFactory(new GC_SYNC_COMMONDATA_PF());
AddFactory(new GC_SYNC_COMMONFLAG_PF());
AddFactory(new GC_ASK_COMMONFLAG_RET_PF());
AddFactory(new CG_PING_PF());
AddFactory(new CG_LOGIN_PF());
AddFactory(new CG_CREATEROLE_PF());
AddFactory(new CG_SELECTROLE_PF());
AddFactory(new CG_REQ_RANDOMNAME_PF());
AddFactory(new CG_REQ_CHANGE_SCENE_PF());
AddFactory(new CG_ENTER_SCENE_OK_PF());
AddFactory(new CG_CONNECTED_HEARTBEAT_PF());
AddFactory(new CG_ACCEPTMISSION_PF());
AddFactory(new CG_COMPLETEMISSION_PF());
AddFactory(new CG_ABANDONMISSION_PF());
AddFactory(new CG_SYNC_POS_PF());
AddFactory(new CG_MOVE_PF());
AddFactory(new CG_ASK_SETCOMMONFLAG_PF());
 AddPacketHander(MessageID.PACKET_GC_RET_PING, new GC_RET_PINGHandler());
AddPacketHander(MessageID.PACKET_GC_LOGIN_RET, new GC_LOGIN_RETHandler());
AddPacketHander(MessageID.PACKET_GC_LOGIN_QUEUE_STATUS, new GC_LOGIN_QUEUE_STATUSHandler());
AddPacketHander(MessageID.PACKET_GC_CREATEROLE_RET, new GC_CREATEROLE_RETHandler());
AddPacketHander(MessageID.PACKET_GC_SELECTROLE_RET, new GC_SELECTROLE_RETHandler());
AddPacketHander(MessageID.PACKET_GC_RET_RANDOMNAME, new GC_RET_RANDOMNAMEHandler());
AddPacketHander(MessageID.PACKET_GC_ENTER_SCENE, new GC_ENTER_SCENEHandler());
AddPacketHander(MessageID.PACKET_GC_CONNECTED_HEARTBEAT, new GC_CONNECTED_HEARTBEATHandler());
AddPacketHander(MessageID.PACKET_GC_NOTICE, new GC_NOTICEHandler());
AddPacketHander(MessageID.PACKET_GC_MISSION_SYNC_MISSIONLIST, new GC_MISSION_SYNC_MISSIONLISTHandler());
AddPacketHander(MessageID.PACKET_GC_ACCEPTMISSION_RET, new GC_ACCEPTMISSION_RETHandler());
AddPacketHander(MessageID.PACKET_GC_COMPLETEMISSION_RET, new GC_COMPLETEMISSION_RETHandler());
AddPacketHander(MessageID.PACKET_GC_ABANDONMISSION_RET, new GC_ABANDONMISSION_RETHandler());
AddPacketHander(MessageID.PACKET_GC_MISSION_STATE, new GC_MISSION_STATEHandler());
AddPacketHander(MessageID.PACKET_GC_MISSION_PARAM, new GC_MISSION_PARAMHandler());
AddPacketHander(MessageID.PACKET_GC_CREATE_PLAYER, new GC_CREATE_PLAYERHandler());
AddPacketHander(MessageID.PACKET_GC_DELETE_OBJ, new GC_DELETE_OBJHandler());
AddPacketHander(MessageID.PACKET_GC_SYNC_POS, new GC_SYNC_POSHandler());
AddPacketHander(MessageID.PACKET_GC_MOVE, new GC_MOVEHandler());
AddPacketHander(MessageID.PACKET_GC_STOP, new GC_STOPHandler());
AddPacketHander(MessageID.PACKET_GC_BROADCAST_ATTR, new GC_BROADCAST_ATTRHandler());
AddPacketHander(MessageID.PACKET_GC_SYN_ATTR, new GC_SYN_ATTRHandler());
AddPacketHander(MessageID.PACKET_GC_SYNC_COMMONDATA, new GC_SYNC_COMMONDATAHandler());
AddPacketHander(MessageID.PACKET_GC_SYNC_COMMONFLAG, new GC_SYNC_COMMONFLAGHandler());
AddPacketHander(MessageID.PACKET_GC_ASK_COMMONFLAG_RET, new GC_ASK_COMMONFLAG_RETHandler());
AddPacketHander(MessageID.PACKET_CG_PING, new CG_PINGHandler());
AddPacketHander(MessageID.PACKET_CG_LOGIN, new CG_LOGINHandler());
AddPacketHander(MessageID.PACKET_CG_CREATEROLE, new CG_CREATEROLEHandler());
AddPacketHander(MessageID.PACKET_CG_SELECTROLE, new CG_SELECTROLEHandler());
AddPacketHander(MessageID.PACKET_CG_REQ_RANDOMNAME, new CG_REQ_RANDOMNAMEHandler());
AddPacketHander(MessageID.PACKET_CG_REQ_CHANGE_SCENE, new CG_REQ_CHANGE_SCENEHandler());
AddPacketHander(MessageID.PACKET_CG_ENTER_SCENE_OK, new CG_ENTER_SCENE_OKHandler());
AddPacketHander(MessageID.PACKET_CG_CONNECTED_HEARTBEAT, new CG_CONNECTED_HEARTBEATHandler());
AddPacketHander(MessageID.PACKET_CG_ACCEPTMISSION, new CG_ACCEPTMISSIONHandler());
AddPacketHander(MessageID.PACKET_CG_COMPLETEMISSION, new CG_COMPLETEMISSIONHandler());
AddPacketHander(MessageID.PACKET_CG_ABANDONMISSION, new CG_ABANDONMISSIONHandler());
AddPacketHander(MessageID.PACKET_CG_SYNC_POS, new CG_SYNC_POSHandler());
AddPacketHander(MessageID.PACKET_CG_MOVE, new CG_MOVEHandler());
AddPacketHander(MessageID.PACKET_CG_ASK_SETCOMMONFLAG, new CG_ASK_SETCOMMONFLAGHandler());
 return true;
 } 
 }
 

 

public class GC_ABANDONMISSION_RET_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_ABANDONMISSION_RET;
 }
 }
public class GC_ACCEPTMISSION_RET_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_ACCEPTMISSION_RET;
 }
 }
public class GC_ASK_COMMONFLAG_RET_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_ASK_COMMONFLAG_RET;
 }
 }
public class GC_BROADCAST_ATTR_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_BROADCAST_ATTR;
 }
 }
public class GC_COMPLETEMISSION_RET_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_COMPLETEMISSION_RET;
 }
 }
public class GC_CONNECTED_HEARTBEAT_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_CONNECTED_HEARTBEAT;
 }
 }
public class GC_CREATEROLE_RET_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_CREATEROLE_RET;
 }
 }
public class GC_CREATE_PLAYER_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_CREATE_PLAYER;
 }
 }
public class GC_DELETE_OBJ_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_DELETE_OBJ;
 }
 }
public class GC_ENTER_SCENE_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_ENTER_SCENE;
 }
 }
public class GC_LOGIN_QUEUE_STATUS_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_LOGIN_QUEUE_STATUS;
 }
 }
public class GC_LOGIN_RET_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_LOGIN_RET;
 }
 }
public class GC_MISSION_PARAM_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_MISSION_PARAM;
 }
 }
public class GC_MISSION_STATE_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_MISSION_STATE;
 }
 }
public class GC_MISSION_SYNC_MISSIONLIST_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_MISSION_SYNC_MISSIONLIST;
 }
 }
public class GC_MOVE_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_MOVE;
 }
 }
public class GC_NOTICE_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_NOTICE;
 }
 }
public class GC_RET_PING_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_RET_PING;
 }
 }
public class GC_RET_RANDOMNAME_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_RET_RANDOMNAME;
 }
 }
public class GC_SELECTROLE_RET_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_SELECTROLE_RET;
 }
 }
public class GC_STOP_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_STOP;
 }
 }
public class GC_SYNC_COMMONDATA_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_SYNC_COMMONDATA;
 }
 }
public class GC_SYNC_COMMONFLAG_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_SYNC_COMMONFLAG;
 }
 }
public class GC_SYNC_POS_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_SYNC_POS;
 }
 }
public class GC_SYN_ATTR_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_GC_SYN_ATTR;
 }
 }
public class CG_ABANDONMISSION_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_ABANDONMISSION;
 }
 }
public class CG_ACCEPTMISSION_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_ACCEPTMISSION;
 }
 }
public class CG_ASK_SETCOMMONFLAG_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_ASK_SETCOMMONFLAG;
 }
 }
public class CG_COMPLETEMISSION_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_COMPLETEMISSION;
 }
 }
public class CG_CONNECTED_HEARTBEAT_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_CONNECTED_HEARTBEAT;
 }
 }
public class CG_CREATEROLE_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_CREATEROLE;
 }
 }
public class CG_ENTER_SCENE_OK_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_ENTER_SCENE_OK;
 }
 }
public class CG_LOGIN_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_LOGIN;
 }
 }
public class CG_MOVE_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_MOVE;
 }
 }
public class CG_PING_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_PING;
 }
 }
public class CG_REQ_CHANGE_SCENE_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_REQ_CHANGE_SCENE;
 }
 }
public class CG_REQ_RANDOMNAME_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_REQ_RANDOMNAME;
 }
 }
public class CG_SELECTROLE_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_SELECTROLE;
 }
 }
public class CG_SYNC_POS_PF : PacketFactory
 {
 public MessageID GetPacketID()
 {
 return MessageID.PACKET_CG_SYNC_POS;
 }
 }
}
