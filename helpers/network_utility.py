import socket

from typing import Optional


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
