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