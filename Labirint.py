import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block
import time
mc.player.setPos(0,65,0)
pos=mc.player.getTilePos()

x=pos.x
y=pos.y
z=pos.z
x+=10
z+=20
mc.player.setPos(x+5,y+1,z+2)
#очистка
block=block.AIR.id
mc.setBlocks(x-10,y-1,z-10,x+50,y+30,z+50,block)
mc.setBlocks(x-10,y-1,z-10,x+50,y-1,z+50,49)


mc.setBlocks(x,y,z,x+20,y+2,z,49)
mc.setBlocks(x+20,y,z,x+20,y+2,z+50,49)
mc.setBlocks(x,y,z,x,y+2,z+50,49)
mc.setBlocks(x,y,z+50,x+20,y+2,z+50,49)
mc.setBlocks(x,y,z+6,x+20,y+2,z+6,49)
mc.setBlocks(x+15,y,z+6,x+15,y+2,z+30,49)
mc.setBlocks(x+12,y,z+6,x+12,y+2,z+30,49)
mc.setBlocks(x+13,y,z+6,x+14,y+2,z+6,0)
mc.setBlocks(x,y,z+15,x+12,y+2,z+15,49)
mc.setBlocks(x,y,z+18,x+12,y+2,z+18,49)
mc.setBlocks(x+12,y,z+16,x+12,y+2,z+17,0)
mc.setBlocks(x+4,y,z+18,x+4,y+2,z+30,49)
mc.setBlocks(x+1,y,z+18,x+3,y+2,z+18,0)
mc.setBlocks(x+20,y,z+30,x,y+2,z+30,49)
mc.setBlocks(x+20,y,z+35,x,y+2,z+35,49)
mc.setBlocks(x+19,y,z+30,x+16,y+2,z+30,0)
mc.setBlocks(x+4,y,z+35,x+4,y+2,z+50,49)
mc.setBlocks(x+18,y,z+35,x,y+2,z+35,49)
mc.setBlocks(x+15,y,z+30,x+13,y+2,z+30,0)
mc.setBlocks(x+3,y,z+30,x+1,y+2,z+30,0)
mc.setBlocks(x,y,z+45,x+20,y+2,z+45,49)
mc.setBlocks(x,y,z,x,y+2,z+50,49)
mc.setBlocks(x+1,y,z+35,x+3,y+2,z+35,0)
mc.setBlocks(x+1,y,z+45,x+3,y+2,z+45,0)
mc.setBlocks(x+4,y,z+46,x+4,y+2,z+49,0)

mc.setBlocks(x+20,y,z+46,x+20,y+2,z+49,0)
a=23
b=38

while True:
               pos=mc.player.getTilePos()
               x=pos.x
               y=pos.y
               z=pos.z
               if x>=23 and z>=38:
                    mc.setBlock(x,y-1,z,0)
                   
               
