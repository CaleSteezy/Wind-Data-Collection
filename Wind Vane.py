from gpiozero import MCP3008
import time

def voltage_div(r1, r2, v_in):
  v_out = (v_in * r1)/(r1 + r2) #v_in is voltage input and v_out is the voltage output
  return round(v_out, 3)



resistances = [33000, 6570, 8200, 891, 1000, 688, 2200, 1410, 3900,
               3140, 16000, 14120, 120000, 42120, 64900, 21880]
# got these from the data sheet, assuming its correct
for x in range(len(resistances)):
  print(resistances[x],voltage_div(4700, resistances[x], 3.3)) 
#if voltage is 3.3, use 4.7kΩ resistor, if voltage is 5v, use 10kΩ resistor

adc = MCP3008(channel=0)
count = 0
volts = [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 1.2, 1.4, 1.8, 2.0, 2.2, 2.5, 2.7, 2.8, 2.9] 
while True:
  wind = round((adc.value * 3.3), 3)
  if not wind in volts:
    print('Unknown value: ' + str(wind))
  else:
    print('Match: ' + str(wind))


