def make_table(f,x):
    """f is a function; x is a list
    makes a table for HTML
    returns a string"""

    out = "<table>"
    out += "<tr><th>x</th><th>f(x)</th></tr>\n"
    for i in x:
        out +=  f"\t<tr><td>{i}</td><td>{f(i)}</td></tr>\n"
    out += "</table>"
    return out

def filter_bif(x,largest): #x is a numerical list, largest is a number
    """Return a list with all numbers larger than largest excluded."""
    
print(make_table(lambda x: x*x*x, range(1,20)))