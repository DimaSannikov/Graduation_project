array = []
edit_letters = []

with open("00:35_checkboxes.txt", "r") as file:
    for line in file:
        array.append(line.strip())

with open("translit_new.txt", "r") as fl:
    for ln in fl:

        edit_letters.append(ln.strip())

for line in array:

    translate_line = line
    for symbol in line:

        for letter in edit_letters:
            if symbol == letter[0]:
                line = line.replace(":", "")
                translate_line = translate_line.replace(symbol, letter[2:]).replace(":", "")

    if len(translate_line) != 0:
        translate_line = translate_line.split("_")[0][0: 3] + "_" + translate_line.split("_")[1]
        
        print(f"{translate_line}\t{line}")

        with open("translate_for_test.txt", "a") as file:
            file.writelines(f"{translate_line}\t{line}")
            file.write("\n")