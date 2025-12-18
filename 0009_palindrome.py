# --- Function 002 - To Check the string for palindrome ------------------------------- #
def CheckPalindrome(inp_str):
    str_len = len(inp_str)
    mid_point = 0

    if str_len % 2 == 0:
        mid_point = str_len // 2
    else:
        mid_point = str_len // 2

    print(str_len)
    print(mid_point)

    for i in range(0, mid_point):
        if inp_str[i] != inp_str[str_len - 1]:
            return False
        str_len = str_len - 1
    return True
# --- Function 002 - END -------------------------------------------------------------- #

print(CheckPalindrome("aba"))