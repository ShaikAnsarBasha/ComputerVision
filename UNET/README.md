# UNET implementation
![img2mask](https://blogs.rstudio.com/ai/posts/2019-08-23-unet/images/examples.png)

## 📝 Description
- This implemantation is based from official paper https://arxiv.org/abs/1505.04597
- In this project we are converting **Car** Images to **Mask** Images 

## ⏳ Dataset
- Download the dataset for custom training
- https://www.kaggle.com/c/carvana-image-masking-challenge

## UNET Architecture
![architecture](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/u-net-architecture.png)

## 🏽‍ Download Pretrained Weights 
- Download pretrained weights of **UNET** model manually : **unet.pth.tar** file from following Drive Link
- https://drive.google.com/file/d/1HLj2rF5IE6T20KIQA1V-EtBGBT_RgnCd/view?usp=share_link
- Place downloaded weights into current working directory **" UNET/ "** folder.

## :desktop_computer:	Installation

### :hammer_and_wrench: Requirements
* Python 3
* PyTorch

## :gear: Setup
1. Install Latest Version of PyTorch :-
```bash
$ pip install torch

```
## 🎯 Inference demo

## UNET/saved_imgs/real.png (actual_output)
![actual_output](https://github.com/ShaikAnsarBasha/ComputerVision/blob/main/UNET/saved_imgs/real.png)
## UNET/saved_imgs/fake.png (predicted_output)
![predicted_output](https://github.com/ShaikAnsarBasha/ComputerVision/blob/main/UNET/saved_imgs/fake.png)
