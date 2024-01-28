# FONTOS amíg még hátra vannak ebből a programból:
# - mozgó animáció menjen, ezért lecserélni valamire a dvd logót
# - ha neki ütközik a falnak random legyen az elmozdulása(most még kirepül)
# - szebb háttér választása
# - idő számláló kíiratása ami nullázódik ha hozzáér a sarokhoz


import pygame

pygame.init()
# képernyő hossza
width = 1200
# képernyő magassága
height = 1000
screen_res = (width, height)

pygame.display.set_caption("Pattogó dvd")
screen = pygame.display.set_mode(screen_res)
clock = pygame.time.Clock()
# színek
piros = (255, 0, 0)
fehér = (255, 255, 255)

# labda
# labda = pygame.draw.circle(surface=screen, color=piros, center=[100, 100], radius=40)
dvdkép = pygame.image.load("dvd.png")
dvd = pygame.transform.scale(dvdkép, (150, 80)).convert_alpha()
dvd_rect = dvd.get_rect(midleft=(150, 80))
# milyen gyors
# gyorsaság = [X tengelyen, Y tengelyen]
gyorsaság = [5.3, 6.2]
# game loop
while True:
    # event loop
    for event in pygame.event.get():
        # check if a user wants to exit the game or not
        if event.type == pygame.QUIT:
            exit()

    # háttér kitoltése
    screen.fill(fehér)
    # dvd mozog
    dvd_rect = dvd_rect.move(gyorsaság)
    # mostmár a dvd közepe (101,101)
    # ezen a mentén fog a falunk mozogni
    # ha a dvd kimely a képből jöjjön vissza
    if dvd_rect.left <= 0 or dvd_rect.right >= width:
        gyorsaság[0] = -gyorsaság[0]
    if dvd_rect.top <= 0 or dvd_rect.bottom >= height:
        gyorsaság[1] = -gyorsaság[1]
    screen.blit(dvd, dvd_rect)
    # frissiteni a képernyőt
    pygame.display.update()
    clock.tick(60)
pygame.quit()
