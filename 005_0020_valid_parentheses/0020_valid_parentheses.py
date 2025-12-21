# --- Function 001 - Check if the parentheses are valid ------------------------------- #
def CheckValidParentheses(s):

    stack = []

    last_pushed = ""
    last_popped = ""

    for each in s:

        if(each in ("{", "[","(")):
            stack.append(each)
            last_pushed = each
            
            print("last_push :", last_pushed)
        else:
            if not stack:
                return False
            last_popped = stack.pop()

            print("last pop :", last_popped)
            print("each :", each)
            if not ((last_popped == "{" and each == "}") or (last_popped == "[" and each == "]") or (last_popped == "(" and each ==")")):
                return False

    if not stack:
        return True
        
    return False


print(CheckValidParentheses("]"))
            
# --- Function 001 - END -------------------------------------------------------------- #


# --- Best Approach ------------------------------------------------------------------- #
def BestCheckValidParentheses(s):

    mapped_dict = {
            "}":"{"
            , ")":"("
            , "]":"["
        }

    result_stack = []

    for each in s;
        if each in mapped_dict:
            top_element = result_stack.pop() if result_stack else "#"

            if top_element != mapped_dict[each]:
                return False
        else:
            result_stack.push(each)

    return not result_stack

# --- Best Approach - END ------------------------------------------------------------- #
