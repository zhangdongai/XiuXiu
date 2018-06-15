//This code create by CodeEngine mrd.cyou.com ,don't modify

using System;
 using scg = global::System.Collections.Generic;
 using pb = global::Google.ProtocolBuffers;
 using pbc = global::Google.ProtocolBuffers.Collections;
 #pragma warning disable



[Serializable]
public class CG_PING : PacketDistributed
{

public const int noparamFieldNumber = 1;
 private bool hasNoparam;
 private Int32 noparam_ = 0;
 public bool HasNoparam {
 get { return hasNoparam; }
 }
 public Int32 Noparam {
 get { return noparam_; }
 set { SetNoparam(value); }
 }
 public void SetNoparam(Int32 value) { 
 hasNoparam = true;
 noparam_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasNoparam) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Noparam);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasNoparam) {
output.WriteInt32(1, Noparam);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_PING _inst = (CG_PING) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Noparam = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  return true;
 }

}


[Serializable]
public class GC_RET_PING : PacketDistributed
{

public const int noparamFieldNumber = 1;
 private bool hasNoparam;
 private Int32 noparam_ = 0;
 public bool HasNoparam {
 get { return hasNoparam; }
 }
 public Int32 Noparam {
 get { return noparam_; }
 set { SetNoparam(value); }
 }
 public void SetNoparam(Int32 value) { 
 hasNoparam = true;
 noparam_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasNoparam) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Noparam);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasNoparam) {
output.WriteInt32(1, Noparam);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_RET_PING _inst = (GC_RET_PING) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Noparam = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  return true;
 }

}


[Serializable]
public class CG_LOGIN : PacketDistributed
{
public enum VALIDATETYPE 
 { 
  TEST = 0,                 //测试登录模式 
  CYOU = 1,                 //聚合SDK登陆模式 
 }
public const int vtypeFieldNumber = 1;
 private bool hasVtype;
 private Int32 vtype_ = 0;
 public bool HasVtype {
 get { return hasVtype; }
 }
 public Int32 Vtype {
 get { return vtype_; }
 set { SetVtype(value); }
 }
 public void SetVtype(Int32 value) { 
 hasVtype = true;
 vtype_ = value;
 }

public const int gameversionFieldNumber = 2;
 private bool hasGameversion;
 private Int32 gameversion_ = 0;
 public bool HasGameversion {
 get { return hasGameversion; }
 }
 public Int32 Gameversion {
 get { return gameversion_; }
 set { SetGameversion(value); }
 }
 public void SetGameversion(Int32 value) { 
 hasGameversion = true;
 gameversion_ = value;
 }

public const int programversionFieldNumber = 3;
 private bool hasProgramversion;
 private Int32 programversion_ = 0;
 public bool HasProgramversion {
 get { return hasProgramversion; }
 }
 public Int32 Programversion {
 get { return programversion_; }
 set { SetProgramversion(value); }
 }
 public void SetProgramversion(Int32 value) { 
 hasProgramversion = true;
 programversion_ = value;
 }

public const int publicresourceversionFieldNumber = 4;
 private bool hasPublicresourceversion;
 private Int32 publicresourceversion_ = 0;
 public bool HasPublicresourceversion {
 get { return hasPublicresourceversion; }
 }
 public Int32 Publicresourceversion {
 get { return publicresourceversion_; }
 set { SetPublicresourceversion(value); }
 }
 public void SetPublicresourceversion(Int32 value) { 
 hasPublicresourceversion = true;
 publicresourceversion_ = value;
 }

public const int maxpacketidFieldNumber = 5;
 private bool hasMaxpacketid;
 private Int32 maxpacketid_ = 0;
 public bool HasMaxpacketid {
 get { return hasMaxpacketid; }
 }
 public Int32 Maxpacketid {
 get { return maxpacketid_; }
 set { SetMaxpacketid(value); }
 }
 public void SetMaxpacketid(Int32 value) { 
 hasMaxpacketid = true;
 maxpacketid_ = value;
 }

public const int forceenterFieldNumber = 6;
 private bool hasForceenter;
 private Int32 forceenter_ = 0;
 public bool HasForceenter {
 get { return hasForceenter; }
 }
 public Int32 Forceenter {
 get { return forceenter_; }
 set { SetForceenter(value); }
 }
 public void SetForceenter(Int32 value) { 
 hasForceenter = true;
 forceenter_ = value;
 }

public const int deviceidFieldNumber = 7;
 private bool hasDeviceid;
 private string deviceid_ = "";
 public bool HasDeviceid {
 get { return hasDeviceid; }
 }
 public string Deviceid {
 get { return deviceid_; }
 set { SetDeviceid(value); }
 }
 public void SetDeviceid(string value) { 
 hasDeviceid = true;
 deviceid_ = value;
 }

public const int devicetypeFieldNumber = 8;
 private bool hasDevicetype;
 private string devicetype_ = "";
 public bool HasDevicetype {
 get { return hasDevicetype; }
 }
 public string Devicetype {
 get { return devicetype_; }
 set { SetDevicetype(value); }
 }
 public void SetDevicetype(string value) { 
 hasDevicetype = true;
 devicetype_ = value;
 }

public const int deviceversionFieldNumber = 9;
 private bool hasDeviceversion;
 private string deviceversion_ = "";
 public bool HasDeviceversion {
 get { return hasDeviceversion; }
 }
 public string Deviceversion {
 get { return deviceversion_; }
 set { SetDeviceversion(value); }
 }
 public void SetDeviceversion(string value) { 
 hasDeviceversion = true;
 deviceversion_ = value;
 }

public const int accountFieldNumber = 10;
 private bool hasAccount;
 private string account_ = "";
 public bool HasAccount {
 get { return hasAccount; }
 }
 public string Account {
 get { return account_; }
 set { SetAccount(value); }
 }
 public void SetAccount(string value) { 
 hasAccount = true;
 account_ = value;
 }

public const int validateinfoFieldNumber = 11;
 private bool hasValidateinfo;
 private string validateinfo_ = "";
 public bool HasValidateinfo {
 get { return hasValidateinfo; }
 }
 public string Validateinfo {
 get { return validateinfo_; }
 set { SetValidateinfo(value); }
 }
 public void SetValidateinfo(string value) { 
 hasValidateinfo = true;
 validateinfo_ = value;
 }

public const int channelidFieldNumber = 12;
 private bool hasChannelid;
 private string channelid_ = "";
 public bool HasChannelid {
 get { return hasChannelid; }
 }
 public string Channelid {
 get { return channelid_; }
 set { SetChannelid(value); }
 }
 public void SetChannelid(string value) { 
 hasChannelid = true;
 channelid_ = value;
 }

public const int mediachannelFieldNumber = 13;
 private bool hasMediachannel;
 private string mediachannel_ = "";
 public bool HasMediachannel {
 get { return hasMediachannel; }
 }
 public string Mediachannel {
 get { return mediachannel_; }
 set { SetMediachannel(value); }
 }
 public void SetMediachannel(string value) { 
 hasMediachannel = true;
 mediachannel_ = value;
 }

public const int rapidvalidatecodeFieldNumber = 14;
 private bool hasRapidvalidatecode;
 private Int32 rapidvalidatecode_ = 0;
 public bool HasRapidvalidatecode {
 get { return hasRapidvalidatecode; }
 }
 public Int32 Rapidvalidatecode {
 get { return rapidvalidatecode_; }
 set { SetRapidvalidatecode(value); }
 }
 public void SetRapidvalidatecode(Int32 value) { 
 hasRapidvalidatecode = true;
 rapidvalidatecode_ = value;
 }

public const int reservedint1FieldNumber = 15;
 private bool hasReservedint1;
 private Int32 reservedint1_ = 0;
 public bool HasReservedint1 {
 get { return hasReservedint1; }
 }
 public Int32 Reservedint1 {
 get { return reservedint1_; }
 set { SetReservedint1(value); }
 }
 public void SetReservedint1(Int32 value) { 
 hasReservedint1 = true;
 reservedint1_ = value;
 }

public const int reservedint2FieldNumber = 16;
 private bool hasReservedint2;
 private Int32 reservedint2_ = 0;
 public bool HasReservedint2 {
 get { return hasReservedint2; }
 }
 public Int32 Reservedint2 {
 get { return reservedint2_; }
 set { SetReservedint2(value); }
 }
 public void SetReservedint2(Int32 value) { 
 hasReservedint2 = true;
 reservedint2_ = value;
 }

public const int reservedint3FieldNumber = 17;
 private bool hasReservedint3;
 private Int32 reservedint3_ = 0;
 public bool HasReservedint3 {
 get { return hasReservedint3; }
 }
 public Int32 Reservedint3 {
 get { return reservedint3_; }
 set { SetReservedint3(value); }
 }
 public void SetReservedint3(Int32 value) { 
 hasReservedint3 = true;
 reservedint3_ = value;
 }

public const int reservedint4FieldNumber = 18;
 private bool hasReservedint4;
 private Int32 reservedint4_ = 0;
 public bool HasReservedint4 {
 get { return hasReservedint4; }
 }
 public Int32 Reservedint4 {
 get { return reservedint4_; }
 set { SetReservedint4(value); }
 }
 public void SetReservedint4(Int32 value) { 
 hasReservedint4 = true;
 reservedint4_ = value;
 }

public const int reservedstring1FieldNumber = 19;
 private bool hasReservedstring1;
 private string reservedstring1_ = "";
 public bool HasReservedstring1 {
 get { return hasReservedstring1; }
 }
 public string Reservedstring1 {
 get { return reservedstring1_; }
 set { SetReservedstring1(value); }
 }
 public void SetReservedstring1(string value) { 
 hasReservedstring1 = true;
 reservedstring1_ = value;
 }

public const int reservedstring2FieldNumber = 20;
 private bool hasReservedstring2;
 private string reservedstring2_ = "";
 public bool HasReservedstring2 {
 get { return hasReservedstring2; }
 }
 public string Reservedstring2 {
 get { return reservedstring2_; }
 set { SetReservedstring2(value); }
 }
 public void SetReservedstring2(string value) { 
 hasReservedstring2 = true;
 reservedstring2_ = value;
 }

public const int reservedstring3FieldNumber = 21;
 private bool hasReservedstring3;
 private string reservedstring3_ = "";
 public bool HasReservedstring3 {
 get { return hasReservedstring3; }
 }
 public string Reservedstring3 {
 get { return reservedstring3_; }
 set { SetReservedstring3(value); }
 }
 public void SetReservedstring3(string value) { 
 hasReservedstring3 = true;
 reservedstring3_ = value;
 }

public const int reservedstring4FieldNumber = 22;
 private bool hasReservedstring4;
 private string reservedstring4_ = "";
 public bool HasReservedstring4 {
 get { return hasReservedstring4; }
 }
 public string Reservedstring4 {
 get { return reservedstring4_; }
 set { SetReservedstring4(value); }
 }
 public void SetReservedstring4(string value) { 
 hasReservedstring4 = true;
 reservedstring4_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasVtype) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Vtype);
}
 if (HasGameversion) {
size += pb::CodedOutputStream.ComputeInt32Size(2, Gameversion);
}
 if (HasProgramversion) {
size += pb::CodedOutputStream.ComputeInt32Size(3, Programversion);
}
 if (HasPublicresourceversion) {
size += pb::CodedOutputStream.ComputeInt32Size(4, Publicresourceversion);
}
 if (HasMaxpacketid) {
size += pb::CodedOutputStream.ComputeInt32Size(5, Maxpacketid);
}
 if (HasForceenter) {
size += pb::CodedOutputStream.ComputeInt32Size(6, Forceenter);
}
 if (HasDeviceid) {
size += pb::CodedOutputStream.ComputeStringSize(7, Deviceid);
}
 if (HasDevicetype) {
size += pb::CodedOutputStream.ComputeStringSize(8, Devicetype);
}
 if (HasDeviceversion) {
size += pb::CodedOutputStream.ComputeStringSize(9, Deviceversion);
}
 if (HasAccount) {
size += pb::CodedOutputStream.ComputeStringSize(10, Account);
}
 if (HasValidateinfo) {
size += pb::CodedOutputStream.ComputeStringSize(11, Validateinfo);
}
 if (HasChannelid) {
size += pb::CodedOutputStream.ComputeStringSize(12, Channelid);
}
 if (HasMediachannel) {
size += pb::CodedOutputStream.ComputeStringSize(13, Mediachannel);
}
 if (HasRapidvalidatecode) {
size += pb::CodedOutputStream.ComputeInt32Size(14, Rapidvalidatecode);
}
 if (HasReservedint1) {
size += pb::CodedOutputStream.ComputeInt32Size(15, Reservedint1);
}
 if (HasReservedint2) {
size += pb::CodedOutputStream.ComputeInt32Size(16, Reservedint2);
}
 if (HasReservedint3) {
size += pb::CodedOutputStream.ComputeInt32Size(17, Reservedint3);
}
 if (HasReservedint4) {
size += pb::CodedOutputStream.ComputeInt32Size(18, Reservedint4);
}
 if (HasReservedstring1) {
size += pb::CodedOutputStream.ComputeStringSize(19, Reservedstring1);
}
 if (HasReservedstring2) {
size += pb::CodedOutputStream.ComputeStringSize(20, Reservedstring2);
}
 if (HasReservedstring3) {
size += pb::CodedOutputStream.ComputeStringSize(21, Reservedstring3);
}
 if (HasReservedstring4) {
size += pb::CodedOutputStream.ComputeStringSize(22, Reservedstring4);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasVtype) {
output.WriteInt32(1, Vtype);
}
 
if (HasGameversion) {
output.WriteInt32(2, Gameversion);
}
 
if (HasProgramversion) {
output.WriteInt32(3, Programversion);
}
 
if (HasPublicresourceversion) {
output.WriteInt32(4, Publicresourceversion);
}
 
if (HasMaxpacketid) {
output.WriteInt32(5, Maxpacketid);
}
 
if (HasForceenter) {
output.WriteInt32(6, Forceenter);
}
 
if (HasDeviceid) {
output.WriteString(7, Deviceid);
}
 
if (HasDevicetype) {
output.WriteString(8, Devicetype);
}
 
if (HasDeviceversion) {
output.WriteString(9, Deviceversion);
}
 
if (HasAccount) {
output.WriteString(10, Account);
}
 
if (HasValidateinfo) {
output.WriteString(11, Validateinfo);
}
 
if (HasChannelid) {
output.WriteString(12, Channelid);
}
 
if (HasMediachannel) {
output.WriteString(13, Mediachannel);
}
 
if (HasRapidvalidatecode) {
output.WriteInt32(14, Rapidvalidatecode);
}
 
if (HasReservedint1) {
output.WriteInt32(15, Reservedint1);
}
 
if (HasReservedint2) {
output.WriteInt32(16, Reservedint2);
}
 
if (HasReservedint3) {
output.WriteInt32(17, Reservedint3);
}
 
if (HasReservedint4) {
output.WriteInt32(18, Reservedint4);
}
 
if (HasReservedstring1) {
output.WriteString(19, Reservedstring1);
}
 
if (HasReservedstring2) {
output.WriteString(20, Reservedstring2);
}
 
if (HasReservedstring3) {
output.WriteString(21, Reservedstring3);
}
 
