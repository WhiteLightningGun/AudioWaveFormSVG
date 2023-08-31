import drawsvg as draw

# Notes: https://pypi.org/project/drawsvg/

d = draw.Drawing(300, 80, origin=(0,0))

# Draw a rectangle

max_height = 80

r3 = draw.Rectangle(12, (max_height - 60)/2, 8, 60, fill='#003300') #vdark green

r4 = draw.Rectangle(24, (max_height - 50)/2, 8, 50, fill='#003300') #vdark green

r5 = draw.Rectangle(36, (max_height - 40)/2, 8, 40, fill='#003300') #vdark green



d.save_svg('example.svg')