from django.shortcuts import render

# Create your views here.

def course_list(request):
    courses = [
        {
            'id': 1,
            'level': 'Principiante',
            'rating': 4.8,
            'course_title': 'Python: fundamentos hasta los detalles',
            'instructor': 'Elizabeth Olsen',
            'course_image': 'images/curso_1.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg'
        },
        {
            'id': 2,
            'level': 'Intermedio',
            'rating': 4.9,
            'course_title': 'Django: Aplicaciones robustas',
            'instructor': 'Alonso Murray',
            'course_image': 'images/curso_2.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/20.jpg'
        },
        {
            'id': 3,
            'level': 'Principiante',
            'rating': 5.0,
            'course_title': 'Fast API',
            'instructor': 'Gregory Harris',
            'course_image': 'images/curso_3.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/32.jpg'
        },
        {
            'id': 4,
            'level': 'Avanzado',
            'rating': 5.0,
            'course_title': 'Django Rest',
            'instructor': 'Alison Walsh',
            'course_image': 'images/curso_4.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/45.jpg'
        }
    ]
    return render(request, "courses/courses.html", {
        'courses': courses
    })

def course_detail(request):
    course = [
        {
            "course_title": "Python: Fundamentos hasta los Detalles",
            "course_link": "course_lessons",
            "course_image": "images/curso_1.jpg",
            "info_course": {
                "lessons": 60,
                "duration": 12,
                "instructor": "Alison Walsh",
            },
            "course_content": [
                {
                    "id": 1,
                    "name": "Introducción a Python",
                    "total_lessons": 2,
                    "complete_lessons": 2,
                    "lessons": [
                        {"name": "¿Qué aprenderás en este curso de Python?",
                            "type": "video"},
                        {"name": "Instalación del entorno y primeros pasos",
                            "type": "article"},
                    ],
                },
                {
                    "id": 2,
                    "name": "Fundamentos del lenguaje",
                    "total_lessons": 3,
                    "complete_lessons": 3,
                    "lessons": [
                        {"name": "Variables, tipos de datos y operadores",
                            "type": "video"},
                        {"name": "Estructuras condicionales", "type": "video"},
                        {"name": "Bucles y control de flujo", "type": "article"},
                    ],
                },
                {
                    "id": 3,
                    "name": "Colecciones y manejo de datos",
                    "total_lessons": 3,
                    "complete_lessons": 3,
                    "lessons": [
                        {"name": "Listas y tuplas", "type": "video"},
                        {"name": "Diccionarios y conjuntos", "type": "video"},
                        {"name": "Comprensión de listas", "type": "article"},
                    ],
                },
                {
                    "id": 4,
                    "name": "Funciones y módulos",
                    "total_lessons": 3,
                    "complete_lessons": 2,
                    "lessons": [
                        {"name": "Creación y uso de funciones", "type": "video"},
                        {"name": "Argumentos, retorno y ámbito", "type": "article"},
                        {"name": "Módulos y paquetes nativos", "type": "video"},
                    ],
                },
                {
                    "id": 5,
                    "name": "Python práctico",
                    "total_lessons": 3,
                    "complete_lessons": 0,
                    "lessons": [
                        {"name": "Trabajo con archivos", "type": "video"},
                        {"name": "Errores y excepciones", "type": "article"},
                        {"name": "Mini-proyecto final", "type": "video"},
                    ],
                },
            ],
        }
    ]

    return render(request, 'courses/course_detail.html', {
        'course': course
    })

def course_lessons(request):
    pass
