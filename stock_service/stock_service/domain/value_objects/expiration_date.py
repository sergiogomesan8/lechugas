from dataclasses import dataclass
from datetime import date

from stock_service.domain.exceptions.expired_product_exception import ExpiredProductException

@dataclass(frozen=True)
class ExpirationDate:
    value: date

    def __post_init__(self) -> None:
        if self.value < date.today():
            raise ExpiredProductException(self.value)
 
    def __str__(self):
        return self.value.isoformat()