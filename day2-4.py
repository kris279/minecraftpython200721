# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:19:53 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    
    
    mc.setBlock(x,y-1,z,46)
    mc.setBlock(x,y-2,z,51)