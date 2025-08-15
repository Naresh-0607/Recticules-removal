import matplotlib.pyplot as plt
import numpy as np
import os

def inpaint_diffussion(image, mask, iterations = 150):
    img_inpaint = image.copy()
    if not np.issubdtype(img_inpaint.dtype, np.floating):
        img_inpaint = img_inpaint.astype(np.float32)/ 255
    
    print(f'Starting inpainting for {iterations} iterations')
    for i in range(iterations):
        up = np.roll(img_inpaint, 1, axis=0)
        down = np.roll(img_inpaint, -1, axis=0)
        left = np.roll(img_inpaint, 1, axis=1)
        right = np.roll(img_inpaint, -1, axis=1)

        avg_neighbors = (up+down+right+left) / 4.0

        img_inpaint[mask] = avg_neighbors[mask]

    return np.clip(img_inpaint, 0.0,1.0)

input_folder = 'Frames'
output_folder = 'Cleaned'
os.makedirs(output_folder, exist_ok=True)
coordinates = [
    (235,177,293,183),
    (290,147,348,153),
    (342,176,404,182),
    (290,202,348,208),
    (316,177,322,182)
]


for frame_file in sorted(os.listdir(input_folder)):
    if not frame_file.endswith('.jpg'):
        continue

    image_path = os.path.join(input_folder, frame_file)
    img = plt.imread(image_path)
    if img.shape[2] == 4:
        img = img[:,:,:3]
    height, width, _ = img.shape
    combined_mask = np.zeros((height,width), dtype=bool)

    for x1,y1,x2,y2 in coordinates:
        combined_mask[y1:y2, x1:x2] = True

    img_blended = inpaint_diffussion(img, mask=combined_mask, iterations = 200)
    print("Inpaint Successful")
    # fig, axes = plt.subplots(1,2, figsize = (20,10))

    # axes[0].imshow(img)
    # axes[0].set_title("Original Image")
    # axes[0].axis('off')

    # axes[1].imshow(img_blended)
    # axes[1].set_title("Image with Lines Removed")
    # axes[1].axis('off')

    # plt.tight_layout()
    # plt.show()

    save_path = os.path.join(output_folder, frame_file)
    plt.imsave(save_path, img_blended)
    print(f'Processed: {frame_file}')