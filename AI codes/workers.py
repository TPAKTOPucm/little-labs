import os


import requests
import torch
from PIL import Image

from super_gradients.training import Trainer, dataloaders, models
from super_gradients.training.dataloaders.dataloaders import (
    coco_detection_yolo_format_train, coco_detection_yolo_format_val
)
from super_gradients.training.losses import PPYoloELoss
from super_gradients.training.metrics import DetectionMetrics_050
from super_gradients.training.models.detection_models.pp_yolo_e import (
    PPYoloEPostPredictionCallback
)


class config:
    CHECKPOINT_DIR = 'checkpoint'
    EXPERIMENT_NAME = 'workers'

    DATA_DIR = './archive'

    TRAIN_IMAGES_DIR = 'images/train'
    TRAIN_LABELS_DIR = 'labels/train'

    VAL_IMAGES_DIR = 'images/val'
    VAL_LABELS_DIR = 'labels/val'

    TEST_IMAGES_DIR = 'images/test'
    TEST_LABELS_DIR = 'labels/test'

    CLASSES = ['helmet', 'vest', 'head', 'person']

    NUM_CLASSES = len(CLASSES)

    DATALOADER_PARAMS = {
        'batch_size': 16,
        'num_workers': 2
    }

    MODEL_NAME = 'yolo_nas_s'
    PRETRAINED_WEIGHTS = 'coco'

trainer = Trainer(experiment_name=config.EXPERIMENT_NAME, ckpt_root_dir=config.CHECKPOINT_DIR)
train_data = coco_detection_yolo_format_train(
        dataset_params={
            'data_dir': config.DATA_DIR,
            'images_dir': config.TRAIN_IMAGES_DIR,
            'labels_dir': config.TRAIN_LABELS_DIR,
            'classes': config.CLASSES
        },
        dataloader_params=config.DATALOADER_PARAMS
)


val_data = coco_detection_yolo_format_val(
    dataset_params={
        'data_dir': config.DATA_DIR,
        'images_dir': config.VAL_IMAGES_DIR,
        'labels_dir': config.VAL_LABELS_DIR,
        'classes': config.CLASSES
    },
    dataloader_params=config.DATALOADER_PARAMS
)

test_data = coco_detection_yolo_format_val(
    dataset_params={
        'data_dir': config.DATA_DIR,
        'images_dir': config.TEST_IMAGES_DIR,
        'labels_dir': config.TEST_LABELS_DIR,
        'classes': config.CLASSES
    },
    dataloader_params=config.DATALOADER_PARAMS
)
train_data.dataset.plot()

model = models.get(config.MODEL_NAME,
                   num_classes=config.NUM_CLASSES,
                   pretrained_weights=config.PRETRAINED_WEIGHTS
                   )
train_params = {
    "average_best_models": True,
    "warmup_mode": "linear_epoch_step",
    "warmup_initial_lr": 1e-6,
    "lr_warmup_epochs": 3,
    "initial_lr": 5e-4,
    "lr_mode": "cosine",
    "cosine_final_lr_ratio": 0.1,
    "optimizer": "Adam",
    "optimizer_params": {"weight_decay": 0.0001},
    "zero_weight_decay_on_bias_and_bn": True,
    "ema": True,
    "ema_params": {"decay": 0.9, "decay_type": "threshold"},
    "max_epochs": 10,
    "mixed_precision": False,
    "loss": PPYoloELoss(
        use_static_assigner=False,
        num_classes=config.NUM_CLASSES,
        reg_max=16
    ),
    "valid_metrics_list": [
        DetectionMetrics_050(
            score_thres=0.1,
            top_k_predictions=300,
            num_cls=config.NUM_CLASSES,
            normalize_targets=True,
            post_prediction_callback=PPYoloEPostPredictionCallback(
                score_threshold=0.01,
                nms_top_k=1000,
                max_predictions=300,
                nms_threshold=0.7
            )
        )
    ],
    "metric_to_watch": 'mAP@0.50'
}
if name == 'main':
    trainer.train(model=model,
                  training_params=train_params,
                  train_loader=train_data,
                  valid_loader=val_data
                )
    try:
        trainer.test(model=model,
            test_loader=torch.utils.data.DataLoader(
                dataset=test_data, batch_size=16, shuffle=False),
            test_metrics_list=DetectionMetrics_050(score_thres=0.1,
                                                   top_k_predictions=300,
                                                   num_cls=config.NUM_CLASSES,
                                                   normalize_targets=True,
                                                   post_prediction_callback=PPYoloEPostPredictionCallback(
                                                        score_threshold=0.01,
                                                        nms_top_k=1000,
                                                        max_predictions=300, nms_threshold=0.7)
                                                 ))
    except BaseException:
        print("Ne rabotaet!!!!!!!!!!!!!!")

    model.predict("C:/Users/Nikit/PycharmProjects/VKR/archive/images/val", conf=0.25).show()