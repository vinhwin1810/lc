# Let's implement the decode function and apply it to the uploaded input file

def decode(message_file_path):
    # Read the content of the file
    with open(message_file_path, 'r') as file:
        lines = file.readlines()

    # Split the content into a list of tuples (number, word)
    number_word_pairs = [line.strip().split(' ') for line in lines]
    number_word_pairs = [(int(number), word) for number, word in number_word_pairs]

    # Sort the list by the number (first item in the tuples)
    number_word_pairs.sort(key=lambda pair: pair[0])

    # Initialize the pyramid
    pyramid = []
    current_line = []
    expected_number = 1

    # Decode the message
    decoded_words = []

    for number, word in number_word_pairs:
        # Add the number to the current line
        current_line.append(number)

        # Check if the number is at the end of the current line of the pyramid
        if number == expected_number:
            # If it is, add the corresponding word to the decoded message
            decoded_words.append(word)
            # And reset the current line for the next level of the pyramid
            current_line = []
            # Increment the expected number at the end of the next pyramid line
            expected_number += len(pyramid) + 2

    # Join the decoded words into a single string
    return ' '.join(decoded_words)

# Use the provided input file
input_file_path = '/mnt/data/coding_qual_input.txt'
decoded_message = decode(input_file_path)
decoded_message
