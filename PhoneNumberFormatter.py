import re
import sys

class PhoneNumberFormatter:
    class UK:
        def format(self, number):
            """
            Format input number to output a proper number with UK area code
            number: Input number
            return: Output number
            """

            number = number.replace(" ", "") # Remove all white spaces

            # Use regular expressions to match numbers starting with either
            # 07, +447, or 447 followed by 9 other digits to have a total
            # of 11 digits
            match = re.compile(r'^(07(\d{9})|\+?447(\d{9}))$').search(number)

            # Return the following message if no match was found
            if not match:
                return("Invalid number.")
               
            # Construct the 9 digits without the areacode. group(2) matches
            # 07 case, while group(3) matches +447 or 447 cases
            remainingDigits = match.group(2) if match.group(2) else match.group(3)
            return "+447" + remainingDigits

if __name__ == "__main__": 
    formatter = PhoneNumberFormatter()
    UKFormatter = formatter.UK()

    # Only allow 1 argument to be passed in command line argument
    if len(sys.argv) > 2:
        exit("Please provide only a single number.")

    print(UKFormatter.format(sys.argv[1]))
