from twisted.internet.protocol import Factory, Protocol
import json
import time
import os,sys,base64

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import GUI
from pythonCompanionGUI import Ui_MainWindow

# =========================================================================== Twisted setup

class Iphone(Protocol):
    def connectionMade(self):
        global x
        x = self
        print "Client Connected ", x
        enable()

    def connectionLost(self, reason):
        print "Client disconnected"

    def dataReceived(self, data):
        print data
        decode(data)         
                
    def sendMsg(self, msg):
        x.message(msg)

    def message(self, message):
        self.transport.write(message + '\n')

# ==================================================================== Main

# Create a class for our main window       
class Main(QtGui.QMainWindow):
    
    def resizeEvent(self,resizeEvent):
        testX = self.ui.centralwidget.geometry()
        print self.ui.titleLabel.geometry()
        print self.ui.titleLabel.sizeHint()
        print testX
        if (testX > 0):
            print "greater"
        else:
            print "else"
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(28)
        font.setBold(True)
        self.ui.titleLabel.setFont(font)
    
    def __init__(self,reactor, parent=None):
        super(Main, self).__init__(parent)
        QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)

        factory = Factory()
        factory.protocol = Iphone
        factory.clients = []
        reactor.listenTCP(8080, factory)
        print "Server started"

        # This is always the same
        self.ui=Ui_MainWindow() 
        self.ui.setupUi(self)

        global labelArtistAlbum
        global labelSong
        global playButton
        global artworkImg
        global labelDuration
        global labelTime
        global progressBar
        global playButton
        global nextButton
        global previousButton
        labelArtistAlbum = self.ui.artistAlbumLabel
        labelSong = self.ui.titleLabel
        playButton = self.ui.playButton
        artworkImg = self.ui.artworkImg
        labelDuration = self.ui.durationLabel
        labelTime = self.ui.timeLabel
        progressBar = self.ui.progressBar
        playButton = self.ui.playButton
        nextButton = self.ui.nextButton
        previousButton = self.ui.previousButton

        playButton.clicked.connect(lambda:buttons("play"))
        nextButton.clicked.connect(lambda:buttons("next"))
        previousButton.clicked.connect(lambda:buttons("previous"))

        self.progressTimer = QtCore.QTimer()
        self.progressTimer.start(1000)

        QtCore.QObject.connect(self.progressTimer, QtCore.SIGNAL("imeout()"), timerRun)

    def closeEvent(self, e):
        reactor.stop()

def decode(data):
    if data.startswith("["):
        jsonData = json.loads(data)
        print jsonData[0]['artist']
        print jsonData[0]['album']
        print jsonData[0]['title']
        print jsonData[0]['duration']
        print jsonData[1]['playBackState']
        print jsonData[0]['time']
        songTitle = jsonData[0]['title']
        songArtist = jsonData[0]['artist']
        songAlbum = jsonData[0]['album']
        songDuration = jsonData[0]['duration']
        songTime = jsonData[0]['time']
        if (songTime == "-1:60"):
            print "matched"
            songTime = "0:00"
        global playStatus
        playStatus = jsonData[1]['playBackState']
        durationSplit = songDuration.split(':')
        durationMinutes = int(durationSplit[0])
        durationSeconds = int(durationSplit[1])
        durationMinutes *= 60
        global durationAdd
        durationAdd = durationMinutes + durationSeconds
        timeSplit = songTime.split(':')
        timeSeconds = int(timeSplit[1])
        timeMinutes = int(timeSplit[0])
        timeMinutes *= 60
        global timeAdd
        timeAdd = int(timeMinutes + timeSeconds)
        progressBar.setProperty("maximum", durationAdd)
        progressBar.setProperty("value", timeAdd)
##        print timeAdd

        labelSong.setText(songTitle)
        labelArtistAlbum.setText(songArtist + " - " + songAlbum)
        playButton.setText(playStatus)
        labelTime.setText(songTime)
        labelDuration.setText(songDuration)
#        artworkImg.setPixmap(pixmap)                            

##       imgString = jsonData[0]['artworkImg']
##
##       dataStripped = imgString.replace("<","").replace(">","").replace(" ","")
##       print dataStripped
##       imgStringDecoded = dataStripped.decode("hex")
##       print imgStringDecoded
##       qimg = QtGui.QImage.fromData(imgStringDecoded)
##       pixmap = QtGui.QPixmap.fromImage(qimg)

    else:
        print data

def timerRun():
##    print "timer run"
    if (labelSong.text() != "Title"):
        if (playStatus == "Pause"):
##            print "return pause"
            global timeAdd
##            print timeAdd
            if (timeAdd < durationAdd):
                timeAdd += 1
                progressBar.setProperty("value", timeAdd)
                minutes = timeAdd //60
                seconds = timeAdd - (minutes * 60)
                totalCurrentTime = str('%s:%02d' % (minutes, seconds))
                labelTime.setText(totalCurrentTime)
##                print totalCurrentTime
                app.processEvents()

def enable():
    playButton.setEnabled(True)
    nextButton.setEnabled(True)
    previousButton.setEnabled(True)

def buttons(button):
    p = Iphone()
    if button == "play":
        print "play button pressed"
        p.sendMsg("play")
    elif button == "next":
        print "next button pressed"
        p.sendMsg("next")
    elif button == "previous":
        print "previous button pressed"
        p.sendMsg("previous")
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    try:
        from qt4reactor import qt4reactor
        print "qt4reactor found"
    except ImportError:
        print "qt4reactor import error"
        from twisted.internet import qt4reactor
    qt4reactor.install()

    from twisted.internet import reactor
    mainwindow = Main(reactor)
    mainwindow.show()

    reactor.run()
