from django.core.cache import cache
from django.utils import crypto

GENERATION_KEY_NAME = 'metric:generation'

def generation_key(timeout=60 * 60 * 24 * 365):
    generation = cache.get(GENERATION_KEY_NAME)
    if generation is None:
        generation = crypto.get_random_string(length=12)
        cache.set(GENERATION_KEY_NAME, generation, timeout)
    return generation


def reset_generation_key():
    cache.delete(GENERATION_KEY_NAME)