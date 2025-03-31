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
                print(direccionImagen)
                piezas.append(Pieza((7 - x) * 100,0, direccionImagen))
                direccionImagen = "piezas/"
                sumando = sumando + 1
                print(x)
def PintarCuadro():
    #pygame.draw.rect(pantalla, colores[0], (100,100,100,100),0)
    for fila in range (nfilas):
        for columna in range (ncolumnas):
            pygame.draw.rect(pantalla, colores[(columna + fila)%2], (columna * 100, fila * 100, 100,100),0)

def PintarPieza():
    for pieza in piezas:
        print(pieza.nombre)
        pieza.dibujar()



   



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pantalla.fill("white")
    PintarCuadro()
    crearPiezas()
    PintarPieza()
    pygame.display.flip()

pygame.quit()

