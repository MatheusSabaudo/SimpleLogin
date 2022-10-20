# ////////////////////////////////////////
# //                                    //
# // Name: Sabaudo Matteo               //
# //                                    //
# // Assignment: Simple Login System    //
# //                                    //
# ////////////////////////////////////////


#USERNAME AND PASSWORD DATA INPUT
print("SIMPLE LOGIN SYSTEM - Sabaudo Matteo")
username = input("\nUsername: ").lower()
pwd = input("Password: ")

if username == "matteosabaudo" and pwd == "password123":
    print(f"\nWelcome to the system! {username}")
else:
    print("\n[ERROR] Username and/or Password Incorrect!")
