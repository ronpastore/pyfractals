from config import getInputOptions
getInputOptions()
from config import MATRIX_SIZE
from config import DEPTH
from config import FRAMES
from config import IMAGE_STORE
from renderers.frame_creator import FrameCreator
import os

#dont yet know why theres zoom for x and y but it seems right
x_zoom_modifier = 1.0
y_zoom_modifier = 1.0

if not os.path.exists(IMAGE_STORE):
    os.mkdir(IMAGE_STORE)

for x in range(1,FRAMES):
    
        
    frame_creator = FrameCreator(MATRIX_SIZE)
    image = frame_creator.createFrame(x_zoom_modifier, y_zoom_modifier)
    image.save("%s/%s.png" % (IMAGE_STORE, x), "PNG")
    x_zoom_modifier = x_zoom_modifier - 0.006
    y_zoom_modifier = y_zoom_modifier - 0.006  #this should steer the zoom    
    print "wrote frame %s with depth %s" % (x, DEPTH)
    
    