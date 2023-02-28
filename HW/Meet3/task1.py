zen = "Beautiful is better than ugly. \n\
Explicit is better than implicit. \n\
Simple is better than complex. \n\
Complex is better than complicated. \n\
Flat is better than nested. \n\
Sparse is better than dense. \n\
Readability counts. \n\
Special cases aren't special enough to break the rules. \n\
Although practicality beats purity. \n\
Errors should never pass silently. \n\
Unless explicitly silenced. \n\
In the face of ambiguity, refuse the temptation to guess. \n\
There should be one-- and preferably only one --obvious way to do it. \n\
Although that way may not be obvious at first unless you're Dutch. \n\
Now is better than never. \n\
Although never is often better than *right* now. \n\
If the implementation is hard to explain, it's a bad idea. \n\
If the implementation is easy to explain, it may be a good idea. \n\
Namespaces are one honking great idea -- let's do more of those!\n"



found_better = zen.count('better')
found_never = zen.count('never')
found_is = zen.count('is')


print(f'the word "never" was found {found_never} times')
print(f'the word "is" was found {found_is} times')
print(f'the word "better" was found {found_better} times\n')

zen_repl = zen.replace('i', '&')
print(zen_repl.upper())