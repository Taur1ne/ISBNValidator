class ISBNValidator(object):
	@staticmethod
	def validate(isbn):
		lst = isbn.replace('-', '')
		sum = 0
		index = 0
		for x in range(1,11,)[::-1]:	
			item = lst[index].upper()
			if item != "X" :
				sum += int(item) * x
			else:
				sum += 10 * x
			index += 1
		return (sum % 11 == 0)
		

print ISBNValidator.validate("0-7475-3269-9")
print ISBNValidator.validate("156881111x")

	
