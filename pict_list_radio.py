new_line = []
new_letters = []

with open("19:09_radiobuttons.txt", "r") as file:
    for line in file:
        # print(line.rstrip())
        new_line.append(line.rstrip())

# print(new_line)

with open("translit_new.txt", "r") as fl:
    for ln in fl:
        # print(ln.rstrip())

        new_letters.append(ln.rstrip())

for line in new_line:

    translate_line = line

    for symbol in line:

        for letter in new_letters:
            if symbol == letter[0]:
                # print(f"{symbol} ==>> {letter[-1]}")
                translate_line = translate_line.replace(symbol, letter[2:])
            if symbol == " ":
                line = line.replace(":", ",")
                translate_line = translate_line.replace(":", ",")

    line = line.strip(",").split(", ")
    translate_line = translate_line.strip(",").split(", ")

    elements_count = 0

    while elements_count < len(line):
        with open("translate_pairwise.txt", "a") as file:
            file.writelines(f"{translate_line[elements_count]}\t{line[elements_count]}")
            file.write("\n")
        
        elements_count += 1
