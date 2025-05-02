import turtle

t=turtle.Turtle()

def koch(t, length):
    """Draws a koch curve """

    if length < 10:
        t.fd(length)
        return
    step = length/3
    l_angle= 60
    r_angle= 120
    koch(t, step)
    t.lt(l_angle)
    koch(t, step)
    t.rt(r_angle)
    koch(t, step)
    t.lt(l_angle)
    koch(t, step)
    
def snowflake(t, length):
    for i in range(3):
        koch(t, length)
        t.rt(120)

t.teleport(x=-400, y=100)
snowflake(t,1000)
turtle.mainloop()