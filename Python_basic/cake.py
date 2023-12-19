class Cake(object):

  def bakery(self):
    print('Welcome \n')

class order_details(Cake):
    def __init__(self, o_id, cake_name, cake_p, cake_q):
      self.o_id = o_id
      self.cake_name = cake_name
      self.cake_p = cake_p
      self.cake_q = cake_q

    def od(self):
      print(f"Order Id: {self.o_id}, Cake name {self.cake_name}, Price {self.cake_p}, quantity {self.cake_q}")
      
class customer_detail(Cake):
    def __init__(self,c_name, c_no):
      self.c_name = c_name
      self.c_no = c_no

    def cd(self):
      print(f"Customer name : {self.c_name}, Contact number : {self.c_no}")

class order_customer(order_details, customer_detail):
  def __init__(self, o_id, cake_name, cake_p, cake_q, c_name, c_no):
    super().__init__(o_id, cake_name, cake_p, cake_q)
    customer_detail.__init__(self, c_name, c_no)


o1 = order_customer('12345', 'Vanilla', '350', '1', 'Piyush', '123456')
# o1.od()
# o1.cd()

o2 = order_customer('12346', 'Chocolate', '550', '1', 'test1', '1234568')
o3 = order_customer('12347', 'Pineapple', '250', '1', 'test2', '1234569')
oc = [o1, o2, o3]

target = (input('Enter Order Id: \n'))

def search_by_o_id(oc, temp):
  for i in range(len(oc)):
    if temp == oc[i].o_id:
        return oc[i]
  return None

found_order = search_by_o_id(oc, target)

if found_order:
  print('Order found')
  found_order.od()
  found_order.cd()

else:
  print(f'order with order is: {target} not found')