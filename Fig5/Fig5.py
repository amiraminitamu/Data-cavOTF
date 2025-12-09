import numpy as np
import matplotlib.pyplot as plt
import matplotlib

plt.rcParams.update({'font.size': 18})

L = 423341.7992
ω_fixed = np.arange(0.03, 0.850, 0.0001)

files = [
    "16_born.dat", "19_born.dat", "22_born.dat", "43_born.dat",
    "16_mul.dat",  "19_mul.dat",  "22_mul.dat",  "43_mul.dat"
]

for fname in files:

    hist_full = np.loadtxt(fname)  

    N = 41
    k_points = 2*np.pi*np.arange(N)/L
    k_pos = k_points * 1e4
    k_neg = -k_pos[::-1]
    k_full = np.concatenate([k_neg, k_pos])

    plt.figure(figsize=(12,6))

    plt.imshow(
        hist_full,
        aspect='auto',
        extent=[k_full[0], k_full[-1], ω_fixed[0], ω_fixed[-1]],
        cmap=matplotlib.colors.LinearSegmentedColormap.from_list(
            'custom',['#020024','#547bff','#00d4ff','#a9f0ff','#a9ffe2']
        )
    )

    plt.xlabel(r"$k\,(10^{-4}\ \mathrm{\AA^{-1}})$")
    plt.ylabel("Energy (eV)")

    if fname.startswith("43"):
        plt.clim(0, 0.5*np.max(hist_full))
    else:
        plt.clim(0, 0.3*np.max(hist_full))

    plt.yticks(np.arange(0.1,0.71,0.1))

    if fname.startswith("43"):
        plt.ylim(0.3, 0.7)
        plt.xlim(-2, 2)
    else:
        plt.ylim(0.1, 0.4)
        plt.xlim(-1.5, 1.5)

    outfig = fname.replace(".dat", ".pdf")
    plt.savefig(outfig, dpi=400, bbox_inches="tight")
    plt.close()
