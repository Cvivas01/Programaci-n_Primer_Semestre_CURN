capitales_col = {
    "Amazonas": "Leticia",
    "Antioquia": "Medellín",
    "Arauca": "Arauca",
    "Atlántico": "Barranquilla",
    "Bolívar": "Cartagena",
    "Boyacá": "Tunja",
    "Caldas": "Manizales",
    "Caquetá": "Florencia",
    "Casanare": "Yopal",
    "Cauca": "Popayán",
    "Cesar": "Valledupar",
    "Chocó": "Quibdó",
    "Córdoba": "Montería",
    "Cundinamarca": "Bogotá",
    "Guainía": "Inírida",
    "Guaviare": "San José del Guaviare",
    "Huila": "Neiva",
    "La Guajira": "Riohacha",
    "Magdalena": "Santa Marta",
    "Meta": "Villavicencio",
    "Nariño": "Pasto",
    "Norte de Santander": "Cúcuta",
    "Putumayo": "Mocoa",
    "Quindío": "Armenia",
    "Risaralda": "Pereira",
    "San Andrés y Providencia": "San Andrés",
    "Santander": "Bucaramanga",
    "Sucre": "Sincelejo",
    "Tolima": "Ibagué",
    "Valle del Cauca": "Cali",
    "Vaupés": "Mitú",
    "Vichada": "Puerto Carreño"
}

regiones_col = [ "Atlántico", 
    "Bolívar", 
    "Cesar", 
    "Córdoba", 
    "La Guajira", 
    "Magdalena", 
    "Sucre"
]

for departamento in regiones_col:
    capital = capitales_col[departamento]
    print(capital)

