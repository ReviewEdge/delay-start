from datetime import datetime
import time
import os


# NOTES:
# get rid of miliseconds on delay time
# Make it so it can go back to where you were, if you mess up and get an invalid error
# add input condition checks


# sets an amount of time to wait from input, as a list
def delay_set_time():
    when_days = int(input("Enter days:\n"))
    when_hours = int(input("Enter hours:\n"))    #add conditions checks for time inputs!
    when_minutes = int(input("Enter minutes:\n"))
    when_seconds = int(input("Enter seconds:\n"))

    set_time = [when_days, when_hours, when_minutes, when_seconds]

    confirm = input("Your set time:\n" + str(set_time) + "\nConfirm? ('y' or 'n'):\n").lower()
    if confirm != "y":
        exit()

    return set_time


# sets a date from input, as a datetime object
def pick_date_set_time():
    when_year = int(input("Enter year:\n"))
    when_month = int(input("Enter month:\n"))
    when_day = int(input("Enter day:\n"))
    when_hour = int(input("Enter hour (24-hour time):\n"))  # add conditions checks for time inputs!
    when_minute = int(input("Enter minute:\n"))
    when_second = int(input("Enter second:\n"))

    set_time = datetime(when_year, when_month, when_day, when_hour, when_minute, when_second)

    confirm = input("Your scheduled date:\n" + str(set_time) + "\nConfirm? ('y' or 'n'):\n").lower()
    if confirm != "y":
        exit()

    return set_time


# calculates how many seconds to wait, using a "time until" input
def u_calc_seconds_delay(set_time):
    delay = set_time[0]*86400 + set_time[1]*3600 + set_time[2]*60 + set_time[3]

    print("Your file will be executed in " + str(delay) + " seconds.")

    return delay


# calculates how many seconds to wait, using a "time of start" input
def o_calc_seconds_delay(set_time):
    now = datetime.now()

    my_timedelta = set_time - now

    delay = my_timedelta.total_seconds()

    if delay < 0:
        print("Invalid date.")
        exit()

    print("Your file will be executed in " + str(delay) + " seconds.")

    return delay


# runs the terminal command to execute the file
def run_script(file, file_type):
    terminal_command = file_type + " " + file
    os.system('echo "as scheduled, now executing ' + file + '"')
    os.system(terminal_command)


def main():
    file = input("Enter the full file path (make sure the file has been made executable):\n")

    file_type = input("Enter the file type ('python3' or 'sh'):\n").lower()
    # checks to make sure file type is valid, exits if not
    if file_type not in ["sh", "python3"]:
        print("Invalid file type.")
        exit()

    mode = input("Choose scheduling method:\n'u' - set a time until start\n'o' - set time/date of start\n").lower()
    # checks to make sure mode entered is valid, exits if not
    if mode not in ["u", "o"]:
        print("Invalid mode.")
        exit()

    if mode == "u":
        set_time = delay_set_time()
        delay = u_calc_seconds_delay(set_time)

    elif mode == "o":
        set_time = pick_date_set_time()
        delay = o_calc_seconds_delay(set_time)

    # waits until the scheduled time
    time.sleep(delay)

    run_script(file, file_type)


# runs main if called directly
if __name__ == '__main__':
    main()
