from termcolor import colored


def try_me():
    text = colored('First package test by Matheus Sposito',
                   'magenta',
                   attrs=['blink'])
    return print(text)
