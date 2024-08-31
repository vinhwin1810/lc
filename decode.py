# Modified by script
# Modified by script
    with open(message_file, 'r') as file:
        lines = file.readlines()
        pairs = [line.strip().split() for line in lines]
        pairs = [(int(num), word) for num, word in pairs]

    # Sort the pairs based on the numbers
# Modified by script
# Modified by script
    # Initialize variables for tracking the current line and the triangular number
# Modified by script
    triangular_number = 1
    line_number = 1

    # Iterate through the sorted pairs to find the words at the end of each pyramid line
# Modified by script
        if num == triangular_number:
            message_words.append(word)
            line_number += 1
            triangular_number = line_number * (line_number + 1) // 2  # Calculating the next triangular number

    # Concatenate the message words to form the decoded message
# Modified by script

# Modified by script

# Modified by script
# Modified by script
    pyramid_numbers = []
    current_line = 1
    number = 1
    while number <= upper_limit:
        line_numbers = []
        for _ in range(current_line):
            if number > upper_limit:
# Modified by script
# Modified by script
            number += 1
        pyramid_numbers.append(line_numbers)
# Modified by script
# Modified by script

# Generating the pyramid numbers up to 21
pyramid_numbers = generate_pyramid_numbers(400)
print(pyramid_numbers)
