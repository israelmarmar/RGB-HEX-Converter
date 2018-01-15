hexdigits="0123456789ABCDEF"

def bintohex(b):
	b=int(b[2:],2)
	g1=b & 0b000000001111
	g2=(b & 0b000011110000) >> 4
	g3=(b & 0b111100000000) >> 8

	if g3==0:
		return hexdigits[g2]+hexdigits[g1]
	else:
		return hexdigits[g3]+hexdigits[g2]+hexdigits[g1]


def rgbtohex(r,g,b):
	r=bintohex(bin(r))
	g=bintohex(bin(g))
	b=bintohex(bin(b))
	return "#"+r+g+b

print rgbtohex(255,255,254)
