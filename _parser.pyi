LITERALS: list[str]
SYMBOLS: dict[str, str]
__all__: list[str]

def _is_char(char: str) -> bool: ...
def strip_punctuation(value: str, *args: tuple[str]) -> str: ...
def parse_url(url: str) -> str: ...
