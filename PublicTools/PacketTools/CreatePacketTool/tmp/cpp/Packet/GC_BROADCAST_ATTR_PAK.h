//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _GC_BROADCAST_ATTR_PAK_H_
 #define _GC_BROADCAST_ATTR_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class GC_BROADCAST_ATTR_PAK:public Packet
 {
 public:
 GC_BROADCAST_ATTR_PAK():Packet(m_PacketData){}
 virtual ~GC_BROADCAST_ATTR_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_GC_BROADCAST_ATTR_PAK;}
 public:
 ::GC_BROADCAST_ATTR m_PacketData;
 };

 class GC_BROADCAST_ATTR_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::GC_BROADCAST_ATTR_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_GC_BROADCAST_ATTR_PAK ; }
 };

 class GC_BROADCAST_ATTR_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::GC_BROADCAST_ATTR_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
