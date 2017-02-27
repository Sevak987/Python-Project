s = raw_input("Dwse noumera me kena na ta valw se lista       ")
numbers = map(int, s.split())

for i in range (len(numbers)) :
     if numbers[i]==0:
	  numbers.remove(0)
	  numbers.append(0)
	
print numbers