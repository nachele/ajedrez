import pygame
pygame.init()
pantalla = pygame.display.set_mode((800,800))
colores = [(0,255,0),(255,255,255)]
nfilas = 8
ncolumnas = 8
piezas = []
direccionImagen = "piezas/"
variable = 0
seleccionadaIndicie = 0


class Ficha:
    def __init__(self,x,y, imagen,indice,color):
        self.nombre = imagen
        self.indice = indice
        self.color = color
        self.x = x
        self.y = y
        self.dibujo = pygame.image.load(imagen)
        self.seleccionada = False
    def pintar(self):
        pantalla.blit(self.dibujo,(self.x,self.y))
    def mouseOn(self):
        global seleccionadaIndicie
        if posicionRaton()[0] > self.x and posicionRaton()[0] < self.x + 100 and posicionRaton()[1] > self.y and posicionRaton()[1] < self.y + 100 and teclaMouse()[0] == True and seleccionadaIndicie < 2:
            self.seleccionada = True
            seleccionadaIndicie += 1
        elif teclaMouse()[0] == False:
            self.seleccionada = False
            seleccionadaIndicie = 0

    def movimiento(self):
        if self.seleccionada == True:
            self.x = posicionRaton()[0] - 50
            self.y = posicionRaton()[1] - 50

def posicionRaton():
    return pygame.mouse.get_pos()
def teclaMouse():
    return pygame.mouse.get_pressed()






def PintarCuadro():
    #pygame.draw.rect(pantalla, colores[0], (100,100,100,100),0)
    for fila in range (nfilas):
        for columna in range (ncolumnas):

            pygame.draw.rect(pantalla, colores[(columna + fila)%2], (columna * 100, fila * 100, 100,100),0)
            
def crearPiezas():
    #pygame.draw.rect(pantalla, colores[0], (100,100,100,100),0)
    for fila in range (nfilas):
        for columna in range (ncolumnas):
            if fila == 0:
                piezas.append(Ficha(columna * 100, fila, direccionImagen + str(columna) + ".png",columna, "blanca"))
            if fila == 1:
                piezas.append(Ficha(columna * 100, fila * 100, direccionImagen + "8.png", 8 + columna, "blanca"))
            if fila == 6:
                piezas.append(Ficha(columna * 100, fila * 100, direccionImagen + "17.png", 16 + columna, "negra"))
            if fila == 7:
                piezas.append(Ficha(columna * 100, fila * 100, direccionImagen + str(columna + fila + 2) + ".png", 24 + columna,"negra"))
crearPiezas()
def PintarPiezas():
    for pieza in piezas:
        pieza.mouseOn()
        pieza.movimiento()
        pieza.pintar()


            


   
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