# Unified Pedestrian Attribute Recognition (UPAR) Dataset

The UPAR dataset is the harmonization of four public datasets (PA100K, PETA, RAP2, and Market1501-Attributes).
40 binary attributes have been unified between those for which we provide additional annotations.
This dataset enables the investigation of Pedestrian Attribute Recognition (PAR) methods' generalization ability under different attribute distributions, viewpoints, varying illumination, and low resolutions.
The UPAR annotations and this repository are published under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/de/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License</a>.
If you use the UPAR dataset, please cite our papers as well as the papers of the sub-datasets (see [Dataset information](#Datasetinformation))
```
@inproceedings{specker2023upar,
  title={UPAR: Unified Pedestrian Attribute Recognition and Person Retrieval},
  author={Specker, Andreas and Cormier, Mickael and Beyerer, J{\"u}rgen},
  booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
  year={2023}
}
@InProceedings{Cormier_2023_WACV,
    author    = {Cormier, Mickael and Specker, Andreas and Junior, Julio C. S. Jacques and Florin, Lucas and Metzler, J\"urgen and Moeslund, Thomas B. and Nasrollahi, Kamal and Escalera, Sergio and Beyerer, J\"urgen},
    title     = {UPAR Challenge: Pedestrian Attribute Recognition and Attribute-Based Person Retrieval -- Dataset, Design, and Results},
    booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) Workshops},
    month     = {January},
    year      = {2023},
    pages     = {166-175}
}
@InProceedings{Cormier_2024_WACV,
    author    = {Cormier, Mickael and Specker, Andreas and Junior, Julio C. S. Jacques and Moritz, Lennart and Metzler, J\"urgen and Moeslund, Thomas B. and Nasrollahi, Kamal and Escalera, Sergio and Beyerer, J\"urgen},
    title     = {UPAR Challenge 2024: Pedestrian Attribute Recognition and Attribute-Based Person Retrieval - Dataset, Design, and Results},
    booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) Workshops},
    month     = {January},
    year      = {2024},
    pages     = {359-367}
}
```

## Usage
Annotations can be found [here](./UPAR/dataset_all.pkl). 
We also provide a python class to load the annotations as a pytorch dataset: [UPAR.py](./UPAR/UPAR.py).
To use it, the original sub-datasets must be extracted in a directory, e.g., datasets/Market-1501, datasets/PA100k, etc.
In contrast to the generalization splits presented in the paper, the pickle file contains nine different partitions which correspond to the different training sets.
Partition 0 uses all data for training.
Partions 1,3,5,7 should be used for the cross-validation evaluation protocol and 2,4,6,8 for the leave-one-out protocol, respectively.

## Dataset information
### PA-100K Dataset
Liu, Xihui, et al. "Hydraplus-net: Attentive deep features for pedestrian analysis." Proceedings of the IEEE international conference on computer vision. 2017.

https://github.com/xh-liu/HydraPlus-Net

License: [CC-BY 4.0 license "Creative Commons — Attribution 4.0 International — CC BY 4.0"](https://creativecommons.org/licenses/by/4.0/).

### PETA Dataset
Y. Deng, P. Luo, C. C. Loy, X. Tang, "Pedestrian attribute recognition at far distance," in Proceedings of ACM Multimedia (ACM MM), 2014

http://mmlab.ie.cuhk.edu.hk/projects/PETA.html

License: "This dataset is intended for research purposes only and as such cannot be used commercially. In addition, reference must be made to the aforementioned publications when this dataset is used in any academic and research reports."

### Market
Zheng, Liang, et al. "Scalable person re-identification: A benchmark." Proceedings of the IEEE international conference on computer vision. 2015.

https://drive.google.com/file/d/0B8-rUzbwVRk0c054eEozWG9COHM/view?resourcekey=0-8nyl7K9_x37HlQm34MmrYQ

License: No license available.


### License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/de/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License</a>.
