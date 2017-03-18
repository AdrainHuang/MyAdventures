#coding:utf-8
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

size = 30
mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    # size = int(raw_input("你想清域是多大？ "))
    mc.postToChat('x=' + str(pos.x) + 'y=' + str(pos.y) + 'z=' + str(pos.z))
    mc.setBlocks(pos.x,pos.y,pos.z, pos.x+size,pos.y+size,pos.z+size, block.AIR.id)