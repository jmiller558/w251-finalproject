# undefined > aicook-augmented
https://public.roboflow.ai/object-detection/undefined

Provided by undefined
License: MIT

## Background Information
This dataset was curated and annotated by - [Karel Cornelis](https://www.linkedin.com/in/corneliskarel).

The original dataset *(v1)* is composed of 516 images of various ingredients inside a fridge. The project was created as part of a groupwork for a [postgraduate applied AI](https://www.erasmushogeschool.be/nl/opleidingen/toegepaste-artificiele-intelligentie) at Erasmus Brussels - we made an object detection model to identify ingredients in a fridge.

From [the recipe dataset we used](https://github.com/davestroud/Wine) (which is a subset of the [recipe1M dataset](http://pic2recipe.csail.mit.edu/)) we distilled the top50 ingredients and used 30 of those to randomly fill our fridge.

#### Read this blog post to learn more about the model production process: [How I Used Computer Vision to Make Sense of My Fridge](https://blog.roboflow.com/smart-fridge/)
#### Watch this video to see the model in action: [AICook](https://www.youtube.com/watch?v=lk2s39rf6I4)
![](https://i.imgur.com/jLFKv1F.png)

The dataset is available under the MIT License.

## Getting Started
You can download this dataset for use within your own project, fork it into a workspace on Roboflow to create your own model, or test one of the trained versions within the app.

## Dataset Versions
### Version 1 (v1) - 516 images *(original-images)*
* **Preprocessing**: Auto-Orient
* **Augmentations**: *No augmentations applied*
* Training Metrics: *This version of the dataset was not trained*

### Version 2 (v2) - 3,050 images *(aicook-augmented-trainFromCOCO)*
* Preprocessing: Auto-Orient, Resize (Stretch to 416x416)
* Augmentations:
	* Outputs per training example: 8
Rotation: Between -3° and +3°
Exposure: Between -20% and +20%
Blur: Up to 3px
Noise: Up to 5% of pixels
Cutout: 12 boxes with 10% size each
* Training Metrics: Trained from the COCO Checkpoint in Public Models ("[transfer learning](https://blog.roboflow.com/a-primer-on-transfer-learning/)") on Roboflow
	* mAP = 97.6%, precision = 86.9%, recall = 98.5%

### Version 3 (v3) - 3,050 images *(aicook-augmented-trainFromScratch)*
* Preprocessing: Auto-Orient, Resize (Stretch to 416x416)
* Augmentations:
	* Outputs per training example: 8
Rotation: Between -3° and +3°
Exposure: Between -20% and +20%
Blur: Up to 3px
Noise: Up to 5% of pixels
Cutout: 12 boxes with 10% size each
* Training Metrics: Trained from "scratch" (no transfer learning employed) on Roboflow
	* mAP = 97.9%, precision = 79.6%, recall = 98.6%

### Version 4 (v4) - 3,050 images images *(aicook-augmented)*
* Preprocessing: Auto-Orient, Resize (Stretch to 416x416)
* Augmentations:
	* Outputs per training example: 8
Rotation: Between -3° and +3°
Exposure: Between -20% and +20%
Blur: Up to 3px
Noise: Up to 5% of pixels
Cutout: 12 boxes with 10% size each
* Training Metrics: *This version of the dataset was not trained*

Karel Cornelis - [LinkedIn](https://www.linkedin.com/in/corneliskarel)