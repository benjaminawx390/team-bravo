#Defining datetime library
from datetime import datetime, timedelta

schedule = ["Day","Night","Off","Off"]
date_ref_str = "2024-12-20"

#Recurring function for determining inputs
def get_work_status(date_input_str, date_ref_str, schedule):
    #Defining references and inputs
    date_input = datetime.strptime(date_input_str, "%Y-%m-%d")
    date_ref = datetime.strptime(date_ref_str, "%Y-%m-%d")

    #Differences between days
    diff = (date_input - date_ref).days ##.days is used to make integer calculations

    ##Determining work status using modulo ops
    schedule_index = diff % len(schedule)
    return schedule[schedule_index]


#Main
#__name ==__main is to prevent unwanted code execution when importing as a module.

if __name__ == "__main__":
    # Prompt the user to enter a date
    date_input_str = input("Enter a date (YYYY-MM-DD) to check your schedule: ")
    
    try:
        # Get the work status for the given date
        work_status = get_work_status(date_input_str, date_ref_str, schedule)
        
        # Output the result
        print(f"On {date_input_str}, your schedule is: {work_status}")
    
    except ValueError:
        # Handle invalid date format
        print("Invalid date format! Please enter the date in 'YYYY-MM-DD' format.")

