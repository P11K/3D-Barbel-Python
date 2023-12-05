from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Inisialisasi variabel untuk sudut rotasi
vertikal = 0.0
horizontal = 0.0

def barbel():
    # Bagian atas barbel (silinder hitam)
    glColor3f(0.0, 0.0, 0.0)  # Warna hitam
    glPushMatrix()
    glTranslatef(0, 1, 0)  # Posisi bagian atas barbel
    glRotatef(90, 1, 0, 0)  # Rotasi silinder
    glutSolidCylinder(0.5, 0.2, 50, 50)  # Gambar silinder solid
    glPopMatrix()

    # Silinder kecil di atas (abu-abu tua, diperkecil skala)
    glColor3f(0.48, 0.47, 0.45)  # Warna abu-abu tua
    glPushMatrix()
    glTranslatef(0, 1.1, 0)  # Posisi silinder kecil
    glRotatef(90, 1, 0, 0)  # Rotasi silinder
    glScalef(0.5, 0.5, 0.5)  # Perkecil skala silinder kecil
    glutSolidCylinder(0.5, 0.2, 50, 50)  # Gambar silinder solid
    glPopMatrix()

    # Bagian bawah barbel (silinder hitam)
    glColor3f(0.0, 0.0, 0.0)  # Warna hitam
    glPushMatrix()
    glTranslatef(0, -1, 0)  # Posisi bagian bawah barbel
    glRotatef(90, 1, 0, 0)  # Rotasi silinder
    glutSolidCylinder(0.5, 0.2, 50, 50)  # Gambar silinder solid
    glPopMatrix()

    # Silinder kecil di bawah (abu-abu tua, diperkecil skala)
    glColor3f(0.48, 0.47, 0.45)  # Warna abu-abu tua
    glPushMatrix()
    glTranslatef(0, -1.2, 0)  # Posisi silinder kecil
    glRotatef(90, 1, 0, 0)  # Rotasi silinder
    glScalef(0.5, 0.5, 0.5)  # Perkecil skala silinder kecil
    glutSolidCylinder(0.5, 0.2, 50, 50)  # Gambar silinder solid
    glPopMatrix()

    # Badan barbel (silinder abu-abu muda)
    glColor3f(0.7, 0.7, 0.7)  # Warna abu-abu muda
    glPushMatrix()
    glTranslatef(0, 1, 0)  # Posisi badan barbel
    glScalef(0.5, 1, 0.5)  # Perbesar skala silinder
    glRotatef(90, 1, 0, 0)  # Rotasi silinder
    glutSolidCylinder(0.2, 2, 50, 50)  # Gambar silinder solid
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(2, 2, 5, 0, 0, 0, 0, 1, 0)  # Posisi kamera

    glClearColor(0.2, 0.2, 0.2, 1.0)  # Warna latar belakang (background) abu-abu gelap
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glRotatef(horizontal, 0, 1, 0)  # Rotasi horizontal
    glRotatef(vertikal, 1, 0, 0)    # Rotasi vertikal

    barbel()  # Gambar barbel

    glutSwapBuffers()

def idle():
    global horizontal, vertikal
    horizontal += 0.1  # Increment sudut rotasi horizontal
    vertikal += 0.05    # Increment sudut rotasi vertikal
    glutPostRedisplay()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 10.0)  # Perspektif proyeksi
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b'Barbel 3D')  # Nama window

    glEnable(GL_DEPTH_TEST)  # Aktifkan uji kedalaman (depth test)
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)

    glutMainLoop()

if __name__ == "__main__":
    main()
