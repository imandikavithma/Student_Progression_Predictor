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