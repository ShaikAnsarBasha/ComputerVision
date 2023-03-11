# IMAGE2IMAGE TRANSLATION
## 📝 Description
- This implemantation is based from official paper https://arxiv.org/abs/1611.07004
- In this project we are converting **Satellite** Images to **Map** Images

## ⏳ Dataset
- Download the dataset for custom training of Map Images
- https://www.kaggle.com/datasets/vikramtiwari/pix2pix-dataset

## Generator Architecture
![architecture](https://learnopencv.com/wp-content/uploads/2021/07/Pix2Pix-employs-a-UNET-Generator-an-encoder-decoder.jpg)

## 🏽‍ Download Pretrained Weights 
- Download pretrained weights of **Generator** model manually : **gen.pth.tar** file from following Drive Link
- https://drive.google.com/file/d/1-p_JzdPpHHgiUlNUSBfy7qakrGbBt3eO/view?usp=share_link
- Download pretrained weights of **Discriminator** model manually : **disc.pth.tar** file from following Drive Link
- https://drive.google.com/file/d/1-h7qCHF7VSWK_fiCzmWhYGyHlvIEs0s1/view?usp=share_link
- Place downloaded weights into current working directory **" PIX2PIX/ "** folder.

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
* Comment the training loop and run the inference function.
* To track the training progress of our Generator download the following zip file
* https://drive.google.com/file/d/1-I3vFNyBh8W1Xkao3bmM1kHdGkloeWUR/view?usp=share_link


## PIX2PIX/saved_imgs/input_0.png
![test img baboon_LR](https://github.com/ShaikAnsarBasha/ComputerVision/blob/main/PIX2PIX/saved_imgs/input_0.png)
## PIX2PIX/saved_imgs/fake_0.png
![test img baboon_LR](https://github.com/ShaikAnsarBasha/ComputerVision/blob/main/PIX2PIX/saved_imgs/fake_0.png)
