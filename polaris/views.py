from django.shortcuts import render

from .models import Cargo, Empleado


def home(request):
    context = {
        'total_cargos': Cargo.objects.count(),
        'total_empleados': Empleado.objects.count(),
    }
    return render(request, 'polaris/home.html', context)
