augmentation_config = {
    # Все доступные типы аугментаций (включаются/выключаются через enabled)
    'available_augmentations': [
        'noise',
        'rotate',
        'flip',
        'shift',
        'brightness'
    ],

    # Параметры каждой аугментации
    'noise': {
        'enabled': True,
        'types': ['gaussian', 'salt_pepper'],
        'params': {
            'gaussian': {
                'std_range': (1, 25)
            },
            'salt_pepper': {
                'amount_range': (0.01, 0.1),
                'salt_vs_pepper': 0.5
            }
        }
    },

    'rotate': {
        'enabled': True,
        'params': {
            'angle_range': (-45, 45)
        }
    },

    'flip': {
        'enabled': True,
        'params': {
            'mode_options': ['horizontal', 'vertical']
        }
    },

    'shift': {
        'enabled': True,
        'params': {
            'max_shift_range': (0.05, 0.2)
        }
    },

    'brightness': {
        'enabled': True,
        'params': {
            'factor_range': (0.7, 1.5)
        }
    },

    # Теперь уровни влияют на количество выходных изображений
    'volume_presets': {
        'low': 25,
        'medium': 50,
        'high': 100
    }
}