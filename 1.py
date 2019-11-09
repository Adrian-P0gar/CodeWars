def toJadenCase(string):
    list_of_string = string.split()
    final_string = ""

    for word in list_of_string:
        final_string = final_string + word.capitalize() + " "
    final_string = final_string[:-1]
    return final_string


quote = "How can mirrors be real if our eyes aren't real"
print(toJadenCase(quote))
