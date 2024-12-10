#  max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# Finds the maximum achievable bitrate.
# Parameters:
# tx_w: transmitted power (Watts)
# tx_gain_db: transmitter gain (dB)
# freq_hz: frequency (Hz)
# dist_km: separation vector magnitude (km)
# rx_gain_db: receiver gain (dB)
# n0_j: noise spectral density (J)
# bw_hz: bandwidth (Hz)
# ...
# Output:
# r_max: maximum achievable bitrate
# Outputs the maximum achievable bitrate.
#
# Written by Josefine Krohn
# Other contributors: Brad Denby
#
# import Python modules
import math # math module
import sys # argv
# "constants"
c = 2.99792458e8 # m/s, speed of light
# helper functions
## gain to multiplicative factor conversion
def dB_to_factor(i):
    return 10**(i/10)
# initialize script arguments
tx_w = float('nan') # transmitted power (Watts)
tx_gain_db = float('nan') # transmitter gain (dB)
freq_hz = float('nan') # frequency (Hz)
dist_km = float('nan') # separation vector magnitude (km)
rx_gain_db = float('nan') # receiver gain (dB)
n0_j = float('nan') # noise spectral density (J)
bw_hz = float('nan') # bandwidth (Hz)
# parse script arguments
if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
    print(\
        'Usage: '\
            'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
    )
    exit()
# write script below this line

# assumptions
L_l = -1 # dB, transmitter to antenna line loss
L_a = 0 # dB, atmospheric loss
N = n0_j*bw_hz # received noise power

wl = c/freq_hz # wavelength
dist_m = dist_km*1000 # converting distance from km to m

# converting from dB to multiplicative factor
L_l = dB_to_factor(L_l)
tx_gain_db = dB_to_factor(tx_gain_db)
L_a = dB_to_factor(L_a)
rx_gain_db = dB_to_factor(rx_gain_db)

C = tx_w*L_l*tx_gain_db*((wl/(4*math.pi*dist_m))^2)*L_a*rx_gain_db # received signal power


r_max = bw_hz*math.log(1 + C/N, 2) # max achievable bitrate
print(math.floor(r_max))