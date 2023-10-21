s = input().rstrip()
left = ['(', '[']
right = {')': '(', ']': '['}


def is_correct():
    st = []
    for ch in s:
        if ch in left:
            st.append(ch)
        else:
            if len(st) and st[-1] == right[ch]:
                st.pop()
            else:
                return False

    if len(st):
        return False

    else:
        return True


def calculate():
    st = []
    for ch in s:
        if ch in left:
            st.append(ch)
        else:
            if len(st) and st[-1] == right[ch]:
                st.pop()
                if right[ch] == '(':
                    st.append(2)
                else:
                    st.append(3)

            elif len(st) >= 2 and st[-1] not in left and st[-2] == right[ch]:
                num = st[-1]
                st.pop()
                st.pop()
                if right[ch] == '(':
                    st.append(2 * num)
                else:
                    st.append(3 * num)

        if len(st) >= 2 and st[-1] not in left and st[-2] not in left:
            x = st[-1]
            y = st[-2]
            st.pop()
            st.pop()
            st.append(x + y)

    ans = 0

    while st:
        ans += st.pop()
    return ans


if not is_correct():
    print(0)
else:
    print(calculate())
