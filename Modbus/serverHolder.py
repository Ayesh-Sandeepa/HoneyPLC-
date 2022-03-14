

class ServerHolder:
    servers=list()

    def addServer(self,srv):
        ServerHolder.servers.append(srv)

    def updateHoneysim(self):
        ServerHolder.servers[0]._updateHoneysim()

