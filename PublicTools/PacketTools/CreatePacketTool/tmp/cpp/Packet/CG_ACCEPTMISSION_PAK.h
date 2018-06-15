//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _CG_ACCEPTMISSION_PAK_H_
 #define _CG_ACCEPTMISSION_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class CG_ACCEPTMISSION_PAK:public Packet
 {
 public:
 CG_ACCEPTMISSION_PAK():Packet(m_PacketData){}
 virtual ~CG_ACCEPTMISSION_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_CG_ACCEPTMISSION_PAK;}
 public:
 ::CG_ACCEPTMISSION m_PacketData;
 };

 class CG_ACCEPTMISSION_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::CG_ACCEPTMISSION_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_CG_ACCEPTMISSION_PAK ; }
 };

 class CG_ACCEPTMISSION_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::CG_ACCEPTMISSION_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
