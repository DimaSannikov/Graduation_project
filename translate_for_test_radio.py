array = []
edit_letters = []

with open("00:35_radiobuttons.txt", "r") as file:
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
        line = line.rstrip(",").replace(":", ",").split("_")[0].split(", ")
        translate_line = translate_line.rstrip(",").replace(":", ",").split("_")[0].split(", ")
        print(f"{translate_line}\t{line}")
        for i in range(1, len(line)):
            print(f"{translate_line[0]}_{translate_line[i]}\t{line[0]}_{line[i]}")
        
            with open("translate_for_test.txt", "a") as file:
                file.writelines(f"{translate_line[0]}_{translate_line[i]}\t{line[0]}_{line[i]}")
                file.write("\n")
