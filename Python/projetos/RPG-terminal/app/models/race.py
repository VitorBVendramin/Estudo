from dataclasses import dataclass

@dataclass
class Race:
    nome: str
    vitalidade: int
    mana: int
    forca: int
    destreza: int
    velocidade: int
    sorte: int
    inteligencia: int
    carisma: int
    percepcao: int
    subclasse_foco: str
    descricao: str = ""

    def total_atributos(self) -> int:
        return (
            self.vitalidade + self.mana + self.forca + self.destreza
            + self.velocidade + self.sorte + self.inteligencia
            + self.carisma + self.percepcao
        )

    def to_dict(self) -> dict:
        return {
            "vitalidade": self.vitalidade,
            "mana": self.mana,
            "forca": self.forca,
            "destreza": self.destreza,
            "velocidade": self.velocidade,
            "sorte": self.sorte,
            "inteligencia": self.inteligencia,
            "carisma": self.carisma,
            "percepcao": self.percepcao,
        }

    def __str__(self) -> str:
        return f"{self.nome} (foco: {self.subclasse_foco})"