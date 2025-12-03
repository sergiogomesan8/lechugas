from dataclasses import dataclass

import uuid

@dataclass(frozen=True)
class OrderId:
    value: str

    @classmethod
    def new_one(cls) -> "OrderId":
        return cls(str(uuid.uuid4()))
    
    def __str__(self) -> str:
        return str(self.value)