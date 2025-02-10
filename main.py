from src.config import Config
from src.multiprocess_handler import MultiProcessHandler

if __name__ == "__main__":
    config = Config()
    sources = config.get_sources()
    output_path = config.output_path

    multi_handler = MultiProcessHandler(sources, output_path)
    multi_handler.run()