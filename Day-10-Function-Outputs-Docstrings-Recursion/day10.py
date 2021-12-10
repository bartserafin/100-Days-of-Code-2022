# DAY 10

#   Function outputs
# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"


# titled_name = format_name("bart", "serafin")
# print(titled_name)


#   Multiple return
def format_name2(f_name, l_name):
    if f_name == '' or l_name == '':
        return  # return None and ends function
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


titled_name = format_name2("bart", "serafin")

# DOCSTRINGS
def format_name(f_name, l_name):
    """Take a first and last name and format to return the title case version of the name."""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


titled_name = format_name("bart", "serafin")
print(titled_name)

