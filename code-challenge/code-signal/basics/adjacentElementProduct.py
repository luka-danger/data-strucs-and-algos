myArray = [4, -6, 3, 7]

def solution(inputArray):
    return max(
        [inputArray[i] * inputArray[i + 1] for i in range(0, len(inputArray) - 1)]
    )

print(solution(myArray))