if (HasReservedstring4) {
output.WriteString(22, Reservedstring4);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_LOGIN _inst = (CG_LOGIN) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Vtype = input.ReadInt32();
break;
}
   case  16: {
 _inst.Gameversion = input.ReadInt32();
break;
}
   case  24: {
 _inst.Programversion = input.ReadInt32();
break;
}
   case  32: {
 _inst.Publicresourceversion = input.ReadInt32();
break;
}
   case  40: {
 _inst.Maxpacketid = input.ReadInt32();
break;
}
   case  48: {
 _inst.Forceenter = input.ReadInt32();
break;
}
   case  58: {
 _inst.Deviceid = input.ReadString();
break;
}
   case  66: {
 _inst.Devicetype = input.ReadString();
break;
}
   case  74: {
 _inst.Deviceversion = input.ReadString();
break;
}
   case  82: {
 _inst.Account = input.ReadString();
break;
}
   case  90: {
 _inst.Validateinfo = input.ReadString();
break;
}
   case  98: {
 _inst.Channelid = input.ReadString();
break;
}
   case  106: {
 _inst.Mediachannel = input.ReadString();
break;
}
   case  112: {
 _inst.Rapidvalidatecode = input.ReadInt32();
break;
}
   case  120: {
 _inst.Reservedint1 = input.ReadInt32();
break;
}
   case  128: {
 _inst.Reservedint2 = input.ReadInt32();
break;
}
   case  136: {
 _inst.Reservedint3 = input.ReadInt32();
break;
}
   case  144: {
 _inst.Reservedint4 = input.ReadInt32();
break;
}
   case  154: {
 _inst.Reservedstring1 = input.ReadString();
break;
}
   case  162: {
 _inst.Reservedstring2 = input.ReadString();
break;
}
   case  170: {
 _inst.Reservedstring3 = input.ReadString();
break;
}
   case  178: {
 _inst.Reservedstring4 = input.ReadString();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasVtype) return false;
 if (!hasGameversion) return false;
 if (!hasProgramversion) return false;
 if (!hasPublicresourceversion) return false;
 if (!hasMaxpacketid) return false;
 if (!hasForceenter) return false;
 if (!hasDeviceid) return false;
 if (!hasDevicetype) return false;
 if (!hasDeviceversion) return false;
 if (!hasAccount) return false;
 if (!hasValidateinfo) return false;
 if (!hasChannelid) return false;
 if (!hasMediachannel) return false;
 if (!hasRapidvalidatecode) return false;
 if (!hasReservedint1) return false;
 if (!hasReservedint2) return false;
 if (!hasReservedint3) return false;
 if (!hasReservedint4) return false;
 if (!hasReservedstring1) return false;
 if (!hasReservedstring2) return false;
 if (!hasReservedstring3) return false;
 if (!hasReservedstring4) return false;
 return true;
 }

}


[Serializable]
public class GC_LOGIN_RET : PacketDistributed
{
public enum LOGINRESULT 
 { 
  SUCCESS      = 1, 
  ACCOUNTVERIFYFAIL = 2, 
  READROLELISTFAIL = 3, 
  ALREADYLOGIN  = 4, 
  QUEUEFULL  = 5, 
  NEEDFORCEENTER = 6, 
  PACKETNOTMATCH = 7, 
  VERSIONNOTMATCH = 8, 
 }public enum VALIDATERESULT 
 { 
  OK           = 0, 
  FAIL_VALIDATETYPEERROR = 1, 
  FAIL_PERFORM      = 2, 
  FAIL_OPCODE       = 3, 
  FAIL_TAG        = 4, 
  FAIL_STATE       = 5, 
  FAIL_DATA_STATUS    = 6, 
  FAIL_CHANNELID     = 7, 
 }
public const int resultFieldNumber = 1;
 private bool hasResult;
 private Int32 result_ = 0;
 public bool HasResult {
 get { return hasResult; }
 }
 public Int32 Result {
 get { return result_; }
 set { SetResult(value); }
 }
 public void SetResult(Int32 value) { 
 hasResult = true;
 result_ = value;
 }

public const int validateresultFieldNumber = 2;
 private bool hasValidateresult;
 private Int32 validateresult_ = 0;
 public bool HasValidateresult {
 get { return hasValidateresult; }
 }
 public Int32 Validateresult {
 get { return validateresult_; }
 set { SetValidateresult(value); }
 }
 public void SetValidateresult(Int32 value) { 
 hasValidateresult = true;
 validateresult_ = value;
 }

public const int useridFieldNumber = 3;
 private bool hasUserid;
 private string userid_ = "";
 public bool HasUserid {
 get { return hasUserid; }
 }
 public string Userid {
 get { return userid_; }
 set { SetUserid(value); }
 }
 public void SetUserid(string value) { 
 hasUserid = true;
 userid_ = value;
 }

public const int oidFieldNumber = 4;
 private bool hasOid;
 private string oid_ = "";
 public bool HasOid {
 get { return hasOid; }
 }
 public string Oid {
 get { return oid_; }
 set { SetOid(value); }
 }
 public void SetOid(string value) { 
 hasOid = true;
 oid_ = value;
 }

public const int accesstokenFieldNumber = 5;
 private bool hasAccesstoken;
 private string accesstoken_ = "";
 public bool HasAccesstoken {
 get { return hasAccesstoken; }
 }
 public string Accesstoken {
 get { return accesstoken_; }
 set { SetAccesstoken(value); }
 }
 public void SetAccesstoken(string value) { 
 hasAccesstoken = true;
 accesstoken_ = value;
 }

public const int rapidvalidatecodeFieldNumber = 6;
 private bool hasRapidvalidatecode;
 private Int32 rapidvalidatecode_ = 0;
 public bool HasRapidvalidatecode {
 get { return hasRapidvalidatecode; }
 }
 public Int32 Rapidvalidatecode {
 get { return rapidvalidatecode_; }
 set { SetRapidvalidatecode(value); }
 }
 public void SetRapidvalidatecode(Int32 value) { 
 hasRapidvalidatecode = true;
 rapidvalidatecode_ = value;
 }

public const int roleGUIDListFieldNumber = 7;
 private pbc::PopsicleList<UInt64> roleGUIDList_ = new pbc::PopsicleList<UInt64>();
 public scg::IList<UInt64> roleGUIDListList {
 get { return pbc::Lists.AsReadOnly(roleGUIDList_); }
 }
 
 public int roleGUIDListCount {
 get { return roleGUIDList_.Count; }
 }
 
public UInt64 GetRoleGUIDList(int index) {
 return roleGUIDList_[index];
 }
 public void AddRoleGUIDList(UInt64 value) {
 roleGUIDList_.Add(value);
 }

public const int roleTypeListFieldNumber = 8;
 private pbc::PopsicleList<Int32> roleTypeList_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> roleTypeListList {
 get { return pbc::Lists.AsReadOnly(roleTypeList_); }
 }
 
 public int roleTypeListCount {
 get { return roleTypeList_.Count; }
 }
 
public Int32 GetRoleTypeList(int index) {
 return roleTypeList_[index];
 }
 public void AddRoleTypeList(Int32 value) {
 roleTypeList_.Add(value);
 }

public const int playerNameListFieldNumber = 9;
 private pbc::PopsicleList<string> playerNameList_ = new pbc::PopsicleList<string>();
 public scg::IList<string> playerNameListList {
 get { return pbc::Lists.AsReadOnly(playerNameList_); }
 }
 
 public int playerNameListCount {
 get { return playerNameList_.Count; }
 }
 
public string GetPlayerNameList(int index) {
 return playerNameList_[index];
 }
 public void AddPlayerNameList(string value) {
 playerNameList_.Add(value);
 }

public const int roleLevelListFieldNumber = 10;
 private pbc::PopsicleList<Int32> roleLevelList_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> roleLevelListList {
 get { return pbc::Lists.AsReadOnly(roleLevelList_); }
 }
 
 public int roleLevelListCount {
 get { return roleLevelList_.Count; }
 }
 
public Int32 GetRoleLevelList(int index) {
 return roleLevelList_[index];
 }
 public void AddRoleLevelList(Int32 value) {
 roleLevelList_.Add(value);
 }

public const int ModelVisualIDFieldNumber = 11;
 private pbc::PopsicleList<Int32> ModelVisualID_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> ModelVisualIDList {
 get { return pbc::Lists.AsReadOnly(ModelVisualID_); }
 }
 
 public int ModelVisualIDCount {
 get { return ModelVisualID_.Count; }
 }
 
public Int32 GetModelVisualID(int index) {
 return ModelVisualID_[index];
 }
 public void AddModelVisualID(Int32 value) {
 ModelVisualID_.Add(value);
 }

public const int WeaponIDFieldNumber = 12;
 private pbc::PopsicleList<Int32> WeaponID_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> WeaponIDList {
 get { return pbc::Lists.AsReadOnly(WeaponID_); }
 }
 
 public int WeaponIDCount {
 get { return WeaponID_.Count; }
 }
 
public Int32 GetWeaponID(int index) {
 return WeaponID_[index];
 }
 public void AddWeaponID(Int32 value) {
 WeaponID_.Add(value);
 }

public const int WeaponEffectGemFieldNumber = 13;
 private pbc::PopsicleList<Int32> WeaponEffectGem_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> WeaponEffectGemList {
 get { return pbc::Lists.AsReadOnly(WeaponEffectGem_); }
 }
 
 public int WeaponEffectGemCount {
 get { return WeaponEffectGem_.Count; }
 }
 
public Int32 GetWeaponEffectGem(int index) {
 return WeaponEffectGem_[index];
 }
 public void AddWeaponEffectGem(Int32 value) {
 WeaponEffectGem_.Add(value);
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasResult) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Result);
}
 if (HasValidateresult) {
size += pb::CodedOutputStream.ComputeInt32Size(2, Validateresult);
}
 if (HasUserid) {
size += pb::CodedOutputStream.ComputeStringSize(3, Userid);
}
 if (HasOid) {
size += pb::CodedOutputStream.ComputeStringSize(4, Oid);
}
 if (HasAccesstoken) {
size += pb::CodedOutputStream.ComputeStringSize(5, Accesstoken);
}
 if (HasRapidvalidatecode) {
size += pb::CodedOutputStream.ComputeInt32Size(6, Rapidvalidatecode);
}
{
int dataSize = 0;
for(int i=0; i<roleGUIDListList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeUInt64SizeNoTag(roleGUIDListList[i]);
}
size += dataSize;
size += 1 * roleGUIDList_.Count;
}
{
int dataSize = 0;
for(int i=0; i<roleTypeListList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(roleTypeListList[i]);
}
size += dataSize;
size += 1 * roleTypeList_.Count;
}
{
int dataSize = 0;
for(int i=0; i<playerNameListList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeStringSizeNoTag(playerNameListList[i]);
}
size += dataSize;
size += 1 * playerNameList_.Count;
}
{
int dataSize = 0;
for(int i=0; i<roleLevelListList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(roleLevelListList[i]);
}
size += dataSize;
size += 1 * roleLevelList_.Count;
}
{
int dataSize = 0;
for(int i=0; i<ModelVisualIDList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(ModelVisualIDList[i]);
}
size += dataSize;
size += 1 * ModelVisualID_.Count;
}
{
int dataSize = 0;
for(int i=0; i<WeaponIDList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(WeaponIDList[i]);
}
size += dataSize;
size += 1 * WeaponID_.Count;
}
{
int dataSize = 0;
for(int i=0; i<WeaponEffectGemList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(WeaponEffectGemList[i]);
}
size += dataSize;
size += 1 * WeaponEffectGem_.Count;
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasResult) {
output.WriteInt32(1, Result);
}
 
if (HasValidateresult) {
output.WriteInt32(2, Validateresult);
}
 
if (HasUserid) {
output.WriteString(3, Userid);
}
 
if (HasOid) {
output.WriteString(4, Oid);
}
 
if (HasAccesstoken) {
output.WriteString(5, Accesstoken);
}
 
if (HasRapidvalidatecode) {
output.WriteInt32(6, Rapidvalidatecode);
}
{
if (roleGUIDList_.Count > 0) {
for(int i=0; i<roleGUIDList_.Count; ++i){
output.WriteUInt64(7,roleGUIDList_[i]);
}
}

}
{
if (roleTypeList_.Count > 0) {
for(int i=0; i<roleTypeList_.Count; ++i){
output.WriteInt32(8,roleTypeList_[i]);
}
}

}
{
if (playerNameList_.Count > 0) {
for(int i=0; i<playerNameList_.Count; ++i){
output.WriteString(9,playerNameList_[i]);
}
}

}
{
if (roleLevelList_.Count > 0) {
for(int i=0; i<roleLevelList_.Count; ++i){
output.WriteInt32(10,roleLevelList_[i]);
}
}

}
{
if (ModelVisualID_.Count > 0) {
for(int i=0; i<ModelVisualID_.Count; ++i){
output.WriteInt32(11,ModelVisualID_[i]);
}
}

}
{
if (WeaponID_.Count > 0) {
for(int i=0; i<WeaponID_.Count; ++i){
output.WriteInt32(12,WeaponID_[i]);
}
}

}
{
if (WeaponEffectGem_.Count > 0) {
for(int i=0; i<WeaponEffectGem_.Count; ++i){
output.WriteInt32(13,WeaponEffectGem_[i]);
}
}

}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_LOGIN_RET _inst = (GC_LOGIN_RET) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Result = input.ReadInt32();
break;
}
   case  16: {
 _inst.Validateresult = input.ReadInt32();
break;
}
   case  26: {
 _inst.Userid = input.ReadString();
break;
}
   case  34: {
 _inst.Oid = input.ReadString();
break;
}
   case  42: {
 _inst.Accesstoken = input.ReadString();
break;
}
   case  48: {
 _inst.Rapidvalidatecode = input.ReadInt32();
break;
}
   case  56: {
 _inst.AddRoleGUIDList(input.ReadUInt64());
break;
}
   case  64: {
 _inst.AddRoleTypeList(input.ReadInt32());
break;
}
   case  74: {
 _inst.AddPlayerNameList(input.ReadString());
break;
}
   case  80: {
 _inst.AddRoleLevelList(input.ReadInt32());
break;
}
   case  88: {
 _inst.AddModelVisualID(input.ReadInt32());
break;
}
   case  96: {
 _inst.AddWeaponID(input.ReadInt32());
break;
}
   case  104: {
 _inst.AddWeaponEffectGem(input.ReadInt32());
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasResult) return false;
 if (!hasValidateresult) return false;
 if (!hasUserid) return false;
 if (!hasOid) return false;
 if (!hasAccesstoken) return false;
 if (!hasRapidvalidatecode) return false;
 return true;
 }

}


[Serializable]
public class GC_LOGIN_QUEUE_STATUS : PacketDistributed
{
public enum QUEUESTATUS 
 { 
  BEGINQUEUE = 0, 
  QUEUING = 1, 
  ENDQUEUE = 2, 
 }
public const int statusFieldNumber = 1;
 private bool hasStatus;
 private Int32 status_ = 0;
 public bool HasStatus {
 get { return hasStatus; }
 }
 public Int32 Status {
 get { return status_; }
 set { SetStatus(value); }
 }
 public void SetStatus(Int32 value) { 
 hasStatus = true;
 status_ = value;
 }

public const int indexFieldNumber = 2;
 private bool hasIndex;
 private Int32 index_ = 0;
 public bool HasIndex {
 get { return hasIndex; }
 }
 public Int32 Index {
 get { return index_; }
 set { SetIndex(value); }
 }
 public void SetIndex(Int32 value) { 
 hasIndex = true;
 index_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasStatus) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Status);
}
 if (HasIndex) {
size += pb::CodedOutputStream.ComputeInt32Size(2, Index);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasStatus) {
output.WriteInt32(1, Status);
}
 
if (HasIndex) {
output.WriteInt32(2, Index);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_LOGIN_QUEUE_STATUS _inst = (GC_LOGIN_QUEUE_STATUS) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Status = input.ReadInt32();
break;
}
   case  16: {
 _inst.Index = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasStatus) return false;
 if (!hasIndex) return false;
 return true;
 }

}


[Serializable]
public class CG_CREATEROLE : PacketDistributed
{

public const int typeFieldNumber = 1;
 private bool hasType;
 private Int32 type_ = 0;
 public bool HasType {
 get { return hasType; }
 }
 public Int32 Type {
 get { return type_; }
 set { SetType(value); }
 }
 public void SetType(Int32 value) { 
 hasType = true;
 type_ = value;
 }

public const int nameFieldNumber = 2;
 private bool hasName;
 private string name_ = "";
 public bool HasName {
 get { return hasName; }
 }
 public string Name {
 get { return name_; }
 set { SetName(value); }
 }
 public void SetName(string value) { 
 hasName = true;
 name_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasType) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Type);
}
 if (HasName) {
size += pb::CodedOutputStream.ComputeStringSize(2, Name);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasType) {
output.WriteInt32(1, Type);
}
 
if (HasName) {
output.WriteString(2, Name);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_CREATEROLE _inst = (CG_CREATEROLE) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Type = input.ReadInt32();
break;
}
   case  18: {
 _inst.Name = input.ReadString();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasType) return false;
 if (!hasName) return false;
 return true;
 }

}


