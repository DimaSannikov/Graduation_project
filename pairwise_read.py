array = []
translate = []


with open("translate_for_test.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        line = line.split("\t")
        translate.append(line)

# print(translate)

# for elem in translate:
#     print(elem[0], elem[1])

with open("pairwise.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        line = line.split("\t")
        array.append(line)

# print(array)

new_array = []

for line in array:
    new_line = []
    for element in line:
        # print(element)
        for elem in translate:
            if element == elem[0]:
                print(element.split("_"), elem[1].split("_"))
            elif element == elem[0].split("_")[1]:
                print(elem[0].split("_")[1], elem[1].split("_")[0], elem[1].split("_")[1])

# while position < len(array[0]):
#     with open(f"testlists/list_for_test_1.txt", "a") as file:
#         file.writelines(f"{array[0][position]}\t{array[1][position]}\n")
#     print(array[0][position], array[1][position])
#     position += 1