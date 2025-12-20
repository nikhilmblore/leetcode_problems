# --- Function 01 - Find the Longest prefix ------------------------------------------- #
def FindLongestPrefix(strs):

    result = ""
    print(strs)

    if len(strs) == 1 :
        return strs[0]
    elif len(strs) > 1:

        result = strs[0]

        for i in range(1, len(strs)):

            if len(result) < len(strs[i]):
                short_str = result
                long_str = strs[i]
            else:
                short_str = strs[i]
                long_str = result

            result = ""
            for j in range(0, len(short_str)):
                if short_str[j] == long_str[j]:
                    result = result + short_str[j]
                else:
                    break

            print(result)


strs = ["flower","flow","flight","flowing", "run"]
FindLongestPrefix(strs)
# --- Function 001 - END --------------------------------------------------------------- #


# === Best Approach ==================================================================== #

def BestFindLongestPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for i in range(1, len(strs)):

        current = strs[i]

        while current.find(prefix) != 0:

            prefix = prefix[:-1]

            if not prefix:
                return ""

