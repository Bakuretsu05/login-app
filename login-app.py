#database
userName = ['admin'] 
userPass = ['admin']

while True:
    userInput = input('Login or New: ')

    if userInput == 'Login' or userInput == 'login':
        inName = input('Username: ')
        if inName in userName:
            inPass = input('Password: ')
            Matcher = userName.index(inName)
            if inPass == userPass[Matcher]:
                print('You\'ve succesfully logged in!')
                input('')
                break
            else: print('You entered the wrong password...')
        else: print('The username you typed in does not exist...')

    elif userInput == 'New' or userInput == 'new':
        inName = input('Please enter a new username: ')
        if inName in userName: print('Username already exists')

        inPass = input('Please enter the password: ')

        userName.append(inName)
        userPass.append(inPass)

    else: print('Input invalid...')
