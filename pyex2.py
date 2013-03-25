def absolute_value(num):
	print '|NUMBER| :',
	if num > int(0) :
		print num
	else :
		print -num

inputNum = int(raw_input('PLEASE INPUT NUMBER : '))
absolute_value(inputNum)
