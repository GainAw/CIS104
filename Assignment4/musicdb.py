try: 
    with open('MusicDB.txt', 'r') as myfile:
        mastertext = myfile.read()
        masterlist = eval(mastertext)
except:
    masterlist = []

def music(choice):
    if choice.lower() == "add":
        new = {}
        new["artist"] = input("Artist Name? ")
        new["title"] = input("Song title? ")
        new["album"] = input("from what album? ")
        new["track"] = input("track number? ")
        new["year"] = input("what year was it published? ")
        new["genre"] = input("what genre is it? ")
        if len(masterlist) <= 7:
            masterlist.append(new)
        else:
            print("too many songs")
        print(masterlist)
    elif choice.lower() == "list":
        for thing in masterlist:
            print("\nyour stuuf that we have you stuff")
            for key, value in thing.items():
                print((f"{key} is {value}"))
    elif choice.lower() == "save":
        string = str(masterlist)
        myfile = open('MusicDB.txt', 'w')
        myfile.write(string)
        myfile.close
    elif choice.lower() == "help":
        print('''
        "add" will add a song\n
        "list" will list your current songs in the database\n
        "save" will save your current list to the database\n
        "help" to bring up this menu\n
        "exit" does just what you think it will
''')
    elif choice.lower() == "exit":
        import sys
        sys.exit()
    elif choice.lower() =="sort":
        sorting_list = []
        string = str(masterlist)
        for thing in masterlist:
            sorting_place = []
            for key, value in thing.items():
                sorting_place.append(f"{key} : {value}")   
            sorting_list.append(sorting_place)
        print(sorting_list)