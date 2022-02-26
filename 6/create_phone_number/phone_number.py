class CreatePhone():
    def check_number(self, number):
        if all(isinstance(x, int) for x in number):
            return "Valid phone number"
        else:
            return "Not a valid phone number"
    
    def check_length(self, number):
        if len(number) != 10:
            return "Insufficient digits"
        else:
            return "Sufficient digits"

    def convert(self, number):
        return str(number)
    
    def first_digits(self, number):
        number.insert(0, "(")
        number.insert(4, ")")
        string_number = [str(int) for int in number]
        phone_number =  "".join(string_number)
        return phone_number

    def create_number(self, number):
        number.insert(0, "(")
        number.insert(4, ")")
        number.insert(5, " ")
        number.insert(9, '-')
        string_number = [str(int) for int in number]
        phone_number =  "".join(string_number)
        return phone_number

    # [(,3, 1, 2, ), "", 3, 1, 5, 5, 5, 1, 1]


        
        
