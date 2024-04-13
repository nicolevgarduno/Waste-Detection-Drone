from roboflow import Roboflow
rf = Roboflow(api_key="fdEGFBcEfNe66DOjxoPw")
project = rf.workspace("trash-dataset-for-oriented-bounded-box").project("trash-detection-1fjjc")
version = project.version(6)
dataset = version.download("yolov5")
