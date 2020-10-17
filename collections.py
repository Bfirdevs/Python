#Collections: Counter, named tuple, Orderec Dict , default dict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque
a = "aaabbbbbbbcccccdddd"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2))
print(my_counter.most_common(2)[0][1])
print(list(my_counter.elements()))

#this creates a class with the fields x and y class name is 'Point'
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# Ordered Dict
ordered_dict = OrderedDict()
#ordered_dict = {}
ordered_dict['d'] = 4
ordered_dict['e'] = 5
ordered_dict['f'] = 6
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)

#Default Dict 
#They will have default type even if they has not been set yet
d = defaultdict(int) 
#d = defaultdict(int) 
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])  #default value for int is 0 so output is 0 
#if you put float for default the output will be 0.0

#Deque is double ended quee, it can be used to remove and add elements 
#from both end 
d1 = deque()
d1.append(1)
d1.append(2)
d1.append(3)
d1.appendleft(0)
print(d1)

d1.pop()
print(d1)
d1.popleft()
print(d1)
d1.clear() #will delete everything
d1.extendleft([4, 5, 6, 7])
print(d1)
d1.rotate(1)
print(d1)
#d1.rotate(-1)
#d1.rotate(2)


