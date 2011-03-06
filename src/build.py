from config import MATRIX_SIZE
from renderers.frame_creator import FrameCreator
import os


#dont yet know why theres zoom for x and y but it seems right

x_zoom_modifier = 1.0
y_zoom_modifier = 1.0

#hmmx = 1.56
#hmmy = 1.20
for x in range(1,200):
    
        
    frame_creator = FrameCreator(MATRIX_SIZE)
    image = frame_creator.createFrame(x_zoom_modifier, y_zoom_modifier)
    image.save("images/%s.png" % x, "PNG")
    x_zoom_modifier = x_zoom_modifier - 0.02 
    y_zoom_modifier = y_zoom_modifier - 0.02  #this should steer the zoom    
    print "wrote frame %s" % x
    
    