
aicook - v4 aicook-augmented
==============================

This dataset was exported via roboflow.ai on October 2, 2021 at 1:37 PM GMT

It includes 3050 images.
Ingredients are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 8 versions of each source image:
* Random rotation of between -3 and +3 degrees
* Random exposure adjustment of between -20 and +20 percent
* Random Gaussian blur of between 0 and 3 pixels
* Salt and pepper noise was applied to 5 percent of pixels


