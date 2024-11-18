import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

ID_DRAW_SUSHI = 1
ID_DRAW_SARA = 2

orbitAngle = 0

rotateAngle=0

def display():
    glClearColor(1., 1., 1., 1.,)
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glPushMatrix()
    glRotated(orbitAngle, 0, 0, 1)

    glPushMatrix()
    glColor3d(0.941, 0.878, 0.745)
    glTranslated(0.5, 0, 0)
    glRotated(0, 0, 0, 1)
    glCallList(ID_DRAW_SUSHI)
    glPopMatrix()
    glPushMatrix()
    glColor3d(0.941, 0.878, 0.745)
    glRotated(0, 0, 0, 1)
    glTranslated(0.65, 0, 0)
    glCallList(ID_DRAW_SUSHI)
    glPopMatrix()

    glPushMatrix()
    glColor3d(1.0, 0.502, 0.4)
    glTranslated(-0.15, -0.5, 0)
    glRotated(0, 0, 0, 1)
    glCallList(ID_DRAW_SUSHI)
    glPopMatrix()
    glPushMatrix()
    glColor3d(1.0, 0.502, 0.4)
    glRotated(0, 0, 0, 1)
    glTranslated(0., -0.5, 0)
    glCallList(ID_DRAW_SUSHI)
    glPopMatrix()

    glPushMatrix()
    glColor3d(1, 0.271, 0.075)
    glRotated(0, 0, 0, 1)
    glTranslated(-0.15, 0.65, 0)
    glCallList(ID_DRAW_SUSHI)
    glPopMatrix()
    glPushMatrix()
    glColor3d(1, 0.271, 0.075)
    glRotated(0, 0, 0, 1)
    glTranslated(0., 0.65, 0)
    glCallList(ID_DRAW_SUSHI)
    glPopMatrix()

    glPushMatrix()
    glColor3d(1.0, 0.714, 0.757)
    glRotated(0, 0, 0, 1)
    glTranslated(-0.75, 0.15, 0)
    glCallList(ID_DRAW_SUSHI)
    glPopMatrix()
    glPushMatrix()
    glColor3d(1.0, 0.714, 0.757)
    glRotated(0, 0, 0, 1)
    glTranslated(-0.6, 0.15, 0)
    glCallList(ID_DRAW_SUSHI)
    glPopMatrix()

    glPushMatrix()
    glColor(0., 0, 0.)
    glTranslated(0.7, -0.125, 0)
    glCallList(ID_DRAW_SARA)
    glPopMatrix()

    glPushMatrix()
    glColor(0., 0, 0.)
    glTranslated(-0.55, 0.05, 0)
    glCallList(ID_DRAW_SARA)
    glPopMatrix()

    glPushMatrix()
    glColor(0., 0, 0.)
    glTranslated(0.05, -0.6, 0)
    glCallList(ID_DRAW_SARA)
    glPopMatrix()

    glPushMatrix()
    glColor(0., 0, 0.)
    glTranslated(0.05, 0.55, 0)
    glCallList(ID_DRAW_SARA)
    glPopMatrix()
   

    glPopMatrix()
    glutSwapBuffers()

def timer(value):
    global orbitAngle
    orbitAngle+=2
    glutPostRedisplay()
    glutTimerFunc(100, timer, 0)

def buildDisplayList():
    glNewList(ID_DRAW_SUSHI,GL_COMPILE)

    glBegin(GL_QUADS)
    glVertex3d(0,0,0)
    glVertex3d(0.125,-0.25,0)
    glVertex3d(0.25,-0.25,0)
    glVertex3d(0.125,0,0)

    glEnd()
    glEndList()

    glNewList(ID_DRAW_SARA,GL_COMPILE)

    glBegin(GL_LINE_LOOP)
    for i in range(360):
        x = math.cos(i * 3.14159 / 180.)
        y = math.sin(i * 3.14159 / 180.)
        glVertex2d(x*0.3, y*0.3)
    glEnd()
    glEndList()
    
if __name__ == "__main__":
    glutInit(sys.argv) #ライブラリの初期化
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(400, 400) #ウィンドウサイズを指定
    glutCreateWindow(sys.argv[0]) #ウィンドウを作成
    timer(0)
    glutDisplayFunc(display) #表示関数を指定
    buildDisplayList()
    glutMainLoop() #イベント待ち