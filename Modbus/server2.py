from operator import truth
from pymodbusMod.server.sync import StartTcpServer
from pymodbusMod.device import ModbusDeviceIdentification
from pymodbusMod.datastore import ModbusSequentialDataBlock
from pymodbusMod.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbusMod.version import version
from threading import Thread 

#from pyModbusTCP.client import ModbusClient
import time

from serverHolder import ServerHolder

class ModbusServer:

    def __init__(self,_ip,_port,_vendorName,_ProductCode,_VendorUrl,_ProductName,_ModelName, honeysimIP):
        self._ip = _ip
        self._port = _port
        self._honeysim=honeysimIP
        store = ModbusSlaveContext(
            di = ModbusSequentialDataBlock(0, [0]*100),
            co = ModbusSequentialDataBlock(0, [0]*100),
            hr = ModbusSequentialDataBlock(0, [0]*100),
            ir = ModbusSequentialDataBlock(0, [0]*100))
        self.context = ModbusServerContext(slaves=store, single=True)

        # initialize the server information
        self.identity = ModbusDeviceIdentification()
        self.identity.VendorName = _vendorName
        self.identity.ProductCode = _ProductCode
        self.identity.VendorUrl = _VendorUrl
        self.identity.ProductName = _ProductName
        self.identity.ModelName = _ModelName
        self.identity.MajorMinorRevision = version.short()

        #serverholder=ServerHolder()
        #serverholder.addServer(self)

    def _run(self):
        print ("Modbus server started")
        StartTcpServer(self.context, identity=self.identity, address=(self._ip, int(self._port)))
        

    def run(self):
        Thread(target=self._run).start()

server=ModbusServer("",1503,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531","192.168.1.101")  
server.run() 