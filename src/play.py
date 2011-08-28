from config import getInputOptions
getInputOptions()
from config import IMAGE_STORE
import pyglet
import os

frame_count = len(
  [ x for x in os.listdir(IMAGE_STORE) if x != "." and x != ".."]
)

image_frames = ["%s/%s.png" % (IMAGE_STORE, x) for x in range(1,frame_count)]


images = map(
    lambda img: pyglet.image.load(img),
    image_frames
)


animation = pyglet.image.Animation.from_image_sequence(images, 0.13)
animSprite = pyglet.sprite.Sprite(animation)

 # The main pyglet window with OpenGL context
w = animSprite.width
h = animSprite.height
win = pyglet.window.Window(width=w, height=h)

 # Set window background color to white.
pyglet.gl.glClearColor(1, 1, 1, 1)

@win.event
def on_draw():
    win.clear()
    animSprite.draw()



pyglet.app.run()

