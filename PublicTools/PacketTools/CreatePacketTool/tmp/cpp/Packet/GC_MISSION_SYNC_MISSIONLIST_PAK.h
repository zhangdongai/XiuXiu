//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _GC_MISSION_SYNC_MISSIONLIST_PAK_H_
 #define _GC_MISSION_SYNC_MISSIONLIST_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class GC_MISSION_SYNC_MISSIONLIST_PAK:public Packet
 {
 public:
 GC_MISSION_SYNC_MISSIONLIST_PAK():Packet(m_PacketData){}
 virtual ~GC_MISSION_SYNC_MISSIONLIST_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_GC_MISSION_SYNC_MISSIONLIST_PAK;}
 public:
 ::GC_MISSION_SYNC_MISSIONLIST m_PacketData;
 };

 class GC_MISSION_SYNC_MISSIONLIST_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::GC_MISSION_SYNC_MISSIONLIST_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_GC_MISSION_SYNC_MISSIONLIST_PAK ; }
 };

 class GC_MISSION_SYNC_MISSIONLIST_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::GC_MISSION_SYNC_MISSIONLIST_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
