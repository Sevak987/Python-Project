print "Dwse mia protasi pou na periexei kai thavmastika kai des to magiko"
text=raw_input()
mhkos=len(text)

flag=1
mhkos2=mhkos

while (mhkos>0) and (flag==1):
	mhkos=mhkos-1
	if text[mhkos]!=("!"):
		mhkos2=mhkos
		flag=0
mhkos2=mhkos2+1	
newtext=text.replace("!","") 
diafora=len(text)-mhkos2
newtext=newtext + diafora*"!"
print newtext