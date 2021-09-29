
# importing the required libraries
  
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from Data_preparation import Targets_df
from prediction import predict
from Data_preparation import clms,pd, Scaler

class Window(QMainWindow):

    def button_clicked(self):
        entry = [self.champ1.text(), self.champ2.text(), self.champ3.text(), 
        self.champ4.text(), self.champ5.text(), self.champ6.text(), self.champ7.text(), 
        self.champ8.text(), self.champ9.text(), self.champ10.text(), self.champ11.text(), 
        self.champ12.text(), self.champ13.text(), self.champ14.text(), self.champ15.text(), 
        self.champ16.text(), self.champ17.text()]

        Data_to_predict = pd.DataFrame(columns = clms)
        Data_to_predict.loc[0] = entry
        Data_to_predict = Scaler.transform(Data_to_predict)

        result = predict(Data_to_predict)

        if result[0] == 3:
            self.label_12.setText("Proche de la défaillance totale")
        elif result[0] == 20:
            self.label_12.setText("Efficacité réduite")
        elif result[0] == 100:
            self.label_12.setText("Efficacité totale")
        self.label_12.setFont(QFont("Times",9, weight=QFont.Bold))
        print(self.label_12.text)

        if result[1] == 100:
            self.label_22.setText("Comportement de commutation optimal")
        elif result[1] == 90:
            self.label_22.setText("Faible décalage")
        elif result[1] == 80:
            self.label_22.setText("Décalage important ")
        elif result[1] == 73:
            self.label_22.setText("Proche de la défaillance totale")
        self.label_22.setFont(QFont("Times",9, weight=QFont.Bold))

        if result[3] == 0:
            self.label_42.setText("Pas de fuite")
        elif result[3] == 1:
            self.label_42.setText("Faible fuite")
        elif result[3] == 2:
            self.label_42.setText("Fuite importante")
        self.label_32.setFont(QFont("Times",9, weight=QFont.Bold))

        if result[2] == 130:
            self.label_32.setText("Pression optimale")
        elif result[2] == 115:
            self.label_32.setText("Pression légèrement réduite")
        elif result[2] == 100:
            self.label_32.setText("Pression fortement réduite")
        elif result[2] == 90:
            self.label_32.setText("Proche de la défaillance totale")
        self.label_42.setFont(QFont("Times",9, weight=QFont.Bold))

        if result[4] == 0:
            self.label_52.setText("Les conditions sont stables")
        elif result[4] == 1:
            self.label_52.setText("Le système présente une anomalie")
        self.label_52.setFont(QFont("Times",9, weight=QFont.Bold))


    def __init__(self):
        super().__init__()
  
        # set the title
        self.setWindowTitle("Système hydraulique")
  
        # setting  the geometry of window
        self.setGeometry(0, 0, 1500, 1500)

        # plotting target graphs
        x = range(1,2206,1)

        self.graphWidget1 = pg.PlotWidget(self)
        self.graphWidget1.setTitle('''Etat de refroidissement''')
        self.graphWidget1.resize(250,250)
        self.graphWidget1.move(700,80)
        self.graphWidget1.setBackground(None)
        self.graphWidget1.plot(x, Targets_df['Cooler condition'].values)

        self.graphWidget2 = pg.PlotWidget(self)
        self.graphWidget2.setTitle('''Etat de la valve''')
        self.graphWidget2.resize(250,250)
        self.graphWidget2.move(1000,80)
        self.graphWidget2.setBackground(None)
        self.graphWidget2.plot(x, Targets_df['Valve condition'].values)

        self.graphWidget3 = pg.PlotWidget(self)
        self.graphWidget3.setTitle('''Fuite interne de la pompe''')
        self.graphWidget3.resize(250,250)
        self.graphWidget3.move(700,380)
        self.graphWidget3.setBackground(None)
        self.graphWidget3.plot(x, Targets_df['Internal pump leakage'].values)

        self.graphWidget4 = pg.PlotWidget(self)
        self.graphWidget4.setTitle('''Accumulateur hydraulique''')
        self.graphWidget4.resize(250,250)
        self.graphWidget4.move(1000,380)
        self.graphWidget4.setBackground(None)
        self.graphWidget4.plot(x, Targets_df['Hydraulic accumulator'].values)

  
        # creating a labels and entries of feartures
        self.label_1 = QLabel("Pression 1:", self)
        self.label_1.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_1.setStyleSheet("color:lightblue")
        self.champ1 = QLineEdit(self)
        self.champ1.setStyleSheet("background-color: lightblue;")
        self.label_1.move(80, 70)
        self.champ1.move(80, 95)
        print(self.champ1.text())
    
        self.label_2 = QLabel("Pression 2:", self)
        self.label_2.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_2.setStyleSheet("color:lightblue")
        self.champ2 = QLineEdit(self)
        self.champ2.setStyleSheet("background-color: lightblue;")
        self.label_2.move(80, 130)
        self.champ2.move(80, 155)

        self.label_3 = QLabel("Pression 3:", self)
        self.label_3.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_3.setStyleSheet("color:lightblue")
        self.champ3 = QLineEdit(self)
        self.champ3.setStyleSheet("background-color: lightblue;")
        self.label_3.move(80, 190)
        self.champ3.move(80, 215)

        self.label_4 = QLabel("Pression 4:", self)
        self.label_4.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_4.setStyleSheet("color:lightblue")
        self.champ4 = QLineEdit(self)
        self.champ4.setStyleSheet("background-color: lightblue;")
        self.label_4.move(80, 250)
        self.champ4.move(80, 275)

        self.label_5 = QLabel("Pression 5:", self)
        self.label_5.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_5.setStyleSheet("color:lightblue")
        self.champ5 = QLineEdit(self)
        self.champ5.setStyleSheet("background-color: lightblue;")
        self.label_5.move(80, 310)
        self.champ5.move(80, 335)

        self.label_6 = QLabel("Pression 6:", self)
        self.label_6.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_6.setStyleSheet("color:lightblue")
        self.champ6 = QLineEdit(self)
        self.champ6.setStyleSheet("background-color: lightblue;")
        self.label_6.move(80, 370)
        self.champ6.move(80, 395)

        self.label_7 = QLabel('Puissance moteur:', self)
        self.label_7.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_7.setStyleSheet("color:lightblue")
        self.champ7 = QLineEdit(self)
        self.champ7.setStyleSheet("background-color: lightblue;")
        self.label_7.move(80, 430)
        self.label_7.resize(110, 15)
        self.champ7.move(80, 455)

        self.label_8 = QLabel('Température 1:', self)
        self.label_8.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_8.setStyleSheet("color:lightblue")
        self.champ8 = QLineEdit(self)
        self.champ8.setStyleSheet("background-color: lightblue;")
        self.label_8.move(80, 490)
        self.champ8.move(80, 515)

        self.label_9 = QLabel('Température 2:', self)
        self.label_9.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_9.setStyleSheet("color:lightblue")
        self.champ9 = QLineEdit(self)
        self.champ9.setStyleSheet("background-color: lightblue;")
        self.label_9.move(200, 70)
        self.champ9.move(200, 95)

        self.label_10 = QLabel('Température 3:', self)
        self.label_10.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_10.setStyleSheet("color:lightblue")
        self.champ10 = QLineEdit(self)
        self.champ10.setStyleSheet("background-color: lightblue;")
        self.label_10.move(200, 130)
        self.champ10.move(200, 155)

        self.label_11 = QLabel('Température 4:', self)
        self.label_11.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_11.setStyleSheet("color:lightblue")
        self.champ11 = QLineEdit(self)
        self.champ11.setStyleSheet("background-color: lightblue;")
        self.label_11.move(200, 190)
        self.champ11.move(200, 215)

        self.label_12 = QLabel('Vibration:', self)
        self.label_12.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_12.setStyleSheet("color:lightblue")
        self.champ12 = QLineEdit(self)
        self.champ12.setStyleSheet("background-color: lightblue;")
        self.label_12.move(200, 250)
        self.champ12.move(200, 275)

        self.label_13 = QLabel('Débit volumique 1:', self)
        self.label_13.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_13.setStyleSheet("color:lightblue")
        self.champ13 = QLineEdit(self)
        self.champ13.setStyleSheet("background-color: lightblue;")
        self.label_13.move(200, 310)
        self.label_13.resize(150, 30)
        self.champ13.move(200, 335)

        self.label_14 = QLabel('Débit volumique2 :', self)
        self.label_14.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_14.setStyleSheet("color:lightblue")
        self.champ14 = QLineEdit(self)
        self.champ14.setStyleSheet("background-color: lightblue;")
        self.label_14.move(200, 370)
        self.label_14.resize(150, 30)
        self.champ14.move(200, 395)

        self.label_15 = QLabel('''Facteur d'efficience:''', self)
        self.label_15.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_15.setStyleSheet("color:lightblue")
        self.champ15 = QLineEdit(self)
        self.champ15.setStyleSheet("background-color: lightblue;")
        self.label_15.move(200, 430)
        self.label_15.resize(150, 30)
        self.champ15.move(200, 455)

        self.label_16 = QLabel('Efficience de refroidissement:', self)
        self.label_16.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_16.setStyleSheet("color:lightblue")
        self.champ16 = QLineEdit(self)
        self.champ16.setStyleSheet("background-color: lightblue;")
        self.label_16.move(200, 490)
        self.label_16.resize(200, 30)
        self.champ16.move(200, 515)

        self.label_17 = QLabel('Puissance de refroidissement:', self)
        self.label_17.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_17.setStyleSheet("color:lightblue")
        self.champ17 = QLineEdit(self)
        self.champ17.setStyleSheet("background-color: lightblue;")
        self.label_17.move(110, 550)
        self.label_17.resize(200, 30)
        self.champ17.move(130, 575)
  
        oImage = QImage("background2.jpg")
        sImage = oImage.scaled(QSize(1400,800))                

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)

        self.label_11 = QLabel("Etat de refroidissement:", self)
        self.label_11.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_11.setStyleSheet("color:lightblue")
        self.label_11.move(430,160)
        self.label_11.resize(160, 30)
        self.label_12 = QLabel("", self)
        self.label_12.resize(200,30)
        self.label_12.setStyleSheet("background-color: lightblue")
        self.label_12.move(430,185)

        self.label_21 = QLabel("Etat de la valve:", self)
        self.label_21.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_21.setStyleSheet("color:lightblue")
        self.label_21.move(430,225)
        self.label_21.resize(150, 30)
        self.label_22 = QLabel("", self)
        self.label_22.resize(200,30)
        self.label_22.setStyleSheet("background-color: lightblue")
        self.label_22.move(430,250)

        self.label_31 = QLabel("Fuite interne de la pompe:", self)
        self.label_31.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_31.setStyleSheet("color:lightblue")
        self.label_31.move(430,355)
        self.label_31.resize(200, 30)
        self.label_32 = QLabel("", self)
        self.label_32.resize(200,30)
        self.label_32.setStyleSheet("background-color: lightblue")
        self.label_32.move(430,380)

        self.label_41 = QLabel("Accumulateur hydraulique:", self)
        self.label_41.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_41.setStyleSheet("color:lightblue")
        self.label_41.move(430,290) 
        self.label_41.resize(200, 30)
        self.label_42 = QLabel("", self)
        self.label_42.resize(200,30)
        self.label_42.setStyleSheet("background-color: lightblue")
        self.label_42.move(430,315)

        self.label_51 = QLabel("Stabilité:", self)
        self.label_51.setFont(QFont("Times",10, weight=QFont.Bold))
        self.label_51.setStyleSheet("color:lightblue")
        self.label_51.move(430,420)
        self.label_52 = QLabel("", self)
        self.label_52.resize(200,30)
        self.label_52.setStyleSheet("background-color: lightblue")
        self.label_52.move(430,445)


        self.bouton = QPushButton("Analyser", self)
        self.bouton.setFont(QFont("Times",10, weight=QFont.Bold))
        self.bouton.setStyleSheet("color:grey; background-color: lightblue; border-style: outset;border-width: 2px;border-radius: 30px;border-color: lightblue;")
        self.bouton.move(460, 120)
        self.bouton.clicked.connect(self.button_clicked)

        #self.result = self.button_clicked()

  
        # show all the widgets
        self.show()
  
  
# create pyqt5 app
App = QApplication(sys.argv)

  
# create the instance of our Window
window = Window()
#print(window.result)
# start the app
sys.exit(App.exec())

