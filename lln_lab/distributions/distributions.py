import logging

import numpy as np

from lln_lab.distributions.distributions_definitions import Distribution


def generate_samples(distribution: Distribution, sample_size: int) -> np.ndarray:
    if sample_size <= 0:
        logging.error(f"Invalid sample size: {sample_size}")

        raise ValueError("Sample size must be positive")

    if distribution == Distribution.UNIFORM:
        samples = np.random.uniform(0, 1, size=sample_size)
    elif distribution == Distribution.Z:
        samples = np.random.normal(0, 1, size=sample_size)
    elif distribution == Distribution.EXPONENTIAL:
        samples = np.random.exponential(1, size=sample_size)
    elif distribution == Distribution.GAMMA:
        samples = np.random.gamma(shape=2.0, scale=2.0, size=sample_size)
    else:
        logging.error(f"Invalid distribution: {distribution}")

        raise ValueError(f"Invalid distribution: {distribution}")

    logging.debug(f"Sample size: {sample_size}, samples: {samples}")
    return samples


def get_expected_value(distribution: Distribution) -> float:
    if distribution == Distribution.UNIFORM:
        return 0.5
    elif distribution == Distribution.Z:
        return 0.0
    elif distribution == Distribution.EXPONENTIAL:
        return 1.0
    elif distribution == Distribution.GAMMA:
        return 4.0
    else:
        raise ValueError(f"No expected value defined for {distribution}")
