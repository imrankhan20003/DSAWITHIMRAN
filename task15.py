empty_tuple =()
print(empty_tuple)

tuple1=('item1','item2')
print(tuple1)

first_item= tuple1[0]
print(first_item)

second_tuple=tuple1[1]
print(second_tuple)

fruits= ('banana','apple')
first_fruit = fruits[0]
second_fruit =fruits[1]
print(first_fruit)
print(second_fruit)

last_index=len(fruits)
print(last_index)
# slicing
tuple2=('item1','item2','item3','item4','item5')
print(tuple2)
middle_two_item=tuple2[0:1]
print(middle_two_item)
all_item=tuple2[0:4]
print(all_item)
first_item=tuple2[0:5]
print(first_item)
#RAnge for negative indexec
tuple3=('item1','item2','item3','item4','item5')
all_item=tuple3[-5]
print(all_item)
tuple3=('item1','item2','item3','item4','item5')
del tuple3
print(tuple3)