x=3
y=3
z=3

print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1)])

---------------------------------

input = number & list of scores
o/p = second max

1. covert list to set
2. sort
3. get second value
----------------------------------

TODO: List vs Set
LIST--> data type that stores values in sequence,
	can have multiple occurrences of same elements

SET--> data type that stores unordered values, 
	cannot have multiple occurrences of same elements 

----------------------------------
TUPLES:
tuples are immutable (meaning that they cannot be modified once created).
tuple use is the swapping of  numbers
used as keys in a dictionary.

i/p --> n=2 and elements [1,2]

o/p --> 3713081631934410656

t = tuple(integer_list)
hash(t) --> id

----------------------------------
STRING split and join:

a = "this is a string"
a = a.split(" ")
print a
['this', 'is', 'a', 'string']

a = "-".join(a)
print a
this-is-a-string 

----------------------------------------

LISTS:

insert i e: Insert integer e at position i .
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

i/p:
n=12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

o/p:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

    N = int(input())
    arr = []
    arr.insert(0,5)
    arr.insert(1,10)
    arr.insert(0,6)
    l = arr
    print(l)

	INCOMPLETE

------------------------------------

-->print textwrap.wrap(string,8)
 The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most.

-->print textwrap.fill(string,8)
  The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

-----------------------------------

--> to capitalize first letter in each word of a sentence:
	string.title()
--> to capitalize first letter : string.capitalize()
  

-------------------------------------

--> two for loops iterations

x=1, y=4  [1,4]
x=1, y=5  [1,4][1,5]
x=1, y=6  [1,4][1,5][1,6]

x=2, y=4  [1,4],[1,5],[1,6],[2,4]
x=2, y=5  [1,4],[1,5],[1,6],[2,4],[2,5]
x=2, y=6  [1,4],[1,5],[1,6],[2,4],[2,5],[2,6]

x=3, y=4  [1,4],[1,5],[1,6],[2,4],[2,5],[2,6],[3,4]
x=3, y=5  [1,4],[1,5],[1,6],[2,4],[2,5],[2,6],[3,4],[3,5]
x=3, y=6  [1,4],[1,5],[1,6],[2,4],[2,5],[2,6], [3,4],[3,5],[3,6]


