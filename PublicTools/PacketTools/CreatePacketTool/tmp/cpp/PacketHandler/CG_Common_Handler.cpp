//This code create by CodeEngine

#include "Packet/CG_PING_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_PING_PAKHandler::Execute( Packets::CG_PING_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_LOGIN_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_LOGIN_PAKHandler::Execute( Packets::CG_LOGIN_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_CREATEROLE_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_CREATEROLE_PAKHandler::Execute( Packets::CG_CREATEROLE_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_SELECTROLE_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_SELECTROLE_PAKHandler::Execute( Packets::CG_SELECTROLE_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_REQ_RANDOMNAME_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_REQ_RANDOMNAME_PAKHandler::Execute( Packets::CG_REQ_RANDOMNAME_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_REQ_CHANGE_SCENE_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_REQ_CHANGE_SCENE_PAKHandler::Execute( Packets::CG_REQ_CHANGE_SCENE_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_ENTER_SCENE_OK_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_ENTER_SCENE_OK_PAKHandler::Execute( Packets::CG_ENTER_SCENE_OK_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_CONNECTED_HEARTBEAT_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_CONNECTED_HEARTBEAT_PAKHandler::Execute( Packets::CG_CONNECTED_HEARTBEAT_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_ACCEPTMISSION_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_ACCEPTMISSION_PAKHandler::Execute( Packets::CG_ACCEPTMISSION_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_COMPLETEMISSION_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_COMPLETEMISSION_PAKHandler::Execute( Packets::CG_COMPLETEMISSION_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_ABANDONMISSION_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_ABANDONMISSION_PAKHandler::Execute( Packets::CG_ABANDONMISSION_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_SYNC_POS_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_SYNC_POS_PAKHandler::Execute( Packets::CG_SYNC_POS_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_MOVE_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_MOVE_PAKHandler::Execute( Packets::CG_MOVE_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
//This code create by CodeEngine

#include "Packet/CG_ASK_SETCOMMONFLAG_PAK.h"
 #include "Player/Player.h"
tuint32 Packets::CG_ASK_SETCOMMONFLAG_PAKHandler::Execute( Packets::CG_ASK_SETCOMMONFLAG_PAK* pPacket, Player* pPlayer )
 {
 __ENTER_FUNCTION
 AssertEx(pPacket, "");
 AssertEx(pPlayer, "");
 return pPlayer->HandlePacket(pPacket->m_PacketData);
 __LEAVE_FUNCTION
 return PACKET_EXE_ERROR ; 
 }
