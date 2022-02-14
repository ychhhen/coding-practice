# Given an array of characters where each character represents a fruit tree, 
# you are given two baskets and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.
# You can start with any tree, but once you have started you can’t skip a tree. 
# You will pick one fruit from each tree until you cannot, 
# i.e., you will stop when you have to pick from a third fruit type.

# Example:
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

'''
ideas:
= find the longest subarray with 2 distinct element

# for loop to pick up fruit
# dict to check types of fruit <=2
# while over 2 fruit types, drop the fruit picked up at the beginning 
# len+1

'''


def fruit_into_basket(fruits):
    # corner case
    if len(fruits)<=2:
        return len(fruits)
    
    basket = {}
    countFruit = 0
    indexStart = 0
    for indexEnd, fruit in enumerate(fruits):

        if fruit not in basket:
            basket[fruit] = 0
        basket[fruit] += 1

        while len(basket)>2:
            left_fruit = fruits[indexStart]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            indexStart += 1

        countFruit = max(countFruit, indexEnd-indexStart+1)
    
    return countFruit

def main():
    # fruits = ['A', 'B', 'C', 'A', 'C']
    fruits = ['A', 'B', 'C', 'B', 'B', 'C']
    print("Fruits are {} and the output is {}".format(fruits, fruit_into_basket(fruits)))

main()