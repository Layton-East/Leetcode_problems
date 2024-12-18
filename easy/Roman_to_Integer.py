def roman_to_integer(roman_numeral):

    roman_dict = {
        'I' : 1,
        'IV' : 4,
        'V' : 5,
        'IX' : 9,
        'X' : 10,
        'XL' : 40,
        'L' : 50,
        'XC' : 90,
        'C' : 100,
        'CD' : 400,
        'D' : 500,
        'CM' : 900,
        'M' : 1000
    }

    roman_length = len(roman_numeral)
    i = 0
    total = 0
    while i < roman_length:
        char_1 = roman_numeral[i]
        if i+1 < roman_length:
            char_2 = roman_numeral[i+1]
            symbol = char_1 + char_2
            try:
                total += roman_dict[symbol]
                i += 2
            except:
                total += roman_dict[char_1]
                i += 1
        else:
            total += roman_dict[char_1]
            i += 1
    #end for

    return total
    

def main():
    some_roman = 'XLIVII'
    print(roman_to_integer(some_roman))


if __name__ == "__main__":
    main()
