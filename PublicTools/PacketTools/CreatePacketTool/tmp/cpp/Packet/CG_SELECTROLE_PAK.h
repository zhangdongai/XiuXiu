//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _CG_SELECTROLE_PAK_H_
 #define _CG_SELECTROLE_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class CG_SELECTROLE_PAK:public Packet
 {
 public:
 CG_SELECTROLE_PAK():Packet(m_PacketData){}
 virtual ~CG_SELECTROLE_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_CG_SELECTROLE_PAK;}
 public:
 ::CG_SELECTROLE m_PacketData;
 };

 class CG_SELECTROLE_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::CG_SELECTROLE_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_CG_SELECTROLE_PAK ; }
 };

 class CG_SELECTROLE_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::CG_SELECTROLE_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
