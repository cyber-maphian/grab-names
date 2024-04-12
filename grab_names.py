import os
while True:
    
    print("GRAB_NAMES HELPS YOU COPY THE NAMES OF FILE AND SAVE IT FOR YOU..")
    print()
    # a simple programm that copy the name of a specific file an paste into a file you provided
    names = os.listdir()
    extention = input('extention of the file name to be copyed eg(.txt,.py):  ')
    save_to = input("save the names to file? eg(names.txt):  ")

    #we loop through the names of the file in the directory
    for i in names:
        #we find the once with your provided extention
        if extention in i:
            #we remove the extention name from the file we want to save
            main_name = i.replace(extention,'')
            print(i,"was successful")
            #open the file we want to save into and paste
            file = open(save_to,"a")
            file.write(main_name)
            file.write("\n")
            file.close()
        else:
            print('this file does not match your extention..',i)
            
    print("\n")
    print("successfuly copied the names to",save_to)
