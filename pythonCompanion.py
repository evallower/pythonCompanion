from twisted.internet.protocol import Factory, Protocol
import json
import os,sys

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import GUI
from pythonCompanionGUI import Ui_MainWindow

# =========================================================================== Twisted setup

class Iphone(Protocol):
    def connectionMade(self):
        self.factory.clients.append(self)
        print "Client connected", self.factory.clients

    def connectionMade(self):
        self.factory.clients.append(self)
        print "Client connected", self.factory.clients

    def connectionLost(self, reason):
        self.factory.clients.remove(self)
        print "Client disconnected"

    def dataReceived(self, data):
        print data
        jsonData = json.loads(data)
        print jsonData
        print jsonData[0]['artist']
        print jsonData[0]['album']
        print jsonData[0]['title']
        print jsonData[0]['duration']
        songTitle = jsonData[0]['title']
        songArtist = jsonData[0]['artist']
        songAlbum = jsonData[0]['album']
        songDuration = jsonData[0]['duration']

        labelSong.setText(songTitle)
        labelArtist.setText(songArtist)
        labelAlbum.setText(songAlbum)

        msg = "previous"

        for c in self.factory.clients:
            c.message(msg)

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

        global labelAlbum
        global labelArtist
        global labelSong
        labelAlbum = self.ui.albumLabel
        labelArtist = self.ui.artistLabel
        labelSong = self.ui.titleLabel
            
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


