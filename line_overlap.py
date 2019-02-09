# If two lines are connected to each other, ex: 1,5 and 5,6, we define it as overlap (for one point)
def is_line_overlap(line1, line2):
    """
    Send in two lines on x-axis to check if they are overlap
    :param line1: tuple of first line (start_point, end_point), end_point >start_point
    :param line2: 2nd line
    :return: True if overlapped
    """
    if line1[0] >= line1[1] or line2[0] >= line2[1]:
        err_msg = "Incorrect line parameter, start point needs to be less than end point for lines"
        print(err_msg)
        raise ValueError(err_msg)
    if line2[0] > line1[1]:
        return False
    # start point falls in the middle of line1
    elif line2[0] <= line1[1] and line2[0] >= line1[0]:
        return True;
    else:
        if line2[1] < line1[0]:
            return False;
        else:
            return True
