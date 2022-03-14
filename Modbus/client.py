from pyModbusTCP.client import ModbusClient
import time


try:
    c=ModbusClient(host="127.0.0.1", port=1502, unit_id=1, auto_open=True, debug=False)
except ValueError:
    print ("Error with host or port params")


if c.open():

    c.write_single_register(2,65000)
        #c.write_single_register(15,20000)
        #.write_single_register(8,35000)
        #c.write_single_register(13,30000)

    c.close()
    print("Write success at address  : 2")
else:
    c.close()
    print("Write failed at address  : 2")


try:
    c=ModbusClient(host="127.0.0.1", port=1502, unit_id=1, auto_open=True, debug=False)
except ValueError:
    print ("Error with host or port params")


if c.open():

    c.write_single_register(15,20000)
        #.write_single_register(8,35000)
        #c.write_single_register(13,30000)

    c.close()
    print("Write success at address  : 15")
else:
    c.close()
    print("Write failed at address  : 15")


try:
    c=ModbusClient(host="127.0.0.1", port=1502, unit_id=1, auto_open=True, debug=False)
except ValueError:
    print ("Error with host or port params")


if c.open():

    c.write_single_register(8,35000)
        #c.write_single_register(13,30000)

    c.close()
    print("Write success at address  : 8")
else:
    c.close()
    print("Write failed at address  : 8")



try:
    c=ModbusClient(host="127.0.0.1", port=1502, unit_id=1, auto_open=True, debug=False)
except ValueError:
    print ("Error with host or port params")


if c.open():

    c.write_single_register(13,30000)
        #c.write_single_register(13,30000)

    c.close()
    print("Write success at address  : 13")
else:
    c.close()
    print("Write failed at address  : 13")



    

'''       
for j in range(2):
    for i in range(1502,1503):

        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")


        if c.open():
            c.write_single_register(15,20000)
            # c.write_multiple_coils(0, [True,True,True])
            # c.write_multiple_registers(0, [65000]*30)
            # c.write_single_coil(0, True)
            # c.write_single_register(0, 250)

            c.close()
            print("Write success at address  : {}".format(i))
        else:
            c.close()
            print("Write failed at address  : {}".format(i))


for j in range(2):
    for i in range(1502,1503):
        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")


        if c.open():
            c.write_single_register(8,35000)
            # c.write_multiple_coils(0, [True,True,True])
            # c.write_multiple_registers(0, [65000]*30)
            # c.write_single_coil(0, True)
            # c.write_single_register(0, 250)

            c.close()
            print("Write success at address  : {}".format(i))
        else:
            c.close()
            print("Write failed at address  : {}".format(i))

for j in range(2):
    for i in range(1502,1503):

        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")


        if c.open():
            #write_single_register(register_address,value)

            c.write_single_register(13,30000)
            # c.write_multiple_coils(0, [True,True,True])
            # c.write_multiple_registers(0, [65000]*30)
            # c.write_single_coil(0, True)
            # c.write_single_register(0, 250)

            c.close()
            print("Write success at address  : {}".format(i))
        else:
            c.close()
            print("Write failed at address  : {}".format(i))
'''     
'''
while(True):
    # for i in range(1501,1502):

    #     try:
    #         c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
    #     except ValueError:
    #         print ("Error with host or port params")


    #     if c.open():
    #         reg_list = c.read_coils(0, 5)
    #         print(reg_list)
    #         # c.write_multiple_coils(0, [True,True,True])
    #         # c.write_multiple_registers(0, [65000]*30)
    #         # c.write_single_coil(0, True)
    #         # c.write_single_register(0, 250)

    #         c.close()
    #         print("Test success at address  : {}".format(i))
    #     else:
    #         c.close()
    #         print("Test failed at address  : {}".format(i))
        
    for i in range(1505,1512,6):

        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")


        if c.open():
            reg_list = c.read_input_registers(50, 5)
            print(reg_list)
            # c.write_multiple_coils(0, [True,True,True])
            # c.write_multiple_registers(0, [65000]*30)
            # c.write_single_coil(0, True)
            # c.write_single_register(0, 250)

            c.close()
            print("Read success at address  : {}".format(i))
        else:
            c.close()
            print("Read failed at address  : {}".format(i))


    for i in range(1514,1515):

        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")


        if c.open():
            reg_list = c.read_input_registers(50, 5)
            print(reg_list)
            # c.write_multiple_coils(0, [True,True,True])
            # c.write_multiple_registers(0, [65000]*30)
            # c.write_single_coil(0, True)
            # c.write_single_register(0, 250)

            c.close()
            print("Read success at address  : {}".format(i))
        else:
            c.close()
            print("Read failed at address  : {}".format(i))

    
    for i in range(1515,1516):
        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")

        if c.open():
            reg_list = c.read_input_registers(49, 10)
            print(reg_list)
            # c.write_multiple_coils(0, [True,True,True])
            # c.write_multiple_registers(0, [65000]*30)
            # c.write_single_coil(0, True)
            # c.write_single_register(0, 250)

            c.close()
            print("Read success at address  : {}".format(i))
        else:
            c.close()
            print("Read failed at address  : {}".format(i))

    
    for i in range(1525,1526):
        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")


        if c.open():
            reg_list = c.read_input_registers(49, 10)
            print(reg_list)
            # c.write_multiple_coils(0, [True,True,True])
            # c.write_multiple_registers(0, [65000]*30)
            # c.write_single_coil(0, True)
            # c.write_single_register(0, 250)

            c.close()
            print("Read success at address  : {}".format(i))
        else:
            c.close()
            print("Read failed at address  : {}".format(i))

    
    for i in (1528,1529):
        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")


        if c.open():
            reg_list = c.read_input_registers(49, 10)
            print(reg_list)

            c.close()
            print("Read success at address  : {}".format(i))
        else:
            c.close()
            print("Read failed at address  : {}".format(i))

    

    time.sleep(2)

      

'''