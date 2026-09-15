from models.race import Race

RACES: dict[str, Race] = {

    # ---------- CORINGAS ----------
    "humano": Race(
        nome="Humano",
        vitalidade=10, mana=10, forca=10, destreza=10, velocidade=10,
        sorte=10, inteligencia=10, carisma=10, percepcao=10,
        subclasse_foco="Nenhuma",
        descricao="Generalista puro. Sem picos, sem fraquezas — serve para qualquer classe.",
    ),
    "meio_elfo": Race(
        nome="Meio-Elfo",
        vitalidade=9, mana=12, forca=7, destreza=9, velocidade=9,
        sorte=9, inteligencia=12, carisma=9, percepcao=9,
        subclasse_foco="Nenhuma",
        descricao="Leve tendência mágica, mas sem pico forte. Mais flexível, porém inferior ao especialista.",
    ),

    # ---------- GUERREIRO ----------
    "anao": Race(
        nome="Anão",
        vitalidade=11, mana=6, forca=14, destreza=7, velocidade=6,
        sorte=7, inteligencia=6, carisma=7, percepcao=8,
        subclasse_foco="Cavaleiro",
        descricao="Tanque puro. Força e Vitalidade altas, quase sem Mana ou Velocidade.",
    ),
    "meio_orc": Race(
        nome="Meio-Orc",
        vitalidade=10, mana=6, forca=15, destreza=7, velocidade=7,
        sorte=6, inteligencia=6, carisma=6, percepcao=7,
        subclasse_foco="Bárbaro/Berserk",
        descricao="A raça com a maior Força do jogo. Fúria descontrolada, quase nada de magia.",
    ),
    "aasimar": Race(
        nome="Aasimar",
        vitalidade=10, mana=10, forca=9, destreza=6, velocidade=6,
        sorte=10, inteligencia=7, carisma=11, percepcao=6,
        subclasse_foco="Templário",
        descricao="Equilíbrio entre combate e magia sagrada. Carisma alto, Destreza baixa.",
    ),
    "shadar_kai": Race(
        nome="Shadar-Kai",
        vitalidade=8, mana=11, forca=9, destreza=7, velocidade=7,
        sorte=6, inteligencia=8, carisma=6, percepcao=7,
        subclasse_foco="Templário Corrompido",
        descricao="Versão sombria do Templário. Mana alta, mas sem o Carisma 'divino' do Aasimar.",
    ),

    # ---------- MAGO ----------
    "tiefling": Race(
        nome="Tiefling",
        vitalidade=7, mana=12, forca=6, destreza=7, velocidade=6,
        sorte=6, inteligencia=11, carisma=8, percepcao=6,
        subclasse_foco="Necromante",
        descricao="Mana e Inteligência altas com um toque de Carisma sombrio.",
    ),
    "meio_dragao": Race(
        nome="Meio-Dragão",
        vitalidade=9, mana=11, forca=8, destreza=6, velocidade=6,
        sorte=6, inteligencia=11, carisma=7, percepcao=6,
        subclasse_foco="Elementalista",
        descricao="Mago com mais Vitalidade que os outros — sobrevive melhor enquanto conjura.",
    ),
    "changeling": Race(
        nome="Changeling",
        vitalidade=6, mana=11, forca=6, destreza=8, velocidade=7,
        sorte=8, inteligencia=10, carisma=11, percepcao=7,
        subclasse_foco="Ilusionista",
        descricao="Carisma altíssimo para manipulação e ilusões. Muito frágil fisicamente.",
    ),
    "gnomo": Race(
        nome="Gnomo",
        vitalidade=6, mana=13, forca=6, destreza=7, velocidade=6,
        sorte=8, inteligencia=13, carisma=6, percepcao=6,
        subclasse_foco="Arcanista",
        descricao="O mago mais 'puro' do jogo. Mana e Inteligência no topo, o mais fraco fisicamente.",
    ),

    # ---------- ARQUEIRO ----------
    "elfo_da_floresta": Race(
        nome="Elfo da Floresta",
        vitalidade=7, mana=7, forca=6, destreza=13, velocidade=10,
        sorte=7, inteligencia=6, carisma=6, percepcao=11,
        subclasse_foco="Atirador de Elite",
        descricao="Destreza no pico absoluto. Precisão acima de tudo.",
    ),
    "goblin": Race(
        nome="Goblin",
        vitalidade=6, mana=6, forca=6, destreza=10, velocidade=10,
        sorte=9, inteligencia=6, carisma=6, percepcao=12,
        subclasse_foco="Caçador",
        descricao="Percepção altíssima — rastreamento e armadilhas são sua especialidade.",
    ),
    "verdari": Race(
        nome="Verdari",
        vitalidade=9, mana=11, forca=7, destreza=8, velocidade=6,
        sorte=6, inteligencia=9, carisma=6, percepcao=10,
        subclasse_foco="Druida Arqueiro",
        descricao="Mana incomum para um arqueiro — conjura magia nas próprias flechas.",
    ),
    "eladrin": Race(
        nome="Eladrin",
        vitalidade=7, mana=8, forca=6, destreza=10, velocidade=11,
        sorte=7, inteligencia=8, carisma=6, percepcao=10,
        subclasse_foco="Patrulheiro",
        descricao="Velocidade no pico — feito para se mover rápido e se adaptar em campo.",
    ),

    # ---------- LADRÃO ----------
    "yuan_ti": Race(
        nome="Yuan-Ti",
        vitalidade=7, mana=8, forca=6, destreza=11, velocidade=9,
        sorte=6, inteligencia=7, carisma=6, percepcao=10,
        subclasse_foco="Assassino",
        descricao="Assassino com veneno — Destreza e Percepção elevadas.",
    ),
    "vulpari": Race(
        nome="Vulpari",
        vitalidade=6, mana=6, forca=6, destreza=12, velocidade=13,
        sorte=8, inteligencia=6, carisma=6, percepcao=11,
        subclasse_foco="Ninja",
        descricao="Stealth puro. Velocidade é o maior pico do jogo entre as raças ágeis.",
    ),
    "githyanki": Race(
        nome="Githyanki",
        vitalidade=7, mana=11, forca=7, destreza=9, velocidade=6,
        sorte=6, inteligencia=10, carisma=6, percepcao=10,
        subclasse_foco="Assassino das Sombras",
        descricao="O ladrão mágico — Mana e Inteligência altas em vez de força física.",
    ),
    "draconato": Race(
        nome="Draconato",
        vitalidade=9, mana=6, forca=10, destreza=10, velocidade=8,
        sorte=6, inteligencia=6, carisma=7, percepcao=6,
        subclasse_foco="Bucaneiro",
        descricao="Único Ladrão com Força alta — duelista que briga corpo a corpo.",
    ),
}


def get_race(key: str) -> Race:
    key = key.lower().strip()
    if key not in RACES:
        raise KeyError(f"Raça '{key}' não encontrada. Opções: {list(RACES.keys())}")
    return RACES[key]


def list_races() -> list[str]:
    return list(RACES.keys())