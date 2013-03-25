def func(input):
	if input > 0 and input < 10 :
		return input + 10
	elif input >= 10 and input < 100 :
		return input * 0.1
	else :
		return 'False'

inputNum = int(raw_input("PLEASE INPUT NUMBER : "))
print func(inputNum)
