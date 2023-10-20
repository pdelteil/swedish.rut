
from person_validator import validate_swedish_personal_identity_number

def generate_sequential_swedish_personal_identity_numbers():
    #year
    for AA in range(20,80):
        #month
        # companies starting in 20 
        for BB in range(01, 13):
            #day
            for CC in range(1, 32):
                for NNNN in range(10000):
                    # Format AA, BB, CC, and NNNN as strings with leading zeros
                    formatted_AA = str(AA).zfill(2)
                    formatted_BB = str(BB).zfill(2)
                    formatted_CC = str(CC).zfill(2)
                    formatted_NNNN = str(NNNN).zfill(4)

                    # Combine the parts to create the full personal identity number
                    personal_number = f"{formatted_AA}{formatted_BB}{formatted_CC}{formatted_NNNN}"
                    if validate_swedish_personal_identity_number(personal_number):
                        yield personal_number

# Example usage
sequential_numbers_generator = generate_sequential_swedish_personal_identity_numbers()

# Print the first n sequential numbers
for _ in range(10000000):
   # Validate the generated personal number
    print(next(sequential_numbers_generator))
