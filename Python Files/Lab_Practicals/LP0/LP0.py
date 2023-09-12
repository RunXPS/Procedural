from rt import run_test, run_test_float, close_enough

######################Problem 1###########################
def trim_sum(nums, limit):
    """nums is a numerical list, limit is a number
    returns the sum of all elements in nums that are
    <= limit"""
    out = 0
    for i in range(len(nums)):
        if nums[i] <= limit:
            out += nums[i]
    return out
######################Problem 2###########################
def filter_sum(s):
    """prec: s is a string
    postc:  the total of all digits in the string is returned."""

    out = 0
    for i in range(len(s)):
        if s[i].isdigit():
            out += int(s[i])
    return out
######################Problem 3###########################
def sort_letters_backward(word):
    """prec: word is a lower-case string
    postc: returns a string with the letters in word sorted in reverse 
    alphabetical order
    """
    final = ""
    word = sorted(word, reverse=True)
    for i in range(len(word)):
        final += word[i]
    return final
######################Problem 4###########################

def comb_nest(*x):
    """prec: x is a star argument; you pass in a comma separated
    list of lists.  
    postc:  returns a list containing the sum of each of 
    the nested lists inside of x.  
    """
    final = []
    for i in range(len(x)):
        final.append(sum(x[i]))
    return final
######################Problem 5###########################
def paranoid_number(n):
    """prec: n is a nonnegative integer
    postc: returns the nth paranoid number
    paranoid_number(0) = 1
    paranoid_number(1) = 3
    paranoid_number(n+2) = 5*paranoid_number(n+1) -  6*paranoid_number(n) 
    """
    if n == 0:
        return 1
    if n == 1:
        return 3
    return 5*paranoid_number(n-1) -  6*paranoid_number(n-2) 
######################Problem 6###########################
def generate_anagrams(word):
    """prec: word is a string with distinct letters
    postc:  generates a list containing all anagrams of 
    word in alphabetical order.  """
    out = []
    if len(word) <=1:
        return [word]
    for k in generate_anagrams(word[1:]):
        out += lard(word[0], k)
    return(sorted(out))
    
def lard(a, word):
    #word_list = word
    final = []
    for i in range(len(word)+1):
        final.append(word[:i] + a + word[i:])
    return final
    
def main():
    ## do your testing here.
    print("*************** Problem 1 Tests **************")
    run_test(trim_sum, 6, [[1, 2, 3, 4, 5], 3])
    run_test(trim_sum, 13, [[5, 12, 11, 2, 6], 10])
    print("*************** Problem 2 Tests **************")
    run_test(filter_sum, 10, ["c1o2w3s4moo"])
    run_test(filter_sum, 11, ["ch3ckm8"])
    print("*************** Problem 3 Tests **************")
    run_test(sort_letters_backward, "rmmhea", ["hammer"])
    run_test(sort_letters_backward, "mlkjihgfedcba", ["gicdhjablemkf"])
    print("*************** Problem 4 Tests **************")
    run_test(comb_nest, [6, 15, 15], [[1,2,3], [7, 8], [10,3,2]])
    #print("*************** Problem 4 Tests **************")
    print("*************** Problem 5 Tests **************")
    print(run_test(paranoid_number, 1, [0]))
    print(run_test(paranoid_number, 3, [1]))
    print(run_test(paranoid_number, 9, [2]))
    print(run_test(paranoid_number, 27, [3]))
    print("*************** Problem 6 Tests **************")
    run_test(generate_anagrams, ['act', 'atc', 'cat', 'cta', 'tac', 'tca'], ["cat"])
    run_test(generate_anagrams, ['ot', 'to'], ["to"])
    #run_test(generate_anagrams, ['ejry', 'ejyr', 'erjy', 'eryj', 'ey' 'jery', 'jeyr', 'jrey', 'jrye', 'tac', 'tca'], ["jery"])
main()
print(generate_anagrams("cows"))