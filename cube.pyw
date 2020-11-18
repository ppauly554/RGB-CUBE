import pygame
pygame.init()

window = pygame.display.set_mode((768,1024))

RGB = [[x,y,z] for x in range(256) for y in range(256) for z in range(256)]

y0 = [y0 for y0 in RGB if 0 == y0[1]]
y0 = [y0[i * 256:(i + 1) * 256][::-1] for i in range(256)]

x0 = [x0 for x0 in RGB if 0 == x0[0]]
x0 = [x0[::-1][i * 256:(i + 1) * 256] for i in range(256)]

z0 = [z0 for z0 in RGB if 0 == z0[2]]
z0 = [z0[i * 256:(i + 1) * 256] for i in range(256)]

x255 = [x255 for x255 in RGB if 255 == x255[0]]
x255 = [x255[i * 256:(i + 1) * 256][::-1] for i in range(256)]

y255 = [y255 for y255 in RGB if 255 == y255[1]]
y255 = [y255[i * 256:(i + 1) * 256] for i in range(256)]

z255 = [z255 for z255 in RGB if 255 == z255[2]]
z255 = [z255[i * 256:(i + 1) * 256][::-1] for i in range(256)]

dot = pygame.Surface((1, 1))

window.fill((255,255,255))
    
for x in range(256):
    for y in range(256):
        dot.fill(z255[x][y])
        window.blit(dot, (x + 256, y))
        dot.fill(x0[x][y])
        window.blit(dot, (x, y + 256))
        dot.fill(y0[x][y])
        window.blit(dot, (x + 256, y + 256))
        dot.fill(x255[x][y])
        window.blit(dot, (x + 512, y + 256))
        dot.fill(z0[x][y])
        window.blit(dot, (x + 256, y + 512))
        dot.fill(y255[x][y])
        window.blit(dot, (x + 256, y + 768))
        
pygame.display.flip()
pygame.image.save(window, "cube.png")
pygame.quit()
