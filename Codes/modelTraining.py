from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="apple_dataset")
trainer.setTrainConfig(object_names_array=["apple", "damaged_apple"], batch_size=8, num_experiments=15  , train_from_pretrained_model="pretrained-yolov3.h5")
trainer.trainModel()
