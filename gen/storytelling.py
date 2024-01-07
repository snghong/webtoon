from enum import Enum


class FrameType(Enum):
    RECT = 1
    DIAG = 2

class BorderType(Enum):
    NONE = 1
    NORM = 2
    BOLD = 3