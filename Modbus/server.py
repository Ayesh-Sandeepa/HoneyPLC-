#!/usr/bin/env python
from operator import truth
from pymodbusMod.server.sync import StartTcpServer
from pymodbusMod.device import ModbusDeviceIdentification
from pymodbusMod.datastore import ModbusSequentialDataBlock
from pymodbusMod.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbusMod.version import version
from threading import Thread 

from pyModbusTCP.client import ModbusClient
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

        serverholder=ServerHolder()
        serverholder.addServer(self)

    def _run(self):
        StartTcpServer(self.context, identity=self.identity, address=(self._ip, int(self._port)))
        
    def run(self):
        Thread(target=self._run).start()
        Thread(target=self._update).start()

    def _update(self):
        while (True):
            for cnt in [1500,1501,1502,1503,1504,1505,1506,1507,1508,1509,1510,1511,1513,1514,1515,1516,1517,1525,1526,1527,1528,1529]:
                for j in range(1):
                    try:
                        c=ModbusClient(host=self._honeysim, port=cnt, unit_id=1, auto_open=True, debug=False)
                    except ValueError:
                        print ("Error with host or port params")
                
                    if c.open():
                        flow = c.read_input_registers(50, 1)
                        cl=c.read_input_registers(51,1)
                        waterlevel=c.read_input_registers(54,1)

                        #self.context[0].setValues(register,address,values)
                        self.context[0].setValues(4,cnt-1500,flow)
                        self.context[0].setValues(4,cnt-1500+30,cl)
                        self.context[0].setValues(4,cnt-1500+60,waterlevel)
                        #print(str(cnt) + "-flow:"+str(flow)+", cl:"+str(cl)+", waterlevel:"+str(waterlevel))
                
                        c.close()
                        #print("Read success at address  : {}".format(cnt))
                    else:
                        c.close()
                        #print("Read failed at address  : {}".format(cnt))
            
            time.sleep(5)

    def _updateHoneysim(self):

        print ("_updateHoneysim called")
        for cnt2 in [1502,1503,1504,1508,1509,1510,1513,1515,1516,1517]: 
            try:
                c=ModbusClient(host=self._honeysim, port=cnt2, unit_id=1, auto_open=True, debug=False)
            except ValueError:
                print ("Error with host or port params")
                
            if c.open():
                val=self.context[0].getValues(3, cnt2-1500, count=3)
                #print ("val0 "+ str(val))
                c.write_single_register(0,val[0])

                c.close()
                print("Write success at address  : {}".format(cnt2))
            else:
                c.close()
                print("Write failed at address  : {}".format(cnt2))   

        for cnt3 in [1501,1512,1522,1523,1524]: 
            try:
                c=ModbusClient(host=self._honeysim, port=cnt2, unit_id=1, auto_open=True, debug=False)
            except ValueError:
                print ("Error with host or port params")
                
            if c.open():
                val1=self.context[0].getValues(3, cnt3-1500, count=1)
                print ("val10 "+ str(val1))
                c.write_single_register(0,val1[0])

                c.close()
                print("Write success at address  : {}".format(cnt3))
            else:
                c.close()
                print("Write failed at address  : {}".format(cnt3))      

    def get(self,register,address,_count):
        rg= self.context[0].getValues(register, address, count=_count)
        #print (rg)
        return rg

server=ModbusServer("",1502,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531","192.168.1.101")  
server.run() 
