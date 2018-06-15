//This code create by CodeEngine Author:Wendy ,don't modify

#include "LibNetwork.h"
 #include"CG_PING_PAK.h"
#include"CG_LOGIN_PAK.h"
#include"CG_CREATEROLE_PAK.h"
#include"CG_SELECTROLE_PAK.h"
#include"CG_REQ_RANDOMNAME_PAK.h"
#include"CG_REQ_CHANGE_SCENE_PAK.h"
#include"CG_ENTER_SCENE_OK_PAK.h"
#include"CG_CONNECTED_HEARTBEAT_PAK.h"
#include"CG_ACCEPTMISSION_PAK.h"
#include"CG_COMPLETEMISSION_PAK.h"
#include"CG_ABANDONMISSION_PAK.h"
#include"CG_SYNC_POS_PAK.h"
#include"CG_MOVE_PAK.h"
#include"CG_ASK_SETCOMMONFLAG_PAK.h"
#include"GC_RET_PING_PAK.h"
#include"GC_LOGIN_RET_PAK.h"
#include"GC_LOGIN_QUEUE_STATUS_PAK.h"
#include"GC_CREATEROLE_RET_PAK.h"
#include"GC_SELECTROLE_RET_PAK.h"
#include"GC_RET_RANDOMNAME_PAK.h"
#include"GC_ENTER_SCENE_PAK.h"
#include"GC_CONNECTED_HEARTBEAT_PAK.h"
#include"GC_NOTICE_PAK.h"
#include"GC_MISSION_SYNC_MISSIONLIST_PAK.h"
#include"GC_ACCEPTMISSION_RET_PAK.h"
#include"GC_COMPLETEMISSION_RET_PAK.h"
#include"GC_ABANDONMISSION_RET_PAK.h"
#include"GC_MISSION_STATE_PAK.h"
#include"GC_MISSION_PARAM_PAK.h"
#include"GC_CREATE_PLAYER_PAK.h"
#include"GC_DELETE_OBJ_PAK.h"
#include"GC_SYNC_POS_PAK.h"
#include"GC_MOVE_PAK.h"
#include"GC_STOP_PAK.h"
#include"GC_BROADCAST_ATTR_PAK.h"
#include"GC_SYN_ATTR_PAK.h"
#include"GC_SYNC_COMMONDATA_PAK.h"
#include"GC_SYNC_COMMONFLAG_PAK.h"
#include"GC_ASK_COMMONFLAG_RET_PAK.h"
PacketFactoryManager gPacketFactoryManager;
 PacketFactoryManager::PacketFactoryManager( )
 {
 __ENTER_FUNCTION
 m_Factories = null_ptr ;
 m_Size = Packets::PACKET_MAX ;
 AssertEx( m_Size>0, "" ) ;
 m_Factories = new PacketFactory*[ m_Size ];
 AssertEx( m_Factories, "" ) ;
 m_pPacketAllocCount = new tuint32[m_Size] ;
 AssertEx( m_pPacketAllocCount, "" ) ;
 for( tint32 i=0; i<m_Size; i++ )
 {
 m_Factories[i] = null_ptr ;
 m_pPacketAllocCount[i] = 0 ;
 }
 __LEAVE_FUNCTION
 }
 
 PacketFactoryManager::~PacketFactoryManager( ) 
 {
 __ENTER_FUNCTION

 AssertEx( m_Factories!=null_ptr,"" ) ;
 for( tint32 i=0; i<m_Size; i++ ) 
 {
 SAFE_DELETE(m_Factories[i]) ;
 }
 SAFE_DELETE_ARRAY(m_Factories) ;
 SAFE_DELETE_ARRAY(m_pPacketAllocCount) ;
 __LEAVE_FUNCTION
 }
 
 void PacketFactoryManager::AddFactory( PacketFactory* pFactory ) 
 {
 __ENTER_FUNCTION
 
 if( m_Factories[pFactory->GetPacketID()]!=null_ptr )
 {
 AssertEx( false, "") ;
 return ;
 }
 
 m_Factories[pFactory->GetPacketID()] = pFactory ;
 
 __LEAVE_FUNCTION
 }
 Packet* PacketFactoryManager::CreatePacket( PacketID_t packetID ) 
 {
 __ENTER_FUNCTION
 if( packetID>=m_Size || m_Factories[packetID]==null_ptr ) 
 {
 AssertEx(false, "") ;
 return null_ptr ;
 }
 Packet* pPacket = null_ptr ;
 Lock() ;
 try
 {
 pPacket = m_Factories[packetID]->CreatePacket();
 m_pPacketAllocCount[packetID]++ ;
 }
 catch(...)
 {
 pPacket = null_ptr ;
 }
 Unlock() ;
 return pPacket ;
 __LEAVE_FUNCTION
 return null_ptr ;
 }

 void PacketFactoryManager::RemovePacket( Packet* pPacket )
 {
 __ENTER_FUNCTION
 if( pPacket==null_ptr )
 {
 AssertEx(false, "") ;
 return ;
 }
 PacketID_t packetID = pPacket->GetPacketID() ;
 if( packetID>=m_Size ) 

 {
 AssertEx(false, "") ;
 return ;
 }
 
 Lock() ;
 try
 {
 SAFE_DELETE( pPacket ) ;
 m_pPacketAllocCount[packetID] -- ;
 }
 catch(...)
 {
 }
 Unlock() ;
 return ;
 __LEAVE_FUNCTION
 return ;
 }
