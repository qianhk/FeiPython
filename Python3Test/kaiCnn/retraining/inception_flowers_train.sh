#!/usr/bin/env bash

# flowers train 迁移

# cd /AI/models/research/inception/inception/
python3 ./flowers_train.py --train_dir='/OnGit/FeiPython/Python3Test/cache/cifar-10-batches-py/temp/training_results' --data-dir='/OnGit/FeiPython/Python3Test/cache/cifar-10-batches-py/temp/data_dir' --pretrained_model_checkpoint_path='/AI/inception_v3.ckpt' --fine_tune=True --initial_learning_rate=0.001 --input_queue_memory_factor=1
