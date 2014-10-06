pyfractals
==========

A tool for generating fractal images, creating animations and distributing frame creation across multiple machines or processes. NOTE: Currently only supports mandelbrot fractals.


Examples
--------

*Tested with Python 2.6.5, Pyglet 1.1.2 (playback only)*


Spawn 5 processes to create a 100 frame animation, using 200x200 images, outputting all images into a new directory, "new_animation".

```sh
python build.py --size=200 --processes=5 --frames_dir=new_animation --frames=100
```


To play that animation with pyglet.

```sh
python play.py --frames_dir=new_animation
```

Start a frame queue server on a configured host/port, which will distribute frame specifications and reap completed frames from worker processes, passphrase auth optional.

```sh
python build.py --mode=server
```

Start a frame queue client on a configured host/port, which will grab frame specifications from the queue, generate frames and submit back to server using a reaper queue.
```sh
python build.py --mode=client
```

To see help and all options:
```sh
python build.py --help
```
