#!/usr/bin/python
# -*- coding: utf-8 -*-

class Table_SceneClass:
    def __init__(self):
        self.__ID__ = 0
        self.SceneID = 0
        self.Name = ''
        self.ResName = ''
        self.Type = 0
        self.Length = 0
        self.Width = 0
        self.Obstacle = ''
        self.TerrainHeightMax = 0
        self.TerrainHeightMapLength = 0
        self.TerrainHeightMapWidth = 0
        self.BGMusic = 0
        self.PVPRule = 0
        self.ReliveType_1 = 0
        self.ReliveType_2 = 0
        self.ReliveType_3 = 0
        self.Entry_x = 0.0
        self.Entry_z = 0.0
        self.Safe_x = 0.0
        self.Safe_z = 0.0
        self.DeadPunishRule = 0
        self.CopySceneID = 0
        self.PlayersMaxA = 0
        self.PlayersMaxB = 0
        self.IsCanUseXp = 0
        self.IsCanUseLight = 0
        self.SceneMapTexture = ''
        self.SceneMapWidth = 0
        self.SceneMapHeight = 0
        self.SceneMapLogicWidth = 0

    def load(self, row):
        fieldList = row.split()
        self.__ID__ = int(fieldList[0])
        self.SceneID = int(fieldList[0])
        self.Name = fieldList[2]
        self.ResName = fieldList[3]
        self.Type = int(fieldList[4])
        self.Length = int(fieldList[5])
        self.Width = int(fieldList[6])
        self.Obstacle = fieldList[7]
        self.TerrainHeightMax = int(fieldList[8])
        self.TerrainHeightMapLength = int(fieldList[9])
        self.TerrainHeightMapWidth = int(fieldList[10])
        self.BGMusic = int(fieldList[11])
        self.PVPRule = int(fieldList[12])
        self.ReliveType_1 = int(fieldList[13])
        self.ReliveType_2 = int(fieldList[14])
        self.ReliveType_3 = int(fieldList[15])
        self.Entry_x = float(fieldList[16])
        self.Entry_z = float(fieldList[17])
        self.Safe_x = float(fieldList[18])
        self.Safe_z = float(fieldList[19])
        self.DeadPunishRule = int(fieldList[20])
        self.CopySceneID = int(fieldList[21])
        self.PlayersMaxA = int(fieldList[22])
        self.PlayersMaxB = int(fieldList[23])
        self.IsCanUseXp = int(fieldList[24])
        self.IsCanUseLight = int(fieldList[25])
        self.SceneMapTexture = fieldList[26]
        self.SceneMapWidth = int(fieldList[27])
        self.SceneMapHeight = int(fieldList[28])
        self.SceneMapLogicWidth = int(fieldList[29])
