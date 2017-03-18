#coding:utf-8
import mcpi.minecraft as minecraft
import time

HOME_X = 2
HOME_Y = 9
HOME_Z = -2
inField = 0
mc = minecraft.Minecraft.create()
x1 = -10
x2 = -5
z1 = 2
z2 = -8
rent = 0
# mc.player.setPos(HOME_X,HOME_Y,HOME_Z)
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    # mc.postToChat('x=' + str(pos.x) + 'y=' + str(pos.y) + 'z=' + str(pos.z))
    if pos.x >= x1 and pos.x <= x2 and pos.z <= z1 and pos.z >=z2 :
        rent = rent + 1
        mc.postToChat("你欠我租金 :" + str(rent))
        inField = inField + 1
    else: #不在此区域
        inField = 0
    if inField > 5:
        mc.postToChat("你我的围栏停留太久，将传送你回家：")
        mc.player.setPos(HOME_X,HOME_Y+100,HOME_Z)