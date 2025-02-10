# multiprocessing

This project enables real-time video processing across multiple sources, including webcams, pre-recorded videos, and CCTV RTSP streams. It leverages Python multiprocessing for parallel processing, ensuring high performance.

📌 Note: The current implementation converts frames to grayscale as an example, but you can modify the code to apply any other processing, such as edge detection, object tracking, or AI-based processing.
#

### 📌 Features

✅ Supports multiple input sources (Webcams, Video Files, RTSP Streams)
✅ Uses multiprocessing for parallel video processing
✅ Converts video frames to grayscale (as an example)
✅ Saves processed videos in the output_videos/ directory
✅ Allows input source configuration via command-line arguments
#

### 🛠 Installation
1️⃣ Clone the Repository
```
git clone https://github.com/your-username/multiprocessing-video-processing.git
cd multiprocessing-video-processing
```
2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
#

### ⚙️ Usage
▶️ Process Video Files
```
python src/main.py --videos video1.mp4 video2.mp4
```
▶️ Combine Multiple Sources
```
python src/main.py --webcams 0 --videos video1.mp4 --rtsp rtsp://ip:port/stream
```
#

### 📁 Project Structure
```bash
/multiprocessing_video_processing
│── src/
│   │── config.py                # Handles input sources
│   │── video_processor.py       # Processes video 
│   │── multiprocess_handler.py  # Manages multiprocessing
│── main.py                      # Entry point of the program
│── output_videos/               # Processed videos are saved here
│── README.md                    # Project documentation
│── requirements.txt             # Required dependencies
```
#

### 🎨 Modify Video Processing
By default, the code converts frames to grayscale, but you can modify video_processor.py to apply any other processing.

Example: Edge Detection Instead of Grayscale
Modify video_processor.py:
``` 
import cv2
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
edge_frame = cv2.Canny(gray_frame, 100, 200)  # Apply edge detection
out.write(edge_frame)
```
Now, instead of grayscale, the output will show edge-detected frames.

You can replace this with object tracking, filtering, or any AI-based processing.
#

### 📜 License
This project is open-source and free to use under the MIT License.
