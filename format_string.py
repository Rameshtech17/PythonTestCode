String1 = "{} {} {}".format('one', 'two', 'three')
print("String in default order: ")
print(String1)
print("\n")
# Positional Formatting
String1 = "{1} {0} {2}".format('one', 'two', 'three')
print("String in Positional order: ")
print(String1)
print("\n")
# Keyword Formatting
String1 = "{o} {T} {t}".format(o = 'one', t = 'two', T = 'three')
print("String in order of Keywords: ")
print(String1)
