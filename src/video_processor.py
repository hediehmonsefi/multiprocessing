import cv2
import os

class VideoProcessor:
    """Processes video sources"""

    def __init__(self, source, output_path):
        self.source = source
        self.output_path = output_path

    def process_video(self):
        cap = cv2.VideoCapture(self.source)
        if not cap.isOpened():
            print(f"Error: Cannot open source {self.source}")
            return

        # Get video properties
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Create output directory if not exists
        os.makedirs(self.output_path, exist_ok=True)
        output_file = os.path.join(self.output_path, f"processed_{os.path.basename(str(self.source))}.avi")

        # Define video writer
        out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            out.write(gray_frame)

            # Display (optional)
            cv2.imshow(f"Processing: {self.source}", gray_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        print(f"Processing completed for {self.source}. Saved at {output_file}")

def start_processing(source, output_path):
    """Helper function to start video processing inside a separate process."""
    processor = VideoProcessor(source, output_path)
    processor.process_video()