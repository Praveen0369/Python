import math
rad=int(input("What is the radius of the flower? "))
p=int(input("How many petals do you want? "))



def draw_arc(b,r):  
    c=math.pi*r 
    ca=c/(360/60) 
    n=int(ca/3)+1  
    l=ca/n  
    for i in range(n):
        b.fd(l)
        b.lt(360/(n*6))


def draw_petal(b,r):
    draw_arc(b,r)
    b.lt(180-60)
    draw_arc(b,r)
    b.rt(360/petals-30)



import turtle
bob=turtle.Turtle()


for i in range(petals):
    draw_petal(bob,radius)
    bob.lt(360/1)
