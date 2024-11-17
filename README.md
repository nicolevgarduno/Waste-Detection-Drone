## Tello waste detection drone

## Project Description
This is a project that implements real-time object detection with custom and collected data on a [Tello](https://www.ryzerobotics.com/de/tello) drone.

I used the official [YOLOv5](https://github.com/ultralytics/yolov5) model by Ultralytics and trained it on two custom datasets. I used a custom personal dataset with ~70 images annotated and curated, and one dataset [Trash Detection Image Dataset](https://universe.roboflow.com/trash-dataset-for-oriented-bounded-box/trash-detection-1fjjc/dataset/10) was used to train a more accurate model with ~1800 images.

The personal model was labelled and processed using [Roboflow](https://roboflow.com/).

## Real-time detection using YOLOv5s
My custom model was trained on approximately 80 images over 100 epochs with a precision of 64%, using YOLOv5s. Here’s a glimpse of its real-time detection performance::
![personal_gif](/images/ours.gif)

The Roboflow dataset contains approximately 1,800 images and was trained for 50 epochs with a batch size of 244 using the YOLOv5s model with a precision of 90%! Here are the results produced by the model:
![medium_model_gif](/images/model_.gif)

### Comparison

Here is a comparison between my personal dataset and the online roboflow:
![personal](/images/Our%20model%20frame.png)
![online_model](/images/Medium%20model%20frame.png)

## Logging
This project uses real-time detection and logging for each run that you do. Each log is documented in the `'/Logs'` directory with each run being labeled `'/runX'` with `X` being the current run iteration.

In every `'/runX'` folder there is a corresponding `.csv` file containing logs of detections with above 90% confidence. If it detects an object with >90%, the confidence and time will be logged in the corresponding `runX.csv` file. Along with the logging in the file there will also be a corresponding screen capture logged in the `'/runX/images'` folder. 

### Usage

*This is a python based project. You need python installed on your machine to run this program.*

Must connect to a Tello drone and run `python main.py` in the shell. A black box will appear which is used to capture user input for controls. The drone can be controlled via the keyboard with the following commands:

* 'e': takeoff
* 'q': land
* 'w': forward
* 'a': left
* 's': backwards
* 'd': right
* 'K_UP': up
* 'K_DOWN': down
* 'K_LEFT': rotate ccw
* 'K_RIGHT': rotate cw
