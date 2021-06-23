# "args" and "kwargs" in python :-
# using *args in function defination we can call number of arguments we want which generally not possible in normal function call

def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(f"{key} is a {value} ")

har = ("harry","rohan","skillf")
normal = "this is me "
kw = {"x":"aaa","y":"bbb","z":"ccc"}
funargs(normal, *har, **kw)       #.....sequence for defining : (normal-->args---kwargs)
