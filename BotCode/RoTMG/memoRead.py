from ReadWriteMemory import ReadWriteMemory
from random import randint

target = ""
some_address = 0x008

rwm = ReadWriteMemory()

process = rwm.get_process_by_name(target)
process.open()

mem = process.get_pointer(some_address, offsets=[])

