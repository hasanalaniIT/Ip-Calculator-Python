import socket

from typing import Optional

from helpers.utils import Utils


class NetworkHelper:
    """
    A helper class for network utility.
    """
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
    def ip_to_binary(cls, ip_address: str) -> Optional[str]:
        """
        Converts an IPv4 address in dotted decimal notation to its 8bit binary representation.

        Args:
            ip_address (str): A string representing the IP address in dotted decimal notation.

        Returns:
            str: A string representing the binary representation of the IP address.
        """

        try:
            binary_num = Utils.doted_str_2_list(ip_address)
            return Utils.binary_zero_fill_empty(binary_num)
        except Exception as exp:
            print(exp)


if __name__ == '__main__':
    network = NetworkHelper()
    # ipv4 = network.get_ip_address()
    # print(f"{ipv4 = }")
    binary_ip = network.ip_to_binary("0.255.255.255")
    # print(f"{len(binary_ip) = }")
    print(f"binary_ip==============={binary_ip}")