[Serializable]
public class GC_CREATEROLE_RET : PacketDistributed
{
public enum CREATEROLE_RESULT 
 { 
  CREATEROLE_SUCCESS    = 0,  // 创建人物成功 
  CREATEROLE_FAIL    = 1,  // 服务器内部错误 
  CREATEROLE_FAIL_NAMEEXIST  = 2,  // 名字已经存在 
  CREATEROLE_FAIL_NAMESCREENING  = 3,  // 名字含有屏蔽字 
  CREATEROLE_FAIL_LONGNAME  = 4,  // 名字太长 
 
 
 }
public const int resultFieldNumber = 1;
 private bool hasResult;
 private Int32 result_ = 0;
 public bool HasResult {
 get { return hasResult; }
 }
 public Int32 Result {
 get { return result_; }
 set { SetResult(value); }
 }
 public void SetResult(Int32 value) { 
 hasResult = true;
 result_ = value;
 }

public const int professionFieldNumber = 2;
 private bool hasProfession;
 private Int32 profession_ = 0;
 public bool HasProfession {
 get { return hasProfession; }
 }
 public Int32 Profession {
 get { return profession_; }
 set { SetProfession(value); }
 }
 public void SetProfession(Int32 value) { 
 hasProfession = true;
 profession_ = value;
 }

public const int playerGuidFieldNumber = 3;
 private bool hasPlayerGuid;
 private UInt64 playerGuid_ = 0;
 public bool HasPlayerGuid {
 get { return hasPlayerGuid; }
 }
 public UInt64 PlayerGuid {
 get { return playerGuid_; }
 set { SetPlayerGuid(value); }
 }
 public void SetPlayerGuid(UInt64 value) { 
 hasPlayerGuid = true;
 playerGuid_ = value;
 }

public const int playerNameFieldNumber = 4;
 private bool hasPlayerName;
 private string playerName_ = "";
 public bool HasPlayerName {
 get { return hasPlayerName; }
 }
 public string PlayerName {
 get { return playerName_; }
 set { SetPlayerName(value); }
 }
 public void SetPlayerName(string value) { 
 hasPlayerName = true;
 playerName_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasResult) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Result);
}
 if (HasProfession) {
size += pb::CodedOutputStream.ComputeInt32Size(2, Profession);
}
 if (HasPlayerGuid) {
size += pb::CodedOutputStream.ComputeUInt64Size(3, PlayerGuid);
}
 if (HasPlayerName) {
size += pb::CodedOutputStream.ComputeStringSize(4, PlayerName);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasResult) {
output.WriteInt32(1, Result);
}
 
if (HasProfession) {
output.WriteInt32(2, Profession);
}
 
if (HasPlayerGuid) {
output.WriteUInt64(3, PlayerGuid);
}
 
if (HasPlayerName) {
output.WriteString(4, PlayerName);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_CREATEROLE_RET _inst = (GC_CREATEROLE_RET) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Result = input.ReadInt32();
break;
}
   case  16: {
 _inst.Profession = input.ReadInt32();
break;
}
   case  24: {
 _inst.PlayerGuid = input.ReadUInt64();
break;
}
   case  34: {
 _inst.PlayerName = input.ReadString();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasResult) return false;
 if (!hasProfession) return false;
 if (!hasPlayerGuid) return false;
 if (!hasPlayerName) return false;
 return true;
 }

}


[Serializable]
public class CG_SELECTROLE : PacketDistributed
{

public const int roleGUIDFieldNumber = 1;
 private bool hasRoleGUID;
 private UInt64 roleGUID_ = 0;
 public bool HasRoleGUID {
 get { return hasRoleGUID; }
 }
 public UInt64 RoleGUID {
 get { return roleGUID_; }
 set { SetRoleGUID(value); }
 }
 public void SetRoleGUID(UInt64 value) { 
 hasRoleGUID = true;
 roleGUID_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasRoleGUID) {
size += pb::CodedOutputStream.ComputeUInt64Size(1, RoleGUID);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasRoleGUID) {
output.WriteUInt64(1, RoleGUID);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_SELECTROLE _inst = (CG_SELECTROLE) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.RoleGUID = input.ReadUInt64();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasRoleGUID) return false;
 return true;
 }

}


[Serializable]
public class GC_SELECTROLE_RET : PacketDistributed
{
public enum SELECTROLE_RESULT 
 { 
  SELECTROLE_SUCCESS  = 0, 
  SELECTROLE_FAIL   = 1, 
 }
public const int resultFieldNumber = 1;
 private bool hasResult;
 private Int32 result_ = 0;
 public bool HasResult {
 get { return hasResult; }
 }
 public Int32 Result {
 get { return result_; }
 set { SetResult(value); }
 }
 public void SetResult(Int32 value) { 
 hasResult = true;
 result_ = value;
 }

public const int playerGuidFieldNumber = 2;
 private bool hasPlayerGuid;
 private UInt64 playerGuid_ = 0;
 public bool HasPlayerGuid {
 get { return hasPlayerGuid; }
 }
 public UInt64 PlayerGuid {
 get { return playerGuid_; }
 set { SetPlayerGuid(value); }
 }
 public void SetPlayerGuid(UInt64 value) { 
 hasPlayerGuid = true;
 playerGuid_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasResult) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Result);
}
 if (HasPlayerGuid) {
size += pb::CodedOutputStream.ComputeUInt64Size(2, PlayerGuid);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasResult) {
output.WriteInt32(1, Result);
}
 
if (HasPlayerGuid) {
output.WriteUInt64(2, PlayerGuid);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_SELECTROLE_RET _inst = (GC_SELECTROLE_RET) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Result = input.ReadInt32();
break;
}
   case  16: {
 _inst.PlayerGuid = input.ReadUInt64();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasResult) return false;
 if (!hasPlayerGuid) return false;
 return true;
 }

}


[Serializable]
public class CG_REQ_RANDOMNAME : PacketDistributed
{

public const int noneFieldNumber = 1;
 private bool hasNone;
 private Int32 none_ = 0;
 public bool HasNone {
 get { return hasNone; }
 }
 public Int32 None {
 get { return none_; }
 set { SetNone(value); }
 }
 public void SetNone(Int32 value) { 
 hasNone = true;
 none_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasNone) {
size += pb::CodedOutputStream.ComputeInt32Size(1, None);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasNone) {
output.WriteInt32(1, None);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_REQ_RANDOMNAME _inst = (CG_REQ_RANDOMNAME) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.None = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasNone) return false;
 return true;
 }

}


[Serializable]
public class GC_RET_RANDOMNAME : PacketDistributed
{

public const int namesFieldNumber = 1;
 private pbc::PopsicleList<string> names_ = new pbc::PopsicleList<string>();
 public scg::IList<string> namesList {
 get { return pbc::Lists.AsReadOnly(names_); }
 }
 
 public int namesCount {
 get { return names_.Count; }
 }
 
public string GetNames(int index) {
 return names_[index];
 }
 public void AddNames(string value) {
 names_.Add(value);
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
 {
int dataSize = 0;
for(int i=0; i<namesList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeStringSizeNoTag(namesList[i]);
}
size += dataSize;
size += 1 * names_.Count;
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
 {
if (names_.Count > 0) {
for(int i=0; i<names_.Count; ++i){
output.WriteString(1,names_[i]);
}
}

}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_RET_RANDOMNAME _inst = (GC_RET_RANDOMNAME) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  10: {
 _inst.AddNames(input.ReadString());
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  return true;
 }

}


[Serializable]
public class CG_REQ_CHANGE_SCENE : PacketDistributed
{
public enum CHANGETYPE 
 { 
  TELEPORT = 0,    //传送石 
  WORLDMAP = 1,    //世界地图 
  TRAIL   = 2,    //追杀功能 
  POINT   = 3,    //具体点传送 
 }
public const int ctypeFieldNumber = 1;
 private bool hasCtype;
 private Int32 ctype_ = 0;
 public bool HasCtype {
 get { return hasCtype; }
 }
 public Int32 Ctype {
 get { return ctype_; }
 set { SetCtype(value); }
 }
 public void SetCtype(Int32 value) { 
 hasCtype = true;
 ctype_ = value;
 }

public const int teleportidFieldNumber = 2;
 private bool hasTeleportid;
 private Int32 teleportid_ = 0;
 public bool HasTeleportid {
 get { return hasTeleportid; }
 }
 public Int32 Teleportid {
 get { return teleportid_; }
 set { SetTeleportid(value); }
 }
 public void SetTeleportid(Int32 value) { 
 hasTeleportid = true;
 teleportid_ = value;
 }

public const int sceneclassidFieldNumber = 3;
 private bool hasSceneclassid;
 private Int32 sceneclassid_ = 0;
 public bool HasSceneclassid {
 get { return hasSceneclassid; }
 }
 public Int32 Sceneclassid {
 get { return sceneclassid_; }
 set { SetSceneclassid(value); }
 }
 public void SetSceneclassid(Int32 value) { 
 hasSceneclassid = true;
 sceneclassid_ = value;
 }

public const int sceneinstidFieldNumber = 4;
 private bool hasSceneinstid;
 private Int32 sceneinstid_ = 0;
 public bool HasSceneinstid {
 get { return hasSceneinstid; }
 }
 public Int32 Sceneinstid {
 get { return sceneinstid_; }
 set { SetSceneinstid(value); }
 }
 public void SetSceneinstid(Int32 value) { 
 hasSceneinstid = true;
 sceneinstid_ = value;
 }

public const int posXFieldNumber = 5;
 private bool hasPosX;
 private Int32 posX_ = 0;
 public bool HasPosX {
 get { return hasPosX; }
 }
 public Int32 PosX {
 get { return posX_; }
 set { SetPosX(value); }
 }
 public void SetPosX(Int32 value) { 
 hasPosX = true;
 posX_ = value;
 }

public const int posZFieldNumber = 6;
 private bool hasPosZ;
 private Int32 posZ_ = 0;
 public bool HasPosZ {
 get { return hasPosZ; }
 }
 public Int32 PosZ {
 get { return posZ_; }
 set { SetPosZ(value); }
 }
 public void SetPosZ(Int32 value) { 
 hasPosZ = true;
 posZ_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasCtype) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Ctype);
}
 if (HasTeleportid) {
size += pb::CodedOutputStream.ComputeInt32Size(2, Teleportid);
}
 if (HasSceneclassid) {
size += pb::CodedOutputStream.ComputeInt32Size(3, Sceneclassid);
}
 if (HasSceneinstid) {
size += pb::CodedOutputStream.ComputeInt32Size(4, Sceneinstid);
}
 if (HasPosX) {
size += pb::CodedOutputStream.ComputeInt32Size(5, PosX);
}
 if (HasPosZ) {
size += pb::CodedOutputStream.ComputeInt32Size(6, PosZ);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasCtype) {
output.WriteInt32(1, Ctype);
}
 
if (HasTeleportid) {
output.WriteInt32(2, Teleportid);
}
 
if (HasSceneclassid) {
output.WriteInt32(3, Sceneclassid);
}
 
if (HasSceneinstid) {
output.WriteInt32(4, Sceneinstid);
}
 
if (HasPosX) {
output.WriteInt32(5, PosX);
}
 
if (HasPosZ) {
output.WriteInt32(6, PosZ);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_REQ_CHANGE_SCENE _inst = (CG_REQ_CHANGE_SCENE) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Ctype = input.ReadInt32();
break;
}
   case  16: {
 _inst.Teleportid = input.ReadInt32();
break;
}
   case  24: {
 _inst.Sceneclassid = input.ReadInt32();
break;
}
   case  32: {
 _inst.Sceneinstid = input.ReadInt32();
break;
}
   case  40: {
 _inst.PosX = input.ReadInt32();
break;
}
   case  48: {
 _inst.PosZ = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasCtype) return false;
 if (!hasTeleportid) return false;
 if (!hasSceneclassid) return false;
 if (!hasSceneinstid) return false;
 if (!hasPosX) return false;
 if (!hasPosZ) return false;
 return true;
 }

}


[Serializable]
public class GC_ENTER_SCENE : PacketDistributed
{

public const int sceneclassFieldNumber = 1;
 private bool hasSceneclass;
 private Int32 sceneclass_ = 0;
 public bool HasSceneclass {
 get { return hasSceneclass; }
 }
 public Int32 Sceneclass {
 get { return sceneclass_; }
 set { SetSceneclass(value); }
 }
 public void SetSceneclass(Int32 value) { 
 hasSceneclass = true;
 sceneclass_ = value;
 }

public const int sceneinstFieldNumber = 2;
 private bool hasSceneinst;
 private Int32 sceneinst_ = 0;
 public bool HasSceneinst {
 get { return hasSceneinst; }
 }
 public Int32 Sceneinst {
 get { return sceneinst_; }
 set { SetSceneinst(value); }
 }
 public void SetSceneinst(Int32 value) { 
 hasSceneinst = true;
 sceneinst_ = value;
 }

public const int mainplayerserveridFieldNumber = 3;
 private bool hasMainplayerserverid;
 private Int32 mainplayerserverid_ = 0;
 public bool HasMainplayerserverid {
 get { return hasMainplayerserverid; }
 }
 public Int32 Mainplayerserverid {
 get { return mainplayerserverid_; }
 set { SetMainplayerserverid(value); }
 }
 public void SetMainplayerserverid(Int32 value) { 
 hasMainplayerserverid = true;
 mainplayerserverid_ = value;
 }

public const int posXFieldNumber = 4;
 private bool hasPosX;
 private Int32 posX_ = 0;
 public bool HasPosX {
 get { return hasPosX; }
 }
 public Int32 PosX {
 get { return posX_; }
 set { SetPosX(value); }
 }
 public void SetPosX(Int32 value) { 
 hasPosX = true;
 posX_ = value;
 }

public const int posZFieldNumber = 5;
 private bool hasPosZ;
 private Int32 posZ_ = 0;
 public bool HasPosZ {
 get { return hasPosZ; }
 }
 public Int32 PosZ {
 get { return posZ_; }
 set { SetPosZ(value); }
 }
 public void SetPosZ(Int32 value) { 
 hasPosZ = true;
 posZ_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasSceneclass) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Sceneclass);
}
 if (HasSceneinst) {
size += pb::CodedOutputStream.ComputeInt32Size(2, Sceneinst);
}
 if (HasMainplayerserverid) {
size += pb::CodedOutputStream.ComputeInt32Size(3, Mainplayerserverid);
}
 if (HasPosX) {
size += pb::CodedOutputStream.ComputeInt32Size(4, PosX);
}
 if (HasPosZ) {
size += pb::CodedOutputStream.ComputeInt32Size(5, PosZ);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasSceneclass) {
output.WriteInt32(1, Sceneclass);
}
 
if (HasSceneinst) {
output.WriteInt32(2, Sceneinst);
}
 
if (HasMainplayerserverid) {
output.WriteInt32(3, Mainplayerserverid);
}
 
if (HasPosX) {
output.WriteInt32(4, PosX);
}
 
if (HasPosZ) {
output.WriteInt32(5, PosZ);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_ENTER_SCENE _inst = (GC_ENTER_SCENE) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Sceneclass = input.ReadInt32();
break;
}
   case  16: {
 _inst.Sceneinst = input.ReadInt32();
break;
}
   case  24: {
 _inst.Mainplayerserverid = input.ReadInt32();
break;
}
   case  32: {
 _inst.PosX = input.ReadInt32();
break;
}
   case  40: {
 _inst.PosZ = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasSceneclass) return false;
 if (!hasSceneinst) return false;
 if (!hasMainplayerserverid) return false;
 if (!hasPosX) return false;
 if (!hasPosZ) return false;
 return true;
 }

}


[Serializable]
public class CG_ENTER_SCENE_OK : PacketDistributed
{

public const int isOKFieldNumber = 1;
 private bool hasIsOK;
 private Int32 isOK_ = 0;
 public bool HasIsOK {
 get { return hasIsOK; }
 }
 public Int32 IsOK {
 get { return isOK_; }
 set { SetIsOK(value); }
 }
 public void SetIsOK(Int32 value) { 
 hasIsOK = true;
 isOK_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasIsOK) {
size += pb::CodedOutputStream.ComputeInt32Size(1, IsOK);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasIsOK) {
output.WriteInt32(1, IsOK);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_ENTER_SCENE_OK _inst = (CG_ENTER_SCENE_OK) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.IsOK = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasIsOK) return false;
 return true;
 }

}


[Serializable]
public class CG_CONNECTED_HEARTBEAT : PacketDistributed
{

public const int isresponseFieldNumber = 1;
 private bool hasIsresponse;
 private Int32 isresponse_ = 0;
 public bool HasIsresponse {
 get { return hasIsresponse; }
 }
 public Int32 Isresponse {
 get { return isresponse_; }
 set { SetIsresponse(value); }
 }
 public void SetIsresponse(Int32 value) { 
 hasIsresponse = true;
 isresponse_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasIsresponse) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Isresponse);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasIsresponse) {
output.WriteInt32(1, Isresponse);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_CONNECTED_HEARTBEAT _inst = (CG_CONNECTED_HEARTBEAT) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Isresponse = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasIsresponse) return false;
 return true;
 }

}


