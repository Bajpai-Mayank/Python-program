from pathlib import Path
import re
WORDS_DIR = Path(__file__).parent / "Words"
print(WORDS_DIR)

# ANSI Color Codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def anagram_game(stage):
    word_file = WORDS_DIR / f"{stage}_words.txt"
    ct = 0
    while True:
        text = str(input("--> ")).strip()
        if not text:
            continue
            
        ct += 1
        max_len = 0
        txt = 0
        
        with open(word_file) as f:
            for _, line in enumerate(f, 1):
                words = str(line)
                word = words.strip().split()
                
                for i in range(len(word)):
                    current_match_count = 0
                    temp_word = word[i]
                    if((len(word[i])-len(text))<0):
                        print(f"{RED} No words contain of length {len(text)}")
                        return
                    for char in text:
                        safe_char = re.escape(char)
                        if re.search(safe_char, temp_word):
                            current_match_count += 1
                            temp_word = re.sub(safe_char, "", temp_word, count=1)
                    if current_match_count > max_len:
                                txt = len(word[i])
                                max_len = current_match_count
        if txt == 0:
            print(f"{RED} 0% Match! Try typing some different letters. {RESET}")
            continue
            
        prob = (max_len/txt) * 100
        
        if (txt - len(text)) != 0:
            if 0 < prob <= 33:
                print(f"{RED} Try Again ! Match Probability {prob:.2f}% {RESET}")
            elif 33 < prob <= 66:
                print(f"{YELLOW} You are close ! Match Probability {prob:.2f}%{RESET}")
            else:
                print(f"{GREEN} Almost ! :) Match probability {prob:.2f}%{RESET}")
        else:
            print(f"{GREEN} You Win! :) Match probability {prob:.2f}% {RESET}")
            print(f"Attempts : {ct}")
            break

level = ("Exit", "Easy", "Medium", "Hard")

while True:
    print(f"\n{BLUE}********Anagram Game*********{RESET}")
    print(f"{BLUE} 1.{level[1]} \n 2.{level[2]} \n 3.{level[3]}\n 0.{level[0]}{RESET}")
    try:
        choice = int(input("Choose your Level: "))
    except ValueError:
        print(f"{RED}Please enter a valid number.{RESET}")
        continue
        
    match choice:
        case 1 | 2 | 3:
            anagram_game(level[choice])
        case 0:
            print("Thanks for playing!")
            break
        case _:
            print(f"{RED}Invalid choice, try again.{RESET}")