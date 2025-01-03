class Solution:

    def generateParenthesis(self, n: int):

        answer = []
        FINAL_N = n
        lookup_table = []
        to_index = 1 # n will be used for math and index used for lookup

        for i in range(0, FINAL_N):
            lookup_table.append([])


        # n = 1
        # ()

        # n = 2
        # (()), ()()

        # n = 3 
        # ((())), (()())
        # ()(()), (())(), ()()()

        # n = 4
        # (((()))), ((()()))
        # (()(())), ((())()), (()()())
        # ((()))(), ()((()))
        # (()())(), ()(()())
        # ()(())(), ()()(())
        # (())()(), ()(())(), ()()()()
        # (())(()), (())()(), ()()(()), ()()()()

        lookup_table[0].append('()') # base case for n = 1
        if FINAL_N == 1:
            return lookup_table[0]
        index = 0

        # start n = 2 since we've already done n = 1
        for n in range(2, FINAL_N + 1):
        
            index = n - to_index 
            next_key = index
            lookup_table[next_key] = []

            # case 1
            # enclose n-1 variations in ()
            previous_index = index - 1
            bases = lookup_table[previous_index] # get previous variations
            for base in bases:
                # store new value in table
                lookup_table[next_key].append('('+ base + ')')

            # case 2
            # find x,y such that x + y = n
            # lookup table[x] and table[y]
            # find all combinations of table[x] and table[y]
            loop_count = n // 2 # loop counter to avoid doing extra work
            x = 1
            while loop_count > 0: 
                self.create_combinations(x, n, next_key, lookup_table, to_index) 
                loop_count -= 1
                x += 1
            # end while loop

        # end outer for loop
        answer = lookup_table[index]
    
        return answer
    # end generateParenthesis
        
    def create_combinations(self, x, n, next_key, lookup_table, to_index):
        y = n - x
        index_x = x - to_index
        index_y = y - to_index
        bases_x = lookup_table[index_x]
        bases_y = lookup_table[index_y]
        for base_x in bases_x: 
            for base_y in bases_y:
                new_output = base_x + base_y
                if new_output not in lookup_table[next_key]:
                    lookup_table[next_key].append(new_output)
                new_output = base_y + base_x
                if new_output not in lookup_table[next_key]:
                    lookup_table[next_key].append(new_output)
            # end base_y for
        # end base_x for
        return
    # end create_combinations

# end class Solution


def main():


    #temp =  []

    #temp.append('(((())))')
    #temp.append('((()()))')
    #temp.append('(()(()))')
    #temp.append('((())())')
    #temp.append('(()()())')
    #temp.append('((()))()')
    #temp.append('()((()))')
    #temp.append('(()())()')
    #temp.append('()(()())')
    #temp.append('()(())()')
    #temp.append('()()(())')
    #temp.append('(())()()')
    #temp.append('()(())()')
    #temp.append('()()()()')
    #temp.append('(())(())')
    #temp.append('(())()()')
    #temp.append('()()(())')
    #temp.append('()()()()')

    #print(list(set(temp)))

    n = 4

    S1 = Solution()
    
    answer = S1.generateParenthesis(n)
    print(answer)


if __name__ == "__main__":
    main()