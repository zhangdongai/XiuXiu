from __future__ import division
import re
import os

from collections import defaultdict
from heapq import nlargest

def ScanFiles(path): #fun
	for dirs,subdir,files in os.walk(path):
		for fn in files:
			if fn.find("Packet.") >= 0:
				yield fn

def PrintToppestInfo(dict, topIndex, OutPutFile, printName):
	Toppest_List = nlargest(topIndex, dict.items(),key=lambda x: x[1]);
	print("Toppest_"+ printName +": ")
	OutPutFile.write("Toppest_"+printName+": \n");
	OutPutFile.write("rank packetId "+printName+" PacketName \n");
	index = 1;
	for item in Toppest_List:
			print(index, item[0],item[1])
			OutPutFile.write(str(index)+" "+str(item[0])+" "+str(item[1])+" "+ pakcetNameDict[item[0]] + "\n");
			index += 1;
	OutPutFile.write("\n");
	return;

receivecountDict = defaultdict(int); 
receivesizeDict = defaultdict(int);	
sendcountDict = defaultdict(int);		
sendsizeDict = defaultdict(int);
pakcetNameDict = defaultdict(str);
packetSizeDict = defaultdict(int);

if not os.path.isdir("Result"):
	os.makedirs("Result");
OutPutFile = open("Result\PacketLogAnalyseResult.txt", "w");

TopIndex = 10;
print(os.getcwd())
with open(os.getcwd()+"\Config\Config.txt") as configFile:
	for configline in configFile:
			TopIndex = (int)(configline);
			print(TopIndex);

os.chdir("Log");
allFiles = list(ScanFiles(os.getcwd()))
for lfile in allFiles:
	with open(lfile) as logfile:
		for line in logfile:
			dotPos = line.find(",",0);
			if dotPos > 0 and line[0:dotPos].isdigit():
				packetId, szreceivecount, szreceivesize, szsendcount, szsendsize, PacketName, noUse = line.split(",",6);
				receivecount = (int)(szreceivecount);
				receivesize = (int)(szreceivesize);
				sendcount = (int)(szsendcount);
				sendsize = (int)(szsendsize);
				receivecountDict[packetId] += receivecount;
				receivesizeDict[packetId] += receivesize;
				sendcountDict[packetId] += sendcount;
				sendsizeDict[packetId] += sendsize;
				pakcetNameDict[packetId] = PacketName;
				if receivecount > 0 and receivesize >0:
					packetSizeDict[packetId] = receivesize/receivecount;
				elif sendcount >0 and sendsize >0:
					packetSizeDict[packetId] = sendsize/sendcount;


OutPutFile.write("Toppest "+str(TopIndex)+" OutPut: \n");

PrintToppestInfo(receivecountDict,TopIndex, OutPutFile, "receivecount");

PrintToppestInfo(receivesizeDict,TopIndex, OutPutFile, "receivesize");

PrintToppestInfo(sendcountDict,TopIndex, OutPutFile, "sendcount");

PrintToppestInfo(sendsizeDict,TopIndex, OutPutFile, "sendsize");

PrintToppestInfo(packetSizeDict,TopIndex, OutPutFile, "packetsize");

OutPutFile.close();