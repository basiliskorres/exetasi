strs="My name! is! basilis! korres!"
count=strs.count("!")-1
strs = strs.replace('!','',count)
print (strs)
