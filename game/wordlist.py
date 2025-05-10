import random

WORDS = ['python', 'django', 'hangman', 'coding', 'programming',
    'algorithm', 'function', 'variable', 'syntax', 'debug', 'compile',
    'execute', 'runtime', 'binary', 'decimal', 'integer', 'boolean',
    'condition', 'loop', 'iteration', 'recursion', 'inheritance', 'object',
    'class', 'module',
]

def get_random_word():
    return random.choice(WORDS).upper()
