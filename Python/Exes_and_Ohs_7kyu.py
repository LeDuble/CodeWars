# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. 
# The string can contain any char.
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

Examples input/output:
def xo(s):
    if s.lower().count("x") == s.lower().count("o"):
        return(True)
    else:
        return(False)