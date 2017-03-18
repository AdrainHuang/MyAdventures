#coding:utf-8
"""
快速建立一个简单的房子
"""
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
SIZE = 20
mc = minecraft.Minecraft.create()
def house():
    midx = x + SIZE/2
    midy = y + SIZE/2
    # 房子面积
    mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
    # 挖空房子
    mc.setBlocks(x+1,y+1,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
    # 建门
    mc.setBlocks(midx-1,y,z, midx+1,y+3,z,block.AIR.id)
    # 玻璃窗
    mc.setBlocks(x+3, y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
    # 木屋顶
    mc.setBlocks(x,y+SIZE,z,x+SIZE,y+SIZE,z+SIZE,block.WOOD.id)
    # 地毯
    mc.setBlocks(x+1,y+1,z+1,x+SIZE-2,y+1,z+SIZE-2,block.WOOL.id,random.randint(0,15))

pos = mc.player.getTilePos()
x = pos.x +2
y = pos.y
z = pos.z