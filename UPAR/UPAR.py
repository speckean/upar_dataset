import os
import pickle
import glob
import random

import numpy as np
import torch.utils.data as data
from PIL import Image

import torchvision.transforms as T


class UPAR(data.Dataset):
	"""
    Load UPAR dataset from pickle file
	
	split: whether to use train/val/trainval/test split
	partition: partition id 0-9
	root: path to datasets, original datasets must be in this directory
	data_path: path to UPAR pickle file
	transform: training data transforms
	target_transforms: evaluation data transforms
    """
    def __init__(self, split='train', partition=0, root='datasets', data_path='./data/UPAR/dataset_all.pkl', transform=None, target_transform=None):
        dataset_info = pickle.load(open(data_path, 'rb+'))
        self.dataset_info = dataset_info
        img_id = dataset_info.image_name
        attr_label = dataset_info.label

        assert split in dataset_info.partition.keys(), f'split {split} does not exist'

        self.dataset = 'UPAR'
        self.transform = transform  # data transforms during training
        self.target_transform = target_transform  # data transforms during testing

        self.root_path = root  # path to datasets

        self.attr_id = dataset_info.attr_name  # attribute names
        self.attr_num = len(self.attr_id)  # number of attributes

		# load partition
        self.img_idx = dataset_info.partition[split]
		if isinstance(self.img_idx, list):
			self.img_idx = self.img_idx[args.partition]
		if isinstance(self.img_idx, list):
			self.img_idx = np.hstack(self.img_idx)
		self.img_num = self.img_idx.shape[0]
		self.img_id = [img_id[i] for i in self.img_idx]
		self.label = attr_label[self.img_idx]

		# set sub-dataset lengths to enable evaluation on sub-datasets
		self.sub_dataset_lengths = [len(d) for d in dataset_info.partition.test[args.partition]]
        
	"""
	get dataset item by index
	
	index: item index
	return: image data (img) with corresponding ground truth labels (gt_label), dataset id (did), and image path (imgname) 
	"""
    def __getitem__(self, index):
        imgname, gt_label, imgidx = self.img_id[index], self.label[index], self.img_idx[index]
        did = self.dataset_info.dataset_ids[imgidx]
        imgpath = os.path.join(self.root_path, imgname)
        img = Image.open(imgpath)

        if self.transform is not None:
            img = self.transform(img)

        gt_label = gt_label.astype(np.float32)

        if self.target_transform is not None:
            gt_label = self.transform(gt_label)

        return img, gt_label, did, imgname

	"""
	get length of dataset
	"""
    def __len__(self):
        return len(self.img_id)


def get_transform(height, width):
    normalize = T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    train_transform = [
        T.Resize((height, width))
    ]
	
    train_transform += [
        T.Pad(10),
        T.RandomCrop((height, width)),
        T.RandomHorizontalFlip(),
    ]

    train_transform += [
        T.ToTensor(),
        normalize,
    ]
    train_transform = T.Compose(train_transform)

    valid_transform = T.Compose([
        T.Resize((height, width)),
        T.ToTensor(),
        normalize
    ])

    return train_transform, valid_transform