[Serializable]
public class GC_CONNECTED_HEARTBEAT : PacketDistributed
{

public const int serveransitimeFieldNumber = 1;
 private bool hasServeransitime;
 private Int32 serveransitime_ = 0;
 public bool HasServeransitime {
 get { return hasServeransitime; }
 }
 public Int32 Serveransitime {
 get { return serveransitime_; }
 set { SetServeransitime(value); }
 }
 public void SetServeransitime(Int32 value) { 
 hasServeransitime = true;
 serveransitime_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasServeransitime) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Serveransitime);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasServeransitime) {
output.WriteInt32(1, Serveransitime);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_CONNECTED_HEARTBEAT _inst = (GC_CONNECTED_HEARTBEAT) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Serveransitime = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasServeransitime) return false;
 return true;
 }

}


[Serializable]
public class GC_NOTICE : PacketDistributed
{

public const int noticeFieldNumber = 1;
 private bool hasNotice;
 private string notice_ = "";
 public bool HasNotice {
 get { return hasNotice; }
 }
 public string Notice {
 get { return notice_; }
 set { SetNotice(value); }
 }
 public void SetNotice(string value) { 
 hasNotice = true;
 notice_ = value;
 }

public const int filterRepeatFieldNumber = 2;
 private bool hasFilterRepeat;
 private Int32 filterRepeat_ = 0;
 public bool HasFilterRepeat {
 get { return hasFilterRepeat; }
 }
 public Int32 FilterRepeat {
 get { return filterRepeat_; }
 set { SetFilterRepeat(value); }
 }
 public void SetFilterRepeat(Int32 value) { 
 hasFilterRepeat = true;
 filterRepeat_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasNotice) {
size += pb::CodedOutputStream.ComputeStringSize(1, Notice);
}
 if (HasFilterRepeat) {
size += pb::CodedOutputStream.ComputeInt32Size(2, FilterRepeat);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasNotice) {
output.WriteString(1, Notice);
}
 
if (HasFilterRepeat) {
output.WriteInt32(2, FilterRepeat);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_NOTICE _inst = (GC_NOTICE) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  10: {
 _inst.Notice = input.ReadString();
break;
}
   case  16: {
 _inst.FilterRepeat = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasNotice) return false;
 return true;
 }

}


[Serializable]
public class GC_MISSION_SYNC_MISSIONLIST : PacketDistributed
{

public const int missionIDFieldNumber = 1;
 private pbc::PopsicleList<Int32> missionID_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> missionIDList {
 get { return pbc::Lists.AsReadOnly(missionID_); }
 }
 
 public int missionIDCount {
 get { return missionID_.Count; }
 }
 
public Int32 GetMissionID(int index) {
 return missionID_[index];
 }
 public void AddMissionID(Int32 value) {
 missionID_.Add(value);
 }

public const int stateFieldNumber = 2;
 private pbc::PopsicleList<Int32> state_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> stateList {
 get { return pbc::Lists.AsReadOnly(state_); }
 }
 
 public int stateCount {
 get { return state_.Count; }
 }
 
public Int32 GetState(int index) {
 return state_[index];
 }
 public void AddState(Int32 value) {
 state_.Add(value);
 }

public const int nParamFieldNumber = 3;
 private pbc::PopsicleList<Int32> nParam_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> nParamList {
 get { return pbc::Lists.AsReadOnly(nParam_); }
 }
 
 public int nParamCount {
 get { return nParam_.Count; }
 }
 
public Int32 GetNParam(int index) {
 return nParam_[index];
 }
 public void AddNParam(Int32 value) {
 nParam_.Add(value);
 }

public const int havedoneFlagFieldNumber = 4;
 private pbc::PopsicleList<UInt32> havedoneFlag_ = new pbc::PopsicleList<UInt32>();
 public scg::IList<UInt32> havedoneFlagList {
 get { return pbc::Lists.AsReadOnly(havedoneFlag_); }
 }
 
 public int havedoneFlagCount {
 get { return havedoneFlag_.Count; }
 }
 
public UInt32 GetHavedoneFlag(int index) {
 return havedoneFlag_[index];
 }
 public void AddHavedoneFlag(UInt32 value) {
 havedoneFlag_.Add(value);
 }

public const int qualitytypeFieldNumber = 5;
 private pbc::PopsicleList<Int32> qualitytype_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> qualitytypeList {
 get { return pbc::Lists.AsReadOnly(qualitytype_); }
 }
 
 public int qualitytypeCount {
 get { return qualitytype_.Count; }
 }
 
public Int32 GetQualitytype(int index) {
 return qualitytype_[index];
 }
 public void AddQualitytype(Int32 value) {
 qualitytype_.Add(value);
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
 {
int dataSize = 0;
for(int i=0; i<missionIDList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(missionIDList[i]);
}
size += dataSize;
size += 1 * missionID_.Count;
}
{
int dataSize = 0;
for(int i=0; i<stateList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(stateList[i]);
}
size += dataSize;
size += 1 * state_.Count;
}
{
int dataSize = 0;
for(int i=0; i<nParamList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(nParamList[i]);
}
size += dataSize;
size += 1 * nParam_.Count;
}
{
int dataSize = 0;
for(int i=0; i<havedoneFlagList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeUInt32SizeNoTag(havedoneFlagList[i]);
}
size += dataSize;
size += 1 * havedoneFlag_.Count;
}
{
int dataSize = 0;
for(int i=0; i<qualitytypeList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(qualitytypeList[i]);
}
size += dataSize;
size += 1 * qualitytype_.Count;
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
 {
if (missionID_.Count > 0) {
for(int i=0; i<missionID_.Count; ++i){
output.WriteInt32(1,missionID_[i]);
}
}

}
{
if (state_.Count > 0) {
for(int i=0; i<state_.Count; ++i){
output.WriteInt32(2,state_[i]);
}
}

}
{
if (nParam_.Count > 0) {
for(int i=0; i<nParam_.Count; ++i){
output.WriteInt32(3,nParam_[i]);
}
}

}
{
if (havedoneFlag_.Count > 0) {
for(int i=0; i<havedoneFlag_.Count; ++i){
output.WriteUInt32(4,havedoneFlag_[i]);
}
}

}
{
if (qualitytype_.Count > 0) {
for(int i=0; i<qualitytype_.Count; ++i){
output.WriteInt32(5,qualitytype_[i]);
}
}

}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_MISSION_SYNC_MISSIONLIST _inst = (GC_MISSION_SYNC_MISSIONLIST) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.AddMissionID(input.ReadInt32());
break;
}
   case  16: {
 _inst.AddState(input.ReadInt32());
break;
}
   case  24: {
 _inst.AddNParam(input.ReadInt32());
break;
}
   case  32: {
 _inst.AddHavedoneFlag(input.ReadUInt32());
break;
}
   case  40: {
 _inst.AddQualitytype(input.ReadInt32());
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  return true;
 }

}


[Serializable]
public class CG_ACCEPTMISSION : PacketDistributed
{

public const int MissionIDFieldNumber = 1;
 private bool hasMissionID;
 private Int32 MissionID_ = 0;
 public bool HasMissionID {
 get { return hasMissionID; }
 }
 public Int32 MissionID {
 get { return MissionID_; }
 set { SetMissionID(value); }
 }
 public void SetMissionID(Int32 value) { 
 hasMissionID = true;
 MissionID_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasMissionID) {
size += pb::CodedOutputStream.ComputeInt32Size(1, MissionID);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasMissionID) {
output.WriteInt32(1, MissionID);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_ACCEPTMISSION _inst = (CG_ACCEPTMISSION) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.MissionID = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasMissionID) return false;
 return true;
 }

}


[Serializable]
public class GC_ACCEPTMISSION_RET : PacketDistributed
{

public const int MissionIDFieldNumber = 1;
 private bool hasMissionID;
 private Int32 MissionID_ = 0;
 public bool HasMissionID {
 get { return hasMissionID; }
 }
 public Int32 MissionID {
 get { return MissionID_; }
 set { SetMissionID(value); }
 }
 public void SetMissionID(Int32 value) { 
 hasMissionID = true;
 MissionID_ = value;
 }

public const int QualityTypeFieldNumber = 2;
 private bool hasQualityType;
 private Int32 QualityType_ = 0;
 public bool HasQualityType {
 get { return hasQualityType; }
 }
 public Int32 QualityType {
 get { return QualityType_; }
 set { SetQualityType(value); }
 }
 public void SetQualityType(Int32 value) { 
 hasQualityType = true;
 QualityType_ = value;
 }

public const int RetFieldNumber = 3;
 private bool hasRet;
 private Int32 Ret_ = 0;
 public bool HasRet {
 get { return hasRet; }
 }
 public Int32 Ret {
 get { return Ret_; }
 set { SetRet(value); }
 }
 public void SetRet(Int32 value) { 
 hasRet = true;
 Ret_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasMissionID) {
size += pb::CodedOutputStream.ComputeInt32Size(1, MissionID);
}
 if (HasQualityType) {
size += pb::CodedOutputStream.ComputeInt32Size(2, QualityType);
}
 if (HasRet) {
size += pb::CodedOutputStream.ComputeInt32Size(3, Ret);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasMissionID) {
output.WriteInt32(1, MissionID);
}
 
if (HasQualityType) {
output.WriteInt32(2, QualityType);
}
 
if (HasRet) {
output.WriteInt32(3, Ret);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_ACCEPTMISSION_RET _inst = (GC_ACCEPTMISSION_RET) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.MissionID = input.ReadInt32();
break;
}
   case  16: {
 _inst.QualityType = input.ReadInt32();
break;
}
   case  24: {
 _inst.Ret = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasMissionID) return false;
 if (!hasQualityType) return false;
 if (!hasRet) return false;
 return true;
 }

}


[Serializable]
public class CG_COMPLETEMISSION : PacketDistributed
{

public const int MissionIDFieldNumber = 1;
 private bool hasMissionID;
 private Int32 MissionID_ = 0;
 public bool HasMissionID {
 get { return hasMissionID; }
 }
 public Int32 MissionID {
 get { return MissionID_; }
 set { SetMissionID(value); }
 }
 public void SetMissionID(Int32 value) { 
 hasMissionID = true;
 MissionID_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasMissionID) {
size += pb::CodedOutputStream.ComputeInt32Size(1, MissionID);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasMissionID) {
output.WriteInt32(1, MissionID);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_COMPLETEMISSION _inst = (CG_COMPLETEMISSION) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.MissionID = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasMissionID) return false;
 return true;
 }

}


[Serializable]
public class GC_COMPLETEMISSION_RET : PacketDistributed
{

public const int MissionIDFieldNumber = 1;
 private bool hasMissionID;
 private Int32 MissionID_ = 0;
 public bool HasMissionID {
 get { return hasMissionID; }
 }
 public Int32 MissionID {
 get { return MissionID_; }
 set { SetMissionID(value); }
 }
 public void SetMissionID(Int32 value) { 
 hasMissionID = true;
 MissionID_ = value;
 }

public const int RetFieldNumber = 2;
 private bool hasRet;
 private Int32 Ret_ = 0;
 public bool HasRet {
 get { return hasRet; }
 }
 public Int32 Ret {
 get { return Ret_; }
 set { SetRet(value); }
 }
 public void SetRet(Int32 value) { 
 hasRet = true;
 Ret_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasMissionID) {
size += pb::CodedOutputStream.ComputeInt32Size(1, MissionID);
}
 if (HasRet) {
size += pb::CodedOutputStream.ComputeInt32Size(2, Ret);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasMissionID) {
output.WriteInt32(1, MissionID);
}
 
if (HasRet) {
output.WriteInt32(2, Ret);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_COMPLETEMISSION_RET _inst = (GC_COMPLETEMISSION_RET) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.MissionID = input.ReadInt32();
break;
}
   case  16: {
 _inst.Ret = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasMissionID) return false;
 if (!hasRet) return false;
 return true;
 }

}


[Serializable]
public class CG_ABANDONMISSION : PacketDistributed
{

public const int MissionIDFieldNumber = 1;
 private bool hasMissionID;
 private Int32 MissionID_ = 0;
 public bool HasMissionID {
 get { return hasMissionID; }
 }
 public Int32 MissionID {
 get { return MissionID_; }
 set { SetMissionID(value); }
 }
 public void SetMissionID(Int32 value) { 
 hasMissionID = true;
 MissionID_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasMissionID) {
size += pb::CodedOutputStream.ComputeInt32Size(1, MissionID);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasMissionID) {
output.WriteInt32(1, MissionID);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_ABANDONMISSION _inst = (CG_ABANDONMISSION) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.MissionID = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasMissionID) return false;
 return true;
 }

}


[Serializable]
public class GC_ABANDONMISSION_RET : PacketDistributed
{

public const int MissionIDFieldNumber = 1;
 private bool hasMissionID;
 private Int32 MissionID_ = 0;
 public bool HasMissionID {
 get { return hasMissionID; }
 }
 public Int32 MissionID {
 get { return MissionID_; }
 set { SetMissionID(value); }
 }
 public void SetMissionID(Int32 value) { 
 hasMissionID = true;
 MissionID_ = value;
 }

public const int RetFieldNumber = 2;
 private bool hasRet;
 private Int32 Ret_ = 0;
 public bool HasRet {
 get { return hasRet; }
 }
 public Int32 Ret {
 get { return Ret_; }
 set { SetRet(value); }
 }
 public void SetRet(Int32 value) { 
 hasRet = true;
 Ret_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasMissionID) {
size += pb::CodedOutputStream.ComputeInt32Size(1, MissionID);
}
 if (HasRet) {
size += pb::CodedOutputStream.ComputeInt32Size(2, Ret);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasMissionID) {
output.WriteInt32(1, MissionID);
}
 
if (HasRet) {
output.WriteInt32(2, Ret);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_ABANDONMISSION_RET _inst = (GC_ABANDONMISSION_RET) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.MissionID = input.ReadInt32();
break;
}
   case  16: {
 _inst.Ret = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasMissionID) return false;
 if (!hasRet) return false;
 return true;
 }

}


[Serializable]
public class GC_MISSION_STATE : PacketDistributed
{

public const int MissionIDFieldNumber = 1;
 private bool hasMissionID;
 private Int32 MissionID_ = 0;
 public bool HasMissionID {
 get { return hasMissionID; }
 }
 public Int32 MissionID {
 get { return MissionID_; }
 set { SetMissionID(value); }
 }
 public void SetMissionID(Int32 value) { 
 hasMissionID = true;
 MissionID_ = value;
 }

public const int StateFieldNumber = 2;
 private bool hasState;
 private Int32 State_ = 0;
 public bool HasState {
 get { return hasState; }
 }
 public Int32 State {
 get { return State_; }
 set { SetState(value); }
 }
 public void SetState(Int32 value) { 
 hasState = true;
 State_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasMissionID) {
size += pb::CodedOutputStream.ComputeInt32Size(1, MissionID);
}
 if (HasState) {
size += pb::CodedOutputStream.ComputeInt32Size(2, State);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasMissionID) {
output.WriteInt32(1, MissionID);
}
 
if (HasState) {
output.WriteInt32(2, State);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_MISSION_STATE _inst = (GC_MISSION_STATE) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.MissionID = input.ReadInt32();
break;
}
   case  16: {
 _inst.State = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasMissionID) return false;
 if (!hasState) return false;
 return true;
 }

}


[Serializable]
public class GC_MISSION_PARAM : PacketDistributed
{

public const int MissionIDFieldNumber = 1;
 private bool hasMissionID;
 private Int32 MissionID_ = 0;
 public bool HasMissionID {
 get { return hasMissionID; }
 }
 public Int32 MissionID {
 get { return MissionID_; }
 set { SetMissionID(value); }
 }
 public void SetMissionID(Int32 value) { 
 hasMissionID = true;
 MissionID_ = value;
 }

public const int ParamIndexFieldNumber = 2;
 private bool hasParamIndex;
 private Int32 ParamIndex_ = 0;
 public bool HasParamIndex {
 get { return hasParamIndex; }
 }
 public Int32 ParamIndex {
 get { return ParamIndex_; }
 set { SetParamIndex(value); }
 }
 public void SetParamIndex(Int32 value) { 
 hasParamIndex = true;
 ParamIndex_ = value;
 }

public const int ParamFieldNumber = 3;
 private bool hasParam;
 private Int32 Param_ = 0;
 public bool HasParam {
 get { return hasParam; }
 }
 public Int32 Param {
 get { return Param_; }
 set { SetParam(value); }
 }
 public void SetParam(Int32 value) { 
 hasParam = true;
 Param_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasMissionID) {
size += pb::CodedOutputStream.ComputeInt32Size(1, MissionID);
}
 if (HasParamIndex) {
size += pb::CodedOutputStream.ComputeInt32Size(2, ParamIndex);
}
 if (HasParam) {
size += pb::CodedOutputStream.ComputeInt32Size(3, Param);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasMissionID) {
output.WriteInt32(1, MissionID);
}
 
if (HasParamIndex) {
output.WriteInt32(2, ParamIndex);
}
 
if (HasParam) {
output.WriteInt32(3, Param);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_MISSION_PARAM _inst = (GC_MISSION_PARAM) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.MissionID = input.ReadInt32();
break;
}
   case  16: {
 _inst.ParamIndex = input.ReadInt32();
break;
}
   case  24: {
 _inst.Param = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasMissionID) return false;
 if (!hasParamIndex) return false;
 if (!hasParam) return false;
 return true;
 }

}


