from window import Point, Line

class Cell():
    def __init__(self, win=None):
        # Set walls and Top-Left/Bottom-Right points
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._center = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2, center):
        if self._win is None:
            return
        # Assign point inputs to cell
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._center = center
        # Check if walls exist then draw
        if self.has_left_wall:
            line = Line(Point(x1, y2), Point(x1, y1))
            self._win.draw_line(line, 'black')
        else:
            line = Line(Point(x1, y2), Point(x1, y1))
            self._win.draw_line(line, '#d9d9d9')
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, 'black')
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, '#d9d9d9')
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, 'black')
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, '#d9d9d9')
        if self.has_bottom_wall:
            line = Line(Point(x2, y2), Point(x1, y2))
            self._win.draw_line(line, 'black')
        else:
            line = Line(Point(x2, y2), Point(x1, y2))
            self._win.draw_line(line, '#d9d9d9')
    
    def draw_move(self, to_cell, undo=False):
        # Find center point of cells
        origin = self._center
        dest = to_cell._center
        line = Line(Point(origin[0], origin[1]), Point(dest[0], dest[1]))
        # Check if line is an undo then draw
        if undo == True:
            self._win.draw_line(line, 'gray')
        else:
            self._win.draw_line(line, 'red')