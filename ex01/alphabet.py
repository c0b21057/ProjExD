import random
import datetime

num_of_alphabet = 26  # 全アルファベット数
num_of_all_chars = 10 # 対象文字数
num_of_abs_chars = 2  # 欠損文字数
num_of_trials = 2 # チャレンジできる回数

def shutudai(alphabet):
    all_chars = random.sample(alphabet, num_of_all_chars)
    print("対象文字：", end="")
    for c in sorted(all_chars): 
        print(c, end=" ")
    print()
    abs_chars = random.sample(all_chars, num_of_abs_chars)
    print("表示文字：", end="")
    for c in all_chars: 
        if c not in abs_chars: 
            print(c, end=" ")
    print()
    print("デバッグ用欠損文字：", abs_chars)




def kaito():
    pass


if __name__ == "__main__":
    alphabet = [chr(i+65) for i in range(num_of_alphabet)]
    #print(alphabet)
    shutudai(alphabet)