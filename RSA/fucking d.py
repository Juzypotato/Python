d = 1
e = 83
l = 144
while True:
	if (d*e) % l == 1:
		print("The first possible value of d is ",d)
		break
	else:
		d += 1
