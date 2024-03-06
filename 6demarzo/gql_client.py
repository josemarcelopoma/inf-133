import requests

# Definir la consulta GraphQL
query = """
    # consulta la lista de estudiantes completa con todos los parametros
    # {
    #     estudiantes{id,
    #     nombre
    #     apellido
    #     carrera}
    # },
    # consulta el nombre solamente de todos losestudiantes
    {
        estudiantes{
            nombre
        }
    }
    # {
        # Consulta el nombre y el apellido de todos los estudiantes y los muestra
    #     estudiantes{
    #         nombre
    #         apellido
    #     }
    # }

"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)