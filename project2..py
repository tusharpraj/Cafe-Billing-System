billl=0
gst=0
tot=0
print("_*_*_*_*_*_*_*_*_*_*_*_*_*_( WELCOME TO SYSTEM CAFE )_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")

tu="y"
while(tu=="y"):
    print("""
    Press 1 for Tea 
    Press 2 for Coffee
    Press 3 for Snacks
    Press 4 for Cold-drink """)
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        print("--Tea-- ")
        print("""
            Press 1 for Masala Tea--7rs
            Press 2 for Ginger Tea--10rs
            Press 3 for Elaichi Tea--12rs
            Press 4 for Rose Tea--17rs """)
        select=int(input("Choose Your Tea: "))
        if select==1:
            pr=7
            print("--Masala Tea--")
        if select==2:
            pr=10
            print("--Ginger Tea--")
        if select==3:
            pr=12
            print("--Elaichi Tea--")      
        if select==4:
            pr=17
            print("--Rose Tea--")
        print("""
            Press 1 for Disposal Cup --1rs
            Press 2 for Chini Cup --2rs
            Press 3 for Kulhad Cup --3rs
            Press 4 for Cookie Cup --10rs """)
        cup=int(input("Enter Your Cup: "))
        if cup==1:
            cp=1
            print("--Disposal Cup--")
        if cup==2:
            cp=2
            print("--Chini Cup--")
        if cup==3:
            cp=3
            print("--Kulhad Cup--")
        if cup==4:
            cp=10
            print("--Cookie Cup--")
        print("""
            Press 1 For Small Cup -- 2rs
            Press 2 for Medium Cup -- 4rs
            Press 3 for Large Cup -- 6rs """)
        size=int(input("Enter Your Cup Size: "))
        if size==1:
            sz=2
            print("--Small Cup-- ")
        if size==2:
            sz=4
            print("--Medium Cup-- ")
        if size==3:
            sz=6
            print("--Large Cup-- ")
            
        qt=int(input("Enter Quantity: "))
        tot=((qt*pr)+cp+sz)
        gst=((5/100)*tot)
        print("GST Tax: ",gst)
        billl=billl+gst+tot
        print("Total Bill(Incl.Tax): ",tot+gst,"Rs")
        print("Total Bill After Add New Item:",billl,"Rs")
        print("Note:--Payment Accepted Via Online Only--")
        

    if choice==2:
        print("--Coffee-- ")
        print("""
        Press 1 for Hot Coffee
        Press 2 for Cold-Coffee
        Press 3 for Coffee with Ice-Cream
        Press 4 for Dark Coffee Spcl.""")
        coffee=int(input("Enter Your Selection: "))
        if coffee==1:
            pr=15
            print("--Hot Coffee--")
        if coffee==2:
            pr=30
            print("--Cold-Coffee--")
        if coffee==3:
            pr=35
            print("--Coffee with Ice-Cream--")
        if coffee==4:
            pr=40
            print("--Dark Coffee Spcl.--")
        print("""
        Press 1 For Small Cup
        Press 2 for Medium Cup
        Press 3 for Large Cup  """)
        cup=int(input("Enter Cup Size: "))
        if cup==1:
            cs=5
            print("--Small Cup--")
        if cup==2:
            cs=10
            print("--Medium Cup--")
        if cup==3:
            cs=15
            print("--Large Cup--")
        qt=int(input("Enter Quantity: "))
        tot=(qt*pr)+cs
        gst=((5/100)*tot)
        print("GST Tax: ",gst)
        billl=billl+gst+tot
        print("Total Bill(Incl.Tax): ",tot+gst,"Rs")
        print("Total Bill After Add New Item:",billl,"Rs")
        print("Note:--Payment Accepted Via Online Only--")

    if choice==3:
        print("--Snacks-- ")
        print("""
        Press 1 For Cookies
        Press 2 For Patties
        Press 3 For Burger
        Press 4 For Sandwich """)
        snack=int(input("Choose Your Snack: "))
        if snack==1:
            pr=10
            print("--Cookies--")
        if snack==2:
            pr=20
            print("--Patties--")
        if snack==3:
            pr=30
            print("--Burger--")
        if snack==4:
            pr=40
            print("--Sandwich--")
        qt=int(input("Enter Quantity: "))
        tot=(qt*pr)
        gst=((5/100)*tot)
        print("GST Tax: ",gst)
        billl=billl+gst+tot
        print("Total Bill(Incl.Tax): ",tot+gst,"Rs")
        print("Total Bill After Add New Item:",billl,"Rs")
        print("Note:--Payment Accepted Via Online Only--")
        
      
    if choice==4:
        print("--Cold-drinks-- ")
        print("""
        Press 1 For Sprite
        Press 2 For Mirinda
        Press 3 For Mountain Dew
        Press 4 For Pepsi """)
        cold=int(input("Enter Your Drink Type: "))
        if cold==1:
            print("--Sprite--")
        if cold==2:
            print("--Mirinda--")
        if cold==3:
            print("--Mountain dew--")
        if cold==4:
            print("--Pepsi--")
        print("""
        Press 1 For 300Ml
        Press 2 For 600Ml
        Press 3 For 750Ml
        Press 4 For 1.5Lit
        Press 5 For 2 Lit""")
        size=int(input("Choose Drink Volume: "))
        if size==1:
            pr=36
            print("--300Ml only Can-- ")
        if size==2:
            pr=36
            print("--600Ml--")
        if size==3:
            pr=40
            print("--750Ml--")
        if size==4:
            pr=66
            print("--1.5 Litre--")
        if size==5:
            pr=78
            print("--2 Litre--")
        qt=int(input("Enter Quantity: "))
        tot=(qt*pr)
        gst=((5/100)*tot)
        print("GST Tax: ",gst)
        print("Total Bill(Incl. Tax): ",tot+gst,"Rs")
        billl=billl+gst+tot
        print("Total Bill After Add New Item:",billl,"Rs")
        print("Note:--Payment Accepted Via Online Only--")
    if choice>=4:
        print("invalid choice")
    tu=input("do you want to continue press y / n ")
    print("Thank you for visiting System Cafe. Have a great day!")
