import echo


def info(text, bold=False, underline=False):
    echo.text(text=text, level='INFO', bold=bold, underline=underline)


def notice(text, bold=False, underline=False):
    echo.text(text=text, level='NOTICE', bold=bold, underline=underline)


def warning(text, bold=False, underline=False):
    echo.text(text=text, level='WARNING', bold=bold, underline=underline)


def fail(text, bold=False, underline=False):
    echo.text(text=text, level='FAIL', bold=bold, underline=underline)


def success(text, bold=False, underline=False):
    echo.text(text=text, level='SUCCESS', bold=bold, underline=underline)


def default(text=None, bold=False, underline=False):
    echo.text(text=text, level='DEFAULT', bold=bold, underline=underline)


def log(text=None, level=None, bold=False, underline=False):
    echo.text(text=text, level=level, bold=bold, underline=underline)
