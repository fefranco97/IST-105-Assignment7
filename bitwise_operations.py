import sys
numbers_str = sys.argv[1].split(',')
threshold = int(sys.argv[2])

def validate_input(numbers):
    return [int(num) for num in numbers]

def bitwise_operations(numbers):
    if not numbers:
        return 0, 0, 0

    bitwise_and = numbers[0]
    bitwise_or = numbers[0]
    bitwise_xor = numbers[0]

    for num in numbers[1:]:
        bitwise_and &= num
        bitwise_or |= num
        bitwise_xor ^= num

    return bitwise_and, bitwise_or, bitwise_xor

def filter_numbers(numbers, threshold):
    return [num for num in numbers if num > threshold]


def main():
    numbers = validate_input(numbers_str)
    bitwise_and, bitwise_or, bitwise_xor = bitwise_operations(numbers)
    
    print(f"Bitwise AND: {bitwise_and}")
    print(f"Bitwise OR: {bitwise_or}")
    print(f"Bitwise XOR: {bitwise_xor}")
    
    filtered_numbers = filter_numbers(numbers, threshold)
    print(f"Numbers greater than threshold: {filtered_numbers}")

if __name__ == "__main__":
    main()

    

