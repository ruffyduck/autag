import readline

defaultText = 'I am the default value'
readline.set_startup_hook(lambda: readline.insert_text(defaultText))
res = raw_input('Edit this:')
print (res)
