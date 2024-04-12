from roboflow import Roboflow
rf = Roboflow(api_key="fdEGFBcEfNe66DOjxoPw")
project = rf.workspace("garbage-detection-oa9nh").project("yolov5-garbage-detection")
version = project.version(1)
dataset = version.download("yolov5")