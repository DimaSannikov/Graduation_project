def translated_list():
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

    return array, translate


def test_list(array, translate):
    new_array = []

    for line in array:
        new_line = []
        for element in line:
            for elem in translate:
                test_array = []

                if element == elem[0]:
                    test_array.append(elem[1].split("_")[0])
                    test_array.append(elem[1].split("_")[1])
                    new_line.append(test_array)
                
                elif element == elem[0].split("_")[0]:
                    test_array.append(elem[1].split("_")[0])
                    if test_array not in new_line:
                        new_line.append(test_array)
                
                elif element == elem[0].split("_")[1]:
                    if test_array not in new_line:
                        new_line.append(elem[1].split("_")[1])

            if len(element) == 1:
                new_line.append(element)

        new_array.append(new_line)
    return new_array


def lists_of_testing():
    array, translate = translated_list()
    new_array = test_list(array, translate)

    for line in range(1, len(new_array)):
        count = 0
        for element in new_array[line]:
            if len(new_array[0][count]) == 2:
                print(f"{new_array[0][count][0]}_{new_array[0][count][1]}_{element}")
                with open(f"testlists/ready_for_test_{line}.txt", "a") as file:
                    file.writelines(f"{new_array[0][count][0]}_{new_array[0][count][1]}_{element}\n")
            else:
                print(f"{new_array[0][count][0]}_{element}")
                with open(f"testlists/ready_for_test_{line}.txt", "a") as file:
                    file.writelines(f"{new_array[0][count][0]}_{element}\n")
            count += 1

    return len(new_array)

# lists_of_testing()