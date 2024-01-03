# Waste-and-Litter-Detection
The introduction of AI in waste management is an important step to keep out environment clean. Government and private organisations cannot always use human to look around for wastes and garbages to clean. It requires a lot of manpower and is inefficient. With the combination of AI and CCTV, we can be more efficient in identifying amount of garbages and wastes in a certain location. This information is valuable because thus we can determine how much manpower and equipment we need to take care of those garbages in that location.

Another use case of identifying garbage from images or video could be to understand the location of garbage within a city using Google Images and placing it over a map like this: https://glasgow-litter.garyblackwood.co.uk/ 

# Dataset
We collceted most of the datasets from this repo-'https://github.com/AgaMiko/waste-datasets-review?tab=readme-ov-file'

All the datasets were uploaded to google drive and then we performed tasks by downloading them o kaggle.

# Dataset source and review
### garbage pile dataset
This dataset was collceted from this location-'https://universe.roboflow.com/garbage-detection-czeg5/garbage_detection-wvzwv'

This garbage detection dataset uses images of large groupings of garbage. A garbage image dataset can be used to recognize garbage pileups at various distances, depths, environments and times of day. A garbage recognition API could be used to help governments monitor garbage by using stationary cameras or cameras used during asset management collection efforts.

As is, this dataset helps localize the location of the garbage within an image or video and draw a bounding box around the area to give an idea of the size of the garbage pile. This dataset could be used to label individual garbage as well.

Yolov8n was used in this and we had a precision of 0.841, recall of 0.715 and mAP50 of 0.756.

### Litter detection
This dataset was collected from this location-'https://universe.roboflow.com/sushiteam/litter-dataset-fxyqc'

### Trash detection Using ICRA19 dataset
This dataset was collected from this location-'https://conservancy.umn.edu/handle/11299/214366'

### Wastebasket trash detection
This dataset was collcted from this location-'https://universe.roboflow.com/asmaa-rashed-alahmari-fvl6d/wastebasket_trash_detecation'


The main.py file is used to track garbage and other wastes in video files or live camera. We need to tweak the source and model in it for different applications and models. 

The img_object_detector.py can be used to detect and mark object in a image with bounding boxes

Note: YOLOv8n is not perfroming good in some datasets. I will update this repo in future after further training or with different model

Your contribution is welcome
