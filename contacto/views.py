from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()


def contacto(request):
    form = FormularioContacto()

    if request.method == "POST":
        form = FormularioContacto(request.POST)
        if form.is_valid():

            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage(
                "Mensaje desde App django",
                "El usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {}".format(
                    nombre, email, contenido),
                "", [os.getenv('EMAIL_RECIBED')], reply_to=[email]
            )

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

        else:
            form = FormularioContacto()

    return render(request, 'contacto/contacto.html', {"form": form})
