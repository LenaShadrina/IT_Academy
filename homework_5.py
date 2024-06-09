import datetime
import os
import time

from termcolor import colored
import pyfiglet

# запуск в терминале, PyCharm не чистит терминал
if __name__ == '__main__':
    while True:
        os.system(['clear', 'cls'][os.name == 'nt'])
        time_now = datetime.datetime.now()
        hour = time_now.hour
        minutes = time_now.minute
        seconds = time_now.second

        clock = [
            pyfiglet.figlet_format(str(hour), font='ansi_regular', width=40).split('\n'),
            pyfiglet.figlet_format(str(minutes), font='ansi_regular', width=40).split('\n'),
            pyfiglet.figlet_format(str(seconds), font='ansi_regular', width=40).split('\n')
        ]
        for i in range(len(clock[0])):
            print(
                colored(clock[0][i], 'red'), '        ',
                colored(clock[1][i], 'green'), '        ',
                colored(clock[2][i], 'yellow'), sep=''
            )

        time.sleep(1)
