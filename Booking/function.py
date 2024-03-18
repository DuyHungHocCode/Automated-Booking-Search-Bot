def month_to_number(month_name):
    # Dictionary mapping month names to their corresponding numbers
    months_dict = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }

    # Convert the month name to its corresponding number
    month_number = months_dict.get(month_name)

    if month_number is not None:
        return month_number
    else:
        return "Invalid month name"
