#from digits import sudoku
from Sudoku import solve, valid
import pygame
pygame.init()
pygame.font.init()


sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


WIDTH, HEIGHT = 543, 543
GRID_SIZE     = 9
GRID_WIDTH_X  = WIDTH  // GRID_SIZE
GRID_HEIGHT_Y = HEIGHT // GRID_SIZE


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60

font = pygame.font.SysFont("Arial", 40)

def draw_window():
    WINDOW.fill(WHITE)
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(WINDOW, BLACK, (i * 60, 0), (i * 60, HEIGHT), thickness)
        pygame.draw.line(WINDOW, BLACK, (0, i * 60), (WIDTH, i * 60), thickness)
            
    font = pygame.font.Font(None, 40)
    for i in range(9):
        for j in range(9):
            num = sudoku[i][j]
            if num != 0:
                text = font.render(str(num), True, BLACK)
                text_rect = text.get_rect(center=(j*60+30, i*60+30))
                WINDOW.blit(text, text_rect)
    
    
    pygame.display.update()


def main():
    
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                cell_x = mouse_x // GRID_WIDTH_X 
                cell_y = mouse_y // GRID_HEIGHT_Y
                #print( "Click in cell [%d,%d]" % ( mouse_x, mouse_y ))
                #print( "Click in cell [%d,%d]" % ( cell_x, cell_y ))
                
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_1]:
                sudoku[cell_y][cell_x] = 1
            elif keys[pygame.K_2]:
                sudoku[cell_y][cell_x] = 2
            elif keys[pygame.K_3]:
                sudoku[cell_y][cell_x] = 3
            elif keys[pygame.K_4]:
                sudoku[cell_y][cell_x] = 4
            elif keys[pygame.K_5]:
                sudoku[cell_y][cell_x] = 5
            elif keys[pygame.K_6]:
                sudoku[cell_y][cell_x] = 6
            elif keys[pygame.K_7]:
                sudoku[cell_y][cell_x] = 7
            elif keys[pygame.K_8]:
                sudoku[cell_y][cell_x] = 8
            elif keys[pygame.K_9]:
                sudoku[cell_y][cell_x] = 9
            elif keys[pygame.K_BACKSPACE]:
                sudoku[cell_y][cell_x] = 0
            elif keys[pygame.K_SPACE]:
                solve(sudoku)
                
        draw_window()
        
            
    pygame.quit
    
    
if __name__ == "__main__":
    main()