bool PacketFactoryManager::Init( )
 {
 __ENTER_FUNCTION
 AddFactory(new Packets::CG_PING_PAKFactory());
AddFactory(new Packets::CG_LOGIN_PAKFactory());
AddFactory(new Packets::CG_CREATEROLE_PAKFactory());
AddFactory(new Packets::CG_SELECTROLE_PAKFactory());
AddFactory(new Packets::CG_REQ_RANDOMNAME_PAKFactory());
AddFactory(new Packets::CG_REQ_CHANGE_SCENE_PAKFactory());
AddFactory(new Packets::CG_ENTER_SCENE_OK_PAKFactory());
AddFactory(new Packets::CG_CONNECTED_HEARTBEAT_PAKFactory());
AddFactory(new Packets::CG_ACCEPTMISSION_PAKFactory());
AddFactory(new Packets::CG_COMPLETEMISSION_PAKFactory());
AddFactory(new Packets::CG_ABANDONMISSION_PAKFactory());
AddFactory(new Packets::CG_SYNC_POS_PAKFactory());
AddFactory(new Packets::CG_MOVE_PAKFactory());
AddFactory(new Packets::CG_ASK_SETCOMMONFLAG_PAKFactory());
 AddFactory(new Packets::GC_RET_PING_PAKFactory());
AddFactory(new Packets::GC_LOGIN_RET_PAKFactory());
AddFactory(new Packets::GC_LOGIN_QUEUE_STATUS_PAKFactory());
AddFactory(new Packets::GC_CREATEROLE_RET_PAKFactory());
AddFactory(new Packets::GC_SELECTROLE_RET_PAKFactory());
AddFactory(new Packets::GC_RET_RANDOMNAME_PAKFactory());
AddFactory(new Packets::GC_ENTER_SCENE_PAKFactory());
AddFactory(new Packets::GC_CONNECTED_HEARTBEAT_PAKFactory());
AddFactory(new Packets::GC_NOTICE_PAKFactory());
AddFactory(new Packets::GC_MISSION_SYNC_MISSIONLIST_PAKFactory());
AddFactory(new Packets::GC_ACCEPTMISSION_RET_PAKFactory());
AddFactory(new Packets::GC_COMPLETEMISSION_RET_PAKFactory());
AddFactory(new Packets::GC_ABANDONMISSION_RET_PAKFactory());
AddFactory(new Packets::GC_MISSION_STATE_PAKFactory());
AddFactory(new Packets::GC_MISSION_PARAM_PAKFactory());
AddFactory(new Packets::GC_CREATE_PLAYER_PAKFactory());
AddFactory(new Packets::GC_DELETE_OBJ_PAKFactory());
AddFactory(new Packets::GC_SYNC_POS_PAKFactory());
AddFactory(new Packets::GC_MOVE_PAKFactory());
AddFactory(new Packets::GC_STOP_PAKFactory());
AddFactory(new Packets::GC_BROADCAST_ATTR_PAKFactory());
AddFactory(new Packets::GC_SYN_ATTR_PAKFactory());
AddFactory(new Packets::GC_SYNC_COMMONDATA_PAKFactory());
AddFactory(new Packets::GC_SYNC_COMMONFLAG_PAKFactory());
AddFactory(new Packets::GC_ASK_COMMONFLAG_RET_PAKFactory());
 return true ;
 __LEAVE_FUNCTION
 return false ;
 }
