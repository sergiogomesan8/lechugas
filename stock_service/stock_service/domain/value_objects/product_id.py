from dataclasses import dataclass

import uuid


@dataclass(frozen=True)
class ProductId:
    value: str

    @classmethod
    def new_one(cls) -> "ProductId":
        return cls(str(uuid.uuid4()))
            

    def __str__(self) -> str:
        return str(self.value)