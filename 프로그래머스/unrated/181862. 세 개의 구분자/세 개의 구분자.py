def solution(myStr):
    result = []
    current_str = ""
    for char in myStr:
        if char in ["a", "b", "c"]:
            if current_str != "":
                result.append(current_str)
                current_str = ""
        else:
            current_str += char

    if current_str != "":
        result.append(current_str)

    if len(result) == 0:
        return ["EMPTY"]
    else:
        return result