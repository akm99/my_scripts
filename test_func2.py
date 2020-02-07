def find_detail():
    name = input("enter your name: ")
    loc = input("Enter your location: ")
    job = input("Enter your job: ")
    race = input("Enter your race: ")
    interest = input("Enter your interest: ")
    print ("how are you today {}".format(name))
    print ("Location is {}".format(loc))
    print ("Job is {}".format(job))
    print ("Race is {}".format(race))
    print ("Interest is {}".format(interest))
    
def get_info():
    find_detail()


get_info()
