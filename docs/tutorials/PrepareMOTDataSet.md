English | [简体中文](PrepareMOTDataSet_cn.md)

# Contents
## Multi-Object Tracking Dataset Preparation
- [MOT Dataset](#MOT_Dataset)
- [Data Format](#Data_Format)
- [Dataset Directory](#Dataset_Directory)
- [Download Links](#Download_Links)
- [Custom Dataset Preparation](#Custom_Dataset_Preparation)
- [Citations](#Citations)

### MOT Dataset
PaddleDetection uses the same training data as [JDE](https://github.com/Zhongdao/Towards-Realtime-MOT) and [FairMOT](https://github.com/ifzhang/FairMOT). Please download and prepare all the training data including **Caltech Pedestrian, CityPersons, CUHK-SYSU, PRW, ETHZ, MOT17 and MOT16**. **MOT15 and MOT20** can also be downloaded from the official webpage of MOT challenge. If you want to use these datasets, please **follow their licenses**.

### Data Format
These several relevant datasets have the following structure:
```
Caltech
   |——————images
   |        └——————00001.jpg
   |        |—————— ...
   |        └——————0000N.jpg
   └——————labels_with_ids
            └——————00001.txt
            |—————— ...
            └——————0000N.txt
MOT17
   |——————images
   |        └——————train
   |        └——————test
   └——————labels_with_ids
            └——————train
```
Annotations of these datasets are provided in a unified format. Every image has a corresponding annotation text. Given an image path, the annotation text path can be generated by replacing the string `images` with `labels_with_ids` and replacing `.jpg` with `.txt`.

In the annotation text, each line is describing a bounding box and has the following format:
```
[class] [identity] [x_center] [y_center] [width] [height]
```
**Notes:**
- `class` should be `0`. Only single-class multi-object tracking is supported now.
- `identity` is an integer from `1` to `num_identities`(`num_identities` is the total number of instances of objects in the dataset), or `-1` if this box has no identity annotation.
- `[x_center] [y_center] [width] [height]` are the center coordinates, width and height, note that they are normalized by the width/height of the image, so they are floating point numbers ranging from 0 to 1.


### Dataset Directory

First, follow the command below to download the `image_list.zip` and unzip it in the `dataset/mot` directory:
```
wget https://dataset.bj.bcebos.com/mot/image_lists.zip
```
Then download and unzip each dataset, and the final directory is as follows:
```
dataset/mot
  |——————image_lists
            |——————caltech.10k.val  
            |——————caltech.all  
            |——————caltech.train  
            |——————caltech.val  
            |——————citypersons.train  
            |——————citypersons.val  
            |——————cuhksysu.train  
            |——————cuhksysu.val  
            |——————eth.train  
            |——————mot15.train  
            |——————mot16.train  
            |——————mot17.train  
            |——————mot20.train  
            |——————prw.train  
            |——————prw.val
  |——————Caltech
  |——————Cityscapes
  |——————CUHKSYSU
  |——————ETHZ
  |——————MOT15
  |——————MOT16
  |——————MOT17
  |——————MOT20
  |——————PRW
```

### Custom Dataset Preparation

In order to standardize training and evaluation, custom data needs to be converted into the same directory and format as MOT-16 dataset:
```
custom_data
   |——————images
   |        └——————test
   |        └——————train
   |                └——————seq1
   |                |        └——————gt
   |                |        |       └——————gt.txt
   |                |        └——————img1
   |                |        |       └——————000001.jpg
   |                |        |       |——————000002.jpg
   |                |        |       └—————— ...
   |                |        └——————seqinfo.ini
   |                └——————seq2
   |                └——————...
   └——————labels_with_ids
            └——————train
                    └——————seq1
                    |        └——————000001.txt
                    |        |——————000002.txt
                    |        └—————— ...
                    └——————seq2
                    └—————— ...
```

#### images
- `gt.txt` is the original annotation file of all images extracted from the video.
- `img1` is the folder of images extracted from the video by a certain frame rate.
- `seqinfo.ini` is a video information description file, and the following format is required:
```
[Sequence]
name=MOT16-02
imDir=img1
frameRate=30
seqLength=600
imWidth=1920
imHeight=1080
imExt=.jpg
```

Each line in `gt.txt`  describes a bounding box, with the format as follows:
```
[frame_id],[identity],[bb_left],[bb_top],[width],[height],[score],[label],[vis_ratio]
```
**Notes:**:
- `frame_id` is the current frame id.
- `identity` is an integer from `1` to `num_identities`(`num_identities` is the total number of instances of objects in the dataset), or `-1` if this box has no identity annotation.
- `bb_left` is the x coordinate of the left boundary of the target box
- `bb_top` is the Y coordinate of the upper boundary of the target box
- `width, height` are the pixel width and height
- `score` acts as a flag whether the entry is to be considered. A value of 0 means that this particular instance is ignored in the evaluation, while a value of 1 is used to mark it as active. `1` by default.
- `label` is the type of object annotated, use `1` as default because only single-class multi-object tracking is supported now. There are other classes of object in MOT-16, but they are treated as ignore.
- `vis_ratio` is the visibility ratio of each bounding box. This can be due to occlusion by another
static or moving object, or due to image border cropping. `1` by default.

#### labels_with_ids
Annotations of these datasets are provided in a unified format. Every image has a corresponding annotation text. Given an image path, the annotation text path can be generated by replacing the string `images` with `labels_with_ids` and replacing `.jpg` with `.txt`.

In the annotation text, each line is describing a bounding box and has the following format:
```
[class] [identity] [x_center] [y_center] [width] [height]
```
**Notes:**
- `class` should be `0`. Only single-class multi-object tracking is supported now.
- `identity` is an integer from `1` to `num_identities`(`num_identities` is the total number of instances of objects in the dataset), or `-1` if this box has no identity annotation.
- `[x_center] [y_center] [width] [height]` are the center coordinates, width and height, note that they are normalized by the width/height of the image, so they are floating point numbers ranging from 0 to 1.

Generate the corresponding `labels_with_ids` with following command:
```
cd dataset/mot
python gen_labels_MOT.py
```


### Download Links

#### Caltech Pedestrian
Baidu NetDisk:
[[0]](https://pan.baidu.com/s/1sYBXXvQaXZ8TuNwQxMcAgg)
[[1]](https://pan.baidu.com/s/1lVO7YBzagex1xlzqPksaPw)
[[2]](https://pan.baidu.com/s/1PZXxxy_lrswaqTVg0GuHWg)
[[3]](https://pan.baidu.com/s/1M93NCo_E6naeYPpykmaNgA)
[[4]](https://pan.baidu.com/s/1ZXCdPNXfwbxQ4xCbVu5Dtw)
[[5]](https://pan.baidu.com/s/1kcZkh1tcEiBEJqnDtYuejg)
[[6]](https://pan.baidu.com/s/1sDjhtgdFrzR60KKxSjNb2A)
[[7]](https://pan.baidu.com/s/18Zvp_d33qj1pmutFDUbJyw)

Google Drive: [[annotations]](https://drive.google.com/file/d/1h8vxl_6tgi9QVYoer9XcY9YwNB32TE5k/view?usp=sharing) ,
please download all the images `.tar` files from [this page](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/datasets/USA/) and unzip the images under `Caltech/images`

You may need [this tool](https://github.com/mitmul/caltech-pedestrian-dataset-converter) to convert the original data format to jpeg images.
Original dataset webpage: [CaltechPedestrians](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/)

#### CityPersons
Baidu NetDisk:
[[0]](https://pan.baidu.com/s/1g24doGOdkKqmbgbJf03vsw)
[[1]](https://pan.baidu.com/s/1mqDF9M5MdD3MGxSfe0ENsA)
[[2]](https://pan.baidu.com/s/1Qrbh9lQUaEORCIlfI25wdA)
[[3]](https://pan.baidu.com/s/1lw7shaffBgARDuk8mkkHhw)

Google Drive:
[[0]](https://drive.google.com/file/d/1DgLHqEkQUOj63mCrS_0UGFEM9BG8sIZs/view?usp=sharing)
[[1]](https://drive.google.com/file/d/1BH9Xz59UImIGUdYwUR-cnP1g7Ton_LcZ/view?usp=sharing)
[[2]](https://drive.google.com/file/d/1q_OltirP68YFvRWgYkBHLEFSUayjkKYE/view?usp=sharing)
[[3]](https://drive.google.com/file/d/1VSL0SFoQxPXnIdBamOZJzHrHJ1N2gsTW/view?usp=sharing)

Original dataset webpage: [Citypersons pedestrian detection dataset](https://github.com/cvgroup-njust/CityPersons)

#### CUHK-SYSU
Baidu NetDisk:
[[0]](https://pan.baidu.com/s/1YFrlyB1WjcQmFW3Vt_sEaQ)

Google Drive:
[[0]](https://drive.google.com/file/d/1D7VL43kIV9uJrdSCYl53j89RE2K-IoQA/view?usp=sharing)

Original dataset webpage: [CUHK-SYSU Person Search Dataset](http://www.ee.cuhk.edu.hk/~xgwang/PS/dataset.html)

#### PRW
Baidu NetDisk:
[[0]](https://pan.baidu.com/s/1iqOVKO57dL53OI1KOmWeGQ)

Google Drive:
[[0]](https://drive.google.com/file/d/116_mIdjgB-WJXGe8RYJDWxlFnc_4sqS8/view?usp=sharing)


#### ETHZ (overlapping videos with MOT-16 removed):
Baidu NetDisk:
[[0]](https://pan.baidu.com/s/14EauGb2nLrcB3GRSlQ4K9Q)

Google Drive:
[[0]](https://drive.google.com/file/d/19QyGOCqn8K_rc9TXJ8UwLSxCx17e0GoY/view?usp=sharing)

Original dataset webpage: [ETHZ pedestrian datset](https://data.vision.ee.ethz.ch/cvl/aess/dataset/)

#### MOT-17
Baidu NetDisk:
[[0]](https://pan.baidu.com/s/1lHa6UagcosRBz-_Y308GvQ)

Google Drive:
[[0]](https://drive.google.com/file/d/1ET-6w12yHNo8DKevOVgK1dBlYs739e_3/view?usp=sharing)

Original dataset webpage: [MOT-17](https://motchallenge.net/data/MOT17/)

#### MOT-16
Baidu NetDisk:
[[0]](https://pan.baidu.com/s/10pUuB32Hro-h-KUZv8duiw)

Google Drive:
[[0]](https://drive.google.com/file/d/1254q3ruzBzgn4LUejDVsCtT05SIEieQg/view?usp=sharing)

Original dataset webpage: [MOT-16](https://motchallenge.net/data/MOT16/)

#### MOT-15
Original dataset webpage: [MOT-15](https://motchallenge.net/data/MOT15/)

#### MOT-20
Original dataset webpage: [MOT-20](https://motchallenge.net/data/MOT20/)





### Citation
Caltech:
```
@inproceedings{ dollarCVPR09peds,
       author = "P. Doll\'ar and C. Wojek and B. Schiele and  P. Perona",
       title = "Pedestrian Detection: A Benchmark",
       booktitle = "CVPR",
       month = "June",
       year = "2009",
       city = "Miami",
}
```
Citypersons:
```
@INPROCEEDINGS{Shanshan2017CVPR,
  Author = {Shanshan Zhang and Rodrigo Benenson and Bernt Schiele},
  Title = {CityPersons: A Diverse Dataset for Pedestrian Detection},
  Booktitle = {CVPR},
  Year = {2017}
 }

@INPROCEEDINGS{Cordts2016Cityscapes,
title={The Cityscapes Dataset for Semantic Urban Scene Understanding},
author={Cordts, Marius and Omran, Mohamed and Ramos, Sebastian and Rehfeld, Timo and Enzweiler, Markus and Benenson, Rodrigo and Franke, Uwe and Roth, Stefan and Schiele, Bernt},
booktitle={Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
year={2016}
}
```
CUHK-SYSU:
```
@inproceedings{xiaoli2017joint,
  title={Joint Detection and Identification Feature Learning for Person Search},
  author={Xiao, Tong and Li, Shuang and Wang, Bochao and Lin, Liang and Wang, Xiaogang},
  booktitle={CVPR},
  year={2017}
}
```
PRW:
```
@inproceedings{zheng2017person,
  title={Person re-identification in the wild},
  author={Zheng, Liang and Zhang, Hengheng and Sun, Shaoyan and Chandraker, Manmohan and Yang, Yi and Tian, Qi},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={1367--1376},
  year={2017}
}
```
ETHZ:
```
@InProceedings{eth_biwi_00534,
author = {A. Ess and B. Leibe and K. Schindler and and L. van Gool},
title = {A Mobile Vision System for Robust Multi-Person Tracking},
booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR'08)},
year = {2008},
month = {June},
publisher = {IEEE Press},
keywords = {}
}
```
MOT-16&17:
```
@article{milan2016mot16,
  title={MOT16: A benchmark for multi-object tracking},
  author={Milan, Anton and Leal-Taix{\'e}, Laura and Reid, Ian and Roth, Stefan and Schindler, Konrad},
  journal={arXiv preprint arXiv:1603.00831},
  year={2016}
}
```
