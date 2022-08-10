# n={10,20,30}
# print(n[1]) #TypeEror:'set' object is not subscriptable. we are trying to find the index position in set. but we cant coz the set is non sequuenace.

# a={2,5,7}
# b='Hello',1,2,3
# a.add(b)
# print(a) #{2,5,7,('Hello',1,2,3)} or {('Hello',1,2,3),2,5,7}. to add the two variables then use the method called add. but we cant say that which variables comes first coz the set is unordered.

# a={1,2,3,4}
# b={5,6,7,8}
# b.add(a)
# print(b) #TypeError:unhashable type'set' . coz we cant add the two sets. but we cant add one set and another one as tuple

# a={"hello"}
# b=3
# a.add(b)
# print(a) #{3,'hello'}.  this is add method

# a={1,"Hello",2,"python"}
# a.clear()
# print(a) #set(). the set never represent the empty flower bracket. the clear method is used to clear all the elements.


# a={1,2,3,3}; b={4,5,2}; c={4,6,7}; d={8,9,10}
# print(a.intersection(b)) #{2}
# print(a.intersection(c)) #set()
# print(c.intersection(b)) #{4}. this method will tell the what are the common elements in the both the sets. if nothing is commmon then the output will be set().

# a={"hello","python",3,4,5}
# b={"language",4.6,7}
# print(a.union(b)) #{'hello',3,4,5,4.6,7'python','language'} 
# print(b.union(a)) #it will be anything we cant sepficy that this element wil be comming first in set. coz sets are unorderd.

# a={1,2,3}
# b={3,4,5}
# c={5,6,7}
# a.update(b)
# print(a)  #{1,2,3,4,5}
# a.update(c) 
# print(a)  #{1,2,3,5,6,7}
# print(b.update(c))
# print(b) #{3,4,5,6,7}. update method with means adding the two elements.if their are common elements in both the set then it will print for one time only that element.

# a={1,2,3,4}
# b={4,3,6,7}
# c={8,9,10}
# print(a.difference(b)) #{1,2}.in differece method what is not common in the both the sets that wil show as the output.
# print(b.difference(a)) #{6,7}.in differece method what is not common in the both the sets that wil show as the output.
# print(b.difference(c)) #{6,7}. if nothing is common the set will remains same.

# a={1,2,3,4,5,50,60,70}
# a.discard(50) #{1,2,3,4,5,60,70}. discard which means the certain element get removed from the set. if the elements is not there in the set then the orginal set gives back
# b={1,2,3,4,5}
# b.discard(6) #{1,2,3,4,5} . the element is not there so the set gave it back.

# a={40,50,200,900}
# a.pop()
# print(a) #{50,200,900} . pop which means the random element will be getting poped out we cant say which element and we cant mention that we need to poped out certain element.

# a={1,2,3,4}
# b={4,5,6,7}
# c={10,20,30}
# print('Are a and b disjoint?', a.isdisjoint(b)) #False. isdisjoint will represent that if anything is not common in betwenn both the elemts then it  shows False orelse if nothing common it shows True.
# print('Are b and c disjoint?', b.isdisjoint(c)) #True

# a={1,2,3}
# b={1,2,3,4,5}
# c={1,2,4,5}
# print(a.issubset(b)) #True. the whole element cantains same element in other set then it is True. if not one element is also missing then it is False.
# print(b.issubset(c)) #False
# print(b.issubset(a)) #False

# a={1,2,3}
# a.remove(2) 
# print(a) #{1,3}. the remove is used to remove the certain elemetments from the list. if the element is not there in list then it shows keyerror.
# b={1,2,3}
# b.remove(4)
# print(b) #KeyError: 4

# a={8,9,10,12,14}
# b={8,9,10}
# print(a.issuperset(b))#True
# print(b.issuperset(a))#False. the two sets should contain the same elements then it shows True. if not if one element is extra then it shows False.
