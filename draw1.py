import turtle

t=turtle.Turtle()

def draw(t, length, n):
    if n == 0:
        t.fd(n)
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)
    
draw(t, 10, 5)
