//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _CG_ABANDONMISSION_PAK_H_
 #define _CG_ABANDONMISSION_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class CG_ABANDONMISSION_PAK:public Packet
 {
 public:
 CG_ABANDONMISSION_PAK():Packet(m_PacketData){}
 virtual ~CG_ABANDONMISSION_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_CG_ABANDONMISSION_PAK;}
 public:
 ::CG_ABANDONMISSION m_PacketData;
 };

 class CG_ABANDONMISSION_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::CG_ABANDONMISSION_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_CG_ABANDONMISSION_PAK ; }
 };

 class CG_ABANDONMISSION_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::CG_ABANDONMISSION_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
