import enum


class Role(str, enum.Enum):
    player = "player"
    leading = "leading"


class Attempts(int, enum.Enum):
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven = 11
    twelve = 12
    thirteen = 13
