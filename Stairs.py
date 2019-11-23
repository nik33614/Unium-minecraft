from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
block = 45
pos = mc.player.getTilePos()
x = round(pos.x + 2)
y = round(pos.y)
z = round(pos.z)

for a in range(0 ,256):
   x+=1
   y+=1
   for b in range(2):
       mc.setBlocks(x - 1, y, z - 1, x- 1, y, z + 1, block)
       time.sleep(1)

