from web_graphics import *

if __name__ == '__main__':
    bg = (0xee, ) * 3
    write_png("static/images/background.png", 400, 400, gradient(LINEAR_Y, GAUSSIAN(0.01), [
        (1.00, bg, bg)
    ]))
