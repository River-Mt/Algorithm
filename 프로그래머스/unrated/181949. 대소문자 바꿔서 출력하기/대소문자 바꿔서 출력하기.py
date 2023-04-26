str = input()
ans = ""
for i in str:
    if i.isupper() == 1:
        ans += i.lower()
    else :
        ans += i.upper()
        
print(ans)