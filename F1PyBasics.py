x = 5
num = 10
sum = x*num
print("sum", sum)

print(type(num))

print(5/2)
print(5//2)

print(5*2)
print(5**2)

a = "hello"
print('h' in a)
print('g' in a)

if('h' in a):
    print("hurra!")

if('g' in a):
    print("buu!")


age = 18
if age > 18:
    print("you were allowed")
else:
    print("not allowed")

count = 1
while(count < 10):
    print("the value of count is:", count)
    count+=1
print("normal block")

for i in 'hello':
    print(i)

for j in range(1,10,3):     # Starter på 1, til (ikke tom.) 10, hopper 3 om gangen)
    print(j)

fruits = ['apple', 'banana', 'mango']
# Unødvendig:
# for fruit in fruits:
#     print(fruits)
print(*fruits)

fruits[1] = 'orange'
print(*fruits)

print("Listens lengde:", len(fruits))

a = [1,2]
b = [3,4]
c = a+b
print(c)

print(c[1:])
print(c[1:3])

c.append(100)
print(c)

print(1 in c)
print(1000 in c)

#Tuple is immutable
#Parentes i stedet for brackets

print("Dictionary:")

car = {
    "brand": "tesla",
    "year": 2022
}
print(car['year'])

print("Function:")

def add(num1, num2):
    return int(num1) + int(num2)
n1 = input('Enter number 1:')
n2 = input('Enter number 2:')
output = add(n1,n2)
print('Result is: ', output)

print("Oblig:")

# bw = []
# with open(data.txt) as file_name:
#     for line in file_name:
#         bw.append(line.split()[0])
# print()