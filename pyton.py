import pygame
pygame.init()
pantalla = pygame.display.set_mode((800,800))
colores = [(0,255,0),(255,255,255)]
nfilas = 8
ncolumnas = 8

class Reina:
    def __init__(self, x , y, imagen):
        self.nombre = "reina"
        self.x = x
        self.y = y
        self.dibujo = pygame.image.load(imagen)
        
    def dibujar(self):
        pantalla.blit(self.dibujo,(self.x,self.y))
reina = Reina(100,100,"reinaNegra.jpg")
pieza = []
pieza.append(reina)
def PintarCuadro():
    #pygame.draw.rect(pantalla, colores[0], (100,100,100,100),0)
    for fila in range (nfilas):
        for columna in range (ncolumnas):
            pygame.draw.rect(pantalla, colores[(columna + fila)%2], (columna * 100, fila * 100, 100,100),0)

def PintarPieza():
    #reina = pygame.image.load("reinaNegra.jpg")
    #pantalla.blit(reina,(100,100))
    pieza[0].dibujar()
    



   




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pantalla.fill("white")
    PintarCuadro()
    PintarPieza()
    pygame.display.flip()

pygame.quit()

