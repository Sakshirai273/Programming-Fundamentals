"""Format strings can be helpful to visualize or output byte values. 
Format strings require an integer value so the byte will have to be converted 
to an integer first."""

a_byte = b'\xff'  # 255
i = ord(a_byte)   # Get the integer value of the byte

bin = "{0:b}".format(i) # binary: 11111111
hex = "{0:x}".format(i) # hexadecimal: ff
oct = "{0:o}".format(i) # octal: 377

print(bin)
print(hex)
print(oct)


