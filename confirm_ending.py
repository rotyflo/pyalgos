def confirm_ending(string, target):
    """Check if a string (first arg) ends with the given target string"""
    return target == string[-len(target):]


print(confirm_ending("Bastion", "n"))