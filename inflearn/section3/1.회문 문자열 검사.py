N = int(input())

for i in range(N):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" % (i+1))
            break
    else:
        print("#%d YES" % (i+1))

# for i in range(N):
#     s = input()
#     s = s.upper()
#     if(s == s[::-1]):
#         print("#%d YES" % (i+1))
#     else:
#         print("#%d NO" % (i+1))
