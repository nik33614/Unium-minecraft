import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block
import time
import random
pos=mc.player.getTilePos()

x=pos.x
y=pos.y
z=pos.z


mc.setBlocks(x,y,z,x+50,y+50,z+50,0)
mc.setBlocks(x,y,z,x+50,y-1,z+50,2)

a=x+50
c=z+50
while True:
     
    while True:
         d=random.randint(-500,500)
         e=random.randint(-500,500)
         if d>=x and a>=d and  e>=z and c>=e:
                mc.setBlock(d,y+1,e,41)
                while True:
                             pos=mc.player.getTilePos()
                             g=pos.x
                             h=pos.y
                             i=pos.z
                
                             if g>=d and g<=d and i>=e and i<=e:
                                     mc.setBlock(g,h-1,i,0)
                                     break

                              
                                     
                             
          
               
                    
                             
    
                                
                    
