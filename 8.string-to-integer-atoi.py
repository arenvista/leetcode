# @leet start
class Solution:
    def myAtoi(self, s: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(s) == 0:
            return 0
        
        while pos < len(s):
            char_curr = s[pos]
            if state == 0:
                if char_curr == ' ':
                    pos += 1
                elif char_curr in ['-', '+']:
                    pos += 1
                    state = 1
                    sign = -1 if char_curr == '-' else 1
                elif char_curr.isdigit():
                    state = 2
                    pos += 1
                    value = value * 10 + int(char_curr)
                else:
                    return 0
            elif state == 1:
                if char_curr.isdigit():
                    state = 2
                    value = value * 10 + int(char_curr)
                    pos += 1
                else:
                    return 0
            elif state == 2:
                if char_curr.isdigit():
                    value = value * 10 + int(char_curr)
                    pos += 1
                else:
                    break



        value = sign * value
        if value < -2**31:
            return -2**31
        elif value > 2**31 - 1:
            return 2**31 - 1
        return value


	# 1. Whitespace: Ignore any leading whitespace (" ").
	# 2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
	# 3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
	# 4. Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. Specifically, integers less than -2^31 should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.
# @leet end
