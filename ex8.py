# this defines the variable formatter, it is made up of 4 raw strings
formatter = "%r %r %r %r"

# this is a call to action to print the formatter, the raw strings are filled in with
# respective information provided within the parentheses after the call to print the formatter
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
