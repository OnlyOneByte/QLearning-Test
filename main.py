"""
    Author: Rengang (Angelo) Yang
"""

from Board import BoardObj
import pygame


def main():
    # Color Define
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    # This sets the WIDTH and HEIGHT of each box
    WIDTH = 50
    HEIGHT = 50
    # Weight of border between cells.
    MARGIN = 2

    # Read in board config files
    testBoard = BoardObj("test_board.txt")

    # Calculate size of screen
    size = (WIDTH * testBoard.cols + (MARGIN*testBoard.cols+1),
             HEIGHT * testBoard.rows + (MARGIN*testBoard.rows+1))
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Q-Learn-test")

    # Finished = false. Keeps running until closed
    done = False
    clock = pygame.time.Clock()

    # ************** main loop **************
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
        # --- Game logic should go here
    
        # Resets screen to white.
        screen.fill(BLACK)
        # Draws grid
        for row in range(testBoard.rows):
            for column in range(testBoard.cols):
                dimen = [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT]
                pygame.draw.rect(screen, WHITE, dimen)
        
            
    
        # Updates changes
        pygame.display.flip()
    
        # Framerate limiter (60 fps)
        clock.tick(60)
    
    # Close the window and quit.
    pygame.quit()

    testBoard = BoardObj("test_board.txt")




if __name__ == "__main__":
    main()