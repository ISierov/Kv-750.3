def setNewClassName(OldClass, newClassName) :
    if str(newClassName).isalnum():
        class NewClass(OldClass):
            pass
        NewClass.__name__ = newClassName
        return NewClass
    else:
        raise Exception("Entered new value '" + str(newClassName) + "' is sick of nonalnum chars ")


print(setNewClassName(int, ".inb"))


