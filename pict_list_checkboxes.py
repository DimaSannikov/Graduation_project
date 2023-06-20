new_line = []
new_letters = []

with open("19:09_checkboxes.txt", "r") as file:
    for line in file:
        # print(line.rstrip())
        new_line.append(line.rstrip())

with open("translit_new.txt", "r") as fl:
    for ln in fl:
        # print(ln.rstrip())

        new_letters.append(ln.rstrip())

for line in new_line:

    translate_line = line
    # print(line)
    for symbol in line:
        # print(symbol)

        for letter in new_letters:
            if symbol == letter[0]:
                # print(f"{symbol} ==>> {letter[-1]}")
                translate_line = translate_line.replace(symbol, letter[2:])
            # if symbol == " ":
            #     translate_line = translate_line.replace(" ", "_")

    if len(translate_line) != 0:
        with open("translate_for_pict.txt", "a") as file:
            # yuuniworks.append()
            file.writelines(f"{translate_line} active, inactive")
            file.write("\n")

        # with open("translate_pairwise.txt", "a") as file:
        #     # yuuniworks.append()
        #     line = line.replace("_", " ").split(" ", 1)[1].replace(":", "")
        #     translate_line = translate_line.replace(":", "")
        #     file.writelines(f"{translate_line}\t{line}")
        #     file.write("\n")