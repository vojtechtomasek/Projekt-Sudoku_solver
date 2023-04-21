from digits import sudoku
import pygame

pygame.init()

WIDTH = 515
HEIGHT = 540
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Arial", 40)


running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the SCREEN with white
    SCREEN.fill(WHITE)
    
    # draw the Sudoku grid
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(SCREEN, BLACK, (30 + i * 50, 30), (30 + i * 50, 480), thickness)
        pygame.draw.line(SCREEN, BLACK, (30, 30 + i * 50), (480, 30 + i * 50), thickness)
    
    # draw the numbers
    for i in range(9):
        for j in range(9):
            num = sudoku[i][j]
            if num != 0:
                text = font.render(str(num), True, BLACK)
                text_rect = text.get_rect(center=(50*j+55, 50*i+55))
                SCREEN.blit(text, text_rect)
    
    # update the screen
    pygame.display.flip()

# quit Pygame
pygame.quit()
