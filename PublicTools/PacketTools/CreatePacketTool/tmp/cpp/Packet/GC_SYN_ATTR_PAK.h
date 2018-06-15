//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _GC_SYN_ATTR_PAK_H_
 #define _GC_SYN_ATTR_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class GC_SYN_ATTR_PAK:public Packet
 {
 public:
 GC_SYN_ATTR_PAK():Packet(m_PacketData){}
 virtual ~GC_SYN_ATTR_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_GC_SYN_ATTR_PAK;}
 public:
 ::GC_SYN_ATTR m_PacketData;
 };

 class GC_SYN_ATTR_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::GC_SYN_ATTR_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_GC_SYN_ATTR_PAK ; }
 };

 class GC_SYN_ATTR_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::GC_SYN_ATTR_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
