def main():
    first_list, second_list = __load_input_data("src/day_1/input.txt")
    result_1 = problem_1(first_list, second_list)
    print(result_1)
    result_2 = problem_2(first_list, second_list)
    print(result_2)


def problem_1(first_list: list, second_list: list) -> int:
    sorted_first_list = sorted(first_list)
    sorted_second_list = sorted(second_list)

    return sum(
        [
            abs(sorted_first_list[i] - sorted_second_list[i])
            for i in range(len(sorted_first_list))
        ]
    )


def problem_2(first_list: list, second_list: list) -> int:
    similarity_score = 0
    for x in first_list:
        num_appearances = 0
        for y in second_list:
            if x == y:
                num_appearances += 1
        similarity_score += x * num_appearances

    return similarity_score


def __load_input_data(file_name: str) -> tuple[list, list]:
    # Load input.txt each line is two numbers separated by spaces, load first column into one list and second column into another list
    with open(file_name) as f:
        lines = f.readlines()
        first_column = []
        second_column = []
        for line in lines:
            first, second = line.split()
            first_column.append(int(first))
            second_column.append(int(second))
    return first_column, second_column


if __name__ == "__main__":
    main()
