def user_info(name, age=0, city="Colombo") :
    #This function prints name,age,and city from an argument provided to the function

    print ("{} is {} years old, from {}".format(name, age, city))

user_info("Thara", 30, "Matara")
user_info("Thara")
user_info(age = 20, name ="Thara")

def application(fname,lname,company,email, *args, **kwargs) :
    print ("{} {} works at {} and her email is {} ".format(fname,lname,company,email))
    print(args)
    print(kwargs)

application("Thara","Perera","BlackSwan","thara@test.com", 50000 , age="28")
