import traceback
print()
def f1(): return abc()
def abc(): traceback.print_stack()


f1()
print()
