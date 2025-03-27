import os
booklist=[]
booklist1=[]
booklist2={}
account={}
allbooklist='C:\\Users\\Lenovo\\Desktop\\Python Training Files\\Booklist.txt'
credentials='C:\\Users\\Lenovo\\Desktop\\Python Training Files\\Credentials.txt'

#making a function to check if an input is apart of the designated functions of my library system.
def inputtask(*tasks):
    #takes prompts and puts them into a list
    actions=[]
    original=[]
    for choices in tasks:
        actions.append(choices.lower())
        original.append(choices)
    string=', '.join(original)
    task=input('Pick a task from '+string+': ').lower()
    #to check if the input in valid.
    while task not in actions:
        task=input('Please only type '+string+': ').lower()
        if task in actions:
            break
    return task


#a function to check whether if the input is only 'yes' or 'no'.
def repeat(ans,caps,*criteria):
    list=[]
    for choices in criteria:
        list.append(choices)
    if ans in list:
        pass
    else:
        while ans not in list:
            string=', '.join(list)
            ans=input('Please only type '+string+'. ')
            if caps == 'up':
                ans=ans.upper()
            else:
                ans=ans.lower()
            if ans in list:
                break
    return ans



#a function to check whether the user input is intended.     
def compare(original,category,*other):
    try:
        if other[0] == 'other':
            ask=input('is '+original+' the '+category+' ?\nPlease check carefully and only type yes or no ').lower()
            ask=repeat(ask,'no','yes','no').lower()
        else:
            ask=input('is '+original+' the '+category+' of the book?\nPlease check carefully and only type yes or no ').lower()
            ask=repeat(ask,'no','yes','no').lower()
    except IndexError:
        ask=input('is '+original+' the '+category+' of the book?\nPlease check carefully and only type yes or no ').lower()
        ask=repeat(ask,'no','yes','no').lower()
    if ask == 'no':#if the input is unintended e.g. typos then repeat the question.
        while ask =='no':
            try:
                if other[1] == 'no':
                    addinfo = input('Type in '+category+' ').lower()
                else:
                    addinfo = input('Type in '+category+' ').upper()
            except IndexError:
                addinfo = input('Type in '+category+' ').lower()
            list=['ISBN','PUBLICATION YEAR','QUANTITY']
            if category in list:#check if the input is only numbers for the categories in the list
                addinfo=intcheck(addinfo)#a function to make sure the input is an integer
                if category=='ISBN':
                    addinfo=addinfo.rjust(6,'0')#add leading zeros to ISBN numbers
                else:
                    pass    
            else:
                pass  
                    
            ask=input('is '+addinfo+' the '+category+' of the book? Please only type yes or no: ').lower()
            ask=repeat(ask,'no','yes','no')
            if ask =='yes':
                print(addinfo)
                return addinfo #return actual value
            else:
                continue
    else:
        print(original)
        return original#return original value if it is intended


#to check whether an input is an integer
def intcheck(input_):
    try:
        input_=int(input_)
        
    except:
        while input_ != int():
            try:
                input_=int(input_)
                break
            except:
                input_=input('Please only type in a number! ')
    else:
        pass
    input_=str(input_)
    return input_

def library():
   
    #open the text file  
    with open(allbooklist, 'r') as f: 
      #read the text file into a list of lines 
      lines=f.readlines()
    for i in range(len(lines)):
        var=lines[i]#put the keyword as a variable
        split=var.split(": ",1)
        rawdata=split[0].strip(" {}\n[] ")#remove said symbols from the string
        rawdata=rawdata.replace("'","")#replaces apostrophe with empty string
        raw_data=split[1].strip(" {}\n[] ")#remove symbol from list
        raw_data=raw_data.replace("'","")#replaces apostrophe with empty string
        value=[]
        values=raw_data.split(', ')#split value into list
        for i in range(len(values)):
            elements=values[i]
            elements=str(elements)
            elements.strip(" \n[]{} ")
            value.append(elements)
            for i in range(len(elements)):
                res=elements.split(':')#find the details of the book
                for i in range(len(res)):
                    key=res[0].strip("'' ")
                    value1=res[1].strip("'' ")
                    details={}
                    details[key]=value1
            booklist2[rawdata]=value#put the values into a dictionary

    return booklist2
def register():#to register accounts
    user=input('Type in user name: ')#get preferred username
    user=compare(user,'user name','other')
    with open(credentials, 'r') as f:
        lines=f.readlines()
    for i in range(len(lines)):
        key=lines[i].split(': ')[0]
        keys=[]
        keys.append(key)
        if user in keys:
            while user in keys:
                user=input('that user name is already taken\nType in a new username or no to terminate program: ')
                if user == 'no':
                    return 'Goodbye. Hope to see you again'
                user=compare(user,'user name','other')
                
    password=input('Type in password: ')#get preferred password
    password=compare(password,'password','other')
    while len(password) < 8:#make sure the password has at least 8 characters
        password=input('Password should at least have 8 characters: ')
        password=compare(password,'password','other')
    with open(credentials,'a') as file:
        file.write(user+': '+password+'\n')#write down the credentials into a file