[Serializable]
public class GC_CREATE_PLAYER : PacketDistributed
{

public const int serverIdFieldNumber = 1;
 private bool hasServerId;
 private Int32 serverId_ = 0;
 public bool HasServerId {
 get { return hasServerId; }
 }
 public Int32 ServerId {
 get { return serverId_; }
 set { SetServerId(value); }
 }
 public void SetServerId(Int32 value) { 
 hasServerId = true;
 serverId_ = value;
 }

public const int guidFieldNumber = 2;
 private bool hasGuid;
 private UInt64 guid_ = 0;
 public bool HasGuid {
 get { return hasGuid; }
 }
 public UInt64 Guid {
 get { return guid_; }
 set { SetGuid(value); }
 }
 public void SetGuid(UInt64 value) { 
 hasGuid = true;
 guid_ = value;
 }

public const int sceneInstFieldNumber = 3;
 private bool hasSceneInst;
 private Int32 sceneInst_ = 0;
 public bool HasSceneInst {
 get { return hasSceneInst; }
 }
 public Int32 SceneInst {
 get { return sceneInst_; }
 set { SetSceneInst(value); }
 }
 public void SetSceneInst(Int32 value) { 
 hasSceneInst = true;
 sceneInst_ = value;
 }

public const int sceneClassFieldNumber = 4;
 private bool hasSceneClass;
 private Int32 sceneClass_ = 0;
 public bool HasSceneClass {
 get { return hasSceneClass; }
 }
 public Int32 SceneClass {
 get { return sceneClass_; }
 set { SetSceneClass(value); }
 }
 public void SetSceneClass(Int32 value) { 
 hasSceneClass = true;
 sceneClass_ = value;
 }

public const int dataIdFieldNumber = 5;
 private bool hasDataId;
 private Int32 dataId_ = 0;
 public bool HasDataId {
 get { return hasDataId; }
 }
 public Int32 DataId {
 get { return dataId_; }
 set { SetDataId(value); }
 }
 public void SetDataId(Int32 value) { 
 hasDataId = true;
 dataId_ = value;
 }

public const int posXFieldNumber = 6;
 private bool hasPosX;
 private Int32 posX_ = 0;
 public bool HasPosX {
 get { return hasPosX; }
 }
 public Int32 PosX {
 get { return posX_; }
 set { SetPosX(value); }
 }
 public void SetPosX(Int32 value) { 
 hasPosX = true;
 posX_ = value;
 }

public const int posZFieldNumber = 7;
 private bool hasPosZ;
 private Int32 posZ_ = 0;
 public bool HasPosZ {
 get { return hasPosZ; }
 }
 public Int32 PosZ {
 get { return posZ_; }
 set { SetPosZ(value); }
 }
 public void SetPosZ(Int32 value) { 
 hasPosZ = true;
 posZ_ = value;
 }

public const int curforceFieldNumber = 8;
 private bool hasCurforce;
 private Int32 curforce_ = 0;
 public bool HasCurforce {
 get { return hasCurforce; }
 }
 public Int32 Curforce {
 get { return curforce_; }
 set { SetCurforce(value); }
 }
 public void SetCurforce(Int32 value) { 
 hasCurforce = true;
 curforce_ = value;
 }

public const int nameFieldNumber = 9;
 private bool hasName;
 private string name_ = "";
 public bool HasName {
 get { return hasName; }
 }
 public string Name {
 get { return name_; }
 set { SetName(value); }
 }
 public void SetName(string value) { 
 hasName = true;
 name_ = value;
 }

public const int curProfessionFieldNumber = 10;
 private bool hasCurProfession;
 private Int32 curProfession_ = 0;
 public bool HasCurProfession {
 get { return hasCurProfession; }
 }
 public Int32 CurProfession {
 get { return curProfession_; }
 set { SetCurProfession(value); }
 }
 public void SetCurProfession(Int32 value) { 
 hasCurProfession = true;
 curProfession_ = value;
 }

public const int facedirFieldNumber = 11;
 private bool hasFacedir;
 private Int32 facedir_ = 0;
 public bool HasFacedir {
 get { return hasFacedir; }
 }
 public Int32 Facedir {
 get { return facedir_; }
 set { SetFacedir(value); }
 }
 public void SetFacedir(Int32 value) { 
 hasFacedir = true;
 facedir_ = value;
 }

public const int titlenameFieldNumber = 12;
 private bool hasTitlename;
 private string titlename_ = "";
 public bool HasTitlename {
 get { return hasTitlename; }
 }
 public string Titlename {
 get { return titlename_; }
 set { SetTitlename(value); }
 }
 public void SetTitlename(string value) { 
 hasTitlename = true;
 titlename_ = value;
 }

public const int isInPkListFieldNumber = 13;
 private bool hasIsInPkList;
 private Int32 isInPkList_ = 0;
 public bool HasIsInPkList {
 get { return hasIsInPkList; }
 }
 public Int32 IsInPkList {
 get { return isInPkList_; }
 set { SetIsInPkList(value); }
 }
 public void SetIsInPkList(Int32 value) { 
 hasIsInPkList = true;
 isInPkList_ = value;
 }

public const int isDieFieldNumber = 14;
 private bool hasIsDie;
 private Int32 isDie_ = 0;
 public bool HasIsDie {
 get { return hasIsDie; }
 }
 public Int32 IsDie {
 get { return isDie_; }
 set { SetIsDie(value); }
 }
 public void SetIsDie(Int32 value) { 
 hasIsDie = true;
 isDie_ = value;
 }

public const int ReliveTimeFieldNumber = 15;
 private bool hasReliveTime;
 private Int32 ReliveTime_ = 0;
 public bool HasReliveTime {
 get { return hasReliveTime; }
 }
 public Int32 ReliveTime {
 get { return ReliveTime_; }
 set { SetReliveTime(value); }
 }
 public void SetReliveTime(Int32 value) { 
 hasReliveTime = true;
 ReliveTime_ = value;
 }

public const int PKModleFieldNumber = 16;
 private bool hasPKModle;
 private Int32 PKModle_ = 0;
 public bool HasPKModle {
 get { return hasPKModle; }
 }
 public Int32 PKModle {
 get { return PKModle_; }
 set { SetPKModle(value); }
 }
 public void SetPKModle(Int32 value) { 
 hasPKModle = true;
 PKModle_ = value;
 }

public const int MountIDFieldNumber = 17;
 private bool hasMountID;
 private Int32 MountID_ = 0;
 public bool HasMountID {
 get { return hasMountID; }
 }
 public Int32 MountID {
 get { return MountID_; }
 set { SetMountID(value); }
 }
 public void SetMountID(Int32 value) { 
 hasMountID = true;
 MountID_ = value;
 }

public const int MoveSpeedFieldNumber = 18;
 private bool hasMoveSpeed;
 private Int32 MoveSpeed_ = 0;
 public bool HasMoveSpeed {
 get { return hasMoveSpeed; }
 }
 public Int32 MoveSpeed {
 get { return MoveSpeed_; }
 set { SetMoveSpeed(value); }
 }
 public void SetMoveSpeed(Int32 value) { 
 hasMoveSpeed = true;
 MoveSpeed_ = value;
 }

public const int ModelVisualIDFieldNumber = 19;
 private bool hasModelVisualID;
 private Int32 ModelVisualID_ = 0;
 public bool HasModelVisualID {
 get { return hasModelVisualID; }
 }
 public Int32 ModelVisualID {
 get { return ModelVisualID_; }
 set { SetModelVisualID(value); }
 }
 public void SetModelVisualID(Int32 value) { 
 hasModelVisualID = true;
 ModelVisualID_ = value;
 }

public const int WeaponDataIDFieldNumber = 20;
 private bool hasWeaponDataID;
 private Int32 WeaponDataID_ = 0;
 public bool HasWeaponDataID {
 get { return hasWeaponDataID; }
 }
 public Int32 WeaponDataID {
 get { return WeaponDataID_; }
 set { SetWeaponDataID(value); }
 }
 public void SetWeaponDataID(Int32 value) { 
 hasWeaponDataID = true;
 WeaponDataID_ = value;
 }

public const int WeaponEffectGemFieldNumber = 22;
 private bool hasWeaponEffectGem;
 private Int32 WeaponEffectGem_ = 0;
 public bool HasWeaponEffectGem {
 get { return hasWeaponEffectGem; }
 }
 public Int32 WeaponEffectGem {
 get { return WeaponEffectGem_; }
 set { SetWeaponEffectGem(value); }
 }
 public void SetWeaponEffectGem(Int32 value) { 
 hasWeaponEffectGem = true;
 WeaponEffectGem_ = value;
 }

public const int CurTitleIDFieldNumber = 23;
 private bool hasCurTitleID;
 private Int32 CurTitleID_ = 0;
 public bool HasCurTitleID {
 get { return hasCurTitleID; }
 }
 public Int32 CurTitleID {
 get { return CurTitleID_; }
 set { SetCurTitleID(value); }
 }
 public void SetCurTitleID(Int32 value) { 
 hasCurTitleID = true;
 CurTitleID_ = value;
 }

public const int StealthLevFieldNumber = 24;
 private bool hasStealthLev;
 private Int32 StealthLev_ = 0;
 public bool HasStealthLev {
 get { return hasStealthLev; }
 }
 public Int32 StealthLev {
 get { return StealthLev_; }
 set { SetStealthLev(value); }
 }
 public void SetStealthLev(Int32 value) { 
 hasStealthLev = true;
 StealthLev_ = value;
 }

public const int VipCostFieldNumber = 25;
 private bool hasVipCost;
 private Int32 VipCost_ = 0;
 public bool HasVipCost {
 get { return hasVipCost; }
 }
 public Int32 VipCost {
 get { return VipCost_; }
 set { SetVipCost(value); }
 }
 public void SetVipCost(Int32 value) { 
 hasVipCost = true;
 VipCost_ = value;
 }

public const int GuildGuidFieldNumber = 26;
 private bool hasGuildGuid;
 private UInt64 GuildGuid_ = 0;
 public bool HasGuildGuid {
 get { return hasGuildGuid; }
 }
 public UInt64 GuildGuid {
 get { return GuildGuid_; }
 set { SetGuildGuid(value); }
 }
 public void SetGuildGuid(UInt64 value) { 
 hasGuildGuid = true;
 GuildGuid_ = value;
 }

public const int CombatValueFieldNumber = 27;
 private bool hasCombatValue;
 private Int32 CombatValue_ = 0;
 public bool HasCombatValue {
 get { return hasCombatValue; }
 }
 public Int32 CombatValue {
 get { return CombatValue_; }
 set { SetCombatValue(value); }
 }
 public void SetCombatValue(Int32 value) { 
 hasCombatValue = true;
 CombatValue_ = value;
 }

public const int bindparentFieldNumber = 28;
 private bool hasBindparent;
 private Int32 bindparent_ = 0;
 public bool HasBindparent {
 get { return hasBindparent; }
 }
 public Int32 Bindparent {
 get { return bindparent_; }
 set { SetBindparent(value); }
 }
 public void SetBindparent(Int32 value) { 
 hasBindparent = true;
 bindparent_ = value;
 }

public const int bindchildrenFieldNumber = 29;
 private pbc::PopsicleList<Int32> bindchildren_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> bindchildrenList {
 get { return pbc::Lists.AsReadOnly(bindchildren_); }
 }
 
