## python 2
from swampy.World import World

world = World()
world.mainloop()
canvas = world.ca(width=500, height=500, background='white')
bbox = [[-150,-100], [150,100]]
canvas.rectangle(bbox, outline='black', width=2, fill='green4')
canvas.circle([-25,0], 70, outline=None, fill='red')