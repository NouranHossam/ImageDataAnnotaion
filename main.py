
import numpy as np
import cv2
import os
import sys
import csv
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi


#showing a Splash Screen
class Splashscreen (QSplashScreen):
    def __init__(self ):
        super(QSplashScreen,self).__init__()
        loadUi("Splash.ui",self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        pixmap=QPixmap("background")
        pixmap_resized = pixmap.scaled(720, 405, Qt.KeepAspectRatio)
        self.setPixmap(pixmap_resized)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
    def progress(self):
        for i in range(100):
            time.sleep(0.1)
            self.progressBar.setValue(i)


class Template(QWidget):
    #TypePaint is for changing category with if and else
    typePaint=0
    def __init__(self):
        super().__init__()
        grid = QGridLayout(self)
        self.title ="Image Data Annotation Tool"
        self.setWindowTitle(self.title)
        
        
#Buttons alignment and Fucntions

#PervImage Button
        PervImage_btn= QPushButton('')
        grid.addWidget(PervImage_btn,10,0,Qt.AlignLeft)
        PervImage_btn.setFont(QFont('Times', 15))
        PervImage_btn.setIcon(QIcon('icons/previous.png'))
        PervImage_btn.setStyleSheet("background-color : White")
        PervImage_btn.setIconSize(QSize(20, 20))
        PervImage_btn.clicked.connect(self.prevImage)


# Next Image Button
        NextImage_btn= QPushButton('')
        grid.addWidget(NextImage_btn,10,50,Qt.AlignRight)
        NextImage_btn.clicked.connect(self.nextImage)
        NextImage_btn.setFont(QFont('Times', 15))
        NextImage_btn.setIcon(QIcon('icons/forward-button.png'))
        NextImage_btn.setIconSize(QSize(20, 20))
        NextImage_btn.setStyleSheet("background-color : White")
        
        

# Browse Button
        Browse_btn= QPushButton('')
        grid.addWidget(Browse_btn,0,0,Qt.AlignLeft)
        Browse_btn.setFixedSize(40,40)
        Browse_btn.clicked.connect(self.open_image)
        Browse_btn.setIcon(QIcon('icons/camera.png'))
        Browse_btn.setStyleSheet("background-color : White")
        Browse_btn.setIconSize(QSize(30, 30))
        Browse_btn.setToolTip("Add Image")
       

# Save Button
        Save_btn= QPushButton('')
        grid.addWidget(Save_btn, 0,50, Qt.AlignRight)
        Save_btn.setFixedSize(40,40)
        Save_btn.clicked.connect(self.exportCSV)
        Save_btn.setIcon(QIcon('icons/floppy-disk.png'))
        Save_btn.setStyleSheet("background-color : White")
        Save_btn.setIconSize(QSize(30, 30))
        Save_btn.setToolTip("Save")
        

# Clear Button
        clean_btn= QPushButton('')
        grid.addWidget(clean_btn, 7,0, Qt.AlignLeft)
        clean_btn.setFixedSize(40,40)
        clean_btn.clicked.connect(self.Clean)
        clean_btn.setIcon(QIcon('icons/eraser.png'))
        clean_btn.setStyleSheet("background-color : White")
        clean_btn.setIconSize(QSize(30, 30))
        clean_btn.setToolTip("Clear")
        

# Draw Human
        DrawHuman_btn= QPushButton('')
        grid.addWidget(DrawHuman_btn, 1, 0, Qt.AlignLeft)
        DrawHuman_btn.setFixedSize(40, 40)
        DrawHuman_btn.setStyleSheet("background-color: White; color: gray;")
        DrawHuman_btn.clicked.connect(self.StartDrawHuman)
        DrawHuman_btn.setFont(QFont('Times', 15))
        DrawHuman_btn.setIcon(QIcon('icons/man.png'))
        DrawHuman_btn.setIconSize(QSize(30, 30))
        DrawHuman_btn.setToolTip("Human")
        

# Draw Car
        DrawCar_btn= QPushButton('')
        grid.addWidget( DrawCar_btn, 2, 0, Qt.AlignLeft)
        DrawCar_btn.setFixedSize(40, 40)
        DrawCar_btn.setStyleSheet("background-color: White; color: gray;")
        DrawCar_btn.clicked.connect(self.StartDrawCar)
        DrawCar_btn.setFont(QFont('Times', 15))
        DrawCar_btn.setIcon(QIcon('icons/sport-car.png'))
        DrawCar_btn.setIconSize(QSize(30, 30))
        DrawCar_btn.setToolTip("Car")
        

# Draw Dog
        DrawDog_btn= QPushButton('')
        grid.addWidget(DrawDog_btn, 3,0, Qt.AlignLeft)
        DrawDog_btn.setFixedSize(40,40)
        DrawDog_btn.setStyleSheet("background-color: White; color: gray;")
        DrawDog_btn.clicked.connect(self.StartDrawDog)
        DrawDog_btn.setFont(QFont('Times', 15))
        DrawDog_btn.setIcon(QIcon('icons/dog.png'))
        DrawDog_btn.setIconSize(QSize(30, 30))
        DrawDog_btn.setToolTip("Dog")

# Draw Cat 
        DrawCat_btn= QPushButton('')
        grid.addWidget(DrawCat_btn, 4, 0, Qt.AlignLeft)
        DrawCat_btn.setFixedSize(40,40)
        DrawCat_btn.setStyleSheet("background-color: White; color: gray;")
        DrawCat_btn.clicked.connect(self.StartDrawCat)
        DrawCat_btn.setFont(QFont('Times', 15))
        DrawCat_btn.setIcon(QIcon('icons/black-cat.png'))
        DrawCat_btn.setIconSize(QSize(30, 30))
        DrawCat_btn.setToolTip("Cat")
        

# Draw Unknown
        DrawUnknown_btn= QPushButton('☐')
        grid.addWidget(DrawUnknown_btn,5, 0, Qt.AlignLeft)
        DrawUnknown_btn.setFixedSize(40, 40)
        DrawUnknown_btn.setStyleSheet("background-color: White; color: gray;")
        DrawUnknown_btn.clicked.connect(self.StartDrawUnknown)
        DrawUnknown_btn.setFont(QFont('Times', 15))
        #DrawUnknown_btn.setIcon(QIcon('icons/eraser.png'))
        DrawUnknown_btn.setIconSize(QSize(30, 30))
        DrawUnknown_btn.setToolTip("Other")

 # Add a button for object detection
        detect_btn = QPushButton('')
        grid.addWidget(detect_btn,6, 0, Qt.AlignLeft)
        detect_btn.setFixedSize(40, 40)
        detect_btn.setStyleSheet("background-color : White")
        detect_btn.clicked.connect(self.detectObjects)
        detect_btn.setIcon(QIcon('icons/artificial-intelligence.png'))
        detect_btn.setIconSize(QSize(30, 30))
        detect_btn.setToolTip("Car Detection")

        verticalSpacer = QSpacerItem(40, 20,  QSizePolicy.Minimum, QSizePolicy.Expanding)
        grid.addItem(verticalSpacer, 6, 0, Qt.AlignTop)
        

    #Buttons  Layouts and widgets and Alignments with their coonection to functions

        #for saving all the images path into one list 
        self.fname=''

        #for going back and forth into the images path list
        self.current=0

        #building a empty pixmap  to show picture  
        self.pix = QPixmap('')

        #making two variable for start and ending postion to draw rectangle 
        self.begin, self.destination = QPoint(), QPoint()

        #two list for saving coordinants of selected rectangle
        self.mouse_press_list = []
        self.mouse_release_list = []

        #for showing the form in a solid place(center) in solid size

        self.resize(1280, 720)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        
    #functions for swaping between every category       
    def StartDrawHuman(self):
        self.typePaint=1
    def StartDrawCar(self):
        self.typePaint=2
    def StartDrawDog(self):
        self.typePaint=3    
    def StartDrawCat(self):
        self.typePaint=4    
    def StartDrawUnknown(self):
        self.typePaint=0    
    

    

   # getting all the images path and put them into the list and show the first picture  
    def open_image(self, filename=None):
        self.fname = QFileDialog.getOpenFileNames(self, 'Open file',os.getcwd(), "Image files (*.jpg *.gif *.jpeg *.png )")
        try: 
            imagePath=self.fname[0][0]
            print("first image Path  = {}".format(imagePath))
            print("list of image fname = {}".format(self.fname))
            print("type imagePath{}".format(type(imagePath)))
            print("type fname {}".format(type(self.fname)))
            pixmap = QPixmap(imagePath)
            pixmap= pixmap.scaled(1280, 720)
            self.pix=QPixmap(pixmap)
            self.pix.scaled(1280, 720)
            self.showMaximized()
            self.resize(1280, 720)
            self.resize(1281, 721)
            centerPoint = QDesktopWidget().availableGeometry().center()
            qtRectangle = self.frameGeometry()
            qtRectangle.moveCenter(centerPoint)
            self.move(qtRectangle.topLeft())
            self.mouse_press_list.clear()
            self.mouse_release_list.clear()  

           
        except IndexError as e:
            print(e)


    #opening the next image    
    def nextImage(self):
        try:
            if self.current >= len(self.fname[0]) - 1 :
                print('End of Next')

            else:
                
                self.current+=1
                imagePath = self.fname[0][self.current]
                pixmap = QPixmap(imagePath)
                pixmap= pixmap.scaled(1280, 720)
                self.pix=QPixmap(pixmap)
                self.pix.scaled(1280, 720)
                #self.showMaximized()
                self.resize(1280, 720)
                self.resize(1281, 721)
                centerPoint = QDesktopWidget().availableGeometry().center()
                qtRectangle = self.frameGeometry()
                qtRectangle.moveCenter(centerPoint)
                self.move(qtRectangle.topLeft())
                print(self.fname[0][self.current])
                self.mouse_press_list.clear()
                self.mouse_release_list.clear()  

        except IndexError as e:
            print(e)    
    #opening the pervious  image 
    def prevImage(self):
        if self.current > 0 :
            
            self.current -= 1 
            imagePath = self.fname[0][self.current]
            pixmap = QPixmap(imagePath)
            pixmap= pixmap.scaled(1280, 720)
            self.pix=QPixmap(pixmap)
            self.pix.scaled(1280, 720)
            #self.showMaximized()
            self.resize(1280, 720)
            self.resize(1281, 721)
            centerPoint = QDesktopWidget().availableGeometry().center()
            qtRectangle = self.frameGeometry()
            qtRectangle.moveCenter(centerPoint)
            self.move(qtRectangle.topLeft())
            print(self.fname[0][self.current])
            self.mouse_press_list.clear()
            self.mouse_release_list.clear()    

        else:
            print('End of Prev  ')


    #Clean the images
    def Clean(self) :
     try: 
       self.mouse_press_list.clear()
       self.mouse_release_list.clear()   
       imagePath1= self.fname[0][self.current]
       pixmap = QPixmap(imagePath1)
       pixmap= pixmap.scaled(1280, 720)
       self.pix=QPixmap(pixmap)
       self.pix.scaled(1280, 720)
       self.resize(1280, 720)
       self.resize(1281, 721)
       centerPoint = QDesktopWidget().availableGeometry().center()
       qtRectangle = self.frameGeometry()
       qtRectangle.moveCenter(centerPoint)
       self.move(qtRectangle.topLeft())
       print(self.fname[0][self.current])
     except IndexError as e:
            print(e)  
    

    #paint start for rectangle        
    def paintEvent(self, event):
      
     if(self.typePaint==1):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.pix)
        painter.setPen(QPen(Qt.magenta, 5))
        if not self.begin.isNull() and not self.destination.isNull():
             rect = QRect(self.begin, self.destination)
             painter.drawRect(rect.normalized())
     elif(self.typePaint==2):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.pix)
        painter.setPen(QPen(Qt.cyan, 5))
        if not self.begin.isNull() and not self.destination.isNull():
             rect = QRect(self.begin, self.destination)
             painter.drawRect(rect.normalized())
     elif(self.typePaint==3):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.pix)
        painter.setPen(QPen(Qt.blue, 5))
        if not self.begin.isNull() and not self.destination.isNull():
             rect = QRect(self.begin, self.destination)
             painter.drawRect(rect.normalized())
     elif(self.typePaint==4):
         painter = QPainter(self)
         painter.drawPixmap(QPoint(), self.pix)
         painter.setPen(QPen(Qt.red, 5))
         if not self.begin.isNull() and not self.destination.isNull():
             rect = QRect(self.begin, self.destination)
             painter.drawRect(rect.normalized())
     else:
         painter = QPainter(self)
         painter.drawPixmap(QPoint(), self.pix)
         painter.setPen(QPen(Qt.gray, 5))
         if not self.begin.isNull() and not self.destination.isNull():
             rect = QRect(self.begin, self.destination)
             painter.drawRect(rect.normalized())

    
    def detectObjects(self):
        # Load the image to detect objects in
        imagePath = self.fname[0][self.current]
        image = cv2.imread(imagePath)
        
        # Load the Haar cascade classifier
        cascade_path = "haarcascade_car.xml"
        cascade = cv2.CascadeClassifier(cascade_path)

        # Convert the image to grayscale and detect objects using the cascade
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles around the detected objects on the image
        #self.object_coords = []
        for (x, y, w, h) in objects:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #self.object_coords.append((x, y, x + w, y + h))

        # Display the image in the application window
        qimage = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(qimage)
        self.pix = pixmap
        self.update()

    
        
        
        
    
    
    #create function to mouse press
    def mousePressEvent(self, event):
      
        if event.buttons() & Qt.LeftButton:
         if(self.typePaint==1):
             self.begin = event.pos()
             self.destination = self.begin
             self.update()
             mouse_press= 'Human Start coords: ( %d : %d )' % (event.x(), event.y())
             print (mouse_press)
             self.mouse_press_list.append(mouse_press)     
         elif(self.typePaint==2):
          #if event.buttons() & Qt.LeftButton:
             self.begin = event.pos()
             self.destination = self.begin
             self.update()
             mouse_press= 'Car Start coords: ( %d : %d )' % (event.x(), event.y())
             print (mouse_press)
             self.mouse_press_list.append(mouse_press)     
         elif(self.typePaint==3):
          #if event.buttons() & Qt.LeftButton:
             self.begin = event.pos()
             self.destination = self.begin
             self.update()
             mouse_press= 'Dog Start coords: ( %d : %d )' % (event.x(), event.y())
             print (mouse_press)
             self.mouse_press_list.append(mouse_press)
         elif(self.typePaint==4):
          #if event.buttons() & Qt.LeftButton:
             self.begin = event.pos()
             self.destination = self.begin
             self.update()
             mouse_press= 'Cat Start coords: ( %d : %d )' % (event.x(), event.y())
             print (mouse_press)
             self.mouse_press_list.append(mouse_press)            
         else:
          #if event.buttons() & Qt.LeftButton:
             self.begin = event.pos()
             self.destination = self.begin
             self.update()
             mouse_press= 'Other Start coords: ( %d : %d )' % (event.x(), event.y())
             print (mouse_press)
             self.mouse_press_list.append(mouse_press)
    #create function to mouse move
    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:		
            self.destination = event.pos()
            self.update()


    #create function to mouse release      
    def mouseReleaseEvent(self, event):
        
        if event.button() & Qt.LeftButton:
            rect = QRect(self.begin, self.destination)
            painter = QPainter(self.pix)
            if(self.typePaint==1):
                painter.setPen(QPen(Qt.magenta, 3))
                painter.drawRect(rect.normalized())
                self.begin, self.destination = QPoint(), QPoint()
                self.update()
                mouse_release = 'Human End Coords: ( %d : %d )' % (event.x(), event.y())
                print(mouse_release)
                self.mouse_release_list.append(mouse_release)
            elif(self.typePaint==2):
              painter.setPen(QPen(Qt.cyan, 3))  
              painter.drawRect(rect.normalized())
              self.begin, self.destination = QPoint(), QPoint()
              self.update()
              mouse_release = 'Car End Coords: ( %d : %d )' % (event.x(), event.y())
              print(mouse_release)
              self.mouse_release_list.append(mouse_release)
            elif(self.typePaint==3):
              painter.setPen(QPen(Qt.blue, 3))
              painter.drawRect(rect.normalized())
              self.begin, self.destination = QPoint(), QPoint()
              self.update()
              mouse_release = 'Dog End Coords: ( %d : %d )' % (event.x(), event.y())
              print(mouse_release)
              self.mouse_release_list.append(mouse_release)
            elif(self.typePaint==4):
              painter.setPen(QPen(Qt.red, 3))
              painter.drawRect(rect.normalized())
              self.begin, self.destination = QPoint(), QPoint()
              self.update()
              mouse_release = 'Cat End Coords: ( %d : %d )' % (event.x(), event.y())
              print(mouse_release)
              self.mouse_release_list.append(mouse_release)
            else:
             painter.setPen(QPen(Qt.gray, 3))
             painter.drawRect(rect.normalized())
             self.begin, self.destination = QPoint(), QPoint()
             self.update()
             mouse_release = 'Other End Coord: ( %d : %d )' % (event.x(), event.y())
             print(mouse_release)
             self.mouse_release_list.append(mouse_release)

       

    #Save CSV file        
    Csv=1
    file=''
    def exportCSV(self):
        
        if (self.Csv==1):
         self.file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
         print(self.file)
        chr1=str(self.Csv)
        pathtosave = self.file+'/AnnotationCoords'+chr1+'.txt'
        if(self.file== ''):
             print('erorr')
        else:
         with open( pathtosave , 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f,delimiter='-')
            a=list({self.fname[0][self.current]})
            writer.writerows([a])
            for row in zip(self.mouse_press_list,self.mouse_release_list):
                writer.writerow(row)
            #writer.writerows(self.object_coords)
            

         self.Csv+=1    
         self.mouse_press_list.clear()
         self.mouse_release_list.clear()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash=Splashscreen()
    splash.show()
    splash.progress()
    splash.close()
    gui = Template()
    gui.show()
    app.exec_()

