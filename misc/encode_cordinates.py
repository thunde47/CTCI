#works only for unsigned integers
bits=16
def encode(x,y):
	return (x<<bits) | y

def decode(encoded):
	#return (encoded>>bits, encoded & ~(~0 <<bits))
	return (encoded>>bits, encoded & 0xFFFF)

if __name__=="__main__":
	encoded=encode(3,1500)
	print(decode(encoded))
