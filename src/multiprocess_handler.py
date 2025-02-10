import multiprocessing as mp
from src.video_processor import start_processing

class MultiProcessHandler:
    """Manages multiprocessing for video processing."""

    def __init__(self, sources, output_path):
        self.sources = sources
        self.output_path = output_path

    def run(self):
        processes = []
        for source in self.sources:
            p = mp.Process(target=start_processing, args=(source, self.output_path))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        print("All processes completed.")