//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _CG_PING_PAK_H_
 #define _CG_PING_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class CG_PING_PAK:public Packet
 {
 public:
 CG_PING_PAK():Packet(m_PacketData){}
 virtual ~CG_PING_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_CG_PING_PAK;}
 public:
 ::CG_PING m_PacketData;
 };

 class CG_PING_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::CG_PING_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_CG_PING_PAK ; }
 };

 class CG_PING_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::CG_PING_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
