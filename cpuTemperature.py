#cpu temperature @see https://raspberrypi.stackexchange.com/questions/85415/how-to-directly-get-cpu-temp-in-python
from gpiozero import CPUTemperature
cpu = CPUTemperature()
print(cpu.temperature)

