'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# current_count = 0
# total_count = 0
# matched = "th"
 
# def count_th(word):
#     global current_count
#     global total_count
#     #base case
#     #if current is more than total 
#     if (current_count>total_count):
#         #current count becomes new total
#         return
#         current_count = total_count
#     # the lenth of the word
#     if range(len(word[:2])) == matched:
#         #add to current count
#         curr_count += 1
#         #check next letter until all 
#     if matched:
#         matched[2::-1] == "ht"
#         print("total: ", total_count)

#     if range(word[0][-1]) == ('t','h' or 'h','t'):
#         Print("Answer", True)



#     if (matched) in (word):
#         total_count + 1
#         return current_count
#         print(current_count)
#     if not matched:
#         if matched[::-1]:
#             return total_count + 1
#             print("if not, match count: ",total_count)
#         else:
#             total_count
#     #recursive 
#     else:
#         total_count = total_count + current_count
#         current_count = current_count + 1
#         #if it doesn match th return total 
#         return count_th
#         # print("matches",count_th)
# print("1st CurrentC: ", current_count)
# print("1st TotalC: ", total_count)



# def count_th3(word):
#     #new value #if first to indes match "th" or "ht"
#     letters in range(1, word + 1
#     accumulating_current = [a
#     ccumulating_current if word[0][1].lower 
#     or word[1][0].lower == "th" or "ht"]
#     #add to the acccumulating 
#     accumulating_current += 1
#     print accumulating_current
#     print(count_th3)



# def count_th(word):
#     matching = 'th'
#     curr_count = 0
#     total = 0
#     #base case if word doesn't have any strings in it
#     if word == 0:
#         return total
#     #if the first to letters are "th", 
#     if word[:2] == "th":
#         #add 1 to current count 
#         curr_count += 1
#         return curr_count
#         print("1st current count",curr_count)
#         #if reverse is th add to current value
#         if word[:2] == "ht":
#         #print current count
#             curr_count += 1
#             print("CC if ht: ",curr_count)
#         print("current: ",curr_count)
#         #print total count
#         return total
#         print("total: ", total)
#         #remove index until all letters have been matched
#         word.pop(0)
#         print("letter removed: ",word.pop(0))
#         #recursive
#         total = curr_count + total
#         curr = curr_count + 1
#         return total
#         print("total", total)
#     print(count_th)



# https://www.ics.uci.edu/~brgallar/week5_1.html
# def Solve(Problem):
#   if (Problem is minimal/not decomposable into a smaller problem: a base case)
#     Solve Problem directly and return solution; i.e., without recursion
#   else:
#     (1) Decompose Problem into one or more SIMILAR,
#         STRICTLY SMALLER subproblems: SP1, SP2, ... , SPn

#     (2) Recursively call Solve (this function) on each smaller subproblem
#         (since they are similar): Solve(SP1), Solve(SP2),..., Solve(SPN)

#     (3) Combine the returned solutions to these smaller subproblems into a
#         solution that solves the original, larger Problem (the one this
#         function call must solve)
  
#     (4) Return the solution to the original Problem




# def count_th(word):
    # current_count = 0
    # total = 0
    
    # word = ''
    # #if word length is less than, return 0
    # print(word)
    # if len(word) < 2:
    #     return 0
    # #or if len(word) == 0:
        #return 1
    #if index in word match th
    # if word[2:-1].lower()== "th":
    #     #increment current count +1
    #     current_count += current_count
    #     return count_th(word[2:])
    #     print("accumulate", current_count)
    #     #check to see if there are revers letters
    # if (word[2::-1].lower()) == "th":
    #     ##increment current count
    #     current_count += current_count
    #     #cut off the last number if 
    #     return count_th(word[:2])
    # else:
    #     #cut off 1st letter if no match
    #     count_th(word[1:])
    #     #cut off last letter if no match
    #     count_th(word[:1])
    #     #calculate current count by adding 1
    #     current_count = current_count + 1
    #     total = total + current_count
    #     return total
    #     print("current count:",current_count)
    #     print(count_th)
    #     return count_th()


# def count_th(word):
#     sub = "th"

#     #f word length is the bas case 
#     if len(word) == 0:
#         return 0
#     # word index starting at 0 
#     elif word[0 : len(sub)] == sub:
#         return 1 + count_th(word[1:])
#     return count_th(word[1:])
def count_th(word):
    subWord = "th"
    
    if len(word) == 0:
        return 0
    if word[0 : len(subWord)] == subWord:
        return 1 + count_th(word[1:])
    return count_th(word[1:])
# def count_th(word):
#     subWord = "th"
#     #base case- if this is true, stop looping
#     #if lengh of word is 0 return )
#     if len(word) == 0:
#         return 0
#     #if word starts at 0 and ends at word length is equal to the subWord which is "th"
#     elif word[0:len(subWord)] == subWord:
#         #add 1 to count_th 
#         return 1 + count_th(word[1:])
#     return count_th(word[1:])

