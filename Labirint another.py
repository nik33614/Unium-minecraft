from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()

x, y, z = pos.x, pos.y, pos.z
blocks = [  [35, 0, 35, 35, 35, 35, 35, 35],
            [35, 0, 35, 35, 35, 35, 35, 35],
            [35, 0, 0, 0, 0, 0, 0, 35],
            [35, 35, 35, 0, 35, 0, 0, 35],
            [35, 35, 35, 0, 35, 0, 35, 35],
            [35, 0, 0, 0, 35, 0, 35, 35],
            [35, 35, 35, 35, 35, 0, 35, 35],
            [35, 35, 35, 35, 35, 0, 35, 35]]
for row in reversed(blocks):
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    z += 1
    x = pos.x


x, y, z = pos.x, pos.y, pos.z
blocks = [  [35, 0, 35, 35, 35, 35, 35, 35],
            [35, 0, 35, 35, 35, 35, 35, 35],
            [35, 0, 0, 0, 0, 0, 0, 35],
            [35, 35, 35, 0, 35, 0, 0, 35],
            [35, 35, 35, 0, 35, 0, 35, 35],
            [35, 0, 0, 0, 35, 0, 35, 35],
            [35, 35, 35, 35, 35, 0, 35, 35],
            [35, 35, 35, 35, 35, 0, 35, 35]]
for row in reversed(blocks):
    for block in row:
        mc.setBlock(x, y+1, z, block)
        x += 1
        
    
    z += 1
    x = pos.x
