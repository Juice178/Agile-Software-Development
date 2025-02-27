from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Self


class Shape(BaseModel, ABC):
    type_order_table: list[int] = [
        sum([ord(c) for c in "Circle"]),
        sum([ord(c) for c in "Square"]),
        0
    ]
    @abstractmethod
    def draw(self) -> None:
        pass

    def __lt__(self, s: Self) -> bool:
        return self.precedes(s)
    
    def precedes(self, s: Self) -> bool:
        this_type: int= sum([ord(c) for c in type(self).__name__])
        arg_type: int = sum([ord(c) for c in type(s).__name__])
        done: bool = False
        this_ord: int = -1
        arg_ord: int = -1

        i = 0
        while not done:
            table_entry = self.type_order_table[i]
            if table_entry != 0:
                if table_entry == this_type:
                    this_ord = i
                if table_entry == arg_type:
                    arg_ord = i
                if arg_ord >= 0 and this_ord >= 0:
                    done = True
            else:
                done = True
            i += 1

        return this_ord < arg_ord
    