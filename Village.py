import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block
import time

pos=mc.player.getTilePos()

x=pos.x
y=pos.y
z=pos.z
a=pos.x
b=pos.y
c=pos.z
d=pos.x
e=pos.y
f=pos.z
g=pos.x
h=pos.y
i=pos.z
j=pos.x
k=pos.y
l=pos.z
j=j+10
l=l+11
d=d+7
a=a+21
c=c+4
i=i+20
la=pos.x
m=pos.y
n=pos.z
la=la+7
n=n+21

#очистка
block=block.AIR.id
mc.setBlocks(x-10,y-1,z-10,x+30,y+30,z+30,block)
mc.setBlocks(x-10,y-1,z-10,x+30,y-1,z+30,2)
#дом 1
mc.setBlocks(x,y,z,x+3,y,z+5,1)
mc.setBlocks(x,y+1,z,x+3,y+4,z,5)
mc.setBlocks(x,y+1,z,x,y+4,z+5,5)
mc.setBlocks(x,y+1,z+5,x+3,y+4,z+5,5)
mc.setBlocks(x+3,y+1,z,x+3,y+4,z+5,5)
mc.setBlocks(x,y+4,z,x+3,y+4,z+5,17)
mc.setBlocks(x+3,y+2,z+3,x+3,y+2,z+5,20)
mc.setBlocks(x+1,y+2,z+5,x+2,y+2,z+5,20)
mc.setBlocks(x+1,y+1,z,x+1,y+2,z,64)
mc.setBlocks(x+1,y,z-1,x+1,y,z-1,44)
mc.setBlocks(x+3,y+3,z+2,x+3,y+3,z+2,89)

#house 2
mc.setBlocks(a+1,b,c,a+8,b,c+12,1)
mc.setBlocks(a+1,b+1,c,a+8,b+5,c,5)
mc.setBlocks(a+1,b+1,c+12,a+8,b+5,c+12,5)
mc.setBlocks(a+1,b+1,c,a+1,b+5,c+12,5)
mc.setBlocks(a+8,b+1,c,a+8,b+5,c+12,5)
mc.setBlocks(a+1,b+5,c,a+8,b+5,c+12,17)
mc.setBlocks(a+2,b+6,c+1,a+7,b+6,c+11,17)
mc.setBlocks(a+3,b+7,c+2,a+6,b+6,c+10,17)
mc.setBlocks(a+4,b+8,c+3,a+5,b+6,c+9,17)
mc.setBlocks(a+1,b+1,c+5,a+1,b+2,c+5,0)
mc.setBlocks(a+1,b+1,c+5,a+1,b+2,c+5,64)
mc.setBlocks(a+7,b+1,c+1,a+7,b+5,c+11,47)
mc.setBlocks(a+7,b+3,c+1,a+7,b+3,c+11,89)
mc.setBlocks(a+6,b+1,c+1,a+6,b+1,c+11,53)
mc.setBlocks(a,b,c+5,a,b,c+5,44)
#house 3


mc.setBlocks(d+1,e,f,d+11,e,f+5,1)
mc.setBlocks(d+1,e+1,f,d+11,e+4,f,5)
mc.setBlocks(d+1,e+1,f+5,d+11,e+4,f+5,5)
mc.setBlocks(d+1,e+1,f,d+1,e+4,f+5,5)
mc.setBlocks(d+11,e+1,f,d+11,e+4,f+5,5)
mc.setBlocks(d+1,e+4,f,d+11,e+5,f+5,17)
mc.setBlocks(d+3,e+5,f+2,d+9,e+5,f+5,17)
mc.setBlocks(d+6,e+1,f+5,d+6,e+2,f+5,0)
mc.setBlocks(d+6,e+1,f,d+6,e+2,f,0)
mc.setBlocks(d+6,e+1,f+5,d+6,e+2,f+5,64)
mc.setBlocks(d+1,e+3,f+1,d+10,e+3,f+2,89)

#jne more

mc.setBlocks(g,h,i,g+3,h,i+5,1)
mc.setBlocks(g,h+1,i,g+3,h+4,i,5)
mc.setBlocks(g,h+1,i,g,h+4,i+5,5)
mc.setBlocks(g,h+1,i+5,g+3,h+4,i+5,5)
mc.setBlocks(g+3,h+1,i,g+3,h+4,i+5,5)
mc.setBlocks(g,h+4,i,g+3,h+4,i+5,17)
mc.setBlocks(g+3,h+2,i+3,g+3,h+2,i+5,20)
mc.setBlocks(g+1,h+2,i+5,g+2,h+2,i+5,20)
mc.setBlocks(g+1,h+1,i,g+1,h+2,i,64)
mc.setBlocks(g+1,h,i-1,g+1,h,i-1,44)
mc.setBlocks(g+3,h+3,i+2,g+3,h+3,i+2,89)
#colodec

mc.setBlocks(j+1,k,l,j+5,k,l+4,17)
mc.setBlocks(j+2,k,l+1,j+4,k,l+3,8)

#graydki


mc.setBlocks(la+1,m,n,la+9,m,n+8,60)
mc.setBlocks(la+2,m,n+4,la+7,m,n+4,8)
mc.setBlocks(la+1,m,n,la+1,m,n+8,17)
mc.setBlocks(la+9,m,n,la+9,m,n+8,17)
mc.setBlocks(la+1,m,n,la+8,m,n,17)
mc.setBlocks(la+8,m,n,la+8,m,n,17)
mc.setBlocks(la+1,m,n+9,la+9,m,n+9,17)


#doroda
p=pos.x
q=pos.y
r=pos.z

q=q-1
r=r+11

#mc.setBlocks(p,q,r,p+6,q,r+1,17)
#mc.setBlocks(p+4,q,r+8,p+5,q,r+18,17)

