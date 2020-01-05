n="((())))"
n=list(n)
opening=0
closing=0
for i in range(0,len(n)):
	if n[i]==')':
		opening=opening+1
	if n[i]=='(':
		closing=closing+1
if opening==closing:
	print(opening)
if opening>closing:
	print(closing*2)
if opening<closing:
	print(opening*2)