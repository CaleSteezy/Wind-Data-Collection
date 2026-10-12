from gpiozero import MCP3008
import time

def voltage_div(r1, r2, v_in):
  v_out = (v_in * r1)/(r1 + r2) #v_in is voltage input and v_out is the voltage output
  return round(v_out, 3)



resistances = [33000, 6570, 8200, 891, 1000, 688, 2200, 1410, 3900,
               3140, 16000, 14120, 120000, 42120, 64900, 21880]
# got these from the data sheet, assuming its correct
for x in range(len(resistances)):
  print(resistances[x],voltage_div(10000, resistances[x], 5.0)) 
#if voltage is 3.3, use 4.7kΩ resistor, if voltage is 5v, use 10kΩ resistor
adc = MCP3008(channel=0)
count = 0
volts = [] #once i connect to the vane and get the readings, I will fill this in with values
while True:
  wind = round((adc.value * 5), 3)
  if not wind in volts:
    volts.append(wind)
    count += 1
    print(adc.value)


