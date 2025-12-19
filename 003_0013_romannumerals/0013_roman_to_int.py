roman_values = {
     "I": 1 
    , "V": 5 
    , "X": 10 
    , "L": 50 
    , "C": 100 
    , "D": 500 
    , "M": 1000 
    , "IV": 4
    , "IX": 9
    , "XL": 40
    , "XC": 90
    , "CD": 400
    , "CM": 900
}

# --- Function 001 - Check the roman dictionary and give integer equivalent ----------- #
def GetRomanValue(roman_val):
    return roman_values[roman_val]
# --- Function 001 - END -------------------------------------------------------------- #


# --- Function 002 - Find the Integer equivalent of the roman value ------------------- #
def GetIntValueForRomanValue(input_val):
    result = 0
    index = 0

    while index < len(input_val):

        if index == len(input_val) - 1:
            int_val = GetRomanValue(input_val[index])
        else:
            int_val = GetRomanValue(input_val[index])
            next_int_val = GetRomanValue(input_val[index+1])

            if int_val < next_int_val:
                int_val = GetRomanValue(input_val[index] + input_val[index+1])
                index = index + 1

        print(int_val, result)

        result = result + int_val    
        index = index + 1

    return result
# --- Function 002 - END -------------------------------------------------------------- #


# print(GetIntValueForRomanValue(input("Enter roman value : ")))

# === Best Approach =================================================================== #
# class Solution:
#     def romanToInt(self, s):
#         roman = {'I':1, 'V':5, 'X':10, 'L':50,
#                  'C':100, 'D':500, 'M':1000}
#         result = 0
#         for i in range(len(s)):
#             curr = roman[s[i]]
#             next_val = roman[s[i+1]] if i+1 < len(s) else 0
#             if curr < next_val:
#                 result -= curr
#             else:
#                 result += curr
#         return result

def RomanToInt(roman_val):
    roman_values = {
        "I": 1 
        , "V": 5 
        , "X": 10 
        , "L": 50 
        , "C": 100 
        , "D": 500 
        , "M": 1000 
    }

    result = 0

    for i in range(0, len(roman_val)):
        cur_val = roman_values[roman_val[i]]
        next_val = roman_values[roman_val[i+1]] if i+1 < len(roman_val) else 0

        if cur_val < next_val:
            result = result - cur_val
        else:
            result = result + cur_val
        print(result, cur_val, next_val)
    return result
    

print(RomanToInt(input("Enter roman value : ")))
# --- END ----------------------------------------------------------------------------- #
