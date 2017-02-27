s = raw_input("Dwse parenthesis      ")
ds=0
da=0
		

for i in range (len(s)) :
	    if s[i]==')':
		   ds=ds + 1
	    if s[i]=='(':
			da=da + 1 
		
 
if (ds==da):
	print "True"
if (ds>da):
		print "False"
if (ds<da):
			print "False"
		

		



    


