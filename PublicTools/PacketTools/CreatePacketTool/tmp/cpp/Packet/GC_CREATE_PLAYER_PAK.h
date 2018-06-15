//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _GC_CREATE_PLAYER_PAK_H_
 #define _GC_CREATE_PLAYER_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class GC_CREATE_PLAYER_PAK:public Packet
 {
 public:
 GC_CREATE_PLAYER_PAK():Packet(m_PacketData){}
 virtual ~GC_CREATE_PLAYER_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_GC_CREATE_PLAYER_PAK;}
 public:
 ::GC_CREATE_PLAYER m_PacketData;
 };

 class GC_CREATE_PLAYER_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::GC_CREATE_PLAYER_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_GC_CREATE_PLAYER_PAK ; }
 };

 class GC_CREATE_PLAYER_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::GC_CREATE_PLAYER_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
