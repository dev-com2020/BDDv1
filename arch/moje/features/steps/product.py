from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    vat_rate: int
    vat_value: float = field(init=False)

    def __post_init__(self):
        self.vat_value = round((self.price * self.vat_rate) / (100 + self.vat_rate), 2)