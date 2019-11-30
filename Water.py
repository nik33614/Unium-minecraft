import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block
import time
pos=mc.player.getTilePos()

x=pos.x
y=pos.y
z=pos.z


for i in range(20):
    time.sleep(1)
    pos=mc.player.getTilePos()

    x=pos.x
    y=pos.y
    z=pos.z
    mc.setBlock(x,y,z,8)
