import math

import functions.function as function
import numpy as np

# Parameter for probability function needed
planet_size_min = 1000 / 6371
planet_size_max = 20000 / 6371  # Convert km to AU
planet_max_eccentricity = 0.95
planet_min_eccentricity = 0.0


def normalize(value, min, max):
    """Normalize a value between 0 and 1.
    Input: value (float) - the value to normalize
           min (float) - the minimum value
           max (float) - the maximum value
    Output: normalized_value (float) - the normalized value"""
    return (value - min) / (max - min)


def calc_probability_in_HZ(OrbSM, OrbSMi, HZ_Inner, HZ_Outer):
    """Calculate the habitability probability of a planet being in the habitable zone compared to Earth
    Input: OrbSM (float) - the semi-major axis of the planet
           OrbSMi (float) - the semi-minor axis of the planet
           HZ_Inner (float) - the inner edge of the habitable zone
           HZ_Outer (float) - the outer edge of the habitable zone
    Output: prob (float) - the habitability probability of the planet being in the habitable zone
    """
    avg = (OrbSM + OrbSMi) / 2
    x = normalize(avg, HZ_Inner, HZ_Outer)
    s = 0.3
    return (
        (1 / (1.33))
        * (1 / (s * math.sqrt(2 * math.pi)))
        * np.exp(-((x - 0.12) ** 2) / (2 * s**2))
    )


def calc_probability_in_planet_size(planetSize):
    """Calculate the habitability probability of a planet being a certain size compared to Earth
    Input: planetSize (float) - the size of the planet
    Output: prob (float) - the habitability probability of the planet being a certain size compared to Earth
    """
    x = normalize(planetSize, planet_size_min, planet_size_max)
    s = 0.3 if x > 0.28 else 0.05
    return (
        (1 / (1.33))
        * (1 / (s * math.sqrt(2 * math.pi)))
        * np.exp(-((x - 0.28) ** 2) / (2 * s**2))
    )


def calc_probability_in_planet_eccentricity(planetEccentricity):
    """Calculate the habitability probability of a planet having a certain eccentricity compared to Earth
    Input: planetEccentricity (float) - the eccentricity of the planet
    Output: prob (float) - the habitability probability of the planet having a certain eccentricity compared to Earth
    """
    x = normalize(planetEccentricity, planet_min_eccentricity, planet_max_eccentricity)
    return 1 / (1 + np.exp(20 * (x - 0.2735)))


def calc_habitability_prob(
    magnitude,
    spectral_type,
    distance,
    OrbSM,
    planetSize,
    planetEccentricity,
    HZ_weight,
    size_weight,
    eccentricity_weight,
):
    """Calculate the habitability probability of a planet
    Input: magnitude (float) - the absolute magnitude of the star
           spectral_type (str) - the spectral type of the star
           distance (float) - the distance of the star from the Sun
           OrbSM (float) - the semi-major axis of the planet
           planetSize (float) - the size of the planet
           planetEccentricity (float) - the eccentricity of the planet
           HZ_weight (float) - the weight of the habitable zone in the calculation
           size_weight (float) - the weight of the planet size in the calculation
           eccentricity_weight (float) - the weight of the planet eccentricity in the calculation
    Output: prob (float) - the habitability probability of the planet
    """
    OrbSMi = function.calc_semi_minor(OrbSM, planetEccentricity)
    HZ_Inner, HZ_Outer = function.calc_hz(magnitude, spectral_type, distance)
    HZ_Prob = calc_probability_in_HZ(OrbSM, OrbSMi, HZ_Inner, HZ_Outer)
    Planet_Size_Prob = calc_probability_in_planet_size(planetSize)
    Planet_Eccentricity_Prob = calc_probability_in_planet_eccentricity(
        planetEccentricity
    )
    return (
        (
            HZ_Prob * HZ_weight
            + Planet_Size_Prob * size_weight
            + Planet_Eccentricity_Prob * eccentricity_weight
        )
        / (HZ_weight + size_weight + eccentricity_weight)
        * 100
    )
