# import sys
# from PyQt4.QtGui import *
#
# # Create an PyQT4 application object.
# a = QApplication(sys.argv)
#
# # The QWidget widget is the base class of all user interface objects in PyQt4.
# w = QWidget()
#
# # Set window size.
# w.resize(320, 240)
#
# # Set window title
# w.setWindowTitle("Hello World!")
#
# # Add a button
# btn = QPushButton('Hello World!', w)
# btn.setToolTip('Click to quit!')
# btn.clicked.connect(exit)
# btn.resize(btn.sizeHint())
# btn.move(100, 80)
#
# # Show window
# w.show()
#
# sys.exit(a.exec_())



import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main2 import start
import os
from threading import Thread
import time

class MoodExample(QGroupBox):
    textbox = None
    textbox2 = None
    enteredText = None
    resultText = None
    textbox1Text = None

    def __init__(self):
        super(MoodExample, self).__init__()

        self.textbox = QLineEdit(self)
        self.textbox.move(150, 20)
        self.textbox.resize(280, 40)
        self.textbox.setVisible(False)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(200, 150)
        self.textbox2.resize(280, 40)
        self.textbox2.returnPressed.connect(lambda: self.onEnterPushed())
        #self.textbox2.setVisible(False)

        # Create an array of radio buttons
        moods = [QRadioButton("Present Simple"), QRadioButton("Present Continuous"), QRadioButton("Present Perfect"),
                 QRadioButton("Present Perfect Continuous"),QRadioButton("Past Simple"), QRadioButton("Past Continuous"),
                 QRadioButton("Past Perfect"), QRadioButton("Past Perfect Continuous"), QRadioButton("Future Simple"),
                 QRadioButton("Future Continuous"), QRadioButton("Future Perfect"), QRadioButton("Future Perfect Continuous")]

        # Set a radio button to be checked by default
        #moods[0].setChecked(True)
        moods[0].setChecked(False)

        # Radio buttons usually are in a vertical layout
        button_layout = QVBoxLayout()

        # Create a button group for radio buttons
        self.mood_button_group = QButtonGroup()

        for i in xrange(len(moods)):
            # Add each radio button to the button layout
            button_layout.addWidget(moods[i])
            # Add each radio button to the button group & give it an ID of i
            self.mood_button_group.addButton(moods[i], i)
            # Connect each radio button to a method to run when it's clicked
            self.connect(moods[i], SIGNAL("clicked()"), self.radio_button_clicked)

        # Set the layout of the group box to the button layout
        self.setLayout(button_layout)

    #Print out the ID & text of the checked radio button
    def radio_button_clicked(self):
        print(self.mood_button_group.checkedId())
        print(self.mood_button_group.checkedButton().text())
        # mod2 = WithTxtBoxes()
        # mod2.resize(500, 500)
        # mod2.show()
        thread = Thread(target=start, args=(int(self.mood_button_group.checkedId()) + 1, self,))
        thread.start()
        #start(int(self.mood_button_group.checkedId()) + 1, self)

    def setTextBox1(self, task, question):
        print "IN SET TEX BOX"
        #self.textbox.setVisible(True)
        self.textbox1Text = "<span style=\" font-size:10pt; font-weight:600; color:#000000;\" >" + task + "<br>" + question + "</span>"
        self.update()
        print "IN SET TEX BOX OUT"

    def getTextBox2(self):
        print "IN SET TEX BOX222"
        text = ""
        #self.textbox2.setVisible(True)
        #os.system("pause")
        while True:
            if self.enteredText != None:
                text = self.enteredText
                self.enteredText = None
                return text
            else:
                time.sleep(0.1)

    def paintEvent(self, event):
        def drawText(text, point):
            st = QStaticText()
            st.setText(text)
            painter = QPainter(self)
            painter.drawStaticText(point, st)

        if self.resultText != None:
            drawText(self.resultText, QPoint(200,300))
            #self.resultText = None
        if self.textbox1Text != None:
            drawText(self.textbox1Text, QPoint(200,50))
            #self.textbox1Text = None

    def showResult(self, result):
        temp = result
        if result == "Correct":
            result = "<span style=\" font-size:8pt; font-weight:600; color:#00ff00;\" >" + temp + "</span>"
        else:
            result = "<span style=\" font-size:8pt; font-weight:600; color:#ff0000;\" >" + temp + "</span>"
        self.resultText = result
        self.update()
        time.sleep(3)
        self.resultText = ""
        self.textbox2.setText("")
        self.update()

    @pyqtSlot()
    def onEnterPushed(self):
        self.enteredText = self.textbox2.text()


app = QApplication(sys.argv)
mood_example = MoodExample()
mood_example.resize(500,500)
mood_example.show()

sys.exit(app.exec_())