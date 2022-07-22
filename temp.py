import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from m7_python.models import Inmuebles, Region, Comuna


def get_list_inmuebles(name, description) -> list:
    lista_inmuebles = Inmuebles.objects.filter(nombre_inmueble__contains=name).filter(descripcion__contains=description)
    file1 = open('inmuebles.txt', 'w', encoding='utf-8')
    for inmueble in lista_inmuebles:
        file1.write(f"""{inmueble.nombre_inmueble}.
            Descripción: {inmueble.descripcion}.
            Ubicación: Comuna de {inmueble.id_comuna.comuna}, {inmueble.id_region.region}.
            Precio: ${inmueble.precio_mensual}.
            Terreno de {inmueble.m2_terreno} metros cuadrados con {inmueble.m2_construido} metros cuadrados construidos.
            Dormitorios: {inmueble.numero_hab}. Baños: {inmueble.numero_banos}. Estacionamientos: {inmueble.numero_estacionamientos}.
            \n""")
    file1.close()

    return lista_inmuebles

#get_list_inmuebles("Providencia", "Cocina")


def get_list_inmuebles_comuna(comuna) -> list:
    comuna_obj = Comuna.objects.get(comuna__contains=comuna)
    lista_inmuebles = Inmuebles.objects.filter(id_comuna=comuna_obj.id)
    file1 = open('inmuebles_por_comuna.txt', 'w', encoding='utf-8')
    file1.write(f"En la comuna de {comuna_obj.comuna} existen las siguientes ofertas:\n\n")

    for inmueble in lista_inmuebles:
        file1.write(f"- {inmueble.nombre_inmueble}.\n")
    file1.close()

    return lista_inmuebles

#get_list_inmuebles_comuna("Bernardo")


def get_list_inmuebles_region(id) -> list:
    region_obj = str(Region.objects.filter(id=id).values()[0]["region"])
    lista_inmuebles = Inmuebles.objects.filter(id_region_id=id)
    file1 = open('inmuebles_por_region_id.txt', 'w', encoding='utf-8')
    file1.write(f"En la {region_obj} existen las siguientes ofertas:\n\n")

    for inmueble in lista_inmuebles:
        file1.write(f"- {inmueble.nombre_inmueble}.\n")
    file1.close()

#get_list_inmuebles_region(16)


def get_list_inmuebles_por_region(region) -> list:
    region_obj = Region.objects.get(region__contains=region)
    lista_inmuebles = Inmuebles.objects.filter(id_region=region_obj.id)
    file1 = open('inmuebles_por_region_name.txt', 'w', encoding='utf-8')
    file1.write(f"En la {region_obj.region} existen las siguientes ofertas:\n\n")

    for inmueble in lista_inmuebles:
        file1.write(f"- {inmueble.nombre_inmueble}.\n")
    file1.close()

    return lista_inmuebles

#get_list_inmuebles_por_region("Metrop")
