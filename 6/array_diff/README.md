Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]



Input format = 2 separate lists
Output format = Return a single list
Input/Output table: array_diff([1,2],[1]) == [2]
Edge cases: 
maximum number of integers in a list?
empty list?
type of elements in a list, can users put strings in the list?

