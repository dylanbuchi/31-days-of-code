import os


class PomodoroAppSettings():
    # files
    TOMATO_IMAGE_PATH = os.path.join(os.getcwd(),
                                     'src/day_26/images/pomodoro.png')
    # colors
    LIGHT_RED = "#F6CFCF"
    RED = "#e7305b"
    GREEN = "#00a130"
    YELLOW = "#f7f5dd"

    # fonts
    FONT_NAME = "Ubuntu Mono"

    TIMER_FONT = (FONT_NAME, 35, 'bold')
    START_BUTTON_FONT = (FONT_NAME, 15, 'normal')
    WORK_BREAK_LABEL = (FONT_NAME, 20, 'bold')

    # timers
    WORK_MINUTES = 25 * 60
    SHORT_BREAK_MINUTES = 5 * 60
    LONG_BREAK_MINUTES = 20 * 60
