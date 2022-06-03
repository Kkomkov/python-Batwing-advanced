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
        return (f"{self.name},{self.last_name},{self.phone_number},{self.address},{self.email},{self.birthday},{self.age} years,{self.sex}")

myProfile = Profile()
myProfile.name="Me"
myProfile.age=10
myProfile.sex="male"
print(myProfile)