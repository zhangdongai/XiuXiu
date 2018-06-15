//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _CG_REQ_RANDOMNAME_PAK_H_
 #define _CG_REQ_RANDOMNAME_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class CG_REQ_RANDOMNAME_PAK:public Packet
 {
 public:
 CG_REQ_RANDOMNAME_PAK():Packet(m_PacketData){}
 virtual ~CG_REQ_RANDOMNAME_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_CG_REQ_RANDOMNAME_PAK;}
 public:
 ::CG_REQ_RANDOMNAME m_PacketData;
 };

 class CG_REQ_RANDOMNAME_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::CG_REQ_RANDOMNAME_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_CG_REQ_RANDOMNAME_PAK ; }
 };

 class CG_REQ_RANDOMNAME_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::CG_REQ_RANDOMNAME_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