def login():#function to log into accounts
    with open (credentials,'r') as file:
        lines=file.readlines()#read the file line by line
    for i in range(len(lines)):#loop through the lines
        var=lines[i]
        var=var.split(': ')#split the line into the username and password
        user=var[0]
        password=var[1].strip('\n ')
        account[user]=password#enter the credentials into a dictionary
    user_name=input('Please enter your username: ')
    pw=input('Please enter your password: ')
    counter=0
    for key in account:
        if user_name == key:
            counter=1#to check if ther user name inputted is in the dictionary
            if account[key]==pw:
                print('Welcome '+user_name)
                return True
                
            else:
                print('password incorrect')
                return False
    if counter==0:#if counter is 0, it means that the inputted user name is not in the dictionary details
        print('user name not found! ')
        return False


#function to add new books with information included into the booklist
def add():
    addinfo = input('Type in book name ').upper()
    addinfo=compare(addinfo,'title')#checking if input is intended.
    print('Please type in author, ISBN, genre, publication year and quantity of the book')
    bookinfo={}#a dictionary to store details of books with title key and a list of book details as values
    ISBN=input('ISBN is: ').upper()
    ISBN=intcheck(ISBN)
    ISBN=ISBN.rjust(6,'0')
    ISBN=compare(ISBN,'ISBN')
    booklist2=library()
    for key in booklist2:
        if 'ISBN is: '+ISBN in booklist2[key]:
            return print('ISBN cannot be duplicate')
    author=input('Author is: ').upper()
    author=compare(author,'author')
    genre=input('Genre: ').upper()
    genre=compare(genre,'Genre')
    pub_year=input('Publication year is: ').upper()
    pub_year=intcheck(pub_year)
    pub_year=compare(pub_year,'PUBLICATION YEAR')
    quantity=input('Quantity is: ').upper()
    quantity=intcheck(quantity)
    quantity=compare(quantity,'QUANTITY')
    #store details into dictionary
    bookinfo[addinfo]=['ISBN is: '+ISBN,
                       'AUTHOR is: '+author,
                       'GENRE is: '+genre,
                       'PUBLICATION YEAR is: '+pub_year,
                       'QUANTITY is: '+quantity]

    #code to write the code into a file
    booklist.append(bookinfo)
    booklist1=booklist
    for i in range(len(booklist)):
        print(booklist[i])
    with open(allbooklist,'a') as file:
        for i in range(len(booklist1)):
            book=str(booklist1[i])+'\n'
            file.write(book)
            booklist1.pop(i)

    print('book successfully added.')
    

#function to edit books
def edit():
    library()#load in all books and details into a dictionary
    delete()#delete the book that needs to be edited
    print('Please retype in the book details. ')
    add()#readd the book with all the new and correct details

#function to delete books
def delete(*keyword):
    library()
    if keyword !=():#if there is an input, then use this function
        key1=keyword[0].strip()#strip the prompt of spaces
        del booklist2[key1]#delete the book with the name inputted in the dictionary booklist2
        return booklist2#return the altered booklist
    task=str(inputtask('TITLE','ISBN')).upper()
    #only allow either title or ISBN to be entered as they are unique keys
    if task == 'TITLE':
        name = input('Type in title of the book. ').upper()
        name=compare(name,'TITLE')
        try:
            print(booklist2[name])
            del booklist2[name]# deletes title inputted from dictionary
            for key in booklist2:
                string=str(key)+' : '+str(booklist2[key])
                booklist.append(string)
            booklist1=booklist
            with open(allbooklist,'w') as file:#code to write in details in dictionary into a text file
                with open(allbooklist,'w') as f:
                    for i in range(len(booklist1)):
                        book=str(booklist1[0])+'\n'
                        f.write(book)
                        booklist1.pop(0)
            print('book successfully deleted! ')
        except:
            print('book title not found')
            
        
        
            

        
            
    else:
        detail=input('Please type in ISBN of the book: ')
        detail=intcheck(detail)    
        detail=detail.rjust(6,'0')
        detail=compare(detail,task)
        detail=task+' is: '+detail
        for key in booklist2.copy():#finds if a value is present in the key.
            #.copy() is used so we can change values in dictionary while iterating through it
            if detail in booklist2[key]:
                del booklist2[key]# deletes title from dictionary
                for key in booklist2:
                    string=str(key)+' : '+str(booklist2[key])
                    booklist.append(string)
                booklist1=booklist
                with open(allbooklist,'w') as file:
                    with open(allbooklist,'w') as f:
                        for i in range(len(booklist1)):
                            book=str(booklist1[0])+'\n'
                            f.write(book)
                            booklist1.pop(0)

                print('book successfully deleted! ')
                break                    
            else:
                print(task+' is not found')

    return booklist2

