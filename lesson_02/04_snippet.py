# Now applied coding: 
# write a short snippet that asks whether a variable items is an empty list.
# Use an explicit comparison rather than relying on truthiness.
# Then print "empty" if it is empty, otherwise print "not empty".


def check_items(items):
    if items == []:
        print("empty")
    else:
        print("not empty")

check_items([])  # empty
check_items([1, 2, 3])  # not empty
