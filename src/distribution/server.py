'''
Created on 31 Aug 2011
@author: ron pastore
'''

from multiprocessing.managers import BaseManager
import Queue
from config import SERVER_HOST, SERVER_PASSWORD, SERVER_PORT
from config import MATRIX_SIZE, IMAGE_STORE
import Image
import os

def initializeWorkload(worker_input):
        class QueueManager(BaseManager): pass
        QueueManager.register('get_distributor')
        QueueManager.register('get_reaper')
        m = QueueManager(address=(SERVER_HOST, SERVER_PORT), authkey=SERVER_PASSWORD)
        m.connect()
        distributor_queue = m.get_distributor()
        
        for input in worker_input:
            distributor_queue.put(input)   
        return m.get_reaper()

def startServer():
    print "Starting frame creation server..."
    distributor_queue = Queue.Queue()
    reaper_queue = Queue.Queue()        
    class QueueManager(BaseManager): pass
    QueueManager.register('get_distributor', callable=lambda:distributor_queue)
    QueueManager.register('get_reaper', callable=lambda:reaper_queue)
    manager = QueueManager(address=(SERVER_HOST, SERVER_PORT), authkey=SERVER_PASSWORD)
    server = manager.get_server()
    server.serve_forever()
       
    
    
def reap(reaper_queue, total_expected_frames):
    while True:
        finished_frame = reaper_queue.get()
        image = Image.new("RGB", (MATRIX_SIZE, MATRIX_SIZE))
        finished_frame.populateImage(image) 
        image.save("%s/%s.png" % (IMAGE_STORE, finished_frame.frame_number), "PNG")
        print "wrote image %s" % finished_frame.frame_number
        
        if len(os.listdir(IMAGE_STORE)) >= total_expected_frames:
            break