"""Context Manager to set a recursion limit."""
import sys

class RecursionLimit():
    def __init__(self, limit: int) -> None:
        """Construct context manager."""
        print(f"CONTEXT MANAGER: desired limit = {limit}")
        self.__limit = limit

    def __enter__(self) -> None:
        """On enter, store existing limit, set new limit."""
        self.__old_limit = sys.getrecursionlimit()
        print(f"Old limit - {self.__old_limit}")
        sys.setrecursionlimit(self.__limit)

    def __exit__(self, _type, _value, _tb) -> None:
        """On exit, restore limit."""
        print("Exiting, reset limit..")
        sys.setrecursionlimit(self.__old_limit)