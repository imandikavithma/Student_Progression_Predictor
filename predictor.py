progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

#ensure user inputs integers in an allowed range
def validate_input(credits):
    try:
        credits = int(credits)
        if credits not in [0,20,40,60,80,100,120]:
            print("Out of range.")
            return False
        return credits
    except ValueError:
        print("Integer required.")
        return False

#calculate the outcome based on credit values
def calculate_outcome(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits
    if total_credits != 120:
        print("Total incorrect.")
        return "Invalid"
    
    if pass_credits == 120:
        return("progress")
    elif pass_credits == 100:
        return("progress (module trailer)") 
    elif pass_credits >= 60:
        return("Do not progress - module retriever")
    elif pass_credits == 40 and defer_credits >= 20 and fail_credits <= 60:
        return("Do not progress - module retriever")
    elif pass_credits == 20 and defer_credits >= 40 and fail_credits <= 60:
        return("Do not progress - module retriever")  
    elif pass_credits == 0 and defer_credits >= 60 and fail_credits <= 60:
        return("Do not progress - module retriever")   
    else:
        return("Exclude")

def display_histogram(progress_count,trailer_count, retriever_count, exclude_count):
    win = GraphWin("Histogram",700,600)

    b1len = 400-(progress_count*25)
    b2len = 400-(trailer_count*25)
    b3len = 400-(retriever_count*25)
    b4len = 400-(exclude_count*25)

    Title1 = Text(Point(150,50),"Histogram Results")
    Title1.setStyle("bold")
    Title1.setSize(16)
    Title1.draw(win)

    Title2 = Text(Point(150,500),f"Total Student = {progress_count + trailer_count + retriever_count + exclude_count }")
    Title2.setStyle("bold")
    Title2.setSize(16)
    Title2.draw(win)

    #line
    Xline = Line(Point(50,400), Point(650,400))
    Xline.draw(win)

    #Text1
    lebel = Text(Point(90,420),"Progress")
    lebel.setStyle("bold")
    lebel.setSize(12)
    lebel.draw(win)

    #Upcount1
    b1name = Text(Point(90,b1len-10),progress_count)
    b1name.draw(win)

    #Rectangle1
    box1 = Rectangle(Point(60,400), Point(120,b1len))
    box1.draw(win)
    box1.setFill("green")


    #Text2
    lebel2 = Text(Point(240,420),"Trailer")
    lebel2.setStyle("bold")
    lebel2.setSize(12)
    lebel2.draw(win)

    #Upcount2
    b2name = Text(Point(240,b2len-10),trailer_count)
    b2name.draw(win)

    #Rectangle2
    box2 = Rectangle(Point(210,400), Point(270,b2len))
    box2.draw(win)
    box2.setFill("yellow")

    #Text3
    lebel3 = Text(Point(390,420),"Retriever")
    lebel3.setStyle("bold")
    lebel3.setSize(12)
    lebel3.draw(win)

    #Upcount3
    b3name = Text(Point(390,b3len-10),retriever_count)
    b3name.draw(win)

    #Rectangle3
    box3 = Rectangle(Point(360,400), Point(420,b3len))
    box3.draw(win)
    box3.setFill("blue")

    #Text4
    lebel4 = Text(Point(540,420),"Exclude")
    lebel4.setStyle("bold")
    lebel4.setSize(12)
    lebel4.draw(win)

    #Upcount4
    b4name = Text(Point(540,b4len-10),exclude_count)
    b4name.draw(win)

    #Rectangle4
    box4 = Rectangle(Point(510,400), Point(570,b4len))
    box4.draw(win)
    box4.setFill("red")

    try:
        win.getMouse()
        win.close()
    except:
        pass

progression_data = []

user = int(input("Are you student (press 1) staff member(press 2) :"))

while True:
    pass_credits = validate_input(input("Please enter your credits at pass: "))
    defer_credits = validate_input(input("Please enter your credit at defer: "))
    fail_credits = validate_input(input("Please enter your credit at fail: "))

    outcome = calculate_outcome(pass_credits, defer_credits, fail_credits)
    print(outcome)

    if user == 1:
    break


    f = open("process_data.txt", "a")# Open the file in append mode

    progression_data.append((outcome, pass_credits, defer_credits, fail_credits))
    f.write(f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}\n") # Write data to the file


    
    if outcome == "progress":
        progress_count += 1
    elif "progress (module trailer)" in outcome:
        trailer_count += 1
    elif "retriever" in outcome:
        retriever_count += 1
    elif outcome == "Exclude":
        exclude_count += 1

    
    continue_program = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit: ")# Ask the user if they want to enter another set of data
    if continue_program.lower() == 'q':
        break    

# If the user is a staff member, display the data and histogram
if user == 2:

    f = open("process_data.txt", "r")
    print (f.read())
    f.close()

    display_histogram(progress_count,trailer_count, retriever_count, exclude_count)