from config import MATRIX_SIZE
from renderers.frame_creator import FrameCreator
import os

zoom_modifier = 1.0
#os.mkdir(
for x in range(1,100):
    
        
    frame_creator = FrameCreator(MATRIX_SIZE)
    image = frame_creator.createFrame(zoom_modifier)
    image.save("images/%s.png" % x, "PNG")
    zoom_modifier = zoom_modifier - 0.02    
    print "wrote frame %s" % x
    
    