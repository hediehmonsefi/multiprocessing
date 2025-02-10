import argparse

class Config:
    """Manages configuration for input sources and output paths."""

    def __init__(self):
        args = self.parse_arguments()

        # Define input sources from command-line arguments
        self.webcams = args.webcams if args.webcams else []
        self.video_files = args.videos if args.videos else []
        self.rtsp_streams = args.rtsp if args.rtsp else []

        # Define output directory
        self.output_path = "output_videos"

    def get_sources(self):
        """Returns all sources combined."""
        return self.webcams + self.video_files + self.rtsp_streams

    @staticmethod
    def parse_arguments():
        """Parses command-line arguments for input sources."""
        parser = argparse.ArgumentParser(description="Multiprocessing")

        parser.add_argument(
            "--webcams", nargs="+", type=int, help="List of webcam indexes (e.g., --webcams 0 1)"
        )
        parser.add_argument(
            "--videos", nargs="+", type=str, help="List of video file paths (e.g., --videos video1.mp4 video2.mp4)"
        )
        parser.add_argument(
            "--rtsp", nargs="+", type=str, help="List of RTSP URLs (e.g., --rtsp rtsp://ip:port/stream)"
        )

        return parser.parse_args()