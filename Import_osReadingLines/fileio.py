try:
    text = open(input("Enter source file name: "))
    destination = input("Enter destination file: ")

    lines = [line.rstrip() for line in text]
    new_text = ""
    header = True

    for line in lines:
        if header:
            new_text += "Name Average\n"
            header = False

        else:
            values = line.split(" ")
            name = values[0]
            average = ((float(values[1]) + float(values[2]) + float(values[3]) + float(values[4]) ) / 4)
            new_text += name + " " + str(average) + "\n"

    new_file = open(destination, "x")
    new_file.write(new_text)
    new_file.close()
    print(new_text)

except FileNotFoundError:
    print("- Error: file not found!")