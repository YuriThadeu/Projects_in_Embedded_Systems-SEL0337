from smbus import SMBus
import time
addr=0x8
bus = SMBus(1)
flag = True

print ("Digite 1 pars ON ou 0 para OFF")

user_imput=input ("Inicializar leitura do potenciometro >>>>>    ")
while flag:
    if user_input=="1":
        flag = False
    
    try:
        data=bus.read_i2c_block_data(addr, 0, 2)
        pot_value_10bit=data[0]*256+data[1]
        print ({pot_value_10bit})
        time.sleep(1)

else:
    flag = False