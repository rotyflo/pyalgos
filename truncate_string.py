def truncate_string(string, num):
    """Truncate a string if it is longer than the given maximum string length. 
       Return the truncated string with a ... ending."""
    if len(string) > num:
        return string[:num] + "..."
    else:
        return string


print(truncate_string("A-tisket a-tasket A green and yellow basket", 8))