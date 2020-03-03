import pygame
import numpy as np

#Initialization
pygame.init()
screen_position = (1000,600)
screen = pygame.display.set_mode(screen_position)
pygame.display.set_caption('Tic Tac Toe')

# Board_settings

board_state = np.zeros((3,3)) # board_state, empty cell is marked with zero

grid_size = 3 # do not change
grid_pixels = 100 # size of board
grid_position = ((screen_position[0]-grid_size*grid_pixels)*0.92, # position of board
                 (screen_position[1]-grid_size*grid_pixels)*0.76)
grid_linewidth = 5 # Linewidth of board, choose odd integer

current_player = - 1
player = dict({-1:"You",1:"computer"})
Computer = 1 # the computers moves are encoded as a one
Human = -1   # the humans moves are encoded as a negative one
ongoing_game = False

button_on = False
#grid cell variables
Xvalue_min = grid_position[0] + grid_linewidth / 2 + 1      # values for grid position
Yvalue_min = grid_position[1] + grid_linewidth / 2 + 1
Xvalue_max = grid_position[0] + grid_linewidth / 2 + 1 + grid_pixels - grid_linewidth
Yvalue_max = grid_position[1] + grid_linewidth / 2 + 1 + grid_pixels - grid_linewidth

#Restart button
restart_Xmin = Xvalue_min + 5                       # values for button position
restart_Ymin = Yvalue_min - 50
restart_Xmax = restart_Xmin + 80
restart_Ymax = restart_Ymin + 35

#Minimax button
minimax_Xmin = 40
minimax_Ymin = 100
minimax_Xmax = minimax_Xmin + 100
minimax_Ymax = minimax_Ymin + 40
### Functions ###

# Creates the visuals for the classic tictoctoe board,
def draw_board():
    screen.fill((45, 45, 45)) # adds a background color

    # adds a white playing field
    rect = pygame.Rect(grid_position[0], grid_position[1], grid_size * grid_pixels, grid_size*grid_pixels)
    pygame.draw.rect(screen, (255,255,220), rect)

    #creates Main text
    font = pygame.font.SysFont("cambriacambriamath", 40)
    text = font.render("Choose computer algorithm:", 1, (240, 240, 240))
    screen.blit(text, (30, 30))

    for x in range(grid_size + 1): # creates black grid lines

        # vertical lines
        pygame.draw.line(
                         screen, (0,0,0), # screen and color
                        (grid_position[0] + x * grid_pixels, # start x coordinate
                         grid_position[1] - grid_linewidth/2 + 1), # start y coordinate
                        (grid_position[0] + x * grid_pixels, # ending x coordinate
                         grid_position[1] + grid_pixels * grid_size + grid_linewidth/2-1),# ending y cordi
                         grid_linewidth) # linewidth
        # horizontal lines
        pygame.draw.line(
                         screen, (0,0,0), # screen and color
                        (grid_position[0] - grid_linewidth/2+1, # start x coordinate
                         grid_position[1] + x * grid_pixels), # start y coordinate
                        (grid_position[0] + grid_pixels * grid_size + grid_linewidth/2-1,# ending y cordi
                         grid_position[1]  + x * grid_pixels), # ending y coordinate
                         grid_linewidth) # linewidth

# creates a reset button when the game is finished
def draw_reset_button():
    # creates rectangle for button
    rect = pygame.Rect(restart_Xmin, restart_Ymin, 80, 35)
    pygame.draw.rect(screen, (255,255,235), rect)

    #creates text on the button
    font = pygame.font.SysFont("cambriacambriamath", 22)
    text = font.render("Restart", 1, (0, 0, 0))
    screen.blit(text, (Xvalue_min + 10, Yvalue_min - 45))

def draw_minimax_button(pressed=False):
    if not pressed:
        rect = pygame.Rect(40, 100, 100, 40)
        pygame.draw.rect(screen, (220, 220, 220), rect)
    if pressed:
        rect = pygame.Rect(40, 100, 100, 40)
        pygame.draw.rect(screen, (80, 80, 80), rect)
        print_footer_text("Make your move!")

    font = pygame.font.SysFont("rockwell", 22)
    text = font.render("Minimax", 1, (0, 0, 0))
    screen.blit(text, (46, 108))

def draw_montecarlo_button(pressed=False):
    if not pressed:
        rect = pygame.Rect(190, 100, 140, 40)
        pygame.draw.rect(screen, (220, 220, 220), rect)
    if pressed:
        rect = pygame.Rect(190, 100, 140, 40)
        pygame.draw.rect(screen, (80, 80, 80), rect)

    font = pygame.font.SysFont("rockwell", 22)
    text = font.render("Monte Carlo", 1, (0, 0, 0))
    screen.blit(text, (196, 108))

def draw_CNN_button(pressed=False):
    if not pressed:
        rect = pygame.Rect(380, 100, 140, 40)
        pygame.draw.rect(screen, (220, 220, 220), rect)
    if pressed:
        rect = pygame.Rect(380, 100, 140, 40)
        pygame.draw.rect(screen, (80, 80, 80), rect)

    font = pygame.font.SysFont("rockwell", 22)
    text = font.render("Convolution", 1, (0, 0, 0))
    screen.blit(text, (386, 108))

def print_footer_text(message):
    rect = pygame.Rect(0, screen_position[1]-36, screen_position[0], screen_position[1])
    pygame.draw.rect(screen, (100,100,100), rect)

    font = pygame.font.SysFont("candara", 30)
    text = font.render(message, 1, (255, 255, 255))
    screen.blit(text, (6, screen_position[1] - 32))


