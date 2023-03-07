zen = """Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested. 
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those!\n"""


found_better = zen.count('better')
found_never = zen.count('never')
found_is = zen.count('is')

print(f'the word "never" was found {found_never} times')
print(f'the word "is" was found {found_is} times')
print(f'the word "better" was found {found_better} times\n')

zen_repl = zen.replace('i', '&')
print(zen_repl.upper())