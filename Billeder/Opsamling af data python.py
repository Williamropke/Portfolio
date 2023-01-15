import datetime
from time import sleep
from sense_hat import SenseHat
import subprocess
from gpiozero import CPUTemperature
sense = SenseHat()


start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds=10)
FACTOR = 1.967307706

with open ("test.csv", "w") as file:
    file.write("Time , Temperature , Pressure, Humidity \n")

while now_time < start_time + duration:
    t_raw = sense.get_temperature()
    cpu = CPUTemperature()
    t_calibrated = t_raw-(cpu.temperature-t_raw)/FACTOR
    p = sense.get_pressure()
    h = sense.get_humidity()
    now_time = datetime.datetime.now()

    with open ("test.csv", "a") as file:
        file.write("%s, %s, %s, %s \n" % (now_time,(t_calibrated),p,h))
    sleep(1)

if now_time > start_time + duration:
    print("done")

carrot_h_max = 87
carrot_h_min = 69
carrot_t_max = 21
carrot_t_min = 14

wheat_h_max = 84
wheat_h_min = 72
wheat_t_max = 25
wheat_t_min = 20

potato_h_max = 92
potato_h_min = 69
potato_t_max = 25
potato_t_min = 18

if potato_h_min<h<potato_h_max and potato_t_min<t_calibrated<potato_t_max:
    print("potato")
    
if carrot_h_min<h>carrot_h_max and carrot_t_min<t_calibrated<carrot_t_max:
    print("carrot")

if wheat_h_min<h<wheat_h_max and wheat_t_min<t_calibrated<wheat_t_max:
    print("wheat")





    
