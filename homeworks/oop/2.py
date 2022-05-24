

class Arm:
    pass

class Person:
    def __init__(self) :
        self.left_arm =Arm()
        self.right_arm=Arm()


class Screen: pass
class CellPhone:
    def __init__(self,screen):
        self.screen=screen


man =Person()
phone1 = CellPhone(Screen())
phone2 = CellPhone(Arm())
phone3 = CellPhone(man)

phone4 = CellPhone(phone3)
for item in (phone1,phone2,phone3,phone4):
    print("CellPhone screen is ",item.screen.__class__.__name__)

print("")
print("")