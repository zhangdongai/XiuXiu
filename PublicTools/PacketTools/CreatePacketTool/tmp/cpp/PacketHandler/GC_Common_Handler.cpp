//This code create by CodeEngine

#include "Packet/GC_RET_PING_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_RET_PING_PAKHandler::Execute( Packets::GC_RET_PING_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_LOGIN_RET_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_LOGIN_RET_PAKHandler::Execute( Packets::GC_LOGIN_RET_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_LOGIN_QUEUE_STATUS_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_LOGIN_QUEUE_STATUS_PAKHandler::Execute( Packets::GC_LOGIN_QUEUE_STATUS_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_CREATEROLE_RET_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_CREATEROLE_RET_PAKHandler::Execute( Packets::GC_CREATEROLE_RET_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_SELECTROLE_RET_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_SELECTROLE_RET_PAKHandler::Execute( Packets::GC_SELECTROLE_RET_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_RET_RANDOMNAME_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_RET_RANDOMNAME_PAKHandler::Execute( Packets::GC_RET_RANDOMNAME_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_ENTER_SCENE_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_ENTER_SCENE_PAKHandler::Execute( Packets::GC_ENTER_SCENE_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_CONNECTED_HEARTBEAT_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_CONNECTED_HEARTBEAT_PAKHandler::Execute( Packets::GC_CONNECTED_HEARTBEAT_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_NOTICE_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_NOTICE_PAKHandler::Execute( Packets::GC_NOTICE_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_MISSION_SYNC_MISSIONLIST_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_MISSION_SYNC_MISSIONLIST_PAKHandler::Execute( Packets::GC_MISSION_SYNC_MISSIONLIST_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_ACCEPTMISSION_RET_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_ACCEPTMISSION_RET_PAKHandler::Execute( Packets::GC_ACCEPTMISSION_RET_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_COMPLETEMISSION_RET_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_COMPLETEMISSION_RET_PAKHandler::Execute( Packets::GC_COMPLETEMISSION_RET_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_ABANDONMISSION_RET_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_ABANDONMISSION_RET_PAKHandler::Execute( Packets::GC_ABANDONMISSION_RET_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_MISSION_STATE_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_MISSION_STATE_PAKHandler::Execute( Packets::GC_MISSION_STATE_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_MISSION_PARAM_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_MISSION_PARAM_PAKHandler::Execute( Packets::GC_MISSION_PARAM_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_CREATE_PLAYER_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_CREATE_PLAYER_PAKHandler::Execute( Packets::GC_CREATE_PLAYER_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_DELETE_OBJ_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_DELETE_OBJ_PAKHandler::Execute( Packets::GC_DELETE_OBJ_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_SYNC_POS_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_SYNC_POS_PAKHandler::Execute( Packets::GC_SYNC_POS_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_MOVE_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_MOVE_PAKHandler::Execute( Packets::GC_MOVE_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_STOP_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_STOP_PAKHandler::Execute( Packets::GC_STOP_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_BROADCAST_ATTR_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_BROADCAST_ATTR_PAKHandler::Execute( Packets::GC_BROADCAST_ATTR_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_SYN_ATTR_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_SYN_ATTR_PAKHandler::Execute( Packets::GC_SYN_ATTR_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_SYNC_COMMONDATA_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_SYNC_COMMONDATA_PAKHandler::Execute( Packets::GC_SYNC_COMMONDATA_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_SYNC_COMMONFLAG_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_SYNC_COMMONFLAG_PAKHandler::Execute( Packets::GC_SYNC_COMMONFLAG_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/GC_ASK_COMMONFLAG_RET_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::GC_ASK_COMMONFLAG_RET_PAKHandler::Execute( Packets::GC_ASK_COMMONFLAG_RET_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
