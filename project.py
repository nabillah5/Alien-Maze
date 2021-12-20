from math import trunc
from os import stat
import OpenGL.GL
import OpenGL.GLUT 
import OpenGL.GLU
import alien

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

posisi_alien=[-480,-250]
speed=20
gerakAtas=True
gerakBawah=True
gerakKiri=True
gerakKanan=True

state='Level 1'

# Fungsi menggunakan objek kotak
def bentuk():

    glBegin(GL_QUADS)
    glColor3ub(138, 50, 0)
    glVertex2f(-600, 400) 
    glVertex2f(-600, 350)
    glVertex2f(600, 350) 
    glVertex2f(600, 400) 
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3ub(138, 50, 0)
    glVertex2f(-600, -400) 
    glVertex2f(-600, -350)
    glVertex2f(600, -350) 
    glVertex2f(600, -400) 
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(138, 50, 0)
    glVertex2f(600, 100) 
    glVertex2f(550, 100)
    glVertex2f(550, -400) 
    glVertex2f(600, -400) 
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(138, 50, 0)
    glVertex2f(-600, 400) 
    glVertex2f(-550, 400)
    glVertex2f(-550, -100) 
    glVertex2f(-600, -100) 
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(138, 50, 0)
    glVertex2f(-400, 100) 
    glVertex2f(-350, 100)
    glVertex2f(-350, -400) 
    glVertex2f(-400, -400) 
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(138, 50, 0)
    glVertex2f(400, 400) 
    glVertex2f(350, 400)
    glVertex2f(350, -200) 
    glVertex2f(400, -200) 
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(138, 50, 0)
    glVertex2f(-400, 100) 
    glVertex2f(-400, 50)
    glVertex2f(-80, 50) 
    glVertex2f(-80, 100) 
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(138, 50, 0)
    glVertex2f(-200, -200) 
    glVertex2f(-200, -150)
    glVertex2f(400, -150) 
    glVertex2f(400, -200) 
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(138, 50, 0)
    glVertex2f(150, 400) 
    glVertex2f(100, 400)
    glVertex2f(100, 50) 
    glVertex2f(150, 50) 
    glEnd()     

# Fungsi untuk mengkonfigurasi tulisan yang berada pada akhir stage atau tiap level
def finish(atas,bawah,kiri,kanan):
    global state
    if ((posisi_alien[0]<=kanan and posisi_alien[0] >=kiri) and (posisi_alien[1] <=atas and posisi_alien[1] >=bawah)):
        state='Winner'

# Fungsi Iterasi    
def iterate():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1200/2,1200/2,-800/2,800/2)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

#Fungsi untuk mengatur colision supaya tembok tidak ditembus
def colisionfull(atas,bawah,kiri,kanan):
    global gerakKanan
    global gerakKiri
    global gerakBawah
    global gerakAtas
    if (posisi_alien[0] + 50 <=kanan and posisi_alien[0]+50 >=kiri) and (posisi_alien[1] <=atas and posisi_alien[1] >=bawah):
        gerakKanan=False
    elif (posisi_alien[1] - 50 <=atas and posisi_alien[1] - 50 >=bawah) and (posisi_alien[0] <=kanan and posisi_alien[0] >=kiri):
        gerakBawah=False
    elif (posisi_alien[0] - 50 <=kanan and posisi_alien[0]-50 >=kiri) and (posisi_alien[1] <=atas and posisi_alien[1] >=bawah):
        gerakKiri=False
    elif (posisi_alien[1] + 50 <=atas and posisi_alien[1] + 50 >=bawah) and (posisi_alien[0] <=kanan and posisi_alien[0] >=kiri):
        gerakAtas=False

#Fungsi mengkonfigurasi Tulisan
def drawText(text,x,y, R, G, B): 
    glPushMatrix()
    glColor3ub(R, G, B)
    glRasterPos2i(x, y)
    for i in str(text):
        c = ord(i)
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, c)
    glPopMatrix()

# Fungsi memunculkan suatu object di sebuah layar 
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Untuk membersihkan layar
    glLoadIdentity() # Untuk mereset semua posisi grafik/bentuk
    iterate() # Fungsi lopping
    if state=='Level 1':
        alien.gabung(posisi_alien[0],posisi_alien[1])
        bentuk()
         
    elif state=='Winner':
        drawText('W I N N E R !!',-50,200,26, 255, 0)
        drawText('Click Next to Level 2',-50,-200,60, 50, 240)
        drawText('Next',400,-300,60, 50, 240)
        drawText('Menu',-400,-300,60, 50, 240)
        print('Menang')
    
    glutSwapBuffers() # Untuk membersihkan layar

# Mengatur mengontrol Gerakan    
def controller(key,x,y): 
    global gerakKanan
    global gerakKiri
    global gerakBawah
    global gerakAtas
    if key==GLUT_KEY_UP and gerakAtas:
        if gerakBawah==False:
            gerakBawah=True
        posisi_alien[1]+=speed
    if key==GLUT_KEY_DOWN and gerakBawah:
        if gerakAtas==False:
            gerakAtas=True
        posisi_alien[1]-=speed
    if key==GLUT_KEY_LEFT and gerakKiri:
        if gerakKanan==False:
            gerakKanan=True
        posisi_alien[0]-=speed
    if key==GLUT_KEY_RIGHT and gerakKanan:
        if gerakKiri==False:
            gerakKiri=True
        posisi_alien[0]+=speed

# Inisialisasi
glutInit() # inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) # Untuk mengatur layar menjadi berwarna
glutInitWindowSize(1200, 800)  # Untuk mengatur ukuran layar/window
glutInitWindowPosition(0, 0) # Untuk mengatur posisi window
wind = glutCreateWindow("Project Akhir = Level 1") # Memberi nama pada window
glutDisplayFunc(showScreen) # Untuk menampilkan objek pada layar, fungsi callback
glutSpecialFunc(controller) # Untuk mengaktifkan Kontrol
glutIdleFunc(showScreen) # Untuk menyuruh OpenGL untuk selalu membuka dan menampilkan objek
glutMainLoop() # Untuk memulai segalanya, untuk me-looping Objek
