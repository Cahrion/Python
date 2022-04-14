
users = {

    "Sadikturan": {
        "Age": "36",
        "Roles": ["user"],
        "Email": "sadik@gmail.com",
        "Address":"Kocaeli",
        "Phone":"125125"
    },
    "Cinarturan": {
        "Age": "2",
        "Roles": ["user", "admin"],
        "Email": "cinar@gmail.com",
        "Address":"Kocaeli",
        "Phone":"125126"
    
    }

}

a1 = input("Ögrenmek istediginiz kişi ismi:  ")
a2 = input("Neyini ögrenmek istersiniz: ")

a1 = a1.split()
a1 = ("").join(a1)
a1 = a1.title()

a2 = a2.split()
a2 = ("").join(a2)
a2 = a2.title()

print(users[a1][a2])



