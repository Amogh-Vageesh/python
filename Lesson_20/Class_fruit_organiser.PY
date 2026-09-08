basket1 = {"apple", "banana", "mango", "apple", "grape"}
basket2 = {"mango", "kiwi", "banana", "kiwi"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

basket1.add("orange")
print("basket 1 after adding orange: ", basket1)

common_Fruits = basket1.intersection(basket2)
print("Fruits in both baskets", common_Fruits)

import array as arr
fruits_count = arr.array('i', [3,5,2,4])
print("Fruits count array:", fruits_count)

fruits_count.insert(0,1)
fruits_count.append(6)
print("Fruits count after adding items: ", fruits_count)

count_of_4 = fruits_count.count(4)
print("No. of times 4 appears: ", count_of_4)

print("")
print("===== CLASS FRUIT BASKET ORGANISER =====")
print("basket1 : ", basket1)
print("basket2 : ", basket2)
print("shared fruits : ", common_Fruits)
print("fruits count : ", fruits_count)
print("========================================")

fruits_count.reverse()
print(f"reversed fruit count array: {fruits_count} \n")