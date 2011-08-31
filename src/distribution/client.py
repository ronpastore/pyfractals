
from multiprocessing.managers import BaseManager
from config import SERVER_HOST, SERVER_PASSWORD, SERVER_PORT
from config import MATRIX_SIZE
from renderers.frame_creator import FrameCreator
import sys

class Client(object):

    @classmethod
    def createFrames(cls):
        class QueueManager(BaseManager): pass
        QueueManager.register('get_distributor')
        QueueManager.register('get_reaper')
        m = QueueManager(address=(SERVER_HOST, SERVER_PORT), authkey=SERVER_PASSWORD)
        m.connect()
        distributor_queue = m.get_distributor()
        reaper_queue = m.get_reaper()
        
        
        try:
            while True:
                frame_spec = distributor_queue.get()
                frame_creator = FrameCreator(MATRIX_SIZE)
                #TODO make frame spec object
                frame = frame_creator.createFrame(frame_spec[1], frame_spec[2], frame_spec[3])    
                frame.setFrameNumber(frame_spec[0])
                print "wrote frame %s with depth %s" % (frame_spec[0], frame_spec[3])
                reaper_queue.put(frame)
        except EOFError:
            print "Frames Completed"
            sys.exit()