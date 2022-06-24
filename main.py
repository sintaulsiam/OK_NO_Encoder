
from os import system


def toBinary(str):
    bin = ""
    for i in str:
        if i == ' ':
            bin += "  "
            continue
        bin += format(ord(i), '8b')
        bin += " "

    return bin


def toEncoded(bin):
    str = ""
    for i in bin:
        if i == '0':
            str += "NO"
        elif i == '1':
            str += ("OK")
        str += (" ")
    return str


def toStirng(str):
    out_str = ""
    for i in str.split("  "):
        temp = ""
        for j in i.split(" "):
            if j == "NO":
                temp += '0'
            elif j == "OK":
                temp += '1'
        out_str += chr(int(temp, 2)) if temp else " "
    out_str += " "
    return out_str


if __name__ == "__main__":
    print("Enter the txt:")
    input_str = ""

    while True:
        input_str = input(">").strip()

        if input_str.startswith('-c'):
            system("clear")
            continue

        if input_str.startswith("q"):
            break
        if (not input_str.startswith("-e") and not input_str.startswith("-d")):
            print("No instruction found")
            continue

        output_str = ""

        if input_str.startswith("-e"):

            bin = toBinary(input_str[2:].strip())
            output_str = toEncoded(bin)

        if input_str.startswith("-d"):
            output_str = toStirng(input_str[2:].strip())

        print(f"The ouput is: {output_str}")
        print("\n")
