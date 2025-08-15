from moviepy import ImageSequenceClip
import os

frames_folder = 'Cleaned/'
fps = 30

# List of image file paths
frames = sorted([os.path.join(frames_folder, f) for f in os.listdir(frames_folder) if f.endswith(".jpg")])

# Create the clip
clip = ImageSequenceClip(frames, fps=fps)
clip.write_videofile("Final Output.mp4", codec="libx264")
