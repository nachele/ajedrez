import pygame
pygame.init()
pantalla = pygame.display.set_mode((800,800))
colores = [(0,255,0),(255,255,255)]
nfilas = 8
ncolumnas = 8
sumando = 0
class Pieza:
    def __init__(self, x , y, imagen):
        self.nombre = imagen
        self.x = x
        self.y = y
        self.dibujo = pygame.image.load(imagen)
        
    def dibujar(self):
        posicionRaton = pygame.mouse.get_pos()
        if posicionRaton[0] > self.x and posicionRaton[0] < self.x + 100 and posicionRaton[1] > self.y and posicionRaton[1] < self.y + 100:
            print(self.nombre)
        pantalla.blit(self.dibujo,(self.x,self.y))

indiceDecrece = [2,1,0]        

piezas = []

direccionImagen = "piezas/"
def crearPiezas():
    global direccionImagen
    for i in range(5):
        #crear hasta el rey
        direccionImagen += str(i) + ".png"
        piezas.append(Pieza(i * 100,0,direccionImagen))
        direccionImagen = "piezas/"
        if i == 4:
            for x in indiceDecrece:
                global sumando
                direccionImagen += str(x) + ".png"
                piezas.append(Pieza((7 - x) * 100,0, direccionImagen))
                direccionImagen = "piezas/"
                sumando = sumando + 1
                
    for i in range (8):
        piezas.append(Pieza(i * 100, 100, direccionImagen + "5.png"))
    direccionImagen = "piezas/"
indiceNegras = [7,8,9,10,11]
indiceNegrasDecrece = [9,8,7]
variableNegras = 5
variableNegras1 = 0
def crearPiezasNegras():
    global variableNegras1
    global direccionImagen
    global indiceNegrasDecrece
    for i in indiceNegras:
        direccionImagen += str(i) + ".png"
        piezas.append(Pieza(variableNegras1 * 100,700,direccionImagen))
        direccionImagen = "piezas/"
        variableNegras1 += 1
        if i == 11:
            for x in indiceNegrasDecrece:
                global variableNegras
                
                direccionImagen += str(x) + ".png"
                piezas.append(Pieza(variableNegras * 100, 700, direccionImagen))
                variableNegras += 1
                direccionImagen = "piezas/"
    for i in range (8):
        piezas.append(Pieza(i * 100, 600, direccionImagen + "6.png"))
        direccionImagen = "piezas/"
def PintarCuadro():
    #pygame.draw.rect(pantalla, colores[0], (100,100,100,100),0)
    for fila in range (nfilas):
        for columna in range (ncolumnas):
            pygame.draw.rect(pantalla, colores[(columna + fila)%2], (columna * 100, fila * 100, 100,100),0)


def PintarPieza():
    for pieza in piezas:
        pieza.dibujar()



   
pygame.mouse.set_cursor(pygame.cursors.diamond)
crearPiezas()
crearPiezasNegras()

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

