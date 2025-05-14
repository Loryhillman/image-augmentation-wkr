augmentation_config = {
    'order': ['noise', 'rotate', 'flip', 'shift', 'brightness'],

    'volume_presets': {
        'low': ['flip', 'brightness'],
        'medium': ['flip', 'brightness', 'rotate', 'noise'],
        'high': ['flip', 'brightness', 'rotate', 'noise', 'shift']
    },

    'noise': {
        'enabled': True,
        'types': ['gaussian', 'salt_pepper'],
        'params': {
            'gaussian': {
                'mean': 0,
                'std': 10
            },
            'salt_pepper': {
                'amount': 0.05,
                'salt_vs_pepper': 0.5
            }
        }
    },

    'rotate': {
        'enabled': True,
        'params': {
            'angle': 15
        }
    },

    'flip': {
        'enabled': True,
        'params': {
            'mode': 'horizontal'
        }
    },

    'shift': {
        'enabled': True,
        'params': {
            'max_shift': 0.1
        }
    },

    'brightness': {
        'enabled': True,
        'params': {
            'factor': 1.5
        }
    }
}
