def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    
    names = fullname.split()
    
    initial = ""
    for name in names:
        initial = initial + name[0]
    return initial.upper()
    

def main():
    username = input("What is your full name?")
    get_initials(fullname)

if __name__ == '__main__':
    main()