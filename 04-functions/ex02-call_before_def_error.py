### Exercise is to move the call before definition and observe the error, uncomment below line to get the error
# repeat_lyrics()

# Traceback (most recent call last):
#  File "04-functions/ex02-call_before_def_error.py", line 1, in <module>
#    repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()