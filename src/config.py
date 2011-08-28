from optparse import OptionParser

MATRIX_SIZE = 100.0
IMAGE_STORE = "images"
DEPTH = 50
FRAMES = 200
PROCESS_COUNT = 1


def getInputOptions():
    parser = OptionParser()
    parser.add_option("-s", "--size", dest="MATRIX_SIZE", help="image size (larger is slower)")
    parser.add_option("-o", "--frames_dir",dest="IMAGE_STORE",help="directory to store output frames")
    parser.add_option("-d", "--depth",dest="DEPTH",help="depth of mandelbrot set test")
    parser.add_option("-f", "--frames",dest="FRAMES",help="number of frames for animation")
    parser.add_option("-p", "--processes",dest="PROCESS_COUNT",help="divide job into x processes")
    
    (options, args) = parser.parse_args()
    
    global DEPTH, MATRIX_SIZE, IMAGE_STORE, FRAMES, PROCESS_COUNT

    if options.MATRIX_SIZE:
        MATRIX_SIZE = int(options.MATRIX_SIZE)
    if options.IMAGE_STORE:
        IMAGE_STORE = options.IMAGE_STORE
    if options.DEPTH:
        DEPTH = int(options.DEPTH)
    if options.FRAMES:
        FRAMES = int(options.FRAMES)
    if options.PROCESS_COUNT:
        PROCESS_COUNT = int(options.PROCESS_COUNT)
         
        
