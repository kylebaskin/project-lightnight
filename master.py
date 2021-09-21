import os
import subprocess
import time
import read_mail
import make_a_call
import check_the_alarm
import arm_the_alarm

while True:
    doCall = read_mail.getEmails()
    if(doCall):
        arm_the_alarm.execute()
        make_a_call.execute()
        time.sleep(60)
        status = check_the_alarm.execute()
        print(status)
        if(status == 0):
            pass
        else:
            read_mail.mark_as_read()
