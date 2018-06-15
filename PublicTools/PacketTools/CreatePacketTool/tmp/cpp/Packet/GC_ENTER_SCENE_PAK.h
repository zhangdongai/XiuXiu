//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _GC_ENTER_SCENE_PAK_H_
 #define _GC_ENTER_SCENE_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class GC_ENTER_SCENE_PAK:public Packet
 {
 public:
 GC_ENTER_SCENE_PAK():Packet(m_PacketData){}
 virtual ~GC_ENTER_SCENE_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_GC_ENTER_SCENE_PAK;}
 public:
 ::GC_ENTER_SCENE m_PacketData;
 };

 class GC_ENTER_SCENE_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::GC_ENTER_SCENE_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_GC_ENTER_SCENE_PAK ; }
 };

 class GC_ENTER_SCENE_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::GC_ENTER_SCENE_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
