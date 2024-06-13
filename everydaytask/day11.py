def roman_to_integer(roman):
    # Dictionary to store Roman numeral values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # Initialize the result variable
    integer_value = 0

    # Loop through the input string
    for i in range(len(roman)):
        # Get the value of the current Roman numeral
        #print(roman_values[roman[i]],roman)
        current_value = roman_values[roman[i]] #IX

        # If not the last character and the current numeral is less than the next numeral
        #print(i,( len(roman)-1),current_value)
        #print("romanvalue",roman_values[roman[i + 1]],"MCMXCIII") #1993
        if i < len(roman) - 1 and current_value < roman_values[roman[i + 1]]:
            # Subtract the current value
            integer_value -= current_value
        else:
            # Add the current value
            integer_value += current_value

    return integer_value

# Example usage
#print(roman_to_integer("IX"))  # Output: 9
print(roman_to_integer("LVIII"))  # Output: 58
print(roman_to_integer("MCMXCIII"))  # Output: 1994
