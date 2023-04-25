def generate_response(choices, level):
    """
    Generate a response based on the given choices and level.

    :param choices: A list of choices to choose from.
    :param level: The desired level of the response.
    :return: A string containing the generated response.
    """
    if level == 1:
        response = random.choice(choices)
    elif level == 2:
        response = f"{random.choice(choices)} {random.choice(choices)}"
    elif level == 3:
        response = f"{random.choice(choices)} {random.choice(choices)} {random.choice(choices)}"
    else:
        response = "Invalid level. Please choose a level between 1 and 3."

    return response