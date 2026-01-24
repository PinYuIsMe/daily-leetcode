class Solution:
    def myAtoi(self, s: str) -> int:
        
        # ignore leading white space
        s = s.lstrip()

        # memorize signedness
        if not s:
            return 0
        positivity = True
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            positivity = False

        # conversion digit by digit from high to low
        accumulate = 0
        for d in s:
            if not d.isdigit():
                break
            accumulate *= 10
            accumulate += int(d)
            print(f"d:c{d} accumulate: {accumulate}")

        if positivity:
            if accumulate > pow(2, 31) - 1:
                return pow(2, 31) - 1
            else: 
                return accumulate
        else:
            if - accumulate < - pow(2, 31):
                return - pow(2, 31)
            else:
                return - accumulate