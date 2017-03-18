#coding:utf-8
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlocks(pos.x,pos.y,pos.z,pos.x+2,pos.y,pos.z,block.WOOL.id)