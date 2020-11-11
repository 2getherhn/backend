class TempData:

    def __init__(self):
        pass

    ShelterTypes = [
        ('shelter', 'Albergue'),
        ('supply_center', 'Centro de acopio'),
    ]

    RequiredBy = [
        ('all', 'Todos'),
        ('baby', 'Bebes'),
        ('children', 'Niños'),
        ('baby', 'Bebes'),
        ('men', 'Hombres'),
        ('women', 'Mujeres'),
        ('women', 'Tercera edad'),
    ]

    Priorities = [
        ('minimal', 'Minima'),
        ('medium', 'Media'),
        ('high', 'Alta'),
        ('highest', 'La mas alta'),
    ]

    ServiceType = [
        ('supplies', 'Insumos'),
        ('medical', 'Medico'),
    ]

    ServiceStatus = [
        ('pending', 'Pendiente'),
        ('assigned', 'Asignada'),
        ('done', 'Hecho'),
        ('cancelled', 'Cancelada'),
    ]

    ShippintStatus = [
        ('pending', 'Pendiente'),
        ('assigned', 'Asignada'),
        ('done', 'Hecho'),
        ('cancelled', 'Cancelada'),
    ]
