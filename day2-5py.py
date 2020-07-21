# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:57:19 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getTilePos()
     
    right=mc.getBlock(x+1,y-1,z)
    left=mc.getBlock(x-1,y-1,z)
    front=mc.getBlock(x,y-1,z+1)
    back=mc.getBlock(x,y-1,z-1)
    print(right)
    if right==8 or left==8 or front==8 or back==8 :
         x,y,z=mc.player.getTilePos()(x-1,y-1,z-1,x+1,y-1,z+1)
     
    
    
    
    
    