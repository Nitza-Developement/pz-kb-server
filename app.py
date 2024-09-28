from src.setup import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(
        debug=app.config.DEBUG,
        host=app.config.HOST,
        port=app.config.PORT,
        load_dotenv=False,
    )
