# ESRGAN implementation
## 📝 Description
- This implemantation is based from official paper https://arxiv.org/abs/1809.00219
- In this project we are converting **Low Resolution** Images to **High Resolution** Images

## ⏳ Dataset
- Download the dataset for custom training
- https://www.kaggle.com/datasets/joe1995/div2k-dataset

## Generator Architecture
![architecture](https://esrgan.readthedocs.io/en/latest/_images/architecture.png)

## 🏽‍ Download Pretrained Weights 
- Download pretrained weights of **Generator** model manually : **gen.pth.tar** file from following Drive Link
- https://drive.google.com/file/d/1kvY1y_qNldf41D6Hrc3uZTFlBuHTnCEp/view?usp=share_link
- Place downloaded weights into current working directory **" ESRGAN/ "** folder.

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
1. Testing with **Images** ( Put test images in **ESRGAN/test_imgs/** )  :-
2. Outputs with **Images** ( saved in **ESRGAN/saved_imgs/** )  :-

```python
# Comment this code
for epoch in range(EPOCHS):
    train(train_data_loader, gen, critic, opt_gen, opt_critic, l1_loss, vgg_loss, gen_scaler, critic_scaler, epoch)

    save_checkpoint(gen, opt_gen, filename=CHECKPOINT_GEN)
    save_checkpoint(critic, opt_critic, filename=CHECKPOINT_CRITIC)
```

```python
# Replace this code
save_imgs(gen, test_transform, test_dir="test_imgs")
```

## ESRGAN/test_imgs/baboon_LR.png
![test img baboon_LR](https://github.com/ShaikAnsarBasha/ComputerVision/blob/main/ESRGAN/test_imgs/baboon_LR.png)
## ESRGAN/saved_imgs/baboon_LR.png
![test img baboon_LR](https://github.com/ShaikAnsarBasha/ComputerVision/blob/main/ESRGAN/saved_imgs/baboon_LR.png)
