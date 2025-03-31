import pygame
pygame.init()
display = pygame.display.set_mode(size=(720, 740))
pygame.display.flip()
surface = str(pygame.display.get_surface())
surface2 = surface.strip('<Surface(')
surface2 = surface2.strip("SW)>")
lst = surface2.split("x")
print(lst)