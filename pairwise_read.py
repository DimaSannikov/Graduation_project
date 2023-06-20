array = []
translate = []


with open("translate_pairwise.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        line = line.split("\t")
        translate.append(line)

# print(translate)

with open("pairwise.txt", "r") as file:
    line_count = 0
    for line in file:
        line = line.replace("\n", "")
        line = line.split("\t")
        array.append(line)
        pos_elem = 0
        while pos_elem < len(array[0]):
            # print(new_line[0][pos_elem])
            for elem in translate:
                if array[line_count][pos_elem] == elem[0]:
                    # print(new_line[line_count][pos_elem], elem[1])
                    array[line_count][pos_elem] = elem[1]
            pos_elem += 1
        line_count += 1

# for line in array:
#     position = 0
#     while position < len(array[0]):
#         print(array[0][position], line[position])
#         position += 1

position = 0
while position < len(array[0]):
    print(array[0][position], array[1][position])
    position += 1