 public int bindchildrenCount {
 get { return bindchildren_.Count; }
 }
 
public Int32 GetBindchildren(int index) {
 return bindchildren_[index];
 }
 public void AddBindchildren(Int32 value) {
 bindchildren_.Add(value);
 }

public const int isEnemy2SelfFieldNumber = 30;
 private bool hasIsEnemy2Self;
 private Int32 isEnemy2Self_ = 0;
 public bool HasIsEnemy2Self {
 get { return hasIsEnemy2Self; }
 }
 public Int32 IsEnemy2Self {
 get { return isEnemy2Self_; }
 set { SetIsEnemy2Self(value); }
 }
 public void SetIsEnemy2Self(Int32 value) { 
 hasIsEnemy2Self = true;
 isEnemy2Self_ = value;
 }

public const int paoshangStateFieldNumber = 31;
 private bool hasPaoshangState;
 private Int32 paoshangState_ = 0;
 public bool HasPaoshangState {
 get { return hasPaoshangState; }
 }
 public Int32 PaoshangState {
 get { return paoshangState_; }
 set { SetPaoshangState(value); }
 }
 public void SetPaoshangState(Int32 value) { 
 hasPaoshangState = true;
 paoshangState_ = value;
 }

public const int lightSkillLevelFieldNumber = 32;
 private bool hasLightSkillLevel;
 private Int32 lightSkillLevel_ = 0;
 public bool HasLightSkillLevel {
 get { return hasLightSkillLevel; }
 }
 public Int32 LightSkillLevel {
 get { return lightSkillLevel_; }
 set { SetLightSkillLevel(value); }
 }
 public void SetLightSkillLevel(Int32 value) { 
 hasLightSkillLevel = true;
 lightSkillLevel_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasServerId) {
size += pb::CodedOutputStream.ComputeInt32Size(1, ServerId);
}
 if (HasGuid) {
size += pb::CodedOutputStream.ComputeUInt64Size(2, Guid);
}
 if (HasSceneInst) {
size += pb::CodedOutputStream.ComputeInt32Size(3, SceneInst);
}
 if (HasSceneClass) {
size += pb::CodedOutputStream.ComputeInt32Size(4, SceneClass);
}
 if (HasDataId) {
size += pb::CodedOutputStream.ComputeInt32Size(5, DataId);
}
 if (HasPosX) {
size += pb::CodedOutputStream.ComputeInt32Size(6, PosX);
}
 if (HasPosZ) {
size += pb::CodedOutputStream.ComputeInt32Size(7, PosZ);
}
 if (HasCurforce) {
size += pb::CodedOutputStream.ComputeInt32Size(8, Curforce);
}
 if (HasName) {
size += pb::CodedOutputStream.ComputeStringSize(9, Name);
}
 if (HasCurProfession) {
size += pb::CodedOutputStream.ComputeInt32Size(10, CurProfession);
}
 if (HasFacedir) {
size += pb::CodedOutputStream.ComputeInt32Size(11, Facedir);
}
 if (HasTitlename) {
size += pb::CodedOutputStream.ComputeStringSize(12, Titlename);
}
 if (HasIsInPkList) {
size += pb::CodedOutputStream.ComputeInt32Size(13, IsInPkList);
}
 if (HasIsDie) {
size += pb::CodedOutputStream.ComputeInt32Size(14, IsDie);
}
 if (HasReliveTime) {
size += pb::CodedOutputStream.ComputeInt32Size(15, ReliveTime);
}
 if (HasPKModle) {
size += pb::CodedOutputStream.ComputeInt32Size(16, PKModle);
}
 if (HasMountID) {
size += pb::CodedOutputStream.ComputeInt32Size(17, MountID);
}
 if (HasMoveSpeed) {
size += pb::CodedOutputStream.ComputeInt32Size(18, MoveSpeed);
}
 if (HasModelVisualID) {
size += pb::CodedOutputStream.ComputeInt32Size(19, ModelVisualID);
}
 if (HasWeaponDataID) {
size += pb::CodedOutputStream.ComputeInt32Size(20, WeaponDataID);
}
 if (HasWeaponEffectGem) {
size += pb::CodedOutputStream.ComputeInt32Size(22, WeaponEffectGem);
}
 if (HasCurTitleID) {
size += pb::CodedOutputStream.ComputeInt32Size(23, CurTitleID);
}
 if (HasStealthLev) {
size += pb::CodedOutputStream.ComputeInt32Size(24, StealthLev);
}
 if (HasVipCost) {
size += pb::CodedOutputStream.ComputeInt32Size(25, VipCost);
}
 if (HasGuildGuid) {
size += pb::CodedOutputStream.ComputeUInt64Size(26, GuildGuid);
}
 if (HasCombatValue) {
size += pb::CodedOutputStream.ComputeInt32Size(27, CombatValue);
}
 if (HasBindparent) {
size += pb::CodedOutputStream.ComputeInt32Size(28, Bindparent);
}
{
int dataSize = 0;
for(int i=0; i<bindchildrenList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(bindchildrenList[i]);
}
size += dataSize;
size += 1 * bindchildren_.Count;
}
 if (HasIsEnemy2Self) {
size += pb::CodedOutputStream.ComputeInt32Size(30, IsEnemy2Self);
}
 if (HasPaoshangState) {
size += pb::CodedOutputStream.ComputeInt32Size(31, PaoshangState);
}
 if (HasLightSkillLevel) {
size += pb::CodedOutputStream.ComputeInt32Size(32, LightSkillLevel);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasServerId) {
output.WriteInt32(1, ServerId);
}
 
if (HasGuid) {
output.WriteUInt64(2, Guid);
}
 
if (HasSceneInst) {
output.WriteInt32(3, SceneInst);
}
 
if (HasSceneClass) {
output.WriteInt32(4, SceneClass);
}
 
if (HasDataId) {
output.WriteInt32(5, DataId);
}
 
if (HasPosX) {
output.WriteInt32(6, PosX);
}
 
if (HasPosZ) {
output.WriteInt32(7, PosZ);
}
 
if (HasCurforce) {
output.WriteInt32(8, Curforce);
}
 
if (HasName) {
output.WriteString(9, Name);
}
 
if (HasCurProfession) {
output.WriteInt32(10, CurProfession);
}
 
if (HasFacedir) {
output.WriteInt32(11, Facedir);
}
 
if (HasTitlename) {
output.WriteString(12, Titlename);
}
 
if (HasIsInPkList) {
output.WriteInt32(13, IsInPkList);
}
 
if (HasIsDie) {
output.WriteInt32(14, IsDie);
}
 
if (HasReliveTime) {
output.WriteInt32(15, ReliveTime);
}
 
if (HasPKModle) {
output.WriteInt32(16, PKModle);
}
 
if (HasMountID) {
output.WriteInt32(17, MountID);
}
 
if (HasMoveSpeed) {
output.WriteInt32(18, MoveSpeed);
}
 
if (HasModelVisualID) {
output.WriteInt32(19, ModelVisualID);
}
 
if (HasWeaponDataID) {
output.WriteInt32(20, WeaponDataID);
}
 
if (HasWeaponEffectGem) {
output.WriteInt32(22, WeaponEffectGem);
}
 
if (HasCurTitleID) {
output.WriteInt32(23, CurTitleID);
}
 
if (HasStealthLev) {
output.WriteInt32(24, StealthLev);
}
 
if (HasVipCost) {
output.WriteInt32(25, VipCost);
}
 
if (HasGuildGuid) {
output.WriteUInt64(26, GuildGuid);
}
 
if (HasCombatValue) {
output.WriteInt32(27, CombatValue);
}
 
if (HasBindparent) {
output.WriteInt32(28, Bindparent);
}
{
if (bindchildren_.Count > 0) {
for(int i=0; i<bindchildren_.Count; ++i){
output.WriteInt32(29,bindchildren_[i]);
}
}

}
 
if (HasIsEnemy2Self) {
output.WriteInt32(30, IsEnemy2Self);
}
 
if (HasPaoshangState) {
output.WriteInt32(31, PaoshangState);
}
 
if (HasLightSkillLevel) {
output.WriteInt32(32, LightSkillLevel);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_CREATE_PLAYER _inst = (GC_CREATE_PLAYER) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.ServerId = input.ReadInt32();
break;
}
   case  16: {
 _inst.Guid = input.ReadUInt64();
break;
}
   case  24: {
 _inst.SceneInst = input.ReadInt32();
break;
}
   case  32: {
 _inst.SceneClass = input.ReadInt32();
break;
}
   case  40: {
 _inst.DataId = input.ReadInt32();
break;
}
   case  48: {
 _inst.PosX = input.ReadInt32();
break;
}
   case  56: {
 _inst.PosZ = input.ReadInt32();
break;
}
   case  64: {
 _inst.Curforce = input.ReadInt32();
break;
}
   case  74: {
 _inst.Name = input.ReadString();
break;
}
   case  80: {
 _inst.CurProfession = input.ReadInt32();
break;
}
   case  88: {
 _inst.Facedir = input.ReadInt32();
break;
}
   case  98: {
 _inst.Titlename = input.ReadString();
break;
}
   case  104: {
 _inst.IsInPkList = input.ReadInt32();
break;
}
   case  112: {
 _inst.IsDie = input.ReadInt32();
break;
}
   case  120: {
 _inst.ReliveTime = input.ReadInt32();
break;
}
   case  128: {
 _inst.PKModle = input.ReadInt32();
break;
}
   case  136: {
 _inst.MountID = input.ReadInt32();
break;
}
   case  144: {
 _inst.MoveSpeed = input.ReadInt32();
break;
}
   case  152: {
 _inst.ModelVisualID = input.ReadInt32();
break;
}
   case  160: {
 _inst.WeaponDataID = input.ReadInt32();
break;
}
   case  176: {
 _inst.WeaponEffectGem = input.ReadInt32();
break;
}
   case  184: {
 _inst.CurTitleID = input.ReadInt32();
break;
}
   case  192: {
 _inst.StealthLev = input.ReadInt32();
break;
}
   case  200: {
 _inst.VipCost = input.ReadInt32();
break;
}
   case  208: {
 _inst.GuildGuid = input.ReadUInt64();
break;
}
   case  216: {
 _inst.CombatValue = input.ReadInt32();
break;
}
   case  224: {
 _inst.Bindparent = input.ReadInt32();
break;
}
   case  232: {
 _inst.AddBindchildren(input.ReadInt32());
break;
}
   case  240: {
 _inst.IsEnemy2Self = input.ReadInt32();
break;
}
   case  248: {
 _inst.PaoshangState = input.ReadInt32();
break;
}
   case  256: {
 _inst.LightSkillLevel = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasServerId) return false;
 if (!hasGuid) return false;
 if (!hasSceneInst) return false;
 if (!hasSceneClass) return false;
 if (!hasDataId) return false;
 if (!hasPosX) return false;
 if (!hasPosZ) return false;
 if (!hasCurforce) return false;
 if (!hasName) return false;
 if (!hasCurProfession) return false;
 if (!hasFacedir) return false;
 if (!hasTitlename) return false;
 if (!hasIsInPkList) return false;
 if (!hasIsDie) return false;
 if (!hasPKModle) return false;
 if (!hasMountID) return false;
 if (!hasMoveSpeed) return false;
 if (!hasModelVisualID) return false;
 if (!hasWeaponDataID) return false;
 if (!hasWeaponEffectGem) return false;
 if (!hasCurTitleID) return false;
 if (!hasStealthLev) return false;
 if (!hasVipCost) return false;
 if (!hasGuildGuid) return false;
 if (!hasCombatValue) return false;
 if (!hasBindparent) return false;
 if (!hasIsEnemy2Self) return false;
 return true;
 }

}


[Serializable]
public class GC_DELETE_OBJ : PacketDistributed
{

public const int serverIdFieldNumber = 1;
 private bool hasServerId;
 private Int32 serverId_ = 0;
 public bool HasServerId {
 get { return hasServerId; }
 }
 public Int32 ServerId {
 get { return serverId_; }
 set { SetServerId(value); }
 }
 public void SetServerId(Int32 value) { 
 hasServerId = true;
 serverId_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasServerId) {
size += pb::CodedOutputStream.ComputeInt32Size(1, ServerId);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasServerId) {
output.WriteInt32(1, ServerId);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_DELETE_OBJ _inst = (GC_DELETE_OBJ) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.ServerId = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasServerId) return false;
 return true;
 }

}


[Serializable]
public class CG_SYNC_POS : PacketDistributed
{

public const int posXFieldNumber = 1;
 private bool hasPosX;
 private Int32 posX_ = 0;
 public bool HasPosX {
 get { return hasPosX; }
 }
 public Int32 PosX {
 get { return posX_; }
 set { SetPosX(value); }
 }
 public void SetPosX(Int32 value) { 
 hasPosX = true;
 posX_ = value;
 }

public const int posZFieldNumber = 2;
 private bool hasPosZ;
 private Int32 posZ_ = 0;
 public bool HasPosZ {
 get { return hasPosZ; }
 }
 public Int32 PosZ {
 get { return posZ_; }
 set { SetPosZ(value); }
 }
 public void SetPosZ(Int32 value) { 
 hasPosZ = true;
 posZ_ = value;
 }

public const int ismoviongFieldNumber = 3;
 private bool hasIsmoviong;
 private Int32 ismoviong_ = 0;
 public bool HasIsmoviong {
 get { return hasIsmoviong; }
 }
 public Int32 Ismoviong {
 get { return ismoviong_; }
 set { SetIsmoviong(value); }
 }
 public void SetIsmoviong(Int32 value) { 
 hasIsmoviong = true;
 ismoviong_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasPosX) {
size += pb::CodedOutputStream.ComputeInt32Size(1, PosX);
}
 if (HasPosZ) {
size += pb::CodedOutputStream.ComputeInt32Size(2, PosZ);
}
 if (HasIsmoviong) {
size += pb::CodedOutputStream.ComputeInt32Size(3, Ismoviong);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasPosX) {
output.WriteInt32(1, PosX);
}
 
if (HasPosZ) {
output.WriteInt32(2, PosZ);
}
 
if (HasIsmoviong) {
output.WriteInt32(3, Ismoviong);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_SYNC_POS _inst = (CG_SYNC_POS) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.PosX = input.ReadInt32();
break;
}
   case  16: {
 _inst.PosZ = input.ReadInt32();
break;
}
   case  24: {
 _inst.Ismoviong = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasPosX) return false;
 if (!hasPosZ) return false;
 if (!hasIsmoviong) return false;
 return true;
 }

}


[Serializable]
public class GC_SYNC_POS : PacketDistributed
{

public const int serverIdFieldNumber = 1;
 private bool hasServerId;
 private Int32 serverId_ = 0;
 public bool HasServerId {
 get { return hasServerId; }
 }
 public Int32 ServerId {
 get { return serverId_; }
 set { SetServerId(value); }
 }
 public void SetServerId(Int32 value) { 
 hasServerId = true;
 serverId_ = value;
 }

public const int posXFieldNumber = 2;
 private bool hasPosX;
 private Int32 posX_ = 0;
 public bool HasPosX {
 get { return hasPosX; }
 }
 public Int32 PosX {
 get { return posX_; }
 set { SetPosX(value); }
 }
 public void SetPosX(Int32 value) { 
 hasPosX = true;
 posX_ = value;
 }

public const int posZFieldNumber = 3;
 private bool hasPosZ;
 private Int32 posZ_ = 0;
 public bool HasPosZ {
 get { return hasPosZ; }
 }
 public Int32 PosZ {
 get { return posZ_; }
 set { SetPosZ(value); }
 }
 public void SetPosZ(Int32 value) { 
 hasPosZ = true;
 posZ_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasServerId) {
size += pb::CodedOutputStream.ComputeInt32Size(1, ServerId);
}
 if (HasPosX) {
size += pb::CodedOutputStream.ComputeInt32Size(2, PosX);
}
 if (HasPosZ) {
size += pb::CodedOutputStream.ComputeInt32Size(3, PosZ);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasServerId) {
output.WriteInt32(1, ServerId);
}
 
if (HasPosX) {
output.WriteInt32(2, PosX);
}
 
if (HasPosZ) {
output.WriteInt32(3, PosZ);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_SYNC_POS _inst = (GC_SYNC_POS) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.ServerId = input.ReadInt32();
break;
}
   case  16: {
 _inst.PosX = input.ReadInt32();
break;
}
   case  24: {
 _inst.PosZ = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasServerId) return false;
 if (!hasPosX) return false;
 if (!hasPosZ) return false;
 return true;
 }

}


[Serializable]
public class CG_MOVE : PacketDistributed
{

public const int poscountFieldNumber = 1;
 private bool hasPoscount;
 private Int32 poscount_ = 0;
 public bool HasPoscount {
 get { return hasPoscount; }
 }
 public Int32 Poscount {
 get { return poscount_; }
 set { SetPoscount(value); }
 }
 public void SetPoscount(Int32 value) { 
 hasPoscount = true;
 poscount_ = value;
 }

public const int posxFieldNumber = 2;
 private pbc::PopsicleList<Int32> posx_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> posxList {
 get { return pbc::Lists.AsReadOnly(posx_); }
 }
 
 public int posxCount {
 get { return posx_.Count; }
 }
 
public Int32 GetPosx(int index) {
 return posx_[index];
 }
 public void AddPosx(Int32 value) {
 posx_.Add(value);
 }

public const int poszFieldNumber = 3;
 private pbc::PopsicleList<Int32> posz_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> poszList {
 get { return pbc::Lists.AsReadOnly(posz_); }
 }
 
 public int poszCount {
 get { return posz_.Count; }
 }
 
public Int32 GetPosz(int index) {
 return posz_[index];
 }
 public void AddPosz(Int32 value) {
 posz_.Add(value);
 }

public const int ismovingFieldNumber = 4;
 private bool hasIsmoving;
 private Int32 ismoving_ = 0;
 public bool HasIsmoving {
 get { return hasIsmoving; }
 }
 public Int32 Ismoving {
 get { return ismoving_; }
 set { SetIsmoving(value); }
 }
 public void SetIsmoving(Int32 value) { 
 hasIsmoving = true;
 ismoving_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasPoscount) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Poscount);
}
{
int dataSize = 0;
for(int i=0; i<posxList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(posxList[i]);
}
size += dataSize;
size += 1 * posx_.Count;
}
{
int dataSize = 0;
for(int i=0; i<poszList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(poszList[i]);
}
size += dataSize;
size += 1 * posz_.Count;
}
 if (HasIsmoving) {
size += pb::CodedOutputStream.ComputeInt32Size(4, Ismoving);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasPoscount) {
output.WriteInt32(1, Poscount);
}
{
if (posx_.Count > 0) {
for(int i=0; i<posx_.Count; ++i){
output.WriteInt32(2,posx_[i]);
}
}

}
{
if (posz_.Count > 0) {
for(int i=0; i<posz_.Count; ++i){
output.WriteInt32(3,posz_[i]);
}
}

}
 
if (HasIsmoving) {
output.WriteInt32(4, Ismoving);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_MOVE _inst = (CG_MOVE) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Poscount = input.ReadInt32();
break;
}
   case  16: {
 _inst.AddPosx(input.ReadInt32());
break;
}
   case  24: {
 _inst.AddPosz(input.ReadInt32());
break;
}
   case  32: {
 _inst.Ismoving = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasPoscount) return false;
 if (!hasIsmoving) return false;
 return true;
 }

}


[Serializable]
public class GC_MOVE : PacketDistributed
{

public const int serveridFieldNumber = 1;
 private bool hasServerid;
 private Int32 serverid_ = 0;
 public bool HasServerid {
 get { return hasServerid; }
 }
 public Int32 Serverid {
 get { return serverid_; }
 set { SetServerid(value); }
 }
 public void SetServerid(Int32 value) { 
 hasServerid = true;
 serverid_ = value;
 }

public const int poscountFieldNumber = 2;
 private bool hasPoscount;
 private Int32 poscount_ = 0;
 public bool HasPoscount {
 get { return hasPoscount; }
 }
 public Int32 Poscount {
 get { return poscount_; }
 set { SetPoscount(value); }
 }
 public void SetPoscount(Int32 value) { 
 hasPoscount = true;
 poscount_ = value;
 }

public const int posserialFieldNumber = 3;
 private pbc::PopsicleList<Int32> posserial_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> posserialList {
 get { return pbc::Lists.AsReadOnly(posserial_); }
 }
 
 public int posserialCount {
 get { return posserial_.Count; }
 }
 
public Int32 GetPosserial(int index) {
 return posserial_[index];
 }
 public void AddPosserial(Int32 value) {
 posserial_.Add(value);
 }

public const int posxFieldNumber = 4;
 private pbc::PopsicleList<Int32> posx_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> posxList {
 get { return pbc::Lists.AsReadOnly(posx_); }
 }
 
