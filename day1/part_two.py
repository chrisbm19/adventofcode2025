def main():
    # initialize variables
    pos = 50
    count = 0

    # update position and increment count if position is 0
    with open("puzzle_input.txt") as input:
        for line in input:
            if line[0] == 'L':
                pos = (pos - int(line[1:])) % 100
                if int(line[1:]) > 100:
                    count += int(line[1:]) // 10
            else:
                pos = (pos + int(line[1:])) % 100
                if int(line[1:]) > 100:
                    count += int(line[1:]) // 10
            count += 1 if pos == 0 else 0

    # print result
    print("--------------------")
    print(f"Password: {count}")
    print("--------------------")

    return 0

main()
