#1
s = "Thirty" + " Days" + " of" + " Python"
print(s)

#2 same as above

#3
company = "Coding For All"

#4
print(company)

#5
print(len(company))

#6
upper_c = company.upper()
print(upper_c)

#7
lower_c = company.lower()
print(lower_c)

#8
print(company.capitalize()) # converts first character into capital letter
print(company.title()) # converts first character of every word into capital letter
print(company.swapcase()) # swaps the case of each letter compared to case in the original string

#9
print(company.split(" ")[0])

#10
print(company.index("Coding")) #raises ValueError if not found. Also works on list, tuples
print(company.find("Coding")) #returns 1 if not found. Works only on string

#11
print(company.replace("Coding","Python"))

#12 same as above

#13 already done in 9

#14 same as above

#15
print(company[0])

#16
print(company[-1])
#17
print(company[10])

#32


#33
print("I am enjoying this challenge.\nI just wonder what is next.")

#34 use \t

#35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

#36
a = 8
b = 6

print(f"{a} + {b } ={a+b}")
print(f"{a} - {b } ={a-b}")
print(f"{a} * {b } ={a*b}")
print(f"{a} / {b } ={a/b:.2f}")
print(f"{a} % {b } ={a %b}")
print(f"{a} // { b} = {a // b}")
print(f"{a} ** { b} = {a ** b}")