array = []
translate = []


with open("translate_for_test.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        line = line.split("\t")
        translate.append(line)

with open("pairwise.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        line = line.split("\t")
        array.append(line)

# print(array[0])


new_array = []

for line in array:
# line = array[0]
    new_line = []
    for element in line:
        for elem in translate:
            test_array = []

            if element == elem[0]:
                test_array.append(elem[1].split("_")[0])
                test_array.append(elem[1].split("_")[1])
                new_line.append(test_array)
                # print(test_array)
                # print(elem[1].split("_")[0], elem[1].split("_")[1])                               # element.split("_"), 
            
            elif element == elem[0].split("_")[0]:
                test_array.append(elem[1].split("_")[0])
                if test_array not in new_line:
                    new_line.append(test_array)
                    # print(test_array)
            
            elif element == elem[0].split("_")[1]:
                # test_array.append(elem[1].split("_")[1])
                if test_array not in new_line:
                    new_line.append(elem[1].split("_")[1])
                    # print(element, test_array)

        if len(element) == 1:
            new_line.append(element)

    # print(new_line)
    new_array.append(new_line)


for line in range(1, len(new_array)):
    count = 0
    for element in new_array[line]:
        print(f"{new_array[0][count]}\t{element}")
        with open(f"testlists/ready_for_test_{line}.txt", "a") as file:
            file.writelines(f"{new_array[0][count]}\t{element}\n")
        count += 1

# while position < len(array[0]):
#     with open(f"testlists/list_for_test_1.txt", "a") as file:
#         file.writelines(f"{array[0][position]}\t{array[1][position]}\n")
#     print(array[0][position], array[1][position])
#     position += 1