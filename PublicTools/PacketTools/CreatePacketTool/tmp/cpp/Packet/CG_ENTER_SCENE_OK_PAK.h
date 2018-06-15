//This code create by CodeEngine Author:Wendy ,don't modify

#ifndef _CG_ENTER_SCENE_OK_PAK_H_
 #define _CG_ENTER_SCENE_OK_PAK_H_

 #include "Base.h"
 #include "PBMessage.pb.h"
 #include "PacketDefine.h"
 #include "LibNetwork.h"
namespace Packets
 {
class CG_ENTER_SCENE_OK_PAK:public Packet
 {
 public:
 CG_ENTER_SCENE_OK_PAK():Packet(m_PacketData){}
 virtual ~CG_ENTER_SCENE_OK_PAK(){}
 virtual tuint32 Execute( Player* pPlayer );
 virtual PacketID_t GetPacketID( ) const {return PACKET_CG_ENTER_SCENE_OK_PAK;}
 public:
 ::CG_ENTER_SCENE_OK m_PacketData;
 };

 class CG_ENTER_SCENE_OK_PAKFactory : public PacketFactory
 {
 public:
 Packet* CreatePacket() { return new Packets::CG_ENTER_SCENE_OK_PAK(); }
 PacketID_t GetPacketID()const { return PACKET_CG_ENTER_SCENE_OK_PAK ; }
 };

 class CG_ENTER_SCENE_OK_PAKHandler 
 {
 public:
 static tuint32 Execute( Packets::CG_ENTER_SCENE_OK_PAK* pPacket, Player* pPlayer ) ;
 };

}
 #endif
