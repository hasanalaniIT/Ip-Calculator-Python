class Utils:

    BINARY_ZEROING = {
        "1": "0",
        "2": "00",
        "3": "000",
        "4": "0000",
        "5": "00000",
        "6": "000000",
        "7": "0000000",
    }

    def __init__(self):
        pass

    @classmethod
    def binary_zero_fill_empty(cls, binary_num_list: list) -> str:
        """
           Adds zero to autofill binary numbers less than 8 bit.

           Args:
               binary_num_list (list): list of the ip binary numbers.

           Returns:
               str: A string representing the binary representation of the IP address After applying zero padding.
           """
        fixed_binary_nums = ""
        for i in range(len(binary_num_list)):
            if len(binary_num_list.__getitem__(i)) > 8:
                return "The Number You Just Entered is above 8 bit"
            if len(binary_num_list.__getitem__(i)) == 8:
                fixed_binary_nums += f"{binary_num_list.__getitem__(i)}."
            if len(binary_num_list.__getitem__(i)) < 8:
                autofill_empty_zero = str(8 - len(binary_num_list.__getitem__(i)))
                fixed_binary_nums += f"{cls.BINARY_ZEROING.get(autofill_empty_zero)}{binary_num_list.__getitem__(i)}."
        return fixed_binary_nums[:-1]

    @staticmethod
    def binary_2_decimal(binary_num: str) -> int:
        """
            Converts a given binary number in any type and returns its decimal value.

            Args:
                binary_num (str): A given Binary number to be converted.

            Returns:
                int: A int representing the decimal value of the binary number after conversion.
            """
        return int(binary_num, 2)

    @staticmethod
    def doted_str_2_list(doted_string_number: str) -> list[str]:
        """
            Converts a given doted string number to a list of strings separated by dot.

            Args:
                doted_string_number (str): A given Binary number to be converted.

            Returns:
                int: A int representing the decimal value of the binary number after conversion.
            """
        return [bin(int(i))[2:] for i in doted_string_number.split('.')]

    @classmethod
    def decimal_2_binary(cls, decimal_num):

        if decimal_num > 1:
            print(decimal_num // 2)
            cls.decimal_2_binary(decimal_num // 2)

        print(decimal_num % 2, end='')


if __name__ == '__main__':
    Utils.decimal_2_binary(255)
    print(f"\n{Utils.binary_2_decimal('11111111')}")
