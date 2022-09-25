# Proyecto Registraduria Backend resultados

Este proyecto de registraduria permite la administración de resultados electorales

Se implementa la coenxión a una base de datos PostgreSQL para las sigueinetes entidades:
- Partidos
- Mesas
- Candidatos
- Resultados.


Cambios para el Sprint 2 (24-sept-2022):

El código de los endpoints, permite la gestion de peticiones y repsuestas del backen hacia la Base de datos.

Se realiza la implementación del módulo de reportes, permitiendo obtener:
1. Conteo Global de todos los votos en las elecciones.
2. Conteo individual de votos por candidato con su partido.
3. Conteo general de votos agrupando a todos los candidatos con sus partido.
4. Conteo de votos del candidato ganador.

Se agrega la colección Postman (REGISTRADURIA TIC.postman_collection), para realiza test, en el directorio raíz
----------------------------------------------------------------------------------------------------------------


Las siguienets son las tecnologías utilizadas durante el desarrollo:
- Python 3.10
- PostgreSQL
- Flask 2.2.2
- SQLAlchemy 1.4
- Waitress 2.1.2

Colaboradores:

* Juan David Picaza Rodelo
* Johan Sebastian Contreras Ariza
* Osnaider Eduardo Deart Carranza
* William Bolaños Belalcazar
* Jersson Alexander Quintero
* Sebastian Casallas
