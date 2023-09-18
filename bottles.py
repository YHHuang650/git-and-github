beverage = "Coke"
count = 100

# print(count, "bottles of", beverage, "on the wall")
# print(count, "bottles of", "water")
# print("Take one down, pass it around")
# count = count - 1
# print(count, "bottles of", beverage, "on the wall")

# print("Take one down, pass it around")
# count = count - 1
# print(beverage,"is healthy!")

# print(count, "bottles of", beverage, "on the wall")
# print(count, "bottles of", beverage)
# print("Take one down, pass it around")
# count = count - 1
# print(beverage,"is healthy!")

# print(count, "bottles of", beverage, "on the wall")
# print(count, "bottles of", beverage)
# print("Take one down, pass it around")
# count = count - 1
# print(beverage,"is healthy!")

# print(count, "bottles of", beverage, "on the wall")
# print(count, "bottles of", beverage)
# print("Take one down, pass it around")
# count = count - 1
# print(beverage,"is healthy!")

# print(count, "bottles of", beverage, "on the wall")
# print(count, "bottles of", beverage)
# print("Take one down, pass it around")
# print(beverage,"is healthy!")

for i in range(100):
    print(count, "bottles of", beverage, "on the wall")
    print(count, "bottles of", "water")
    if(count % 2 == 1):
        print("If one of those bottles should happen to fall, 98 bottles of beer on the wall...")
    else:
        print("Take one down, pass it around")
    count = count - 1

print("No more bottles of beer on the wall, no more bottles of beer.") 
print("We've taken them down and passed them around; now we're drunk and passed out!")
   
