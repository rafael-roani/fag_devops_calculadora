def calcular_total(itens, desconto_percentual=0):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)
    """
    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    # Defeito proposital:
    # o desconto percentual esta sendo subtraido como valor monetario.
    desconto_total = desconto_percentual + receber_cupons(cupom)
    desconto_total = min(desconto_total, 100)
    total = subtotal - (desconto_percentual / 100)

    return round(total, 2)

CUPONS_VALIDOS = {
    "DEVOPS10": 10
}

def receber_cupons(cupom=""):

    if cupom is None:
        return 0;

    codigo = cupom.casefold()
    if codigo not in CUPONS_VALIDOS:
        raise ValueError("Cupom promocional inválido.")

    return CUPONS_VALIDOS(codigo);