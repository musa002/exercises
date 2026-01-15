import datetime

def is_it_valid(pic: str) -> bool:
    century_markers = {"+": 1800, "-": 1900, "A": 2000}
    control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if len(pic) < 11:
        return False

    ddmmyy = pic[:6]
    century_marker = pic[6]
    personal_id = pic[7:10]
    control_char = pic[10]

    if century_marker not in century_markers:
        return False

    day = int(ddmmyy[:2])
    month = int(ddmmyy[2:4])
    year = int(ddmmyy[4:6]) + century_markers[century_marker]

    try:
        datetime.date(year, month, day)
    except ValueError:
        return False

    nine_digit_number = ddmmyy + personal_id
    remainder = int(nine_digit_number) % 31
    expected_char = control_chars[remainder]

    return control_char == expected_char

print(is_it_valid("230827-906F"))  
print(is_it_valid("120488+246L"))  
print(is_it_valid("310823A9877"))  
print(is_it_valid("310823A987X"))  
