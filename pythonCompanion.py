from twisted.internet.protocol import Factory, Protocol
import json
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

    def connectionLost(self, reason):
        print "Client disconnected"

    def dataReceived(self, data):
        print data
        if data.startswith("["):
            jsonData = json.loads(data)
            #print jsonData
            print jsonData[0]['artist']
            print jsonData[0]['album']
            print jsonData[0]['title']
            print jsonData[0]['duration']
            print jsonData[1]['playBackState']
            songTitle = jsonData[0]['title']
            songArtist = jsonData[0]['artist']
            songAlbum = jsonData[0]['album']
            songDuration = jsonData[0]['duration']
            songTime = jsonData[0]['time']
            playStatus = jsonData[1]['playBackState']
##            imgString = jsonData[0]['artworkImg']
##
##            dataStripped = imgString.replace("<","").replace(">","").replace(" ","")
##            print dataStripped
##            imgStringDecoded = dataStripped.decode("hex")
##            print imgStringDecoded
##            qimg = QtGui.QImage.fromData(imgStringDecoded)
##            pixmap = QtGui.QPixmap.fromImage(qimg)

            labelSong.setText(songTitle)
            labelArtistAlbum.setText(songArtist + " - " + songAlbum)
            playButton.setText(playStatus)
            labelDuration.setText(songDuration)
            labelTime.setText(songTime)
#            artworkImg.setPixmap(pixmap)
            

        else:
            print "else"
            print data
##            imgString = data
##            imgArtworkString = base64.b64decode(imgString)
##            print imgArtworkString           

    def testMsg(self, msg):
        x.message(msg)

    def message(self, message):
        self.transport.write(message + '\n')

# ==================================================================== Main

# Create a class for our main window       
class Main(QtGui.QMainWindow):
    def __init__(self,reactor, parent=None):
        super(Main, self).__init__(parent)

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
        labelArtistAlbum = self.ui.artistAlbumLabel
        labelSong = self.ui.titleLabel
        playButton = self.ui.playButton
        artworkImg = self.ui.artworkImg
        labelDuration = self.ui.durationLabel
        labelTime = self.ui.timeLabel

        self.ui.playButton.clicked.connect(lambda:buttons("play"))
        self.ui.nextButton.clicked.connect(lambda:buttons("next"))
        self.ui.previousButton.clicked.connect(lambda:buttons("previous"))

def buttons(button):
    p = Iphone()
    if button == "play":
        print "play button pressed"
        p.testMsg("play")
    elif button == "next":
        print "next button pressed"
        p.testMsg("next")
    elif button == "previous":
        print "previous button pressed"
        p.testMsg("previous")
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    try:
        from qt4reactor import qt4reactor
        print "found"
    except ImportError:
        print "import error"
        from twisted.internet import qt4reactor
    qt4reactor.install()

    from twisted.internet import reactor
    mainwindow = Main(reactor)
    mainwindow.show()

    reactor.run()


