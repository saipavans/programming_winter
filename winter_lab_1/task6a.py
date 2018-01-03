SPACE_BETWEEN_COL_COUNT = 4
SPACE_BETWEEN_ROW_COUNT = 4
HORIZONTAL_CHAR = "-"
VERTICAL_CHAR =  "/"
SPACE_CHAR = " "
INTERSECTION_CHAR = "+"

def draw_edges(cols):
    print(INTERSECTION_CHAR, end="")
    for j in range(0, cols):
        print(HORIZONTAL_CHAR * SPACE_BETWEEN_COL_COUNT, end="")
        print(INTERSECTION_CHAR, end="")
    print("")

def draw_non_edges(cols):
    for k in range(0, SPACE_BETWEEN_ROW_COUNT):
        print(VERTICAL_CHAR, end="")
        for i in range(0, cols):
            print(SPACE_CHAR * SPACE_BETWEEN_COL_COUNT, end="")
            print(VERTICAL_CHAR, end="")
        print("")

def draw_grid(rows, cols):
    for i in range(0,rows):
        draw_edges(cols)
        draw_non_edges(cols)
    draw_edges(cols)



draw_grid(2,2)