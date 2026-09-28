from gpiozero import MCP3008
import time

def voltage_div(r1, r2, v_in):
  v_out = (v_in * r1)/(r1 + r2) #v_in is voltage input and v_out is the voltage output
  return round(v_out, 3)


#Also need an MCP3008 to conevrt analog to digital

resistances = [33000, 6570, 8200, 891, 1000, 688, 2200, 1410, 3900,
               3140, 16000, 14120, 120000, 42120, 64900, 21880]
# got these from the data sheet, assuming its correct
for x in range(len(resistances)):
  print(resistances[x])

adc = MCP3008(channel=0)

print(adc.value)

