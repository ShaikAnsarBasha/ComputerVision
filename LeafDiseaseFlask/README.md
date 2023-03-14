# LeafDiseaseClassification 
## 📝 Description
- We are trying to predict the leaf is healthy or not using **Tensorflow**.
- The dataset contain 3 classes
  1. Healthy
  2. Early Blight
  3. Late Blight

## ⏳ Dataset
- Download the dataset for custom training
- https://www.kaggle.com/datasets/emmarex/plantdisease

## Architecture
- The model architecture is simple conv layers using **Keras**

## 🏽‍ Download the saved_model
- Download pretrained model manually from following github Link
- https://github.com/ShaikAnsarBasha/ComputerVision/tree/main/LeafDiseaseFlask
- Place downloaded weights into current working directory **" LeafDiseaseFlask/ "** folder.

## :desktop_computer:	Installation

### :hammer_and_wrench: Requirements
* Python 3

## 🎯 Inference demo
Step 1: Install the project folder using git 
```bash
git clone path
```

Step 2: Change the current working directory to project folder
```bash
cd ./LeafDiseaseFlask
```

Step 3: Create new conda environment
```bash
conda create -n LeafDiseaseFlask
```

Step 4: Activate the new conda environmnet
```bash
conda activate LeafDiseaseFlask
```

Step 5: Install all the requirements
```bash
pip install -r requirements.txt
```

Step 6: Launch Visual Studio Code in cwd
```bash
code .
```

Step 7: Run main.py Python file in Vs Code and get predictions in localhost:5000 flask server

## Upload Web Page
![Upload img](https://github.com/ShaikAnsarBasha/ComputerVision/blob/main/LeafDiseaseFlask/webpage/upload.png)

## Predict Web Page
![Predict img](https://github.com/ShaikAnsarBasha/ComputerVision/blob/main/LeafDiseaseFlask/webpage/predict.png)
