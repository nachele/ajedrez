import pygame
pygame.init()
pantalla = pygame.display.set_mode((800,800))
colores = [(0,255,0),(255,255,255)]
nfilas = 8
ncolumnas = 8
piezas = []
direccionImagen = "piezas/"


class Ficha:
    def __init__(self,x,y, imagen):
        self.nombre = imagen
        self.x = x
        self.y = y
        self.dibujo = pygame.image.load(imagen)
    def pintar(self):
        pantalla.blit(self.dibujo,(self.x,self.y))
    def mouseOn(self):
        if posicionRaton()[0] > self.x and posicionRaton()[0] < self.x + 100 and posicionRaton()[1] > self.y and posicionRaton()[1] < self.y + 100 and teclaMouse()[0] == True:
            print(self.nombre)

def posicionRaton():
    return pygame.mouse.get_pos()
def teclaMouse():
    return pygame.mouse.get_pressed()






def PintarCuadro():
    #pygame.draw.rect(pantalla, colores[0], (100,100,100,100),0)
    variable = 0
    for fila in range (nfilas):
        for columna in range (ncolumnas):

            pygame.draw.rect(pantalla, colores[(columna + fila)%2], (columna * 100, fila * 100, 100,100),0)
            if fila == 0:
                piezas.append(Ficha(columna * 100, fila, direccionImagen + str(columna) + ".png"))
            if fila == 1:
                piezas.append(Ficha(columna * 100, fila * 100, direccionImagen + "8.png"))
            if fila == 6:
                piezas.append(Ficha(columna * 100, fila * 100, direccionImagen + "17.png"))
            if fila == 7:
                piezas.append(Ficha(columna * 100, fila * 100, direccionImagen + str(columna + fila + 2) + ".png"))

def PintarPiezas():
    for pieza in piezas:
        pieza.pintar()
        pieza.mouseOn()

            


   
pygame.mouse.set_cursor(pygame.cursors.diamond)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pantalla.fill("white")

    PintarCuadro()
    PintarPiezas()
    

    pygame.display.flip()

pygame.quit()