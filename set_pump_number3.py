import serial

### SET THESE PARAMETERS HERE
serial_port = 'COM1'
pump_number =2

### LEAVE EVERYTHING BELOW HERE THE SAME
def print_pump_number(ser,tot_range=100):
    for i in range(tot_range):
        cmd = str.encode('%iADR\x0D'%i)
        print ('writing to')
        ser.write(cmd)
        print ('reading')
        output = ser.readline()
        print (output)
        if len(output)>0:
            print ('current pump set to %i'%i)
            break

ser = serial.Serial(serial_port,19200,timeout=0.1)
print ('Current pump number set to:')
print_pump_number(ser)
print ('setting pump to %i'%pump_number)
ser.write(b'*ADR%iB19200\x0D'%pump_number)
ser.readline()
print_pump_number(ser)
ser.close()
