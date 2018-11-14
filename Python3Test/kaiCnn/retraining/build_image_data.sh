#!/usr/bin/env bash

python3 /AI/models/research/inception/inception/data/build_image_data.py --train_directory='../../cache/cifar-10-batches-py/train_dir' --validation_directory='../../cache/cifar-10-batches-py/validation_dir' --output_directory='../../cache/cifar-10-batches-py/temp/' --labels_file='../../cache/cifar-10-batches-py/cifar10_labels.txt'
