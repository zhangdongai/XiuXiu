//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _GC_RET_PING_PAK_H_
 #define _GC_RET_PING_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class GC_RET_PING_PAK:public Packet
 {
 public:
 GC_RET_PING_PAK():Packet(m_PacketData){}
 virtual ~GC_RET_PING_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_GC_RET_PING_PAK;}
 public:
 ::GC_RET_PING m_PacketData;
 };

 class GC_RET_PING_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::GC_RET_PING_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_GC_RET_PING_PAK ; }
 };

 class GC_RET_PING_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::GC_RET_PING_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
