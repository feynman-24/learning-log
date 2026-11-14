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

#18
print("".join(w[0] for w in 'Python For Everyone'.split()))

#19
print("".join(w[0] for w in company.split()))

#20
print(company.index("C"))

#21
print(company.index("F"))

#22
print(company.rfind("l"))

#23
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

#24
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))


#25
sentence = 'You cannot end a sentence with because because because is a conjunction'
target = 'because because because'
start = sentence.find(target)
end = start + len(target)

print(sentence[start:end])

#26
print(sentence.find("because"))

#27 same as 25

#28
print(company.startswith("Coding"))

#29
print(company.endswith("coding"))

#30
print('   Coding For All      '.strip())

#31 ans is second one
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

#32
print("#".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

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