 public int posxCount {
 get { return posx_.Count; }
 }
 
public Int32 GetPosx(int index) {
 return posx_[index];
 }
 public void AddPosx(Int32 value) {
 posx_.Add(value);
 }

public const int poszFieldNumber = 5;
 private pbc::PopsicleList<Int32> posz_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> poszList {
 get { return pbc::Lists.AsReadOnly(posz_); }
 }
 
 public int poszCount {
 get { return posz_.Count; }
 }
 
public Int32 GetPosz(int index) {
 return posz_[index];
 }
 public void AddPosz(Int32 value) {
 posz_.Add(value);
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasServerid) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Serverid);
}
 if (HasPoscount) {
size += pb::CodedOutputStream.ComputeInt32Size(2, Poscount);
}
{
int dataSize = 0;
for(int i=0; i<posserialList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(posserialList[i]);
}
size += dataSize;
size += 1 * posserial_.Count;
}
{
int dataSize = 0;
for(int i=0; i<posxList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(posxList[i]);
}
size += dataSize;
size += 1 * posx_.Count;
}
{
int dataSize = 0;
for(int i=0; i<poszList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(poszList[i]);
}
size += dataSize;
size += 1 * posz_.Count;
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasServerid) {
output.WriteInt32(1, Serverid);
}
 
if (HasPoscount) {
output.WriteInt32(2, Poscount);
}
{
if (posserial_.Count > 0) {
for(int i=0; i<posserial_.Count; ++i){
output.WriteInt32(3,posserial_[i]);
}
}

}
{
if (posx_.Count > 0) {
for(int i=0; i<posx_.Count; ++i){
output.WriteInt32(4,posx_[i]);
}
}

}
{
if (posz_.Count > 0) {
for(int i=0; i<posz_.Count; ++i){
output.WriteInt32(5,posz_[i]);
}
}

}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_MOVE _inst = (GC_MOVE) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Serverid = input.ReadInt32();
break;
}
   case  16: {
 _inst.Poscount = input.ReadInt32();
break;
}
   case  24: {
 _inst.AddPosserial(input.ReadInt32());
break;
}
   case  32: {
 _inst.AddPosx(input.ReadInt32());
break;
}
   case  40: {
 _inst.AddPosz(input.ReadInt32());
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasServerid) return false;
 if (!hasPoscount) return false;
 return true;
 }

}


[Serializable]
public class GC_STOP : PacketDistributed
{

public const int serveridFieldNumber = 1;
 private bool hasServerid;
 private Int32 serverid_ = 0;
 public bool HasServerid {
 get { return hasServerid; }
 }
 public Int32 Serverid {
 get { return serverid_; }
 set { SetServerid(value); }
 }
 public void SetServerid(Int32 value) { 
 hasServerid = true;
 serverid_ = value;
 }

public const int posserialFieldNumber = 2;
 private bool hasPosserial;
 private Int32 posserial_ = 0;
 public bool HasPosserial {
 get { return hasPosserial; }
 }
 public Int32 Posserial {
 get { return posserial_; }
 set { SetPosserial(value); }
 }
 public void SetPosserial(Int32 value) { 
 hasPosserial = true;
 posserial_ = value;
 }

public const int posxFieldNumber = 3;
 private bool hasPosx;
 private Int32 posx_ = 0;
 public bool HasPosx {
 get { return hasPosx; }
 }
 public Int32 Posx {
 get { return posx_; }
 set { SetPosx(value); }
 }
 public void SetPosx(Int32 value) { 
 hasPosx = true;
 posx_ = value;
 }

public const int poszFieldNumber = 4;
 private bool hasPosz;
 private Int32 posz_ = 0;
 public bool HasPosz {
 get { return hasPosz; }
 }
 public Int32 Posz {
 get { return posz_; }
 set { SetPosz(value); }
 }
 public void SetPosz(Int32 value) { 
 hasPosz = true;
 posz_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasServerid) {
size += pb::CodedOutputStream.ComputeInt32Size(1, Serverid);
}
 if (HasPosserial) {
size += pb::CodedOutputStream.ComputeInt32Size(2, Posserial);
}
 if (HasPosx) {
size += pb::CodedOutputStream.ComputeInt32Size(3, Posx);
}
 if (HasPosz) {
size += pb::CodedOutputStream.ComputeInt32Size(4, Posz);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasServerid) {
output.WriteInt32(1, Serverid);
}
 
if (HasPosserial) {
output.WriteInt32(2, Posserial);
}
 
if (HasPosx) {
output.WriteInt32(3, Posx);
}
 
if (HasPosz) {
output.WriteInt32(4, Posz);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_STOP _inst = (GC_STOP) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.Serverid = input.ReadInt32();
break;
}
   case  16: {
 _inst.Posserial = input.ReadInt32();
break;
}
   case  24: {
 _inst.Posx = input.ReadInt32();
break;
}
   case  32: {
 _inst.Posz = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasServerid) return false;
 if (!hasPosserial) return false;
 if (!hasPosx) return false;
 if (!hasPosz) return false;
 return true;
 }

}


[Serializable]
public class GC_BROADCAST_ATTR : PacketDistributed
{

public const int ObjIdFieldNumber = 1;
 private bool hasObjId;
 private Int32 ObjId_ = 0;
 public bool HasObjId {
 get { return hasObjId; }
 }
 public Int32 ObjId {
 get { return ObjId_; }
 set { SetObjId(value); }
 }
 public void SetObjId(Int32 value) { 
 hasObjId = true;
 ObjId_ = value;
 }

public const int CurProfessionFieldNumber = 2;
 private bool hasCurProfession;
 private Int32 CurProfession_ = 0;
 public bool HasCurProfession {
 get { return hasCurProfession; }
 }
 public Int32 CurProfession {
 get { return CurProfession_; }
 set { SetCurProfession(value); }
 }
 public void SetCurProfession(Int32 value) { 
 hasCurProfession = true;
 CurProfession_ = value;
 }

public const int NameFieldNumber = 3;
 private bool hasName;
 private string Name_ = "";
 public bool HasName {
 get { return hasName; }
 }
 public string Name {
 get { return Name_; }
 set { SetName(value); }
 }
 public void SetName(string value) { 
 hasName = true;
 Name_ = value;
 }

public const int CurForceFieldNumber = 4;
 private bool hasCurForce;
 private Int32 CurForce_ = 0;
 public bool HasCurForce {
 get { return hasCurForce; }
 }
 public Int32 CurForce {
 get { return CurForce_; }
 set { SetCurForce(value); }
 }
 public void SetCurForce(Int32 value) { 
 hasCurForce = true;
 CurForce_ = value;
 }

public const int MoveSpeedFieldNumber = 5;
 private bool hasMoveSpeed;
 private Int32 MoveSpeed_ = 0;
 public bool HasMoveSpeed {
 get { return hasMoveSpeed; }
 }
 public Int32 MoveSpeed {
 get { return MoveSpeed_; }
 set { SetMoveSpeed(value); }
 }
 public void SetMoveSpeed(Int32 value) { 
 hasMoveSpeed = true;
 MoveSpeed_ = value;
 }

public const int bDieFieldNumber = 6;
 private bool hasBDie;
 private Int32 bDie_ = 0;
 public bool HasBDie {
 get { return hasBDie; }
 }
 public Int32 BDie {
 get { return bDie_; }
 set { SetBDie(value); }
 }
 public void SetBDie(Int32 value) { 
 hasBDie = true;
 bDie_ = value;
 }

public const int faceDirFieldNumber = 7;
 private bool hasFaceDir;
 private Int32 faceDir_ = 0;
 public bool HasFaceDir {
 get { return hasFaceDir; }
 }
 public Int32 FaceDir {
 get { return faceDir_; }
 set { SetFaceDir(value); }
 }
 public void SetFaceDir(Int32 value) { 
 hasFaceDir = true;
 faceDir_ = value;
 }

public const int ModelVisualIDFieldNumber = 8;
 private bool hasModelVisualID;
 private Int32 ModelVisualID_ = 0;
 public bool HasModelVisualID {
 get { return hasModelVisualID; }
 }
 public Int32 ModelVisualID {
 get { return ModelVisualID_; }
 set { SetModelVisualID(value); }
 }
 public void SetModelVisualID(Int32 value) { 
 hasModelVisualID = true;
 ModelVisualID_ = value;
 }

public const int WeaponDataIDFieldNumber = 9;
 private bool hasWeaponDataID;
 private Int32 WeaponDataID_ = 0;
 public bool HasWeaponDataID {
 get { return hasWeaponDataID; }
 }
 public Int32 WeaponDataID {
 get { return WeaponDataID_; }
 set { SetWeaponDataID(value); }
 }
 public void SetWeaponDataID(Int32 value) { 
 hasWeaponDataID = true;
 WeaponDataID_ = value;
 }

public const int WeaponEffectGemFieldNumber = 11;
 private bool hasWeaponEffectGem;
 private Int32 WeaponEffectGem_ = 0;
 public bool HasWeaponEffectGem {
 get { return hasWeaponEffectGem; }
 }
 public Int32 WeaponEffectGem {
 get { return WeaponEffectGem_; }
 set { SetWeaponEffectGem(value); }
 }
 public void SetWeaponEffectGem(Int32 value) { 
 hasWeaponEffectGem = true;
 WeaponEffectGem_ = value;
 }

public const int StealthLevFieldNumber = 12;
 private bool hasStealthLev;
 private Int32 StealthLev_ = 0;
 public bool HasStealthLev {
 get { return hasStealthLev; }
 }
 public Int32 StealthLev {
 get { return StealthLev_; }
 set { SetStealthLev(value); }
 }
 public void SetStealthLev(Int32 value) { 
 hasStealthLev = true;
 StealthLev_ = value;
 }

public const int VipCostFieldNumber = 13;
 private bool hasVipCost;
 private Int32 VipCost_ = 0;
 public bool HasVipCost {
 get { return hasVipCost; }
 }
 public Int32 VipCost {
 get { return VipCost_; }
 set { SetVipCost(value); }
 }
 public void SetVipCost(Int32 value) { 
 hasVipCost = true;
 VipCost_ = value;
 }

public const int CombatValueFieldNumber = 14;
 private bool hasCombatValue;
 private Int32 CombatValue_ = 0;
 public bool HasCombatValue {
 get { return hasCombatValue; }
 }
 public Int32 CombatValue {
 get { return CombatValue_; }
 set { SetCombatValue(value); }
 }
 public void SetCombatValue(Int32 value) { 
 hasCombatValue = true;
 CombatValue_ = value;
 }

public const int bindparentFieldNumber = 15;
 private bool hasBindparent;
 private Int32 bindparent_ = 0;
 public bool HasBindparent {
 get { return hasBindparent; }
 }
 public Int32 Bindparent {
 get { return bindparent_; }
 set { SetBindparent(value); }
 }
 public void SetBindparent(Int32 value) { 
 hasBindparent = true;
 bindparent_ = value;
 }

public const int bindchildrenFieldNumber = 16;
 private pbc::PopsicleList<Int32> bindchildren_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> bindchildrenList {
 get { return pbc::Lists.AsReadOnly(bindchildren_); }
 }
 
 public int bindchildrenCount {
 get { return bindchildren_.Count; }
 }
 
public Int32 GetBindchildren(int index) {
 return bindchildren_[index];
 }
 public void AddBindchildren(Int32 value) {
 bindchildren_.Add(value);
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasObjId) {
size += pb::CodedOutputStream.ComputeInt32Size(1, ObjId);
}
 if (HasCurProfession) {
size += pb::CodedOutputStream.ComputeInt32Size(2, CurProfession);
}
 if (HasName) {
size += pb::CodedOutputStream.ComputeStringSize(3, Name);
}
 if (HasCurForce) {
size += pb::CodedOutputStream.ComputeInt32Size(4, CurForce);
}
 if (HasMoveSpeed) {
size += pb::CodedOutputStream.ComputeInt32Size(5, MoveSpeed);
}
 if (HasBDie) {
size += pb::CodedOutputStream.ComputeInt32Size(6, BDie);
}
 if (HasFaceDir) {
size += pb::CodedOutputStream.ComputeInt32Size(7, FaceDir);
}
 if (HasModelVisualID) {
size += pb::CodedOutputStream.ComputeInt32Size(8, ModelVisualID);
}
 if (HasWeaponDataID) {
size += pb::CodedOutputStream.ComputeInt32Size(9, WeaponDataID);
}
 if (HasWeaponEffectGem) {
size += pb::CodedOutputStream.ComputeInt32Size(11, WeaponEffectGem);
}
 if (HasStealthLev) {
size += pb::CodedOutputStream.ComputeInt32Size(12, StealthLev);
}
 if (HasVipCost) {
size += pb::CodedOutputStream.ComputeInt32Size(13, VipCost);
}
 if (HasCombatValue) {
size += pb::CodedOutputStream.ComputeInt32Size(14, CombatValue);
}
 if (HasBindparent) {
size += pb::CodedOutputStream.ComputeInt32Size(15, Bindparent);
}
{
int dataSize = 0;
for(int i=0; i<bindchildrenList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(bindchildrenList[i]);
}
size += dataSize;
size += 1 * bindchildren_.Count;
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasObjId) {
output.WriteInt32(1, ObjId);
}
 
if (HasCurProfession) {
output.WriteInt32(2, CurProfession);
}
 
if (HasName) {
output.WriteString(3, Name);
}
 
if (HasCurForce) {
output.WriteInt32(4, CurForce);
}
 
if (HasMoveSpeed) {
output.WriteInt32(5, MoveSpeed);
}
 
if (HasBDie) {
output.WriteInt32(6, BDie);
}
 
if (HasFaceDir) {
output.WriteInt32(7, FaceDir);
}
 
if (HasModelVisualID) {
output.WriteInt32(8, ModelVisualID);
}
 
if (HasWeaponDataID) {
output.WriteInt32(9, WeaponDataID);
}
 
if (HasWeaponEffectGem) {
output.WriteInt32(11, WeaponEffectGem);
}
 
if (HasStealthLev) {
output.WriteInt32(12, StealthLev);
}
 
if (HasVipCost) {
output.WriteInt32(13, VipCost);
}
 
if (HasCombatValue) {
output.WriteInt32(14, CombatValue);
}
 
if (HasBindparent) {
output.WriteInt32(15, Bindparent);
}
{
if (bindchildren_.Count > 0) {
for(int i=0; i<bindchildren_.Count; ++i){
output.WriteInt32(16,bindchildren_[i]);
}
}

}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_BROADCAST_ATTR _inst = (GC_BROADCAST_ATTR) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.ObjId = input.ReadInt32();
break;
}
   case  16: {
 _inst.CurProfession = input.ReadInt32();
break;
}
   case  26: {
 _inst.Name = input.ReadString();
break;
}
   case  32: {
 _inst.CurForce = input.ReadInt32();
break;
}
   case  40: {
 _inst.MoveSpeed = input.ReadInt32();
break;
}
   case  48: {
 _inst.BDie = input.ReadInt32();
break;
}
   case  56: {
 _inst.FaceDir = input.ReadInt32();
break;
}
   case  64: {
 _inst.ModelVisualID = input.ReadInt32();
break;
}
   case  72: {
 _inst.WeaponDataID = input.ReadInt32();
break;
}
   case  88: {
 _inst.WeaponEffectGem = input.ReadInt32();
break;
}
   case  96: {
 _inst.StealthLev = input.ReadInt32();
break;
}
   case  104: {
 _inst.VipCost = input.ReadInt32();
break;
}
   case  112: {
 _inst.CombatValue = input.ReadInt32();
break;
}
   case  120: {
 _inst.Bindparent = input.ReadInt32();
break;
}
   case  128: {
 _inst.AddBindchildren(input.ReadInt32());
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasObjId) return false;
 return true;
 }

}


