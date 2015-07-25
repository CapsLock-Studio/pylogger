import echo, bcolors

def info(text, bold=False, underline=False):
    echo.text(text=text, level='INFO')

def notice(text, bold=False, underline=False):
    echo.text(text=text, level='NOTICE')

def warning(text, bold=False, underline=False):
    echo.text(text=text, level='WARNING')

def fail(text, bold=False, underline=False):
    echo.text(text=text, level='FAIL')

def success(text, bold=False, underline=False):
    echo.text(text=text, level='SUCCESS')

def default(text=None, bold=False, underline=False):
    echo.text(text=text, level='DEFAULT')

def log(text=None, level=None, bold=False, underline=False):
    echo.text(text=text, level=level)
