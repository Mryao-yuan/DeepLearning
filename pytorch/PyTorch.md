# Pytorch 学习

## 环境安装和配置

- 安装Anaconda (打开Anaconda Prompt 出现 base 表示成功)
- 
- 创建环境
    > conda create -n pytorch python=3.6 
- 激活环境
   > conda activate pytorch
- 查看工具包
   > pip list

### PyTorch 的安装

查看 GPU 是否支持 CUDA

> https:/www.nvidia.cn/geforce/technologies/cuda/supported-gpus/

安装指令
> conda install pytorch torchvision cudatoolkit=9.2 -c pytorch -c defaults -c numba/label/dev

  验证正确安装 torch
 > import torch  未报错

 使用显卡
 >torch.cuda.is_available() True/False

False解决:更新驱动

## python 的两个主要函数

- dir(): 打开
- help():说明书


- Dateset实现的两个功能
  1. 如何让获取每一个数据及其label
  2. 告诉我们总共有多少的数据

- 使用 Dataset
  
- 