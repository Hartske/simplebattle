from node import Cell
import time
import random

class Grid():
    def __init__(
            self,
            x1, y1,
            num_rows, num_cols,
            cell_size_x, cell_size_y,
            win=None,
            seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            random.seed(seed)
        # When Maze() is created, it will run _create_cells()
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        # List containg lists of cells
        self._cells = []
        for col in range(self.num_cols):
            # List to hold list of cells
            cols = []
            for row in range(self.num_rows):
                cell = Cell(self.win)
                cols.append(cell)
            # Add it to list of lists
            self._cells.append(cols)
        # Start the draw for each cell
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # Calculate x, y for the four corners of the Cell()
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        # Draw and animate
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        # Time in seconds to pause
        time.sleep(.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Right check cell exists and if visited
            if i+1 in range(len(self._cells)):
                if self._cells[i+1][j].visited is False:
                    to_visit.append(['right', i + 1, j])
            # Bottom check cell exists and if visited
            if j+1 in range(len(self._cells[0])):
                if self._cells[i][j+1].visited is False:
                    to_visit.append(['bottom', i, j + 1])
            # Left check cell exists and if visited
            if i-1 in range(len(self._cells)):
                if self._cells[i-1][j].visited is False:
                    to_visit.append(['left', i - 1, j])
            # Top check cell exists and if visited
            if j-1 in range(len(self._cells[0])):
                if self._cells[i][j-1].visited is False:
                    to_visit.append(['top', i, j - 1])
            # Nothing to visit, exit
            if len(to_visit) == 0:
                return
            else:
                # Get direction
                direction = random.randrange(len(to_visit))
                # Break walls in direction then move
                if to_visit[direction][0] == 'right':
                    self._cells[i][j].has_right_wall = False
                    self._cells[to_visit[direction][1]][to_visit[direction][2]].has_left_wall = False
                    self._draw_cell(i, j)
                    self._draw_cell(to_visit[direction][1], to_visit[direction][2])
                elif to_visit[direction][0] == 'bottom':
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[to_visit[direction][1]][to_visit[direction][2]].has_top_wall = False
                    self._draw_cell(i, j)
                    self._draw_cell(to_visit[direction][1], to_visit[direction][2])
                elif to_visit[direction][0] == 'left':
                    self._cells[i][j].has_left_wall = False
                    self._cells[to_visit[direction][1]][to_visit[direction][2]].has_right_wall = False
                    self._draw_cell(i, j)
                    self._draw_cell(to_visit[direction][1], to_visit[direction][2])
                elif to_visit[direction][0] == 'top':
                    self._cells[i][j].has_top_wall = False
                    self._cells[to_visit[direction][1]][to_visit[direction][2]].has_bottom_wall = False
                    self._draw_cell(i, j)
                    self._draw_cell(to_visit[direction][1], to_visit[direction][2])
                self._break_walls_r(to_visit[direction][1], to_visit[direction][2])

    def _reset_cells_visited(self):
        for i in self._cells:
            for j in i:
                j.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[-1][-1]:
            return True
        # Right check cell exists and if visited
        if i+1 in range(len(self._cells)) and self._cells[i][j].has_right_wall is False and self._cells[i+1][j].visited is False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j) is True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j],undo=True)
        # Bottom check cell exists and if visited
        if j+1 in range(len(self._cells)) and self._cells[i][j].has_bottom_wall is False and self._cells[i][j+1].visited is False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1) is True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1],undo=True)
        # Left check cell exists and if visited
        if i-1 in range(len(self._cells)) and self._cells[i][j].has_left_wall is False and self._cells[i-1][j].visited is False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j) is True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j],undo=True)
        # Top check cell exists and if visited
        if j-1 in range(len(self._cells)) and self._cells[i][j].has_top_wall is False and self._cells[i][j-1].visited is False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1) is True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1],undo=True)
        else:
            return False