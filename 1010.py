
#1st Solved
a=input().split(" ")
b=input().split(" ")
c,d,e=a
f,g,h=b
p=(int(d)*float(e))+(int(g)*float(h))
print(f"VALOR A PAGAR: R$ {p:.2f}")

#2nd Solved
x=input().split()[1:]
y=input().split()[1:]
p=(int(x[0])*float(x[1]))+(int(y[0])*float(y[1]))
print(f'VALOR A PAGAR: R$ {p:.2f}')

#3rd solved
#Example বুঝার জন্য কিছু উদাহরণ
#আমি পড়াশোনা খুব একটা বুুঝি না  তাই কিছু উদাহরণ লিখে রাখছি

a=('odd')
print('a is odd') if a=='odd' else print('Even')
a=('kkk')
print('a is odd') if a=='odd' else print('Even')
a=float(input())#
print(float()) if a==float() else print("int()")

#বুঝি নাই কিন্তু করে রাখছি কোনো সময় বুঝলে করে রাখব

a= [float(a) if '.' in a else int(a) for a in input().split(' ')[1:]]
b= [float(a) if '.' in a else int(a) for a in input().split(' ')[1:]]

p=a[0]*a[1] + b[0]*b[1]
print(f'VALOR A PAGAR: R$ {p:.2f}')