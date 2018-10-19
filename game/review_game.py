import os

questions_On = True
# Change this to False if you want to turn all the questions off!

def pause():
    print("\n------------------------")
    os.system("pause")

def guess(prompt, key):
    z = input("\t" + prompt +  "\n\t> ")
    while z != key and z != "`" and questions_On:
        print("\n\tNope! Guess again!")
        if z == "help":
            print("\t***Hint, the answer is: " + key + "***")
        z = input("\t" + prompt +  "\n\t> ")
    print("CORRECT!! The answer is: " + key)

def test1():
    print("EXAM ONE REVIEW")
    print("\n(Pardon the Harry Potter stuff, I was initially going to make it Harry Potter-themed but I ran out of magic)\n")
    print("PART ONE: built-in functions!")
    #-----------------------------------------------
    print("First, we'll look at len(*Collection thingy*)!")
    print("Use this spell to find the length of things!")
    pause()
    x = [1,2,3,4,5,6,7]
    print("Here's a list: \n x = " + str(x))
    guess("How do we find its length?","len(x)")
    print("""
        You can use len() to find the number of items in:
        \t- Lists len([1,2,3]) = 3
        \t- Strings len("12345") = 5
        \t- Tuples len((1,2,3,4)) = 4
        \t- Dictionaries (length is # of key-value pairs)
    """)
    pause()
    #-------------------------------------------------
    print("Next up! str()")
    print("str() is a spell that turns things...into STRINGS")
    pause()
    print("Here's a list: \n x = " + str(x))
    guess('How do we change x into "[1,2,3,4,5]"?',"str(x)")
    print("Question: When is this useful? Think about it.")
    pause()
    print("""
    That's right! You should use str() when you
    need something that's not a string to be a string!

        Examples: (x is a list)
        print("Here's my list!" + x) --> FAILS (can't concatenate a list and a string)
        print("Here's my list!" + str(x)) --> GOOD :)

        makeThisStringAllCaps(x) --> FAILS (pretend the function needs a string)
        makeThisStringAllCaps(str(x)) --> GOOD :)
    """)
    pause()
    #---------------------------------------------------
    print("Next up! int()")
    print("int() is a spell that changes a string to an integer!")
    guess("x = '32' THIS IS A STRING. Change this to an integer!","int(x)")
    print("Think, when would you use this?")
    pause()
    print("""
        That's right! Whenever you need an integer!
        ESPECIALLY when getting user input.
        input("ENTER A NUMBER") --> ALWAYS returns a string, even if they enter '32'
    """)
    pause()
    print("Question: can you do int() with decimals, like int(3.455)?")
    pause()
    print("""
        YES! The only time this could cause a problem is when you have a DECIMAL in a STRING.
        Rememeber that int always ROUNDS DOWN (except in a few special cases, which you don't need to know about).
            int(45.4) ->  45
            int(45.4) ->  45
            int("45.9") ->  ERROR
            int(float("45.9")) -> 45
    """)

    pause()

    print("""
        FUN FACT! You do NOT need to know this haha.
        int() can be used on a string of bytes to like change a string of
        binary to an integer in base 10!

        int("1010",2) = 10
            (the 2 means base 2)
        int("10",16) = 16
            (hexadecimal :) )
    """)
    pause()
    #---------------------------------------------------------------------
    print("Next up! float()")
    print("float is a spell that changes a STRING into a decimal!")
    guess("x = '12.32'   CHANGE X TO 12.32","float(x)")
    pause()
    #---------------------------------------------------------
    print("Next up! Using print() with commas")
    guess("use print() to print '1 2 3' without using your spacebar (or using paste lol)","print(1,2,3)")
    pause()
    #---------------------------------------------------------
    print("Next up! input()")
    guess("Get input from the user, with a prompt 'enter val'","input('enter val')")
    print("Hey, what does this ALWAYS return? A number? A string? A pizza?")
    pause()
    print("Yep! It always returns a STRING!")
    print("So. if you're getting a number from the user, you better convert the string to a number (using float or int)!")
    #------------------------------------------------------------------
    print("next up! Type!")
    guess("Get the type of x! (What is x? Use this to find out! :) )","type(x)")
    print("Trivia: What does type(type(x)) return?")
    pause()
    print("""
    <class 'type'>
    This means type(*anything*) is a "type thingy"!
    (Just like how 5 is an "int thingy", which you can find out using type()!)
    Next semester, we'll call "thingys" "objects" :)
    """)


    pause()
    print("That's it for Test 1! I'm gonna redirect your trajectory back to the main page, captain. :)")
    main()

