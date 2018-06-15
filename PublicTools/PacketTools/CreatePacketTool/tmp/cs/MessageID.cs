//This code create by CodeEngine ,don't modify

using System;
 public enum MessageID :ushort
 {
 PACKET_NONE = 0 , // 0£¬¿Õ
 PACKET_CG_LOGIN = 1, //client ask login 
 PACKET_GC_LOGIN_RET =2, //client login result 
 PACKET_CG_PING,	//Client send ping
PACKET_GC_RET_PING,	//sever return ping
PACKET_GC_LOGIN_QUEUE_STATUS,	//login queue status
PACKET_CG_CREATEROLE,	//client send createRole
PACKET_GC_CREATEROLE_RET,	//server send create role result
PACKET_CG_SELECTROLE,	//client send selectRole
PACKET_GC_SELECTROLE_RET,	//server send select role result
PACKET_CG_REQ_RANDOMNAME,	//Client Request Random Name
PACKET_GC_RET_RANDOMNAME,	//Server ret randomname
PACKET_CG_REQ_CHANGE_SCENE,	//Request Change Scene
PACKET_GC_ENTER_SCENE,	//Enter Scene
PACKET_CG_ENTER_SCENE_OK,	//Client Enter Scene OK
PACKET_CG_CONNECTED_HEARTBEAT,	//client connected heartbeat
PACKET_GC_CONNECTED_HEARTBEAT,	//server connected heartbeat
PACKET_GC_NOTICE,	//notice from server
PACKET_GC_MISSION_SYNC_MISSIONLIST,	//server send mission list to client
PACKET_CG_ACCEPTMISSION,	//ask to accept mission
PACKET_GC_ACCEPTMISSION_RET,	//result of accept mission
PACKET_CG_COMPLETEMISSION,	//ask to complete mission
PACKET_GC_COMPLETEMISSION_RET,	//result of complete mission
PACKET_CG_ABANDONMISSION,	//ask to abandon mission
PACKET_GC_ABANDONMISSION_RET,	//result of abandon mission
PACKET_GC_MISSION_STATE,	//update mission state
PACKET_GC_MISSION_PARAM,	//upstate mission param
PACKET_GC_CREATE_PLAYER,	//Create Player
PACKET_GC_DELETE_OBJ,	//Delete Player
PACKET_CG_SYNC_POS,	//Sync Position to Server
PACKET_GC_SYNC_POS,	//Sync Position to Client
PACKET_CG_MOVE,	//Player Move
PACKET_GC_MOVE,	//Notify Character Move
PACKET_GC_STOP,	//Notify Character Stop
PACKET_GC_BROADCAST_ATTR,	//Server Broadcast Attr
PACKET_GC_SYN_ATTR,	//Server Syn Attr
PACKET_GC_SYNC_COMMONDATA,	//Sync CommonData to Client
PACKET_GC_SYNC_COMMONFLAG,	//Sync CommonFlag to Client
PACKET_CG_ASK_SETCOMMONFLAG,	//Client ask to set Commonflag
PACKET_GC_ASK_COMMONFLAG_RET,	//Sync CommonFlag to Client

 PACKET_SIZE
 }
