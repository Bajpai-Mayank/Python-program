# s=input("Text: ")
# if len(s) ==1:
#     print(s)
#     exit()
# l,r=0,len(s)
# size=len(s)
# max_str=""
# while(l<=r):
#     print("if")
#     if(l==r):
#         l+=1
#         r=len(s)
#         continue
#     temp=s[l:r]
#     r-=1
#     rev_temp="".join(reversed(temp))
#     print(rev_temp)
#     if  temp == rev_temp and len(max_str)<len(rev_temp) and l!=r:
#         max_str=temp
#         break
# print(max_str)

def longestPalindrome(self, s: str) -> str:
    max_str = ""

    def expand(l, r):
            # As long as l and r are in bounds and characters match...
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            # Return the valid palindrome substring found
        return s[l + 1:r]

    for i in range(len(s)):
            # Case 1: Odd length (center is i)
        odd_palindrome = expand(i, i)
        if len(odd_palindrome) > len(max_str):
            max_str = odd_palindrome

            # Case 2: Even length (center is between i and i+1)
        even_palindrome = expand(i, i + 1)
        if len(even_palindrome) > len(max_str):
            max_str = even_palindrome
    return max_str
