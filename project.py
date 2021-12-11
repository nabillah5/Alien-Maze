import OpenGL.GL
import OpenGL.GLUT 
import OpenGL.GLU
import alien

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500

posisi_alien=[-480,-250]
speed=12
gerakAtas=True
gerakBawah=True
gerakKiri=True
gerakKanan=True

# Fungsi objek kotak
def bentuk():

    glBegin(GL_QUADS) 
    glColor3ub(0, 204, 0)
    glVertex2f(-600, 400) 
    glVertex2f(-600, 350)
    glVertex2f(600, 350) 
    glVertex2f(600, 400) 
    glEnd()
    
    glBegin(GL_QUADS) 
    glColor3ub(0, 204, 0)
    glVertex2f(-600, -400) 
    glVertex2f(-600, -350)
    glVertex2f(600, -350) 
    glVertex2f(600, -400) 
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(0, 204, 0)
    glVertex2f(600, 100) 
    glVertex2f(550, 100)
    glVertex2f(550, -400) 
    glVertex2f(600, -400) 
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(0, 204, 0)
    glVertex2f(-600, 400) 
    glVertex2f(-550, 400)
    glVertex2f(-550, -100) 
    glVertex2f(-600, -100) 
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(0, 204, 0)
    glVertex2f(-400, 100) 
    glVertex2f(-350, 100)
    glVertex2f(-350, -400) 
    glVertex2f(-400, -400) 
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(0, 204, 0)
    glVertex2f(-400, 100) 
    glVertex2f(-350, 100)
    glVertex2f(-350, -400) 
    glVertex2f(-400, -400) 
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(0, 204, 0)
    glVertex2f(400, 400) 
    glVertex2f(350, 400)
    glVertex2f(350, -200) 
    glVertex2f(400, -200) 
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(0, 204, 0)
    glVertex2f(-400, 100) 
    glVertex2f(-400, 50)
    glVertex2f(-80, 50) 
    glVertex2f(-80, 100) 
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(0, 204, 0)
    glVertex2f(-200, -200) 
    glVertex2f(-200, -150)
    glVertex2f(400, -150) 
    glVertex2f(400, -200) 
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(0, 204, 0)
    glVertex2f(150, 400) 
    glVertex2f(100, 400)
    glVertex2f(100, 50) 
    glVertex2f(150, 50) 
    glEnd()                         
# Fungsi Iterasi    
def iterate():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1200/2,1200/2,-800/2,800/2)
    # gluOrtho2D(0,1200,0,800)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

# Fungsi Membersihkan layar
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Untuk membersihkan layar
    glLoadIdentity() # Untuk mereset semua posisi grafik/bentuk
    iterate() # Fungsi lopping
    alien.gabung(posisi_alien[0],posisi_alien[1])
    bentuk() # Memanggil fungsi kotak
    glutSwapBuffers() # Untuk membersihkan layar

def controller(key,x,y):
    if key==GLUT_KEY_UP and gerakAtas:
        posisi_alien[1]+=speed
        print("atas")
    if key==GLUT_KEY_DOWN and gerakBawah:
        posisi_alien[1]-=speed
        print("bawah")
    if key==GLUT_KEY_LEFT and gerakKiri:
        posisi_alien[0]-=speed
        print("kiri")
    if key==GLUT_KEY_RIGHT and gerakKanan:
        posisi_alien[0]+=speed
        print("kanan")

# Inisialisasi
glutInit() # inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) # Untuk mengatur layar menjadi berwarna
glutInitWindowSize(1200, 800)  # Untuk mengatur ukuran layar/window
glutInitWindowPosition(0, 0) # Untuk mengatur posisi window
wind = glutCreateWindow("Project Akhir") # Memberi nama pada window
glutDisplayFunc(showScreen) # Untuk menampilkan objek pada layar, fungsi callback
glutSpecialFunc(controller)
glutIdleFunc(showScreen) # Untuk menyuruh OpenGL untuk selalu membuka dan menampilkan objek
glutMainLoop() # Untuk memulai segalanya, untuk me-looping Objek
