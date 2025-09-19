from app import create_app

# WSGI entrypoint compatible with all Gunicorn versions
app = create_app()
