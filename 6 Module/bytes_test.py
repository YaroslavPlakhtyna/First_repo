#byte_str = "some text".encode()
#print(byte_str)
#
#numbers = [0, 128, 255]
#byte_numbers = bytes(numbers)
#print(byte_numbers)
#
#for num in [127, 255, 156]:
#  print(hex(num))

byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array) # bytearray(b'Bill Kill')