#Inheritance is the process of acquiring the attributes of a built-in or self-defined class to a class you are just creating;
# Syntax: class NewClass(OriginalClass):

class Member_RockBand(object):
      def __init__(self,name,instrument,years):
            self.name = name
            self.instrument = instrument
            self.years = years
            
member_1 = Member_RockBand('Kirk','Electric Guitar',42) 
member_2 = Member_RockBand('Slash', 'Electric Guitar', 41)

  #Now creating an class that inherit from the initial class the variables;
class Retiree(Member_RockBand):
      def __init__(self, name, instrument,years,status):
            self.name = name
            self.instrument = instrument
            self.years = years
            self.status = status

retiree_1 = Retiree('Ozzy','Vocalist',63,'Retiring')

print(member_1.name)
print(retiree_1.name)
