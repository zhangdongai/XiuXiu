//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _CG_SYNC_POS_PAK_H_
 #define _CG_SYNC_POS_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class CG_SYNC_POS_PAK:public Packet
 {
 public:
 CG_SYNC_POS_PAK():Packet(m_PacketData){}
 virtual ~CG_SYNC_POS_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_CG_SYNC_POS_PAK;}
 public:
 ::CG_SYNC_POS m_PacketData;
 };

 class CG_SYNC_POS_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::CG_SYNC_POS_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_CG_SYNC_POS_PAK ; }
 };

 class CG_SYNC_POS_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::CG_SYNC_POS_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
