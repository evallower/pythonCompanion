from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
from tornado.platform.twisted import TwistedIOLoop
from twisted.internet import reactor
import json
import tornado.web

TwistedIOLoop().install()

class Iphone(Protocol):
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
		global songTitle
		global songArtist
		global songAlbum
		global songDuration
		songTitle = jsonData[0]['title']
		songArtist = jsonData[0]['artist']
		songAlbum = jsonData[0]['album']
		songDuration = jsonData[0]['duration']

		msg = "previous"
				
		for c in self.factory.clients:
			c.message(msg)
						
	def message(self, message):
		self.transport.write(message + '\n')
		
class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.write(songArtist)
        self.write(songTitle)
        self.write(songAlbum)
        self.write(songDuration)

application = tornado.web.Application([
    (r"/", MainHandler),
])
		
if __name__ == "__main__":
    application.listen(8888)
		
factory = Factory()
factory.protocol = Iphone
factory.clients = []
reactor.listenTCP(80, factory)
print "Server started"
reactor.run()