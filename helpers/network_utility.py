import socket

from typing import Optional


class NetworkHelper:
    """
    A helper class for network utility.
    """

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

    @staticmethod
    def get_ip_address() -> Optional[str]:
        """
        Returns the IPv4 address assigned to the computer by the router.

        Returns:
            str: The IP address assigned to the computer by the router.
        """
        try:
            udb_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udb_socket.connect(("8.8.8.8", 80))
            ip_address = udb_socket.getsockname()[0]
            udb_socket.close()
            return ip_address
        except Exception as exp:
            print(f"Connection Error: {exp}")

    @classmethod
    def binary_zero_fill_empty(cls, binary_num: list) -> str:
        """
           Adds zero to autofill binary numbers less than 8 bit.

           Args:
               binary_num (list): list of the ip binary numbers.

           Returns:
               str: A string representing the binary representation of the IP address After applying zero padding.
           """
        fixed_binary_nums = ""
        for i in range(len(binary_num)):
            if len(binary_num.__getitem__(i)) > 8:
                return "The Number You Just Entered is above 8 bit"
            if len(binary_num.__getitem__(i)) == 8:
                fixed_binary_nums += f"{binary_num.__getitem__(i)}."
            if len(binary_num.__getitem__(i)) < 8:
                autofill_empty_zero = str(8 - len(binary_num.__getitem__(i)))
                fixed_binary_nums += f"{cls.BINARY_ZEROING.get(autofill_empty_zero)}{binary_num.__getitem__(i)}."
        return fixed_binary_nums[:-1]

    @classmethod
    def ip_to_binary(cls, ip_address: str) -> Optional[str]:
        """
        Converts an IPv4 address in dotted decimal notation to its 8bit binary representation.

        Args:
            ip_address (str): A string representing the IP address in dotted decimal notation.

        Returns:
            str: A string representing the binary representation of the IP address.
        """

        try:
            binary_num = [bin(int(i))[2:] for i in ip_address.split('.')]
            return cls.binary_zero_fill_empty(binary_num)
        except Exception as exp:
            print(exp)


if __name__ == '__main__':
    network = NetworkHelper()
    # ipv4 = network.get_ip_address()
    # print(f"{ipv4 = }")
    binary_ip = network.ip_to_binary("0.255.255.255")
    # print(f"{len(binary_ip) = }")
    print(f"binary_ip==============={binary_ip}")
