from rt import run_test, run_test_float, close_enough

# ##################### Problem 1 #########################
def describe_string(s):
    """prec:  s is a string
    postc:  returns "LONG" if the string has 10 or
    more characters and "SHORT" otherwise."""
    if len(s) > 10:
        return "LONG"
    else:
        return "SHORT"
# ##################### Problem 2 #########################
def add_evens(nums):
    """prec: nums is a list of integers.  
    postc:  returns the sum of the EVEN numbers in numss."""
    evens = []
    for i in nums:
        if i%2 != 1:
            evens.append(i)
    return sum(evens)
# ##################### Problem 3 #########################
def opposite_letter(ch):
    """prec:  ch is a one-character string containing
    a letter.
    postc: returns the "opposite" letter in the alphabet
    in lower case:
    A -> z
    a -> z
    B -> y
    b -> y
    C -> x 
    c -> x 
    etc."""
    ch = ch.lower()
    alphabeht = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    index_of_ch = alphabeht.index(ch)
    if index_of_ch > 13:
        return alphabeht[(25-index_of_ch)]
    else:
        return alphabeht[-(1+index_of_ch)]
# ##################### Problem 4 #########################
def zipper_strings(a, b):
    """prec: a, b are strings.
    post:  returns a string that, starting with a,
    alternates characters of a and b.  When one list is
    exhausted, the rest of the other is tacked onto the end."""
    out = ""
    lista = list(a)
    listb = list(b)
    counta = 0
    countb = 0
    for i in range(len(lista) + len(listb)):
        if i%2 == 0:
            out+=lista[counta]
            counta += 1
        else:
            out+=listb[countb]
            countb += 1
        if len(lista) == len(listb):
            pass
        elif counta == len(lista):
            out+=b[countb:]
            return out
        elif countb == len(listb):
            out+=a[counta:]
            return out
    return out
# ##################### Problem 5 #########################
def maximum_product(lists):
    """prec: lists is a nonempty list of numerical lists.
    Note that one of the numerical lists could be empty and 
    that the product of an empty list is 1.
    postc:  returns THE LIST with the largest product.
    In the event of a tie, it returns the first such list."""
    answers = []
    greatest = 0
    for i in lists:
        total = 1
        for k in i:
            total *= k
        answers.append(total)
    for j in range(len(answers)):
        if answers[greatest] < answers[j]:
            greatest = j
    return lists[greatest]
# ##################### Problem 6 #########################
def check(first,second,total):
    if (first + second < total):
        return True
    else:
        return False
def nuggets(limit, nugget_list):
    """prec: limit is an nonnegative integer
    postc: nugget_list is a list of nonnegative integers
    returns a list from nugget_list that has the
    highest total without exceeding the limit. """
    final = []
    true_final = []
    if limit == 0:
        return final
    if nugget_list == []:
        return None
    
    for i in range(len(nugget_list)):
        #print("nugget_list[i] is: " + nugget_list[i])
        for k in range(len(nugget_list[i:])):
            #print("nugget_list[k] is: " + nugget_list[k])
            if check(nugget_list[i],nugget_list[k], limit) == True:
                final.append(nugget_list[i])
                final.append(nugget_list[k])
    for i in final:
        decoy = final
        del decoy[decoy.index(i)]
        if decoy.index(i) != -1:
            del final[decoy.index(i)]
    print(final)
    return final
print("************* Tests for Problem 1 **************")
run_test(describe_string, "LONG", ["antidisestablishmentarianism"])
run_test(describe_string, "LONG", ["This is long"])
run_test(describe_string, "SHORT", ["imshort"])
print("************* Tests for Problem 2 **************")
run_test(add_evens, 30, [[1,4,7,9,10,16]])
run_test(add_evens, 0, [[1,3,7,9,11,13]])
print("************* Tests for Problem 3 **************")
run_test(opposite_letter, "z", ["a"])
run_test(opposite_letter, "y", ["B"])
run_test(opposite_letter, "x", ["c"])
run_test(opposite_letter, "a", ["Z"])
run_test(opposite_letter, "b", ["y"])
run_test(opposite_letter, "c", ["x"])
print("************* Tests for Problem 4 **************")
run_test(zipper_strings, "cdaotggie", ["cat", "doggie"])
run_test(zipper_strings, "dcoagtgie", ["doggie", "cat"])
run_test(zipper_strings, "dcoagt", ["dog", "cat"])
print("************* Tests for Problem 5 **************")
run_test(maximum_product, [6,6,6], [[[1,2], [5,6,7], [3, 0], [6,6,6]]])
run_test(maximum_product, [9,9,9], [[[], [1,2,3], [3, 0], [9,9,9]]])
run_test(maximum_product, [9,9,9], [[[9,9,9], [1,2,3], [3, 0], []]])
print("************* Tests for Problem 6 **************")
run_test(nuggets, [4, 16], [20, [1, 2, 4, 8, 16]])