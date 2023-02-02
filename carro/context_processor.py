from carro.carro import Carro


def importe_total_carro(request):

    carro=Carro(request)

    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = round(total + (float(value["precio"])), 2)
    else:
        total = "Debes hacer Login"
    return {"importe_total_carro": total}


"""  total = 0

    # if request.user.is_authenticated:
    session = request.session
    carro = session.get("carro")
    if not carro:
        carro = session["carro"] = {}
    else:
        carro = carro

    carro = carro.items()
    for key, value in carro:

        total = round(total + (float(value["precio"])), 2)

    return {"importe_total_carro": total}
"""
