def Longest_Common_Prefix(strs):

    longest_prefix = strs[0] # initialize to first element

    if len(strs) == 1:
        return longest_prefix

    length_of_strs = len(strs)
    # loop through rest of strings to compare
    for strs_index in range(1, length_of_strs):
    
        string_to_check = strs[strs_index]
        length_string_to_check = len(string_to_check)
        length_longest_prefix = len(longest_prefix)

        # longest_prefix cannot be longer than any string
        if  length_string_to_check < length_longest_prefix:
            longest_prefix = longest_prefix[:length_string_to_check]
            length_longest_prefix = len(longest_prefix)

        char_index = length_longest_prefix-1

        # loop through characters to compare
        while char_index >= 0:

            char_to_check = string_to_check[char_index]
            # if character of longest prefix doesn't match - remove it and everything behind it
            if char_to_check != longest_prefix[char_index]:
                longest_prefix = longest_prefix[:char_index]

            char_index -= 1

        # end while 

        if len(longest_prefix) == 0: 
            break

    # end for loop
        
    return longest_prefix



def main():
    strs = ['ower', 'flow', "flight"]
    print(Longest_Common_Prefix(strs))


if __name__ == "__main__":
    main()
