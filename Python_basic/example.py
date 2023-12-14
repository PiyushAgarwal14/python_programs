class Cat:
  species = 'mammal'

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def oldest_cat(self):
    oldest_cat = None
    if cat1.age > cat2.age and cat1.age > cat3.age:
      # print(f'Oldest cat is {cat1.name}, and age is {cat1.age} \n')
      oldest_cat = cat1
    elif cat2.age > cat3.age:
      # print(f'Oldest cat is {cat2.name}, and age is {cat2.age} \n')
      oldest_cat = cat2

    else:
      # print(f'Oldest cat is {cat3.name}, and age is {cat3.age} \n')
      oldest_cat = cat3

    return oldest_cat


cat1 = Cat('Tom', 5)
cat2 = Cat('Oggy', 4)
cat3 = Cat('Jack', 7)

print(f'first cat name is {cat1.name}, and age is {cat1.age} \n')
print(f'second cat name is {cat2.name}, and age is {cat2.age} \n')
print(f'third cat name is {cat3.name}, and age is {cat3.age} \n')

oldest_cat = cat1.oldest_cat()
print(f'Oldest cat is {oldest_cat.name} and age is {oldest_cat.age}')