def test2():
    print("EXAM TWO REVIEW")
    pause()
    print("""
    First up! Boolean Values.
    First, just know the Boolean literals: True False
        -Think of them as bricks that are just always True or always False
    """)
    pause()
    print("""
    Then, we have the logical operators:
        -and --> A and B == True if A AND B are true (false otherwise)
        -or --> A or B == False if A AND B are false (true otherwise)
        -not --> not A just negates A (A == True --> A == False)
    """)
    guess("What is (not (True and (False or False) or (not False and not True)))?","True")
    print("Question: When do you use boolean operators and values?")
    pause()
    print("You got it! Usually in IF and WHILE blocks")
    pause()
    input("Type 'I, *name*, will look at Professor Tychonievich's slides on Test case selection and debugging strategies' (jk hahaha just enter anything)\n> ")
    #-------------------------------------------------------------------------
    print("Next up! For and while loops")
    print("When should you use a WHILE loop? (Yea! Hoo needs 'em, right?)")
    pause()
    print("""
    When you want a block of code to execute FOREVER until something happens.

    When should you use a FOR loop?
    """)
    pause()
    print("""
    When you want a block of code to execute a specific NUMBER of times (which may depend on something else, like the size of a list)
    """)
    pause()
    print("""
    x = [0,1,2,3,4,5]

    #All of these for loops are the same! Do you see why?

    for i in x:
        print(i)

    for i in range(6):
        print(i)

    for i in range(6):
        print(x[i])
    """)
    pause()
    print("""
    x = [0,1,2,3,4,5]
    range(5) basically equals (0,1,2,3,4)

    ***For-Each loop: i is a different item in x (0 1 2 3 4 5) each time***
    for i in x:
        print(i)

    ***Loop using range: i is a different item in range(6) collection (0 1 2 3 4 5) each time***
    for i in range(6):
        print(i)

    ***Loop using range with index: i is a different item in range(6) collection each time (0 1 2 3 4 5),
    and we use this to get each item of x***
    for i in range(6):
        print(x[i])
    """)
    pause()
    #---------------------------------------------------------
    print(""""
    Question, When you do:
    for i in *something*
        do stuff

    What is *something*? And what are the different types of *something*s?
    """)
    pause()
    print("""
    *something* is a collection type, which includes:
        str
        list
        tuple
        range

    for i in *string*:
        i is each letter of the string!

    for i in list:
        i is each item in the list!

    for i in tuple:
        i is each item in the tuple!

    for i in range:
        i is each number in the range-weird-tuple-object-thingy!
    """)
    pause()
    #----------------------------------------------
    print("DICTIONARIES (get ready for a lot of questions)")
    guess("Make an empty dictionary called d!","d = {}")
    pause()
    guess("Make a dictionary called d where x[3] == 'pizza' initially!","d = {3:'pizza'}")
    pause()
    guess("d = {3:'pizza'}   What does d[3] return?","pizza")
    pause()
    print("d = {3:'pizza'}   What does d['pizza'] return?")
    pause()
    print("TRICK QUESTION! This is an error because 'pizza' isn't a key!")
    guess("d = {3:'pizza'}   Return a list of d's keys","list(d.keys())")
    pause()
    guess("d = {3:'pizza'}   Return a list of d's values","list(d.values())")
    pause()
    guess("d = {3:'pizza'}   Return a list of tuples, where each tuple is (*key*,*value*)","list(d.items())")
    pause()
    guess("d = {3:'pizza'}   Return the corresponding value of 3","d[3]")
    pause()
    guess("d = {3:'pizza'}   REMOVE AND RETURN the corresponding value of 3","list(d.pop(3))")
    pause()
    #-----------------------------------------------------------
    print("IT'S TIME FOR....URLLIB :)")
    print("""
    A good way to learn URLLIB is to first memorize how to do it all in one line, I think.
    It is our goal to print a duck on the screen.

    Let me do the first two lines for you:
    import urllib.request
    z = "http://www.ducksarethebest.com"
    Now, open this url, read it, and decode it so we can see the duck!
    Remember to type 'help' if you want to see the answer!
    """)
    guess("","print(urllib.request.urlopen(z).read().decode('utf-8'))")
    import urllib.request
    z = "http://www.ducksarethebest.com"
    print(urllib.request.urlopen(z).read().decode('utf-8')[780:2141])
    pause()
    print("""
    Let's break this down.

    urllib.request
        - The library that does URL stuff

    .urlopen(z)
        - The method that opens a string url

    .read()
        - Reads the entire URL thingy

    .decode('utf-8')
        - Decodes the URL. Basically, it'll print
        new lines instead of '\\n', etc

    """)
    pause()
    print("""
    Note that we are basically reading all the HTML code on a page.
    If you go to %s in Chrome, right click, and hit "view page source",
    you'll see the same thing.
    """ %(z))
    pause()
    print("""
    Three ways to read URLs:

    ***USING READLINES***
    import urllib.request
    z = urllib.request.urlopen("http://www.noot.space")
    ls = z.readlines() # MAKES A LIST WHERE EACH ITEM IS A LINE OF THE URL THINGY
    for item in ls:
        print(item.decode('utf-8'))

    ***USING A FOR LOOP***
    import urllib.request
    z = urllib.request.urlopen("http://www.noot.space")
    for line in z: # ITERATES THROUGH EACH LINE IN URL THINGY
        print(line.decode('utf-8'))

    ***USING READ()***
    import urllib.request
    z = urllib.request.urlopen("http://www.noot.space")
    print(z.read().decode('utf-8')) #.read() THROWS THE WHOLE THING INTO ONE STRING
    """)
    pause()
    #-------------------------------------------------------------------
    print("Next up! Reading from files!")
    print("""
    y = open('hi.txt','r')

    Similar to URLs:
    y.read() --> puts all the text (after the stream) in a file into one big string
    y.readlines() --> puts all the text (after the stream) into a list, where each line is a line of text from the file
    y.readline() --> takes one line of text (after the stream) and returns it as a string

    for line in y: # "For each line in y"
        *Do stuff with line*
        lets you iterate through the file, where line each time is another line from the file
    """)
    pause()
    #----------------------------------------------------
    print("Next up! Random!")
    guess("return a random number between 0 and 1","random.randrange(0,2)")
    pause()
    guess("Randomly shuffle list x","random.shuffle(x)")
    print("What does random.shuffle(x) RETURN?")
    pause()
    print("none")
    print("It returns none because it just changes the existing list!")
    print("So, if you do x = random.shuffle(x), you are doing x = none !!!")
    pause()
    #--------------------------------------------------------
    print("Next up! String operations!")
    guess("Check if string x is a substring of (is part of) string y!","x in y")
    pause()
    guess("Concatenate strings x and y!","x + y")
    print("When you concatenate strings like x + y, what MUST x and y BOTH be?")
    pause()
    print("They both must be strings!")
    pause()
    guess("x = 'HELLO'   Return hello without typing it","x.lower()")
    pause()
    guess("x = 'hello'   Return HELLO without typing it","x.upper()")
    pause()
    guess("x = '\\n\\n   hello \\n  \\n  '   Return hello without typing it","x.strip()")
    pause()
    guess("x = 'xyxyxyxyxyxyxhelloyyyyyxxxxxx'   Return hello without typing it","x.strip('xy')")
    pause()
    guess("x = 'aHEREbHEREcHEREdHEREe'   Return ['a','b','c','d','e']","x.split('HERE')")
    pause()
    guess("""x = 'let\'s split on the whitespace'  Return ["let's", 'split', 'on', 'the', 'whitespace']""","x.split()")
    pause()
    guess("Return the index of the first occurrence of 'pizza' in string x, or -1 if it's not in x.","x.find('pizza')")
    pause()
    #-------------------------------------------------------
    print("It's time for......LISTS!! :)")
    pause()
    guess("Make an empty list called x","x = []")
    pause()
    guess("Check if 5 is in list x (return True if it is)","5 in x")
    pause()
    guess("Add the number 5 to list x","x.append(5)")
    pause()
    guess("Make the first value of list x 'hello', shifting everything down","x.insert(0,'hello')")
    pause()
    guess("Remove 'pizza' from list x", "x.remove('pizza')")
    print("Does this return anything?")
    pause()
    print("No! It returns none!")
    pause()
    guess("Remove 'pizza' from list x, but also return it", "x.pop('pizza')")
    pause()
    guess("sort list x. Does this return anything?","x.sort()")
    print("Note that this does not return anything (returns none), it just sorts x behind the scenes")
    pause()
    guess("Reverse the order of list x","x.reverse()")
    pause()
    guess("Return the index of the first occurrence of 5 in list x","x.index(5)")
    pause()
    guess("x = '012345'  Return [0,1,2,3,4,5] without typing any brackets","list(x)")
    pause()
    #----------------------------------------------------
    print("it's time for range()!!")
    guess("How do you make this range: 0 1 2 3 4 5","range(6)")
    pause()
    guess("How do you make this range: 3 4 5","range(3,6)")
    pause()
    guess("How do you make this range: 2 4 6 8","range(2,9,2)")
    pause()
    #-------------------------------------------
    print("That's it for Test 2! I'm gonna redirect your trajectory back to the main page, captain. :)")
    main()

