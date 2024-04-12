def decode_with_triangular_pattern(message_file):
    # Read the file and store the number-word pairs
    with open(message_file, 'r') as file:
        lines = file.readlines()
        pairs = [line.strip().split() for line in lines]
        pairs = [(int(num), word) for num, word in pairs]

    # Sort the pairs based on the numbers
    pairs.sort(key=lambda x: x[0])

    # Initialize variables for tracking the current line and the triangular number
    message_words = []
    triangular_number = 1
    line_number = 1

    # Iterate through the sorted pairs to find the words at the end of each pyramid line
    for num, word in pairs:
        if num == triangular_number:
            message_words.append(word)
            line_number += 1
            triangular_number = line_number * (line_number + 1) // 2  # Calculating the next triangular number

    # Concatenate the message words to form the decoded message
    return ' '.join(message_words)

print(decode_with_triangular_pattern('C:/Users/Vinh/Desktop/lc/coding_qual_input.txt'))

# Function to generate the pyramid numbers up to the triangular number 21
def generate_pyramid_numbers(upper_limit):
    pyramid_numbers = []
    current_line = 1
    number = 1
    while number <= upper_limit:
        line_numbers = []
        for _ in range(current_line):
            if number > upper_limit:
                break
            line_numbers.append(number)
            number += 1
        pyramid_numbers.append(line_numbers)
        current_line += 1
    return pyramid_numbers

# Generating the pyramid numbers up to 21
pyramid_numbers = generate_pyramid_numbers(400)
print(pyramid_numbers)
