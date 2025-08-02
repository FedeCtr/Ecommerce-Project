# E-commerce Flask Project

## Estructura inicial

```
ecommerce/
│
├── run.py
├── config.py
│
├── models/
│   └── __init__.py
│
├── auth/
│   └── routes.py
├── admin/
│   └── routes.py
├── shop/
│   └── routes.py
├── api/
│   └── routes.py
│
├── templates/
│   ├── base.html
│   ├── auth/
│   ├── admin/
│   └── shop/
│
└── static/
    ├── css/
    ├── js/
    └── img/
```

## Siguiente paso

1. Instala dependencias:  
   ```
   pip install Flask Flask-SQLAlchemy Flask-Login PyMySQL
   ```
2. Configura tu base de datos en `config.py`.
3. Ejecuta la app con `python run.py`.

---