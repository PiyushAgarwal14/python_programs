
# class Super_list(object):

#   def __len__(self):
#     self.my_list = [1, 2, 3, 4, 5]

#   def __getitem__(self, i):
#     return self.my_list[i]

# super_list1 = Super_list()
# print(*super_list1)

# super_list1.my_list.append(6)
# # print(super_list1[5])
# # print(super_list1[:])
# print(f'Updated list {super_list1.my_list}')
# print(f'Length of the list is {len(super_list1.my_list)}')


class Super_list(list):

  def __len__(self):
    return 1000

super_list1 = Super_list()

print(f'Length of the list is {len(super_list1)}')

super_list1.append(6)
print(super_list1[0])
print(issubclass(Super_list, list))