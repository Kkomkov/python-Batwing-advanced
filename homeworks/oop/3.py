from pickle import NONE


class Profile:
    name = None
    last_name = None
    phone_number = None
    address = None
    email = None
    birthday = None
    age = None
    sex = None
    def __str__(self):        
        return (self.name.__str__()+" "+self.last_name.__str__()+" "+self.phone_number.__str__()+" "
        +self.address.__str__()+" "+self.email.__str__()+" "+self.birthday.__str__()+" "+self.age.__str__()+" "+self.sex.__str__())

myProfile = Profile()
myProfile.name="Me"
myProfile.age=10

print(myProfile)