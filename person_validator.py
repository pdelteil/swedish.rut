import re

def validate_swedish_personal_identity_number(personal_number):
    # Remove any non-digit characters
    personal_number = re.sub(r'\D', '', personal_number)

    # Check if the personal number is the correct length (10 digits)
    if len(personal_number) != 10:
        return False

    # Extract the birthdate and serial number
    # YYMMDDNNNN
    birthdate = personal_number[0:6]
    serial_number = personal_number[6:9]
    checksum = int(personal_number[9])

    # Check that the birthdate is valid
    birthdate_year = int(birthdate[0:2])
    birthdate_month = int(birthdate[2:4])
    birthdate_day = int(birthdate[4:6])

    if birthdate_month < 1 or birthdate_month > 12:
        return False

    if birthdate_day < 1 or birthdate_day > 31:
        return False

    # Check that the serial number is in the range 000-999
    serial_number = int(serial_number)
    if serial_number < 0 or serial_number > 999:
        return False

    # Calculate the checksum
    weights = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    checksum_values = [int(digit) * weight if weight == 2 else int(digit) for digit, weight in zip(personal_number, weights)]
    checksum_sum = sum([value // 10 + value % 10 for value in checksum_values])
    calculated_checksum = (10 - (checksum_sum % 10)) % 10

    # Check that the calculated checksum matches the provided checksum
    valid =  checksum == calculated_checksum

    return valid

