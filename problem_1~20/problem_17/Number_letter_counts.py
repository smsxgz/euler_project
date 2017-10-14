# -*- coding: utf-8 -*-

# Sum of 1 to 9
s1 = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
# 36

# sum of 11 to 19
s2 = 6 + 6 + (4 + 4 + 3 + 3 + 5 + 4 + 4) + 4 * 7
# 67

# Sum of 1 to 99
s3 = s2 + s1 * 9 + (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) * 10 + 3
# 854

# Sun of 1 to 1000
s4 = s1 * 100 + 7 * 900 + 3 * 891 + s3 * 10 + 3 + 8
s4


def to_english(n):
    if 0 <= n < 20:
        return ONES[n]
    elif 20 <= n < 100:
        return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return ONES[n // 100] + "hundred" + (("and" + to_english(n % 100))
                                             if (n % 100 != 0) else "")
    elif 1000 <= n < 1000000:
        return to_english(n // 1000) + "thousand" + (to_english(n % 1000) if
                                                     (n % 1000 != 0) else "")
    else:
        raise ValueError()


ONES = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen"
]
TENS = [
    "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
    "ninety"
]
