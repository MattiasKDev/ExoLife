import math

# Parameter for probability function needed
planet_size_min = 1000 / 6371  # Convert km to AU
planet_size_max = 20000 / 6371  # Convert km to AU
planet_max_eccentricity = 0.95
planet_min_eccentricity = 0.0


def find_bc(spectral_type):
    """
    This function returns the bolometric correction for a given spectral type.
    Input: spectral_type (str) - the spectral type of the star
    Output: bc (float) - the bolometric correction
    """
    if spectral_type == "M":
        return -2
    elif spectral_type == "K":
        return -0.8
    elif spectral_type == "G":
        return -0.4
    elif spectral_type == "F":
        return -0.15
    elif spectral_type == "A":
        return -0.3
    elif spectral_type == "B":
        return -2
    else:
        return -2


def calc_hz(magnitude, spectral_type, distance):
    """
    This function calculates the habitable zone of a star.
    Input: magnitude (float) - the absolute magnitude of the star
           spectral_type (str) - the spectral type of the star
           distance (float) - the distance of the star from the Sun
    """
    # Find the bolometric correction
    bc = find_bc(spectral_type)
    # Calculate the absolute magnitude
    M = magnitude - 5 * math.log10(distance / 10)
    # Calculate bolometric magnitude
    M_bol = M + bc
    # Calculate the luminosity
    L = 10 ** ((4.75 - M_bol) / 2.5)
    # Calculate the habitable zone
    inner = math.sqrt(L / 1.1)
    outer = math.sqrt(L / 0.53)
    return inner, outer


def calc_semi_minor(orbSMAxis, eccentricity):
    """
    This function calculates the semi-minor axis of an ellipse.
    Input: orbSMAxis (float) - the semi-major axis of the ellipse
           eccentricity (float) - the eccentricity of the ellipse
    """
    return orbSMAxis * math.sqrt(1 - eccentricity**2)
