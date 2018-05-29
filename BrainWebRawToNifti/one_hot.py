
"""
Create one hot encoding of the BrainWeb database after nifti conversion.
"""
import os
import numpy as np
import nibabel as nib

import BrainWebDataset.a_params as bw
from LABelsToolkit.main import LABelsToolkit as LaB


def convert_one_hot(num_classes=12, dtype=np.float):
    """
    Converting crisp label volume into one-hot encoding volume,
    i.e., appending an additional axis to crisp volume
    where:
          one_hot[x, y, z, crisp[x, y, z]] = 1
          one_hot[x, y, z, ~crisp[x, y, z]] = 0
    The length of the additional axis is `num_classes`
    """

    for sj in bw.subjects_num_list:

        pfo_sj_nifti = os.path.join(bw.pfo_nifti_in_root, 'BW{}'.format(sj))
        crisp_name = os.path.join(pfo_sj_nifti, 'BW{}_CRISP.nii.gz'.format(sj))
        one_hot_name = os.path.join(pfo_sj_nifti, 'BW{}_ONEHOT.nii.gz'.format(sj))

        crisp_image = nib.load(crisp_name).get_data()
        assert len(np.unique(crisp_image)) == num_classes
        one_hot_data = np.zeros(list(crisp_image.shape) + [num_classes], dtype=dtype)
        for idx in np.unique(crisp_image):
            one_hot_data[..., idx] = (crisp_image == idx)
        one_hot_image = nib.Nifti1Image(one_hot_data, nib.load(crisp_name).affine)
        nib.save(one_hot_image, one_hot_name)

if __name__ == '__main__':
    convert_one_hot(num_classes=12, dtype=np.float)
