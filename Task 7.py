def manual_sort(numbers):

    sorted_list = numbers[:]
    n = len(sorted_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:

                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list


def analyze_list(numbers):

    total = 0
    count = 0

    if len(numbers) == 0:
        return {
            "sum": 0,
            "average": 0,
            "min": None,
            "max": None,
            "sorted_list": []
        }

    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:
        total += num
        count += 1
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    average = total / count if count != 0 else 0

    sorted_numbers = manual_sort(numbers)

    return {
        "sum": total,
        "average": average,
        "min": minimum,
        "max": maximum,
        "sorted_list": sorted_numbers
    }


def print_statistics(stats):

    for index, (key, value) in enumerate(stats.items(), start=1):
        print(f"{index}. {key.capitalize()}: {value}")


def get_user_input():

    while True:
        user_input = input("Enter numbers separated by spaces: ").strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue

        parts = user_input.split()
        numbers = []
        valid = True

        for part in parts:
            try:
                num = float(part)
                numbers.append(num)
            except ValueError:
                print(f"Invalid number '{part}'. Please enter only numbers.")
                valid = False
                break

        if valid:
            return numbers



if __name__ == "__main__":
    numbers = get_user_input()
    stats = analyze_list(numbers)
    print("\nSummary of Calculated Statistics:")
    print_statistics(stats)
