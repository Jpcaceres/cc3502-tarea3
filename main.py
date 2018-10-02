# coding=utf-8
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Eje import *
from CC3501Utils import *
from Bronzor import *
###########################################################################
#INICIALIZACION PYGAME Y OPENGL
###########################################################################


def init(ancho, alto, titulo, color_fondo=[0, 0, 0, 0], far=15000, near=1):
    """
    Función extraida del archivo Aux_3D disponible en ucursos
    :param ancho: Ancho del viewport
    :param alto: Alto del viewport
    :param titulo: Titulo del viewport
    :param color_fondo: Color de Fondo del Viewport
    :param far: Distancia al fondo de la proyeccion
    :param near: Distancia de la proyeccion
    :return: None
    """
    # init pygame
    pygame.init()
    pygame.display.set_mode((ancho, alto), OPENGL | DOUBLEBUF)
    pygame.display.set_caption(titulo)

    # init opengl
    if alto == 0:
        alto = 1
    glViewport(0, 0, ancho, alto)
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    # establecer tipo de proyeccion: perspectiva
    gluPerspective(45, float(ancho) / float(alto), near, far)

    glMatrixMode(GL_MODELVIEW)
    # enable gl

    glClearColor(color_fondo[0], color_fondo[1], color_fondo[2], color_fondo[3])  # setea el color de fondo
    glClearDepth(1.0)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glEnable(GL_BLEND)  # habilitar transparencias
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_DEPTH_TEST)  # habilita comparacion por profundidad en Z-buffer
    glDepthFunc(GL_LEQUAL)   # Se compara profundidad con menor o igual
    # Las normales se modifican al efectuar transfomaciones,
    # dicho efecto puede ser evitado con GL_RESCALE_NORMAL
    # o GL_NORMALIZE
    glEnable(GL_RESCALE_NORMAL)
    glEnable(GL_LIGHTING)  # luz
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # rellenar las caras de los poligonos
    # descomentar estas lineas para no renderizar las caras traseras de los poligonos
    # glEnable(GL_CULL_FACE)
    # glCullFace(GL_BACK)
    return

#####################################################################
#####################################################################
def main():
    # inicializar
    ancho = 800
    alto = 600
    init(ancho, alto, "Bronzor OpenGL")

    # crear objetos
    clock = pygame.time.Clock()

    # camara
    camPos = Vector(400, 400, 300)  # posicion de la camara
    camAt = Vector(100, 100, 50)  # posicion que se enfoca

    # luz
    light = GL_LIGHT0
    l_position = Vector(1000.0, 100.0, 500.0)

    # luz
    light = GL_LIGHT0
    l_position = Vector(1000.0, 100.0, 500.0)

    # crear una luz coherente con su color base
    l_diffuse = [1.0, 1.0, 1.0, 1.0]
    l_ambient = [0.2, 0.2, 0.2, 1]
    l_specular = [1.0, 1.0, 1.0, 1.0]

    # otros valores estandar
    l_constant_attenuation = 1.5
    l_linear_attenuation = 0.5
    l_quadratic_attenuation = 0.2

    l_spot_cutoff = 60.0
    l_spot_direction = Vector(-1.0, -1.0, 0.0)  # direccion de rebote de luz
    l_spot_exponent = 2.0

    eje = Eje(400.0)  # R,G,B = X,Y,Z
    B=Bronzor()
    # variables de tiempo
    fps = 30
    dt = 1.0 / fps

    run = True
    while run:
        # manejo de eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        # obtener teclas presionadas
        pressed = pygame.key.get_pressed()

        if pressed[K_UP]:
            camPos = sumar(ponderar(10, normalizar(camAt)), camPos)
        if pressed[K_DOWN]:
            camPos = sumar(ponderar(-10, normalizar(camAt)), camPos)
        if pressed[K_RIGHT]:
            camPos = sumar(ponderar(-10, rotarFi(normalizar(camAt), 90)), camPos)
        if pressed[K_LEFT]:
            camPos = sumar(ponderar(10, rotarFi(normalizar(camAt), 90)), camPos)

        if pressed[K_w]:
            camAt = sumar(Vector(0, 0, 100), camAt)
        if pressed[K_s]:
            camAt = sumar(Vector(0, 0, -100), camAt)
        if pressed[K_d]:
            camAt = rotarFi(camAt, 0.01)
        if pressed[K_a]:
            camAt = rotarFi(camAt, -0.01)

        # Limpiar buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        B.dibujar()
        eje.dibujar()

        # camara
        glLoadIdentity()
        gluLookAt(camPos.x, camPos.y, camPos.z,  # posicion
                  camAt.x, camAt.y, camAt.z,  # mirando hacia
                  0.0, 0.0, 1.0)  # inclinacion

        # luz
        glLightfv(light, GL_POSITION, l_position.cartesianas())
        glLightfv(light, GL_AMBIENT, l_ambient)
        glLightfv(light, GL_SPECULAR, l_specular)
        glLightfv(light, GL_DIFFUSE, l_diffuse)
        glLightf(light, GL_CONSTANT_ATTENUATION, l_constant_attenuation)
        glLightf(light, GL_LINEAR_ATTENUATION, l_linear_attenuation)
        glLightf(light, GL_QUADRATIC_ATTENUATION, l_quadratic_attenuation)
        glLightf(light, GL_SPOT_CUTOFF, l_spot_cutoff)
        glLightfv(light, GL_SPOT_DIRECTION, l_spot_direction.cartesianas())
        glLightf(light, GL_SPOT_EXPONENT, l_spot_exponent)

        glEnable(light)

        pygame.display.flip()  # cambiar imagen
        clock.tick(fps)  # esperar 1/fps segundos

    pygame.quit()
    return


main()
