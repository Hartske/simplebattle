from window import Window
from grid import Grid

def main():
    win = Window(1280, 720)
    
    grid = Grid(10, 10, 13, 24, 52, 52, win)

    win.wait_for_close()
    
main()