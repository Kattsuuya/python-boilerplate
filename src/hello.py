def make_hello_string(name: str) -> str:
    """
    引数の名前を使って挨拶の文字列を作成する関数。

    Args:
        name (str): 挨拶をする相手の名前

    Returns:
        str: 挨拶の文字列
    """

    if name == "":
        raise ValueError("名前が空です")
    return f"Hello, {name}!"
