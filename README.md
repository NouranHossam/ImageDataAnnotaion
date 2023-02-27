# Data Image Annotation Tool
![ui](https://i.imgur.com/rCf2jRM.png)

## Project Objective
Our goal in developing the Data Image Annotation Tool is to create an effective and streamlined method for annotating images by drawing bounding boxes around objects of interest such as humans, cars, cats, dogs, and others. The tool is designed with an intuitive interface that allows the user to easily insert one or more images and navigate through them using next and previous buttons. The user can interact with the image to draw bounding boxes with unique colors for each label. To improve the efficiency of the annotation process, we have integrated pre-trained object detection models, such as Haar Cascade, which can automatically draw annotations around cars. This not only enhances the accuracy and speed of the annotation process but also reduces the required time and effort. The resulting annotated images can then be used to train machine learning models for various applications, including autonomous driving and object recognition. Our objective is to develop a tool that streamlines the data annotation process, elevates the quality of the annotated data.

## Approaches
We used a variety of technologies to develop our Data Image Annotation Tool, including:

PyQt5: We employed PyQt5 to create an interface that allows the user to interact with the tool to import images and draw bounding boxes for different labels.
OpenCV: We utilized OpenCV, an open-source computer vision library, to process images and detect objects of interest, such as cars.
Haar Cascade: We integrated the Haar Cascade algorithm (car3.xml), a machine learning-based object detection technique, to automatically detect cars in the image and draw bounding boxes around them.
Project Features & Functionalities
Our Data Image Annotation Tool has the following features and functionalities:

## Functionalities
Import one or several Images with PNG, JPG, JPEG and GIF formats.
Navigate through Images using Next and previous buttons.
Interact with Images and draw bounding boxes around objects.
Clear bounding boxes using the clear button.
Choose labels from different label categories such as Human, Cat, dog, Car, and Others.
Export drawn bounding boxes coordinates to CSV or TXT file.
Choose folders to save drawn bounding boxes, each TXT file contains Image path and drawn annotation coordinates.
Extra functionalities for further development: Auto Detect objects. In this implementation, for example, the user can click on the car detection button to detect a car automatically from images.

![alt text](https://i.imgur.com/trhVs2m.png)


## Future Work
Improve the accuracy and consistency of the bounding boxes, we can utilize pre-trained object detection models that have high precision. By applying these models to the image, the objects of interest such as humans, traffic lights, and cars can be easily detected and localized.
Add more functionalities to the interface such as zoom in, zoom out, undo, redo and allowing the user to add new labels that are not offered in the current phase.