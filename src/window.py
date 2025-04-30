from tkinter import Tk, BOTH, Canvas

class  Window(Tk):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Assign Root widget
        self.root = Tk()
        self.root.title("Window")
        # Assign Canvas widget
        self.window = Canvas(self.root, width=self.width, height=self.height)
        self.window.pack()
        # Running check
        self.is_running = False
        # Bind close method to "delete window" action
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        # Checks if window is running
        self.is_running = True
        # Call redraw while running
        while self.is_running == True:
            self.redraw()

    def close(self):
        self.is_running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.window, fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start_point.x, self.start_point.y,
            self.end_point.x, self.end_point.y,
            fill=fill_color, width=2
        )