#function to search for books
def search():
    task=str(inputtask('TITLE','ISBN','AUTHOR','PUBLICATION YEAR', 'GENRE')).upper()
    #ask user which category they want to search for
    booklist2=library()#load in books in file into a dictionary 'booklist2'
    
    if task == 'TITLE':
        name = input('Type in title of the book. ').upper()
        name=str(compare(name,'TITLE'))
        try:
            book=str(name)+': '+str(booklist2[name])
            #show the book title and details if book in dictionary
            return book
        except:
           return 'Title of book not found'
        
            
    else:
        detail=input('Type the '+task+' in here: ').upper()
        task=task.strip()
        list=['ISBN','PUBLICATION YEAR']
        if task in list:
            detail=intcheck(detail)
            if task==list[0]:
                detail=detail.rjust(6,'0')
        else:
            pass
        detail=compare(detail,task)
        detail=task+' is: '+detail
        counter=0
        list_of_books=[]
        for key in booklist2:#finds if a value is present in the key.
            if detail in booklist2[key]:
                string=str(booklist2[key])
                book=key+' : '+string
                print(book)
                list_of_books.append(book)
                counter+=1#to check if multiple books have the same details.
                continue
            else:
                pass
        if counter==0:
            return task+' is not found'
        else:
            if counter>1:
                num=input('Type in the number to pick which book: ')
                num=intcheck(num)
                while int(num)>len(list_of_books):
                    num = input('Please only type a number between 1 to '+str(len(list_of_books))+': ')
                    num=intcheck(num)
                num=int(num)-1
                book=list_of_books[num]
                print(book)
                return book
        
def show():#function to print out all books in library
    x=library()
    for key in x:
        string=str(x[key])
        print(str(key)+' : '+string)
#function taht allows users to loan books
def loan_or_return(action):
    booklist2=library()
    print('Type in details of book you want to loan: ')
    book=search()
    
    if book==None or 'not found' in book:
        return 'Book not found'
    else:
        print(book)
        key=book.split(': ',1)[0]
        value=book.split(': ',1)[1]
        values=[]
        book=book.split("QUANTITY is: ",1)
        quantity=int(book[1].strip("'] "))
        if action == 'loan':
            quantity-=1#minus one from quantity of book if book is loaned
            if quantity <=0:
                return print('not available')#let's user know if there are no more left of said book
            else:
                print('available')
        else:
            quantity+=1

        #code to put the new quantity into the booklist
        book[1]='QUANTITY is: '+str(quantity)+"']"
        book=''.join(book)#turn the list into a string
        print(book)
        book=book.split(': ',1)[1]
        value=book.split(', ')
        for i in range(len(value)):
            value[i]=value[i].strip("'[] '")#remove these symbols from the string
            values.append(value[i])
        booklist2=delete(key)
        booklist2[key]=values
        for key in booklist2:
            string=str(key)+' : '+str(booklist2[key])
            booklist.append(string)
        booklist1=booklist
        with open(allbooklist,'w') as file:
            with open(allbooklist,'w') as f:
                for i in range(len(booklist1)):
                    book=str(booklist1[0])+'\n'
                    f.write(book)
                    booklist1.pop(0)
        return 'Book succesfully '+action+'ed'


def start(choice):#code for what to do responding to the input
    choice=repeat(choice,'no','yes','no')#makes sure that the input is only yes or no
    counter=1
    if choice=='yes':
        
        while choice=='yes':
            if counter==1:
                ans =input('Do you have an account?: ').lower()
                ans=repeat(ans,'no','yes','no')
                if ans == 'yes':
                    counter=0
                    for i in range(3):
                        acc_check=login()
                        if acc_check == False:
                            counter+=1
                        else:
                            break
                    if counter==3:
                        return print('The program has been terminated as you have failed the login phase three times. ')
                else:
                    question=input('Do you want to create an account?: ')
                    question=repeat(question,'no','yes','no')
                    if question == 'yes':
                        x=register()
                        if x=='Goodbye. Hope to see you again':
                            return print(x)
                        else:
                            return print('Please restart the program and login with your account. ')
                    else:
                        return print('You have to login to continue! ')
            task=inputtask('add','search','delete','show','edit','loan','return')
            if task == 'add':
                add()
            elif task == 'search':
                search()
            elif task == 'delete':
                booklist2=delete()
            elif task == 'show':
                show()
            elif task == 'edit':
                edit()
            elif task == 'loan':
                print(loan_or_return('loan'))
            elif task=='return':
                print(loan_or_return('return'))
                
            restart = input('do you want to continue?: ').lower()
            choice=repeat(restart,'no','yes','no')
            if choice =='yes':
                continue
            else:
                print('Thank you for visiting. ')
                break
    else:
        print('Thank you for visiting.')
        
        
    

    
        
choice=input('Welcome. Type yes to start: ')
start(choice)