[Serializable]
public class GC_SYN_ATTR : PacketDistributed
{

public const int ObjIdFieldNumber = 1;
 private bool hasObjId;
 private Int32 ObjId_ = 0;
 public bool HasObjId {
 get { return hasObjId; }
 }
 public Int32 ObjId {
 get { return ObjId_; }
 set { SetObjId(value); }
 }
 public void SetObjId(Int32 value) { 
 hasObjId = true;
 ObjId_ = value;
 }

public const int CurHpFieldNumber = 2;
 private bool hasCurHp;
 private Int32 CurHp_ = 0;
 public bool HasCurHp {
 get { return hasCurHp; }
 }
 public Int32 CurHp {
 get { return CurHp_; }
 set { SetCurHp(value); }
 }
 public void SetCurHp(Int32 value) { 
 hasCurHp = true;
 CurHp_ = value;
 }

public const int CurMpFieldNumber = 3;
 private bool hasCurMp;
 private Int32 CurMp_ = 0;
 public bool HasCurMp {
 get { return hasCurMp; }
 }
 public Int32 CurMp {
 get { return CurMp_; }
 set { SetCurMp(value); }
 }
 public void SetCurMp(Int32 value) { 
 hasCurMp = true;
 CurMp_ = value;
 }

public const int CurXpFieldNumber = 4;
 private bool hasCurXp;
 private Int32 CurXp_ = 0;
 public bool HasCurXp {
 get { return hasCurXp; }
 }
 public Int32 CurXp {
 get { return CurXp_; }
 set { SetCurXp(value); }
 }
 public void SetCurXp(Int32 value) { 
 hasCurXp = true;
 CurXp_ = value;
 }

public const int MaxHPFieldNumber = 5;
 private bool hasMaxHP;
 private Int32 MaxHP_ = 0;
 public bool HasMaxHP {
 get { return hasMaxHP; }
 }
 public Int32 MaxHP {
 get { return MaxHP_; }
 set { SetMaxHP(value); }
 }
 public void SetMaxHP(Int32 value) { 
 hasMaxHP = true;
 MaxHP_ = value;
 }

public const int MaxMPFieldNumber = 6;
 private bool hasMaxMP;
 private Int32 MaxMP_ = 0;
 public bool HasMaxMP {
 get { return hasMaxMP; }
 }
 public Int32 MaxMP {
 get { return MaxMP_; }
 set { SetMaxMP(value); }
 }
 public void SetMaxMP(Int32 value) { 
 hasMaxMP = true;
 MaxMP_ = value;
 }

public const int MaxXPFieldNumber = 7;
 private bool hasMaxXP;
 private Int32 MaxXP_ = 0;
 public bool HasMaxXP {
 get { return hasMaxXP; }
 }
 public Int32 MaxXP {
 get { return MaxXP_; }
 set { SetMaxXP(value); }
 }
 public void SetMaxXP(Int32 value) { 
 hasMaxXP = true;
 MaxXP_ = value;
 }

public const int CurLevFieldNumber = 8;
 private bool hasCurLev;
 private Int32 CurLev_ = 0;
 public bool HasCurLev {
 get { return hasCurLev; }
 }
 public Int32 CurLev {
 get { return CurLev_; }
 set { SetCurLev(value); }
 }
 public void SetCurLev(Int32 value) { 
 hasCurLev = true;
 CurLev_ = value;
 }

public const int CurExpFieldNumber = 9;
 private bool hasCurExp;
 private Int32 CurExp_ = 0;
 public bool HasCurExp {
 get { return hasCurExp; }
 }
 public Int32 CurExp {
 get { return CurExp_; }
 set { SetCurExp(value); }
 }
 public void SetCurExp(Int32 value) { 
 hasCurExp = true;
 CurExp_ = value;
 }

public const int CurMoneyFieldNumber = 10;
 private bool hasCurMoney;
 private Int32 CurMoney_ = 0;
 public bool HasCurMoney {
 get { return hasCurMoney; }
 }
 public Int32 CurMoney {
 get { return CurMoney_; }
 set { SetCurMoney(value); }
 }
 public void SetCurMoney(Int32 value) { 
 hasCurMoney = true;
 CurMoney_ = value;
 }

public const int CurYuanBaoFieldNumber = 11;
 private bool hasCurYuanBao;
 private Int32 CurYuanBao_ = 0;
 public bool HasCurYuanBao {
 get { return hasCurYuanBao; }
 }
 public Int32 CurYuanBao {
 get { return CurYuanBao_; }
 set { SetCurYuanBao(value); }
 }
 public void SetCurYuanBao(Int32 value) { 
 hasCurYuanBao = true;
 CurYuanBao_ = value;
 }

public const int CurBDYuanBaoFieldNumber = 12;
 private bool hasCurBDYuanBao;
 private Int32 CurBDYuanBao_ = 0;
 public bool HasCurBDYuanBao {
 get { return hasCurBDYuanBao; }
 }
 public Int32 CurBDYuanBao {
 get { return CurBDYuanBao_; }
 set { SetCurBDYuanBao(value); }
 }
 public void SetCurBDYuanBao(Int32 value) { 
 hasCurBDYuanBao = true;
 CurBDYuanBao_ = value;
 }

public const int CurZhenQiFieldNumber = 13;
 private bool hasCurZhenQi;
 private Int32 CurZhenQi_ = 0;
 public bool HasCurZhenQi {
 get { return hasCurZhenQi; }
 }
 public Int32 CurZhenQi {
 get { return CurZhenQi_; }
 set { SetCurZhenQi(value); }
 }
 public void SetCurZhenQi(Int32 value) { 
 hasCurZhenQi = true;
 CurZhenQi_ = value;
 }

public const int isInCombatFieldNumber = 14;
 private bool hasIsInCombat;
 private Int32 isInCombat_ = 0;
 public bool HasIsInCombat {
 get { return hasIsInCombat; }
 }
 public Int32 IsInCombat {
 get { return isInCombat_; }
 set { SetIsInCombat(value); }
 }
 public void SetIsInCombat(Int32 value) { 
 hasIsInCombat = true;
 isInCombat_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasObjId) {
size += pb::CodedOutputStream.ComputeInt32Size(1, ObjId);
}
 if (HasCurHp) {
size += pb::CodedOutputStream.ComputeInt32Size(2, CurHp);
}
 if (HasCurMp) {
size += pb::CodedOutputStream.ComputeInt32Size(3, CurMp);
}
 if (HasCurXp) {
size += pb::CodedOutputStream.ComputeInt32Size(4, CurXp);
}
 if (HasMaxHP) {
size += pb::CodedOutputStream.ComputeInt32Size(5, MaxHP);
}
 if (HasMaxMP) {
size += pb::CodedOutputStream.ComputeInt32Size(6, MaxMP);
}
 if (HasMaxXP) {
size += pb::CodedOutputStream.ComputeInt32Size(7, MaxXP);
}
 if (HasCurLev) {
size += pb::CodedOutputStream.ComputeInt32Size(8, CurLev);
}
 if (HasCurExp) {
size += pb::CodedOutputStream.ComputeInt32Size(9, CurExp);
}
 if (HasCurMoney) {
size += pb::CodedOutputStream.ComputeInt32Size(10, CurMoney);
}
 if (HasCurYuanBao) {
size += pb::CodedOutputStream.ComputeInt32Size(11, CurYuanBao);
}
 if (HasCurBDYuanBao) {
size += pb::CodedOutputStream.ComputeInt32Size(12, CurBDYuanBao);
}
 if (HasCurZhenQi) {
size += pb::CodedOutputStream.ComputeInt32Size(13, CurZhenQi);
}
 if (HasIsInCombat) {
size += pb::CodedOutputStream.ComputeInt32Size(14, IsInCombat);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasObjId) {
output.WriteInt32(1, ObjId);
}
 
if (HasCurHp) {
output.WriteInt32(2, CurHp);
}
 
if (HasCurMp) {
output.WriteInt32(3, CurMp);
}
 
if (HasCurXp) {
output.WriteInt32(4, CurXp);
}
 
if (HasMaxHP) {
output.WriteInt32(5, MaxHP);
}
 
if (HasMaxMP) {
output.WriteInt32(6, MaxMP);
}
 
if (HasMaxXP) {
output.WriteInt32(7, MaxXP);
}
 
if (HasCurLev) {
output.WriteInt32(8, CurLev);
}
 
if (HasCurExp) {
output.WriteInt32(9, CurExp);
}
 
if (HasCurMoney) {
output.WriteInt32(10, CurMoney);
}
 
if (HasCurYuanBao) {
output.WriteInt32(11, CurYuanBao);
}
 
if (HasCurBDYuanBao) {
output.WriteInt32(12, CurBDYuanBao);
}
 
if (HasCurZhenQi) {
output.WriteInt32(13, CurZhenQi);
}
 
if (HasIsInCombat) {
output.WriteInt32(14, IsInCombat);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_SYN_ATTR _inst = (GC_SYN_ATTR) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.ObjId = input.ReadInt32();
break;
}
   case  16: {
 _inst.CurHp = input.ReadInt32();
break;
}
   case  24: {
 _inst.CurMp = input.ReadInt32();
break;
}
   case  32: {
 _inst.CurXp = input.ReadInt32();
break;
}
   case  40: {
 _inst.MaxHP = input.ReadInt32();
break;
}
   case  48: {
 _inst.MaxMP = input.ReadInt32();
break;
}
   case  56: {
 _inst.MaxXP = input.ReadInt32();
break;
}
   case  64: {
 _inst.CurLev = input.ReadInt32();
break;
}
   case  72: {
 _inst.CurExp = input.ReadInt32();
break;
}
   case  80: {
 _inst.CurMoney = input.ReadInt32();
break;
}
   case  88: {
 _inst.CurYuanBao = input.ReadInt32();
break;
}
   case  96: {
 _inst.CurBDYuanBao = input.ReadInt32();
break;
}
   case  104: {
 _inst.CurZhenQi = input.ReadInt32();
break;
}
   case  112: {
 _inst.IsInCombat = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasObjId) return false;
 return true;
 }

}


[Serializable]
public class GC_SYNC_COMMONDATA : PacketDistributed
{

public const int nIndexFieldNumber = 1;
 private pbc::PopsicleList<Int32> nIndex_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> nIndexList {
 get { return pbc::Lists.AsReadOnly(nIndex_); }
 }
 
 public int nIndexCount {
 get { return nIndex_.Count; }
 }
 
public Int32 GetNIndex(int index) {
 return nIndex_[index];
 }
 public void AddNIndex(Int32 value) {
 nIndex_.Add(value);
 }

public const int nValueFieldNumber = 2;
 private pbc::PopsicleList<Int32> nValue_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> nValueList {
 get { return pbc::Lists.AsReadOnly(nValue_); }
 }
 
 public int nValueCount {
 get { return nValue_.Count; }
 }
 
public Int32 GetNValue(int index) {
 return nValue_[index];
 }
 public void AddNValue(Int32 value) {
 nValue_.Add(value);
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
 {
int dataSize = 0;
for(int i=0; i<nIndexList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(nIndexList[i]);
}
size += dataSize;
size += 1 * nIndex_.Count;
}
{
int dataSize = 0;
for(int i=0; i<nValueList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(nValueList[i]);
}
size += dataSize;
size += 1 * nValue_.Count;
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
 {
if (nIndex_.Count > 0) {
for(int i=0; i<nIndex_.Count; ++i){
output.WriteInt32(1,nIndex_[i]);
}
}

}
{
if (nValue_.Count > 0) {
for(int i=0; i<nValue_.Count; ++i){
output.WriteInt32(2,nValue_[i]);
}
}

}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_SYNC_COMMONDATA _inst = (GC_SYNC_COMMONDATA) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.AddNIndex(input.ReadInt32());
break;
}
   case  16: {
 _inst.AddNValue(input.ReadInt32());
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  return true;
 }

}


[Serializable]
public class GC_SYNC_COMMONFLAG : PacketDistributed
{

public const int nIndexFieldNumber = 1;
 private pbc::PopsicleList<Int32> nIndex_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> nIndexList {
 get { return pbc::Lists.AsReadOnly(nIndex_); }
 }
 
 public int nIndexCount {
 get { return nIndex_.Count; }
 }
 
public Int32 GetNIndex(int index) {
 return nIndex_[index];
 }
 public void AddNIndex(Int32 value) {
 nIndex_.Add(value);
 }

public const int nValueFieldNumber = 2;
 private pbc::PopsicleList<Int32> nValue_ = new pbc::PopsicleList<Int32>();
 public scg::IList<Int32> nValueList {
 get { return pbc::Lists.AsReadOnly(nValue_); }
 }
 
 public int nValueCount {
 get { return nValue_.Count; }
 }
 
public Int32 GetNValue(int index) {
 return nValue_[index];
 }
 public void AddNValue(Int32 value) {
 nValue_.Add(value);
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
 {
int dataSize = 0;
for(int i=0; i<nIndexList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(nIndexList[i]);
}
size += dataSize;
size += 1 * nIndex_.Count;
}
{
int dataSize = 0;
for(int i=0; i<nValueList.Count; ++i){
dataSize += pb::CodedOutputStream.ComputeInt32SizeNoTag(nValueList[i]);
}
size += dataSize;
size += 1 * nValue_.Count;
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
 {
if (nIndex_.Count > 0) {
for(int i=0; i<nIndex_.Count; ++i){
output.WriteInt32(1,nIndex_[i]);
}
}

}
{
if (nValue_.Count > 0) {
for(int i=0; i<nValue_.Count; ++i){
output.WriteInt32(2,nValue_[i]);
}
}

}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_SYNC_COMMONFLAG _inst = (GC_SYNC_COMMONFLAG) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.AddNIndex(input.ReadInt32());
break;
}
   case  16: {
 _inst.AddNValue(input.ReadInt32());
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  return true;
 }

}


[Serializable]
public class CG_ASK_SETCOMMONFLAG : PacketDistributed
{

public const int nBitsFieldNumber = 1;
 private bool hasNBits;
 private Int32 nBits_ = 0;
 public bool HasNBits {
 get { return hasNBits; }
 }
 public Int32 NBits {
 get { return nBits_; }
 set { SetNBits(value); }
 }
 public void SetNBits(Int32 value) { 
 hasNBits = true;
 nBits_ = value;
 }

public const int nFlagFieldNumber = 2;
 private bool hasNFlag;
 private Int32 nFlag_ = 0;
 public bool HasNFlag {
 get { return hasNFlag; }
 }
 public Int32 NFlag {
 get { return nFlag_; }
 set { SetNFlag(value); }
 }
 public void SetNFlag(Int32 value) { 
 hasNFlag = true;
 nFlag_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasNBits) {
size += pb::CodedOutputStream.ComputeInt32Size(1, NBits);
}
 if (HasNFlag) {
size += pb::CodedOutputStream.ComputeInt32Size(2, NFlag);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasNBits) {
output.WriteInt32(1, NBits);
}
 
if (HasNFlag) {
output.WriteInt32(2, NFlag);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 CG_ASK_SETCOMMONFLAG _inst = (CG_ASK_SETCOMMONFLAG) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.NBits = input.ReadInt32();
break;
}
   case  16: {
 _inst.NFlag = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasNBits) return false;
 if (!hasNFlag) return false;
 return true;
 }

}


[Serializable]
public class GC_ASK_COMMONFLAG_RET : PacketDistributed
{

public const int nBitsFieldNumber = 1;
 private bool hasNBits;
 private Int32 nBits_ = 0;
 public bool HasNBits {
 get { return hasNBits; }
 }
 public Int32 NBits {
 get { return nBits_; }
 set { SetNBits(value); }
 }
 public void SetNBits(Int32 value) { 
 hasNBits = true;
 nBits_ = value;
 }

public const int nFlagFieldNumber = 2;
 private bool hasNFlag;
 private Int32 nFlag_ = 0;
 public bool HasNFlag {
 get { return hasNFlag; }
 }
 public Int32 NFlag {
 get { return nFlag_; }
 set { SetNFlag(value); }
 }
 public void SetNFlag(Int32 value) { 
 hasNFlag = true;
 nFlag_ = value;
 }

 private int memoizedSerializedSize = -1;
 public override int SerializedSize()
 {
 int size = memoizedSerializedSize;
 if (size != -1) return size;
 size = 0;
  if (HasNBits) {
size += pb::CodedOutputStream.ComputeInt32Size(1, NBits);
}
 if (HasNFlag) {
size += pb::CodedOutputStream.ComputeInt32Size(2, NFlag);
}
 memoizedSerializedSize = size;
 return size;
 }

public override void WriteTo(pb::CodedOutputStream output)
 {
 int size = SerializedSize();
  
if (HasNBits) {
output.WriteInt32(1, NBits);
}
 
if (HasNFlag) {
output.WriteInt32(2, NFlag);
}
 }
public override PacketDistributed MergeFrom(pb::CodedInputStream input,PacketDistributed _base) {
 GC_ASK_COMMONFLAG_RET _inst = (GC_ASK_COMMONFLAG_RET) _base;
 while (true) {
 uint tag = input.ReadTag();
 switch (tag) {
 case 0:
 {
 return _inst;
 }
    case  8: {
 _inst.NBits = input.ReadInt32();
break;
}
   case  16: {
 _inst.NFlag = input.ReadInt32();
break;
}

 }
 }
 return _inst;
 }
//end merged
public override bool IsInitialized() {
  if (!hasNBits) return false;
 if (!hasNFlag) return false;
 return true;
 }

}

