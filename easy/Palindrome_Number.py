def check_for_palindrome(some_int):
    some_string = str(some_int)
    is_palindrome = True

    # All strings of length 1 are palindromes
    if len(some_string) == 1:
        is_palindrome=True
        return is_palindrome

    cursor_1 = 0 # start on first index of string
    cursor_2 = len(some_string) - 1 # start on last index of string

    # loop through string moving both cursors inward one index per loop
    # do until cursor 1 is at a greater index than cursor 2
    while cursor_1 < cursor_2: 
        if some_string[cursor_1] != some_string[cursor_2]:
            is_palindrome = False
            break
        cursor_1 += 1
        cursor_2 -= 1

    return is_palindrome


def main():
    some_int = 96769
    print(check_for_palindrome(some_int))


if __name__ == "__main__":
    main()

