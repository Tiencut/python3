T = int(input())

def convert_to_binary(demical):
    binary = ""

    if demical == 0:
        binary = "0"

    while demical > 0:
        binary = str(demical%2) + binary
        demical = demical // 2
        
    return binary

print(convert_to_binary(T))