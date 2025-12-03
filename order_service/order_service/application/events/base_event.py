from dataclasses import dataclass
from typing import Any, Dict
from datetime import datetime

@dataclass(frozen=True)
class BaseEvent:
    name: str
    payload: Dict[str, Any]
    timestamp: datetime

    @classmethod
    def create(cls, *args, **kwargs) -> "BaseEvent":
        """
        Factory method que respeta la herencia.
        Cada subclase puede pasar su propio payload.
        """
        payload = cls.create_payload(*args, **kwargs)
        return cls(
            payload=payload,
            timestamp=datetime.utcnow(),
        )


    @classmethod
    def create_payload(cls, *args, **kwargs) -> Dict[str, Any]:
        """
        Cada subclase debe implementar este método para construir su payload.
        """
        raise NotImplementedError("Subclases deben implementar create_payload")