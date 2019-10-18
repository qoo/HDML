# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 19:02:49 2016

@author: sakurai
"""

from fuel.datasets import H5PYDataset
from fuel.utils import find_in_data_path
from fuel.schemes import SequentialScheme
from fuel.streams import DataStream


class IconEvalv2Dataset(H5PYDataset):

    _filename = 'cars196/cars196.hdf5'

    def __init__(self, which_sets, **kwargs):
        try:
#            path = find_in_data_path(self._filename)
            path = "/root/HDML/datasets/data/cars196/icon_valv2.hdf5"
        except IOError as e:
            msg = str(e) + (""".
         You need to download the dataset and convert it to hdf5 before.""")
            raise IOError(msg)
        super(IconEvalv2Dataset, self).__init__(
            file_or_path=path, which_sets=which_sets, **kwargs)


def load_as_ndarray(which_sets=['train', 'test']):
    datasets = []
    for split in which_sets:
        data = IconEvalv2Dataset([split], load_in_memory=True).data_sources
        datasets.append(data)
    return datasets


if __name__ == '__main__':
    dataset = IconEvalv2Dataset(['train'])

    st = DataStream(
        dataset, iteration_scheme=SequentialScheme(dataset.num_examples, 1))
    it = st.get_epoch_iterator()
    it.next()
