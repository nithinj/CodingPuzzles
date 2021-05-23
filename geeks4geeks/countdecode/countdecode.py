def countDecode(num_str):
    if not num_str:
        return 0

    # if each digit represents an alphabet
    count = 1
    for i in range(len(num_str) - 1):
        if int(num_str[i:i+2]) <= 26:
            count += 1
    return count

if __name__ == "__main__":
    inp = input()
    res = countDecode(inp)
    print(str(res))