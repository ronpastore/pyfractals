from config import getInputOptions
getInputOptions()
from config import MATRIX_SIZE
from config import DEPTH
from config import FRAMES
from config import IMAGE_STORE
from config import PROCESS_COUNT
from config import DISTRIBUTION
from distribution.server import startServer, initializeWorkload, reap
from distribution.client import Client
from renderers.frame_creator import FrameCreator
import os
from multiprocessing import Pool
import Image
import sys

x_zoom_modifier = 1.0
y_zoom_modifier = 1.0

def spawnFrameCreator( (frame_number, x_zoom_modifier, y_zoom_modifier, depth) ):
    frame_creator = FrameCreator(MATRIX_SIZE)
    image = Image.new("RGB", (MATRIX_SIZE, MATRIX_SIZE))
    frame = frame_creator.createFrame(x_zoom_modifier, y_zoom_modifier, depth)
    frame.populateImage(image) 
    image.save("%s/%s.png" % (IMAGE_STORE, frame_number), "PNG")
    print "wrote frame %s with depth %s" % (frame_number, depth)

        
if __name__ == "__main__":
    
    if not os.path.exists(IMAGE_STORE):
        os.mkdir(IMAGE_STORE)
    
    
    worker_input = []
    for frame_number in range(0,FRAMES):
        worker_input.append( (frame_number, x_zoom_modifier, y_zoom_modifier, DEPTH) )
        x_zoom_modifier = x_zoom_modifier - 0.006
        y_zoom_modifier = y_zoom_modifier - 0.006      
        DEPTH = DEPTH+1
    
    if DISTRIBUTION=="standalone":
        process_pool = Pool(PROCESS_COUNT)
        process_pool.map(spawnFrameCreator, worker_input)    
    
    elif DISTRIBUTION == "server":
        pool = Pool(processes=1)
        result = pool.apply_async(startServer) 
        reaper_queue = initializeWorkload(worker_input)
        reap(reaper_queue, FRAMES)
        sys.exit()
        
    elif DISTRIBUTION =="client":
        Client.createFrames()   
    else:
        raise Exception("DISTRIBUTION mode not known: %s" % DISTRIBUTION)    
        
        
