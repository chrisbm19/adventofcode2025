def main():
    # initialize variables
    sum = 0
    puzzle_input = ""

    # read puzzle input
    with open("puzzle_input.txt") as input:
        puzzle_input = input.read()

    input_list = puzzle_input.split(",")

    for r in input_list:
        input_range = r.split("-")
        start = int(input_range[0])
        end = int(input_range[1])
        all_inputs_int = list(range(start, end+1))
        all_inputs_str = [str(x) for x in all_inputs_int]
        for i in all_inputs_str:
            mid = len(i) // 2
            front_half = i[:mid]
            back_half = i[mid:]
            if front_half == back_half:
                sum += int(i)

    # print result
    print("--------------------")
    print(f"Sum: {sum}")
    print("--------------------")

    return

main()
