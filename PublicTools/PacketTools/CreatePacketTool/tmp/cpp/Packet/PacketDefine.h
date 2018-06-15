//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef __PACKET_DEFINE_H__
 #define __PACKET_DEFINE_H__
 
 #include "BaseType.h"
 #define MAX_PACKET_NAME_SIZE (128) 
 
 namespace Packets
 {
 //消息类型值描述格式：PACKET_XX_YYYYYY
 //XX可以描述为：GC、CG 
 //G游戏服务器端、C客户端 
 //YYYYYY表示消息内容
 //例如：PACKET_CG_ATTACK 表示客户端发给游戏服务器端关于攻击的消息
 enum PACKET_DEFINE
 {
 PACKET_NONE = 0 , // 0，空
 PACKET_CG_LOGIN_PAK = 1, //client ask login 
 PACKET_GC_LOGIN_RET_PAK =2, //client login result 
 PACKET_CG_PING_PAK,	//Client send ping
PACKET_GC_RET_PING_PAK,	//sever return ping
PACKET_GC_LOGIN_QUEUE_STATUS_PAK,	//login queue status
PACKET_CG_CREATEROLE_PAK,	//client send createRole
PACKET_GC_CREATEROLE_RET_PAK,	//server send create role result
PACKET_CG_SELECTROLE_PAK,	//client send selectRole
PACKET_GC_SELECTROLE_RET_PAK,	//server send select role result
PACKET_CG_REQ_RANDOMNAME_PAK,	//Client Request Random Name
PACKET_GC_RET_RANDOMNAME_PAK,	//Server ret randomname
PACKET_CG_REQ_CHANGE_SCENE_PAK,	//Request Change Scene
PACKET_GC_ENTER_SCENE_PAK,	//Enter Scene
PACKET_CG_ENTER_SCENE_OK_PAK,	//Client Enter Scene OK
PACKET_CG_CONNECTED_HEARTBEAT_PAK,	//client connected heartbeat
PACKET_GC_CONNECTED_HEARTBEAT_PAK,	//server connected heartbeat
PACKET_GC_NOTICE_PAK,	//notice from server
PACKET_GC_MISSION_SYNC_MISSIONLIST_PAK,	//server send mission list to client
PACKET_CG_ACCEPTMISSION_PAK,	//ask to accept mission
PACKET_GC_ACCEPTMISSION_RET_PAK,	//result of accept mission
PACKET_CG_COMPLETEMISSION_PAK,	//ask to complete mission
PACKET_GC_COMPLETEMISSION_RET_PAK,	//result of complete mission
PACKET_CG_ABANDONMISSION_PAK,	//ask to abandon mission
PACKET_GC_ABANDONMISSION_RET_PAK,	//result of abandon mission
PACKET_GC_MISSION_STATE_PAK,	//update mission state
PACKET_GC_MISSION_PARAM_PAK,	//upstate mission param
PACKET_GC_CREATE_PLAYER_PAK,	//Create Player
PACKET_GC_DELETE_OBJ_PAK,	//Delete Player
PACKET_CG_SYNC_POS_PAK,	//Sync Position to Server
PACKET_GC_SYNC_POS_PAK,	//Sync Position to Client
PACKET_CG_MOVE_PAK,	//Player Move
PACKET_GC_MOVE_PAK,	//Notify Character Move
PACKET_GC_STOP_PAK,	//Notify Character Stop
PACKET_GC_BROADCAST_ATTR_PAK,	//Server Broadcast Attr
PACKET_GC_SYN_ATTR_PAK,	//Server Syn Attr
PACKET_GC_SYNC_COMMONDATA_PAK,	//Sync CommonData to Client
PACKET_GC_SYNC_COMMONFLAG_PAK,	//Sync CommonFlag to Client
PACKET_CG_ASK_SETCOMMONFLAG_PAK,	//Client ask to set Commonflag
PACKET_GC_ASK_COMMONFLAG_RET_PAK,	//Sync CommonFlag to Client

 PACKET_MAX //消息类型的最大值
 };

 
 void InitPacketNameVector();
 const tchar* GetPacketNameByID(tint32 nPacketID);
 }
 #endif
