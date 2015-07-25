import bcolors

def text(text=None, bold=False, underline=False, level='DEFAULT'):
    if text is None: raise AttributeError('text attribute cannot be empty, it should be \'str\'')
    level = getattr(bcolors, level) if hasattr(bcolors, level) else bcolors.DEFAULT
    print level + (bcolors.BOLD if bold else '') +  (bcolors.underline if underline else '') + text + bcolors.ENDC
