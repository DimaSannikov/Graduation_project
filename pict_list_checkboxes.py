array = []
edit_letters = []

with open("checkboxes.txt", "r") as file:
    for line in file:
        array.append(line.rstrip())

with open("translit_new.txt", "r") as fl:
    for ln in fl:

        edit_letters.append(ln.rstrip())

for line in array:

    translate_line = line
    for symbol in line:

        for letter in edit_letters:
            if symbol == letter[0]:
                translate_line = translate_line.replace(symbol, letter[2:])

    if len(translate_line) != 0:
        translate_line = translate_line.split("_")[0][0: 3] + "_" + translate_line.split("_")[1]
        print(f"{translate_line}")
        
        with open("translate_for_pict.txt", "a") as file:
            file.writelines(f"{translate_line} a, i")                      # a - active checkbox, i - inactive
            file.write("\n")