#ax2 + bx + c = 0
def sqrt(x):
	return x**0.5

def NhapDL():
	s = input("Nhập 3 số a, b, c cách nhau bởi dấu cách: ")
	snum = s.split()
	return float(snum[0]), float(snum[1]), float(snum[2])

def GiaiPT1(b, c):
	if b!=0:
		print("Phương trình có 1 nghiệm duy nhất:",round(-c/b,1))
	elif c==0:
		print("Phương trình có vô số nghiệm")
	else:
		print("Phường trình vô nghiệm")

def GiaiPT2(a, b, c):
	if a == 0:
		GiaiPT1(b, c)
	else:
		delta = b*b - 4*a*c
		if delta > 0:
			x1 = (-b + sqrt(delta))/(2*a)
			x2 = (-b - sqrt(delta))/(2*a)
			print("Phương trình có 2 nghiệm phân biệt")
			print("x1=",round(x1,3),"x2=",round(x2,3))
		elif delta == 0:
			x = (-b / (2*a))
			print("Phương trình có nghiệm kép")
			print("x1,2 = ",round(x,1))
		else:
			print("Phương trình vô nghiệm")

a,b,c = NhapDL()
GiaiPT2(a, b, c)