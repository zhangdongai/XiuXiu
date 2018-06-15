//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _CG_COMPLETEMISSION_PAK_H_
 #define _CG_COMPLETEMISSION_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class CG_COMPLETEMISSION_PAK:public Packet
 {
 public:
 CG_COMPLETEMISSION_PAK():Packet(m_PacketData){}
 virtual ~CG_COMPLETEMISSION_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_CG_COMPLETEMISSION_PAK;}
 public:
 ::CG_COMPLETEMISSION m_PacketData;
 };

 class CG_COMPLETEMISSION_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::CG_COMPLETEMISSION_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_CG_COMPLETEMISSION_PAK ; }
 };

 class CG_COMPLETEMISSION_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::CG_COMPLETEMISSION_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
