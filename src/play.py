
import pyglet

image_frames = ["images/%s.png" % x for x in range(1,54)]

# Create the list of pyglet images
images = map(lambda img: pyglet.image.load(img),
      image_frames)

animation = pyglet.image.Animation.from_image_sequence(
       images, 0.13)

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

