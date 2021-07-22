import serial

#ser = serial.Serial('COM5',19200)
#print ser.name       # check which port was really used
#print ser.isOpen()
#ser.close()
#pumps = find_pumps(ser)
#rates = get_rates(ser,pumps)


def find_pumps(ser,tot_range=10):
    pumps = []
    for i in range(tot_range):
        ser.write(str.encode('%iADR\x0D'%i))
        output = ser.readline()
        if len(output)>0:
            pumps.append(i)
    return pumps

def run_all(ser):
    cmd = b'*RUN\x0D'
    ser.write(cmd)
    output = ser.readline()
    if b'?' in output: print (cmd.strip()+' from run_all not understood')

def stop_all(ser):
    cmd = '*STP\x0D'
    ser.write(str.encode(cmd))
    output = ser.readline()
    if b'?' in output: print (cmd.strip()+' from stop_all not understood')

def stop_pump(ser,pump):
    cmd = '%iSTP\x0D'%pump
    ser.write(str.encode(cmd))
    output = ser.readline()
    if b'?' in output: print (cmd.strip()+' from stop_pump not understood')

    cmd = '%iRAT0UH\x0D'%pump
    ser.write(str.encode(cmd))
    output = ser.readline()
    if b'?' in output: print (cmd.strip()+' from stop_pump not understood')

def set_rates(ser,rate):
    cmd = ''
    for pump in rate:
        fr = float(rate[pump])
        ###### Kevin Added 4/2/21
        direction = 'INF'
        if fr<0: 
            direction = 'WDR'
        frcmd = '%iDIR%s\x0D'%(pump,direction)
        ser.write(str.encode(frcmd))
        output = ser.readline()
        if b'?' in output: print (frcmd.strip()+' from set_rates not understood')
        fr = abs(fr)
        ######
        if fr<5000:
            cmd += str(pump)+'RAT'+str(fr)[:5]+'UH*'
        else:
            fr = fr/1000.0
            cmd += str(pump)+'RAT'+str(fr)[:5]+'MH*'
    cmd += '\x0D'
    ser.write(str.encode(cmd))
    output = ser.readline()
    if b'?' in output: print (cmd.strip()+' from set_rates not understood')
    #return(direction)

def get_rate(ser,pump):
    #cmd = '%iRAT\x0D'%pump 
    cmd=f"{pump}RAT\x0D"
    ser.write(str.encode(cmd,encoding='ASCII'))
    output = ser.readline()
    ###### Kevin Added 4/2/21
    sign = ''
    # if output[4:7]=='WDR':
    #     sign = '-'
    #     print(sign)
    if output.decode()[3]=='W':
        sign = '-'
    cmd = '%iRAT\x0D'%pump
    ser.write(str.encode(cmd))
    output = ser.readline()
    if b'?' in output: print (cmd.strip()+' from get_rate not understood')
    ######
    #if b'?' in output:
    #    print (cmd.strip()+' from get_rate not understood')
    units = output[-3:-1]
    if units==b'MH':
        # rate = int(float(output[4:-3])*1000)
        rate = str(float(output[4:-3])*1000)  
    elif units==b'UH':
        # rate = output[4:-3]
        rate = str(float(output[4:-3])) 
    else:
        print (cmd.strip()+' from get_rate not understood')
        ser.close()
    return sign+rate # changed from 'return rate' to 'return sign+rate' KJ 4/2/21

def get_rates(ser,pumps):
    #rates = dict(((p,get_rate(ser,p).split(b'.')[0])) for p in pumps)
    rates = {}
    #print (type(ser))
    #print (type(pumps))
    for p in pumps:
      #  print (type(p))
        #pbyte=p.encode('utf-8')
       rate= str(get_rate(ser,p)).split('.')[0]
       rates[p]=rate
    return rates

def set_diameter(ser,pump,dia):
    cmd = '%iDIA%s\x0D'%(pump,dia)
    ser.write(str.encode(cmd))
    output = ser.readline()
    if b'?' in output: print (cmd.strip()+' from set_diameter not understood')

    
def get_diameter(ser,pump):
    cmd = '%iDIA\x0D'%pump
    ser.write(str.encode(cmd))
    output = ser.readline()
    if b'?' in output: print (cmd.strip()+' from get_diameter not understood')
    dia = output[4:-1]
    return dia

def prime(ser,pump):
    cmd = '%iRAT10.0MH\x0D'%pump
    ser.write(str.encode(cmd))
    output = ser.readline()
    if b'?' in output: print (cmd.strip()+' from prime not understood')

    cmd = '%iRUN\x0D'%pump
    ser.write(str.encode(cmd))
    output = ser.readline()
    if b'?' in output: print (cmd.strip()+' from prime not understood')
