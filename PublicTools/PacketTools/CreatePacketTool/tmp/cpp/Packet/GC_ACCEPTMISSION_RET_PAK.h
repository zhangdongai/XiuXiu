//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _GC_ACCEPTMISSION_RET_PAK_H_
 #define _GC_ACCEPTMISSION_RET_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class GC_ACCEPTMISSION_RET_PAK:public Packet
 {
 public:
 GC_ACCEPTMISSION_RET_PAK():Packet(m_PacketData){}
 virtual ~GC_ACCEPTMISSION_RET_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_GC_ACCEPTMISSION_RET_PAK;}
 public:
 ::GC_ACCEPTMISSION_RET m_PacketData;
 };

 class GC_ACCEPTMISSION_RET_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::GC_ACCEPTMISSION_RET_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_GC_ACCEPTMISSION_RET_PAK ; }
 };

 class GC_ACCEPTMISSION_RET_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::GC_ACCEPTMISSION_RET_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
