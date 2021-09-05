import pygame
import requests

side = 850
background_colour = (251, 247, 245)
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=hard")
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]


def insert(src, position):
    i, j = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if(grid_original[i - 1][j - 1] != 0):
                    return
                if(event.key == 48):
                    grid[i - 1][j -1] = event.key - 48
                    pygame.draw.rect(src, background_colour, (position[0] * 50 + 5 , position[1] * 50 + 5, 30 , 40))
                    pygame.display.update()
                if(1 <= event.key - 48 < 10):
                    pygame.draw.rect(src, background_colour, (position[0] * 50 + 5, position[1] * 50 + 5, 50 - 10, 30))
                    value = myfont.render(str(event.key - 48), True, (0, 0, 0))
                    src.blit(value, (position[0] * 50 + 15, position[1] * 50))
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.display.update()
                    return
                return
                
            

            


def main():
    pygame.init()
    src = pygame.display.set_mode((side, side))
    src.fill(background_colour)
    pygame.display.flip()
    pygame.display.set_caption('Sudoku')
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(src, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 5)
            pygame.draw.line(src, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 5)    
        pygame.draw.line(src, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(src, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0 < grid[i][j] < 10):
                value = myfont.render(str(grid[i][j]), True, (52, 31, 151))
                src.blit(value, ((j + 1) * 50 + 15 , (i + 1) * 50 ))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(src, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()