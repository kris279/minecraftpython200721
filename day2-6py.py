# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:44:25 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
blockid=int(input("要放什麼方塊:"))
mc.setBlock(x+1,y,z,blockid)