import textwrap

def wrapText(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrapText(string, max_width)
    print(result)

# Just note that after looking at the documentation for textwrap and trying it over and over again,
# this solution does not work in VS Code, rather, it only works in the Hackerrank shell.