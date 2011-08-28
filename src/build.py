from config import getInputOptions
getInputOptions()
from config import MATRIX_SIZE
from config import DEPTH
from config import FRAMES
from config import IMAGE_STORE
from config import PROCESS_COUNT
from renderers.frame_creator import FrameCreator
import os
from multiprocessing import Pool
import Image

#dont yet know why theres zoom for x and y but it seems right
x_zoom_modifier = 1.0
y_zoom_modifier = 1.0



def spawnWorker( (frame_number, x_zoom_modifier, y_zoom_modifier, depth) ):
    frame_creator = FrameCreator(MATRIX_SIZE)
    image = Image.new("RGB", (MATRIX_SIZE, MATRIX_SIZE))
    frame = frame_creator.createFrame(x_zoom_modifier, y_zoom_modifier, depth)
    frame.populateImage(image) 
    image.save("%s/%s.png" % (IMAGE_STORE, frame_number), "PNG")
    print "wrote frame %s with depth %s" % (frame_number, depth)


if __name__ == "__main__":
    
    if not os.path.exists(IMAGE_STORE):
        os.mkdir(IMAGE_STORE)
    
    process_pool = Pool(PROCESS_COUNT)
    
    worker_input = []
    for frame_number in range(1,FRAMES):
        worker_input.append( (frame_number, x_zoom_modifier, y_zoom_modifier, DEPTH) )
        x_zoom_modifier = x_zoom_modifier - 0.006
        y_zoom_modifier = y_zoom_modifier - 0.006      
        DEPTH = DEPTH+1
    process_pool.map(spawnWorker, worker_input)    