TOTAL_CHARS = 70
SPACE_CHAR = " "

def right_justify(s):
    leading_space = TOTAL_CHARS - len(s)
    print(SPACE_CHAR * leading_space + s)

right_justify("allen")