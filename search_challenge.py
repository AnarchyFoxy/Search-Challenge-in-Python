def searching_challenge(s):
    words = s.split()
    max_word = None
    max_count = 1  # Minimum count for comparison is 1 (single occurrence)

    for word in words:
        char_counts = [0] * 256  # Assuming ASCII characters
        repeat_count = 0

        # Count occurrences of each character in the word
        for c in word:
            char_counts[ord(c)] += 1

        # Find the maximum count of any character in the word
        for count in char_counts:
            if count > 1 and count > max_count:
                repeat_count = count
                max_count = count

        # If the word has the greatest number of repeated letters, store it
        if repeat_count == max_count:
            max_word = word
            break  # Break out of the loop to get the first word with the max count

    if max_word is None:
        return "-1"

    # Concatenate the first output word with the ChallengeToken
    output1 = max_word + "egfs90hz78b"

    # Replace every third character in the first output with 'X'
    result1 = list(output1)
    for i in range(2, len(result1), 3):
        result1[i] = 'X'
    output1 = ''.join(result1)

    # Concatenate the second output word with the ChallengeToken
    output2 = max_word + "egfs90hz78b"

    # Replace every third character in the second output with 'X'
    result2 = list(output2)
    for i in range(2, len(result2), 3):
        result2[i] = 'X'
    output2 = ''.join(result2)

    # Return the two concatenated and modified output strings
    return output1 + output2

# Test the function with the example input
input_str = "Today, is the greatest day ever!"
output_str = searching_challenge(input_str)
print(output_str)  # Output: "grXatXstXgfX90Xz7XbgrXatXstXgfX90Xz7X"
