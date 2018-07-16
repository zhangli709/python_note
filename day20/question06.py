"""

题目6: 设计一个函数，对传入的字符串（假设字符串中只包含小写字母和空格）进行加密操作，
加密的规则是a变d，b变e，c变f，……，x变a，y变b，z变c，空格不变，返回加密后的字符串 97- 122 chr  ord

"""


def caesar_encrypt(string):  # 97 为基数， 26求余为循环，(num-97) % 26 + 97
    new_string = ''
    for val in string:
        if val != ' ':
            new_letter = chr((ord(val) + 3 - 97) % 26 + 97)
            new_string += new_letter
        else:
            new_string += ' '
    return new_string


def main():
    print(caesar_encrypt('attack at dawn'))  # dwwdfn dw gdzq
    print(caesar_encrypt('dinner is on me'))  # glqqhu lv rq ph


if __name__ == '__main__':
    main()

######################
