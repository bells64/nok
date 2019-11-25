num_inpt = a = 7484
num_inpt_2 = b = 12312
while num_inpt != num_inpt_2:			# nod
	if num_inpt > num_inpt_2:
		num_inpt = num_inpt - num_inpt_2
	elif num_inpt_2 > num_inpt:
		num_inpt_2 = num_inpt_2 - num_inpt
nok = a * b // num_inpt_2				#nok
print(nok)