# check to see if the mouse is on the board
def mouse_on_board(mouseX,mouseY):
    on_X = False
    on_Y = False
    for x in range(3):
        if Xvalue_min + grid_pixels * x <= mouseX and mouseX <= Xvalue_max + grid_pixels * x: # checks the correct x cord
            on_X = True
        if Yvalue_min + grid_pixels * x <= mouseY and mouseY <= Yvalue_max + grid_pixels * x: # checks the correct y cord
            on_Y = True
    return (on_X and on_Y)

# check to see if the mouse is on the reset button
def mouse_on_restart(mouseX,mouseY):
    on_X = False
    on_Y = False
    if restart_Xmin <= mouseX and mouseX <= restart_Xmax:
        on_X = True
    if restart_Ymin <= mouseY and mouseY <= restart_Ymax:
        on_Y = True
    return (on_X and on_Y)

def mouse_on_minimax(mouseX,mouseY):
    on_X = False
    on_Y = False
    if minimax_Xmin <= mouseX and mouseX <= minimax_Xmax:
        on_X = True
    if minimax_Ymin <= mouseY and mouseY <= minimax_Ymax:
        on_Y = True
    return (on_X and on_Y)


# check to see which tictactoe_cell the mouse is on
def get_cell(mouseX,mouseY):
    for x in range(3):
        if Xvalue_min + grid_pixels * x <= mouseX and mouseX <= Xvalue_max + grid_pixels * x:
            row = x
    for y in range(3):
        if Yvalue_min + grid_pixels * y <= mouseY and mouseY <= Yvalue_max + grid_pixels * y:
            col = y
    return (row,col)

# checks which cells are empty
def empty_cells(board_state):
    return np.argwhere(board_state == 0).tolist()

# draws and places the move on the board
def place_move(row,col):
    global current_player
    if len(empty_cells(board_state)) == 0:
        return
    if current_player == 1:
        PlayerImg = pygame.image.load("cross.png")
    else:
        PlayerImg = pygame.image.load("circle.png")

    PlayerImg = pygame.transform.scale(PlayerImg,(grid_pixels-grid_linewidth-1,grid_pixels-grid_linewidth-1))
    position_x = Xvalue_min + grid_pixels * row
    position_y = Yvalue_min + grid_pixels * col
    screen.blit(PlayerImg,(position_x,position_y))
    board_state[row,col] = current_player
    if current_player == -1:
        current_player *= -1
        print_footer_text(f"the {player[current_player]} is thinking...")
    else:
        current_player *= -1
        print_footer_text(f"{player[current_player]}r turn to play")

# minimax algorithm used for calculating the computers move
def minimax(board_state, depth, player):

        if player == Computer:
            move = [-1, -1, -100]
        else:
            move = [-1, -1, 100]

        bol,score = check_winner()
        if depth == 0 or bol:
            return [-1, -1, score]

        for cell in empty_cells(board_state):
            x,y = cell[0], cell[1]
            board_state[x][y] = player
            score = minimax(board_state, depth - 1, -player)
            board_state[x][y] = 0
            score[0], score[1] = x, y

            if player == Computer:
                if score[2] > move[2]:
                    move = score  # max value
            else:
                if score[2] < move[2]:
                    move = score  # min value
        return move


# check to see where the mouse was clicked and choose an action depending on where it was
def check_click():
    global board_state,current_player,ongoing_game,button_on
    (mouseX, mouseY) = pygame.mouse.get_pos()
    if mouse_on_board(mouseX,mouseY):
        (row, col) = get_cell(mouseX, mouseY)
        if ongoing_game:
            if [row,col] in empty_cells(board_state):
                place_move(row, col)
    if not ongoing_game:
        if mouse_on_restart(mouseX,mouseY):
            restart()
        if mouse_on_minimax(mouseX,mouseY):
            pass
            button_on = ~button_on
            draw_minimax_button(pressed=button_on)
            ongoing_game = button_on



def check_winner():

    # check if cross won in row or col
    if np.sum(board_state, axis=0).max() == 3 or np.sum(board_state, axis=1).max() == 3:
        return (True, 1)
    # check if cross won in diagonal
    if np.sum(np.diagonal(board_state)) == 3 or np.sum(np.diagonal(np.flip(board_state, axis=1))) == 3:
        return (True,1)

    # check if circle won in row or col
    if np.sum(board_state, axis=0).min() == -3 or np.sum(board_state, axis=1).min() == -3:
        return (True, -1)
    # check if circle won in diagonal
    if np.sum(np.diagonal(board_state)) == -3 or np.sum(np.diagonal(np.flip(board_state, axis=1))) == -3:
        return (True, -1)

    else:
        return (False, 0)

def check_game_status():
    global ongoing_game
    (bol,winner) = check_winner()
    if bol:
        print_footer_text(f"{player[winner]} won the game!")
        ongoing_game = False
    if check_tie():
        print_footer_text(f"It's a tie!")
        ongoing_game = False


def check_tie():
    if np.sum(np.abs(board_state)) == 9:
        return True
    else:
        return False

def restart():
    global board_state,current_player,ongoing_game
    board_state = np.zeros((3, 3))
    run()

# starts the game
def run():
    draw_board()
    print_footer_text("choose an algorithm!")
    draw_minimax_button()
    #draw_montecarlo_button()
    #draw_CNN_button()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False

        if current_player == Human:
            if pygame.mouse.get_pressed()[0]:
                check_click()
        elif current_player == Computer:
            if len(empty_cells(board_state)) == 9:
                x,y = 1,1
            else:
                x,y,_ = minimax(board_state, len(empty_cells(board_state)), current_player) # Minimax algorithm
            place_move(x,y)

        check_game_status()
        (bol,_) = check_winner()
        if bol or check_tie():
            draw_reset_button()

        if not ongoing_game:
            if pygame.mouse.get_pressed()[0]:
                check_click()

        pygame.display.update()


if __name__ == "__main__":
    run()