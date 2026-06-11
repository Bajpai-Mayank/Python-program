# Solution by me
import sys
n=int(input("Number : "))
if n<0:
    print("Invalid , number shoud be >=0")
    sys.exit()
def chain_form(n):
    arr = [int(d) for d in str(n)]
    sz=len(str(n))-1
    l,r,=0,sz
    ex=0
    while ex!=sz:
        if l==r:
            l+=1
            r=sz
            ex+=1
            continue
        total=arr[l]+arr[r]
        arr.append(total)
        r-=1
    new_arr=list(set(arr))
    new_arr.sort()
    print(new_arr)
    new_arr.append(arr[len(arr)-1]+1)
    new_order=[]
    for i in range(len(new_arr)-1):
        new_order.append(new_arr[i])
        if new_arr[i+1] - new_arr[i] != 1:
            break
    print("Max form : ",new_order)
if('0' in str(n) and n>99):
    chain_form(n)
else:
    print("Max chain not possible,Invalid form")
# Discode User Solution
def chain_number(number_string):
    digits = [int(d) for d in number_string]
   
    combos = []
    for i, digit in enumerate(digits):
        print(i,digit)
        for other_digit in digits[i+1:]:
            print(other_digit)
            combos.append(digit + other_digit)

    combos = list(set(combos + digits)) # Remove duplicates

    chain = []
    for i, number in enumerate(sorted(combos)):
        if i == number:
            chain.append(number)

    print(f"Chain={chain} stops at {max(chain)}")


while True:
    input_number = input("Number to secure: ")

    try: int(input_number)
    except ValueError:
        print("Input must be an integer >99 with at least one 0 digit.")
       
    if int(input_number) <= 99 or not ("0" in input_number):
        print("Invalid form")
        print("Input must be an integer >99 with at least one 0 digit")
    else:
        chain_number(input_number)
# New approach through discuss
def find_chain_max(number_string):
    chain_max = 0
    if "1" in number_string:
        found_next_integer = True
   
        digit_count = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for digit in [int(d) for d in number_string]:
            digit_count[digit] += 1

        while found_next_integer:
            chain_max += 1
            found_next_integer = False

            pairs = pair_table[chain_max + 1]
            for pair in pairs:
                if pair[0] == pair[1]:
                    if digit_count[pair[0]] > 1:
                        found_next_integer = True
                        break
                elif digit_count[pair[0]] and digit_count[pair[1]]:
                    found_next_integer = True
                    break
   
    return chain_max


while True:
    input_number = input("Number to secure: ")

    try: int(input_number)
    except ValueError:
        print("Input must be an integer >99 with at least one 0 digit.")
       
    if int(input_number) <= 99 or not ("0" in input_number):
        print("Invalid form")
        print("Input must be an integer >99 with at least one 0 digit")
    else:
        print(find_chain_max(input_number))