def test3():
    print("TEST 3 REVIEW")
    pause()
    print("First up! Try/except!")
    print("When should you use a try/except block?")
    pause()
    print("""
    try:
        "idk about this Python, but just give this a shot"
        "I think this might throw a ValueError"
        int("pizza") # Throws ValueError
        5/0 # Would throw ZeroDivisionError, but we never get here cuz the previous line Error'd
    except ValueError:
        "Do This if you find a ValueError"
    except ZeroDivisionError:
        "Do this if you find a ZeroDivisionError"
    """)
    pause()
    #---------------------------------------------------
    print("GAMEBOX")
    guess("Import the modules to play with gamebox and pygame?","import gamebox, pygame")
    pause()
    guess("Check if box1 is touching box2","box1.touches(box2)")
    pause()
    guess("Move box1 so it stops overlapping box2","box1.move_to_stop_overlapping(box2)")
    pause()
    guess("Moth both box1 and box2 so they stop overlapping","move_both_to_stop_overlapping(box2)")
    pause()
    guess("Draw box so it can be displayed","camera.draw(box)")
    pause()
    guess("Display everything that has been drawn","camera.display()")
    pause()
    print("You gotta know timer_loop, and I think the API would show it better. So, let's review the API real quick!")
    pause()
    import webbrowser
    webbrowser.open("https://cs1110.cs.virginia.edu/gamebox.html#timer_loop")
    pause()
    #--------------------------------------
    print("Regular Expressions!!!")
    guess("Import the module used to work with regular expressions","import re")
    pause()
    guess("Make a re-machine (object) that runs with the regular expression 'a'","re.compile(r'a')")
    pause()
    guess("z = '1_2_3_4' use x = re.compile(r'_') to return ''1A2A3A4''","x.sub('A',z)")
    pause()
    print("TO BE CONTINUED :)")
    print("In the meantime, let me redirect you to another helpful thingy")
    pause()
    webbrowser.open("https://quizlet.com/207437518/cs-111x-test-3-review-flash-cards/")
    main()

def main():
    print("""
    WELCOME TO THE BIG FINAL PY-CEPTION REVIEW GAME :)

    IF YOU GET STUCK ON A QUESTION, TYPE 'help' TO SEE THE ANSWER

    Use the BackTick ` (weird apostrophe under your escape key probably) to skip a question!
    """)

    x = input("""
    Enter a Test to review!
        1) Test 1
        2) Test 2
        3) Test 3\n\t> """)
    tests = ["1","2","3"]
    while x not in tests:
        x = input("""
        Enter a Test to review!
            1) Test 1
            2) Test 2
            3) Test 3\n\t> """)
    if x == "1":
        test1()
    elif x == "2":
        test2()
    elif x == "3":
        test3()


main()