## BrainWebRawToNifti

Essential code to manipulate the downloaded raw data from the BrainWeb dataset and to convert them to nifti.

### Motivation

The [2015 paper][paperForsdyke] by Donald R. Forsdyke, extending the letter to Nature [Is your brain really necessarily?][paperLorber],
revealed that not much of brain tissue is needed to have normal or exceptional brain functions.

However, in the situation where a segmentation algorithm has to be developed or tested, a good amount of brains, 
possibly in nifti format and already segmented, is instead of crucial importance.

For this reason the online dataset [BrainWeb][brainweb] provides a synthetic dataset of 20 MRI-like images with ground truth segmentation.
Each subject has a T1, 12 individual fuzzy segmentations, and the discrete segmentation. 

This useful resource comes to the limitation that each individual subject can be downloaded only in MINC format
or as raw data (and each component must be downloaded individually, writing name email and institution in a small form).

The code provided [in this repository][here] is aimed at helping in the conversion of the raw data to nifti (after download), 
creating a label descriptor for ITK-snap visualisation and to provide access to further manipulation.


### How to use

1. Download the raw data from [BrainWeb][brainweb]: 

    + Create a folder <data_raw> where to store your zipped files.
    
    + Click on the [Twenty normal anatomical models][brainweb_subpage] link.
    
    + For each subject in the drop down menu (numbered from 04) download each single component in the same folder. Select
    
        + File Format: raw byte (unsigned)
        
        + Compression: gnuzip
        
2. Clone the repository with the usual 

    + `cd <where you want to clone>`
    
    + `git clone <this repository link>`
    
3. Change the parameters in the cloned file `param.py`, specifying the <data_raw> folder, and the ouptut folders.

4. Run `raw_to_nifti.py` with a python interpreter with numpy and nibabel installed.
    
### Extra

To merge the labels into a 4 classes (WM, GM, CSF and background) segmentation, install [nilabels][nilabels] and run `get_subset_labels.py`.

### Requirements

The code had been tested on Python 2.7 and Python 3.7 on a MAC, for the dataset downloaded on March 2018 (BrainWeb does not come with a release date).

It is based on [numpy], [nibabel] and [nilabels][nilabels].

### Acknowledgments
+ If you use the BrainWeb dataset, remember to cite the authors, as specified in the [website][brainweb]. 
+ This code is developed as a small part of my PhD studies at UCL, [giftsurg][giftsurg] group. My studentship is supported by Wellcome / Engineering and Physical Sciences Research Council (EPSRC).


[giftsurg]: http://www.gift-surg.ac.uk
[paperLorber]: http://science.sciencemag.org/content/210/4475/1232/tab-pdf
[paperForsdyke]: https://link.springer.com/article/10.1007%2Fs13752-015-0219-x
[brainweb]: http://brainweb.bic.mni.mcgill.ca/brainweb/
[brainweb_subpage]: http://brainweb.bic.mni.mcgill.ca/brainweb/anatomic_normal_20.html
[giftsurg]: http://www.gift-surg.ac.uk
[nilabels]:https://github.com/SebastianoF/nilabels
[numpy]: http://www.numpy.org/
[nibabel]: http://nipy.org/nibabel/
[matplotlib]: https://matplotlib.org/
[here]: https://github.com/SebastianoF/BrainWebRawToNifti.git
