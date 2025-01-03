class Solution:
    # Given an integer array nums sorted in non-decreasing order, 
    # remove the duplicates in-place such that each unique element appears only once. 
    #
    # The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
    #
    # Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    #
    # Change the array nums such that the first k elements of 
    # nums contain the unique elements in the order they were present in nums initially. 
    #
    # The remaining elements of nums are not important as well as the size of nums.
    #
    # Return k.
    def removeDuplicates(self, nums):

        length_nums = len(nums)
        k = 0

        if nums == []:
            return nums
            #return k

        first = nums[0]
        last =  nums[-1]
        count = 1

        if first == last:
            k = 1
            nums = [first]
            return nums
            #return k
        # end if

        current_index = 1
        for i in range(1, length_nums - 1):

            compare_1 = nums[i]
            compare_2 = nums[i+1]
            if compare_1 != compare_2:
                nums[current_index] = compare_2
                current_index += 1
                count += 1
            # end if
        # end for 

        k = count
        return nums



def remove_temp(my_list):

    my_list.pop(-1)
    return
        

def main():
    s1 = Solution()
    nums = [1, 1, 3, 3, 4, 5, 6, 7, 7]
    nums = s1.removeDuplicates(nums)

    remove_temp(nums)
    #print('k:', k)
    print('nums:', nums)


if __name__ == '__main__':
    main()