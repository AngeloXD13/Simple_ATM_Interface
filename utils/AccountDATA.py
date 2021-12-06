class Account(object):
   def __init__(self):

    self.fname = None
    self.mname = None
    self.lname = None
    self.bday = None
    self.lothouse = None
    self.barangay = None
    self.citymuni = None
    self.province = None
    self.zipcode = None
    self.typeofid = None
    self.idnumber = None
    self.email = None
    self.phonenumber = None
    self.status = None
    self.availablebalance = None
    self.onholdbalance = None
    self.currentbalance = None
    self.pin = None


    def deleteAccountDATA():
     self.fname = None
     self.mname = None
     self.lname = None
     self.bday = None
     self.lothouse = None
     self.barangay = None
     self.citymuni = None
     self.province = None
     self.zipcode = None
     self.typeofid = None
     self.idnumber = None
     self.email = None
     self.phonenumber = None
     self.status = None
     self.availablebalance = None
     self.currentbalance = None
     self.pin = None

"""
    # using property decorator
    # a getter function
    @property
    def fname(self):
      print("setter method called")
      return self.fname

    # a setter function
    @fname.setter
    def fname(self,a):
      print("setter method called")
      self.fname = a


newaccount = Account()
newaccount.fname = "Angelo"
print(newaccount.fname)
"""