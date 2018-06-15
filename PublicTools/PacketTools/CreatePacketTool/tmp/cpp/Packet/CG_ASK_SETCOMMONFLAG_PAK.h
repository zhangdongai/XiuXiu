//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _CG_ASK_SETCOMMONFLAG_PAK_H_
 #define _CG_ASK_SETCOMMONFLAG_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class CG_ASK_SETCOMMONFLAG_PAK:public Packet
 {
 public:
 CG_ASK_SETCOMMONFLAG_PAK():Packet(m_PacketData){}
 virtual ~CG_ASK_SETCOMMONFLAG_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_CG_ASK_SETCOMMONFLAG_PAK;}
 public:
 ::CG_ASK_SETCOMMONFLAG m_PacketData;
 };

 class CG_ASK_SETCOMMONFLAG_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::CG_ASK_SETCOMMONFLAG_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_CG_ASK_SETCOMMONFLAG_PAK ; }
 };

 class CG_ASK_SETCOMMONFLAG_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::CG_ASK_SETCOMMONFLAG_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
