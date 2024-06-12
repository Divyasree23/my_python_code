def count_consecutive_characters(input_string):
    # Initialize an empty list to store the characters and their counts
    result = []

    # Initialize a counter and set the previous character to the first character in the string
    count = 1
    prev_char = input_string[0]

    # Loop through the string starting from the second character
    for char in input_string[1:]:
        if char == prev_char:
            # Increment the count if the current character is the same as the previous one
            count += 1
        else:
            # Append the previous character and its count to the result list
            result.append(f"{prev_char}{count}")
            # Reset the count and update the previous character
            count = 1
            prev_char = char

    # Append the last character and its count to the result list
    result.append(f"{prev_char}{count}")

    # Join the list into a single string and return it
    return "".join(result)


# Example usage
input_string = "abcabbb"
output = count_consecutive_characters(input_string)
print(output)

#############################################################################################################################

def count_consecutive_characters(input_string):
    # Initialize an empty result string
    result = ""

    # Initialize a counter and set the previous character to the first character in the string
    count = 1
    prev_char = input_string[0] #a

    # Loop through the string starting from the second character
    for char in input_string[1:]:
        if char == prev_char:
            # Increment the count if the current character is the same as the previous one
            count += 1
        else:
            # Append the previous character and its count to the result string
            result += f"{prev_char}{count}"
            # Reset the count and update the previous character
            count = 1
            prev_char = char

    # Append the last character and its count to the result string
    result += f"{prev_char}{count}"

    return result


# Example usage
input_string = "abcabbbbccaabdaa"
output = count_consecutive_characters(input_string)
print(output)
