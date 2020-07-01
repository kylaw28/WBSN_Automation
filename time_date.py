import datetime

# step 12
class TimeAndDate:
    def get_time_date(self):
        # get the time and date right now
        now = datetime.datetime.now()
        #print("Current date and time: ")
        # change to a string
        time_now = str(now)
        return time_now
        # reformat the time and date so it matches what needs to be inputted for the command line
        # delete = '.'
        # new_format = time_now.split(delete, 1)[0]
        # new_format = new_format[:-3]
        # correct_format = new_format.replace(' ', ':')
        # use correct_format when sending the time and date command
        # print(correct_format)
        # return(correct_format)


if __name__ == "__main__":
    t_d = TimeAndDate()
    t_d.get_time_date()
