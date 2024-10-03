from window import Window
from maze import Maze

def main():
    width = 64
    height = 64
    margin = 16
    n = 5
    m = 5

    window_height = 2 * margin + m * height
    window_width = 2 * margin + n * width

    win = Window(window_width, window_height)

    maze = Maze(margin, margin, n, m, width, height, win, 10)
    maze.solve()
   
    win.wait_for_close()

if __name__ == "__main__":
    main()
