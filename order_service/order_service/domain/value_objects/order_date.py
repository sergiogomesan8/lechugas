from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class OrderDate:
    value: date

    @classmethod
    def create(cls) -> "OrderDate":
        return cls(date.today())
 
    def __str__(self):
        return self.value.isoformat()