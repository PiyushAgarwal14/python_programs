import turtle as t
import colorsys
t.bgcolor('black')
t.shape('circle')
t.tracer(100)
h = 0

for i in range(350):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    h += 0.008
    t.pencolor(c)
    t.pensize(4)
    t.circle(i,100)
    t.rt(91)
    t.circle(i,-100)
t.done()