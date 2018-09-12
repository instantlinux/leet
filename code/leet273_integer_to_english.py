"""integer_to_english (273)

Convert a non-negative integer to its english words
representation. Given input is guaranteed to be less than 2^31 - 1.

Examples:

  Input: 123
  Output: "One Hundred Twenty Three"

  Input: 12345
  Output: "Twelve Thousand Three Hundred Forty Five"

  Input: 1234567
  Output: "One Million Two Hundred Thirty Four Thousand "
          "Five Hundred Sixty Seven"

  Input: 1234567891
  Output: "One Billion Two Hundred Thirty Four Million Five Hundred "
          "Sixty Seven Thousand Eight Hundred Ninety One"
"""

myinput = [123, 12345, 1234567, 1234567891, 20000, 300000, 412031, 0]

DIGITS = ["", "One", "Two", "Three", "Four", "Five", "Six",
          "Seven", "Eight", "Nine"]
TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
         "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
DECADES = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
           "Eighty", "Ninety"]
MAGNITUDES = ["", "Thousand", "Million", "Billion"]


def leetSolve(num):
    """integer_to_english algorithm

    Obvious way

    Args:
        num (int): a value between zero and 2147483647
    Returns:
        str:  pronounceable representation of integer
    """

    result = ""
    divisor = int(1e9)
    magnitude = 3
    while num > 0:
        three_at_a_time = num / divisor
        if (three_at_a_time):
            hundreds = three_at_a_time / 100
            tens = (three_at_a_time % 100) / 10
            last_digit = three_at_a_time % 10
            if (hundreds):
                result += ' ' + DIGITS[hundreds] + ' Hundred'
            if (tens > 1):
                result += ' ' + DECADES[tens - 2]
            elif (tens == 1):
                result += ' ' + TEENS[last_digit % 10]
            if (last_digit > 0 and tens != 1):
                result += ' ' + DIGITS[last_digit]
            if (hundreds or tens or last_digit):
                result += ' ' + MAGNITUDES[magnitude]
        magnitude -= 1
        num = num % divisor
        divisor = divisor / 1000
    if (result):
        return result.strip()
    return 'Zero'


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input))
