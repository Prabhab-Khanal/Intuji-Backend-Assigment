numbers = [8, 7, 2, 5, 3, 1]
target = 10


def check_sum(numbers,target):
    seen = set()
    pairs = []

    for num in numbers:
        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    print("Pairs found:", pairs)


print(check_sum(numbers,target))