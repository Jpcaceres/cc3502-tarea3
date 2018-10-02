from Eje import *
from CC3501Utils import *

import os
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import uniform
from math import *

class Bronzor:
    def __init__(self, pos=Vector(0, 0, 0)):
        self.pos = pos
        self.angulo = pi
        self.lista = 0
        self.crear()

    def crear(self):
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)
        glEnable(GL_COLOR_MATERIAL)

        glBegin(GL_TRIANGLES)
        #Cilindro Grande
        color = [55,120,135]
        Ncolor = [color[0]/255.0,color[1]/255.0,color[2]/255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        cilindro(200,50,Vector(0,0,-25))  # tronco
        glEnd()

        # Cilindro Menos grande
        glBegin(GL_TRIANGLES)
        color = [32, 58, 79]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        cilindro(150, 60, Vector(0,0,-30))
        glEnd()

        #Esferas Exteriore1
        glBegin(GL_TRIANGLES)
        color = [4, 46, 56]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(40, Vector(0, 200, 0))
        glEnd()

        # Esferas Exteriore2
        glBegin(GL_TRIANGLES)
        color = [4, 46, 56]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(40, Vector(0, -200, 0))
        glEnd()

        # Esferas Exteriore3
        glBegin(GL_TRIANGLES)
        color = [4, 46, 56]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(40, Vector(-160, 125, 0))
        glEnd()

        # Esferas Exteriore4
        glBegin(GL_TRIANGLES)
        color = [4, 46, 56]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(40, Vector(-160, -125, 0))
        glEnd()

        # Esferas Exteriore5
        glBegin(GL_TRIANGLES)
        color = [4, 46, 56]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(40, Vector(160, 125, 0))
        glEnd()

        # Esferas Exteriore6
        glBegin(GL_TRIANGLES)
        color = [4, 46, 56]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(40, Vector(160, -125, 0))
        glEnd()

        # Esferas Interior
        glBegin(GL_TRIANGLES)
        color = [55, 120, 135]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(40, Vector(0, 0, 25))
        glEnd()

        # Esferas Interior1
        glBegin(GL_TRIANGLES)
        color = [55, 120, 135]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(20, Vector(65, 80, 20))
        glEnd()

        # Esferas Interio2
        glBegin(GL_TRIANGLES)
        color = [55, 120, 135]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(20, Vector(-65, 80, 20))
        glEnd()

        # Esferas Interior3
        glBegin(GL_TRIANGLES)
        color = [55, 120, 135]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(20, Vector(65, -80, 20))
        glEnd()

        # Esferas Interior4
        glBegin(GL_TRIANGLES)
        color = [55, 120, 135]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(20, Vector(-65, -80, 20))
        glEnd()

        # Ojo der
        glPushMatrix()
        glScalef(1.0, 2.0, 1.0)
        glBegin(GL_TRIANGLES)
        color = [255, 255, 255]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        cilindro(25,10, Vector(100, 0, 25))
        glEnd()
        glPopMatrix()

        # Ojo izq
        glPushMatrix()
        glScalef(1.0, 2.0, 1.0)
        glBegin(GL_TRIANGLES)
        color = [255, 255, 255]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        cilindro(25, 10, Vector(-100, 0, 25))
        glEnd()
        glPopMatrix()

        # Iris der
        glPushMatrix()
        glScalef(0.5, 1.2, 1.0)
        glBegin(GL_TRIANGLES)
        color = [0, 0, 0]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        cilindro(25, 15, Vector(200, 0, 22))
        glEnd()
        glPopMatrix()

        # Iris izq
        glPushMatrix()
        glScalef(0.5, 1.2, 1.0)
        glBegin(GL_TRIANGLES)
        color = [0, 0, 0]
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        cilindro(25, 15, Vector(-200, 0, 22))
        glEnd()
        glPopMatrix()

        glEndList()

    def dibujar(self):

        glPushMatrix()
        glTranslatef(self.pos.x, self.pos.y, self.pos.z)
        glRotatef(self.angulo, 0, 1, 0)  # Rotacion en torno a eje X
        glCallList(self.lista)
        glPopMatrix()
