amount = int(input("enter the amount : "))

notes_of_500 = 0
notes_of_200 = 0
notes_of_100 = 0
notes_of_50 = 0
notes_of_20 = 0
notes_of_10 = 0

#calculating the notes

notes_of_500 = amount // 500
amount = amount - (notes_of_500 * 500)
notes_of_200 = amount // 200
amount = amount - (notes_of_200 * 200)
notes_of_100 = amount // 100
amount = amount - (notes_of_100 * 100)
notes_of_50 = amount // 50
amount = amount - (notes_of_50 * 50)
notes_of_20 = amount // 20
amount = amount - (notes_of_20 * 20)
notes_of_10 = amount // 10
amount = amount - (notes_of_10 * 10)

#printing results

print("notes of 500 : ", notes_of_500)
print("notes of 200 : ", notes_of_200)
print("notes of 100 : ", notes_of_100)
print("notes of 50 : ", notes_of_50)
print("notes of 20 : ", notes_of_20)
print("notes of 10 : ", notes_of_10)