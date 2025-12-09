import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 14})



def load_xy(path):
    data = np.loadtxt(path, skiprows=1)
    return data[:,0], data[:,1]


Y_TICKS = np.arange(0.2, 1.01, 0.2)

t_mul, T_mul = load_xy("temp_mul.dat")
t_bor, T_bor = load_xy("temp_bor.dat")


fig, axes = plt.subplots(2, 2, figsize=(8, 8))
plt.subplots_adjust(wspace=0.25, hspace=0.30)

# PANEL (c) — NO CAVITY
ax = axes[0,0]

x, y = load_xy("no_cavity.dat")

ax.fill_between(x, y, color="#54a0ff", alpha=0.25)
ax.plot(x, y, color="#273c75", lw=4)

ax.set_ylim(0.065, 1.1)
ax.set_yticks(Y_TICKS)
ax.set_ylabel("Abs. (arb. units)")
ax.set_box_aspect(1)

# Save individual panel
figA = plt.figure(figsize=(4,4))
axA = figA.add_subplot(111)
axA.fill_between(x, y, color="#54a0ff", alpha=0.25)
axA.plot(x, y, color="#273c75", lw=4)
axA.set_ylim(0.065, 1.1)
axA.set_yticks(Y_TICKS)
axA.set_ylabel("Abs. (arb. units)")
axA.set_box_aspect(1)
figA.savefig("Fig3c.pdf", bbox_inches="tight")
plt.close(figA)

# PANEL (e) — TEMPERATURE vs TIME
ax = axes[0,1]

ax.plot(t_mul, T_mul, c="#ff9f43", lw=2)
ax.plot(t_bor,  T_bor,  c="#c23616", lw=2)

ax.set_xlim(0, 1000)
ax.set_ylim(280, 325)
ax.set_xlabel("Time (fs)")
ax.set_ylabel("Temperature (K)")
ax.set_box_aspect(1)

# Save individual panel
figB = plt.figure(figsize=(4,4))
axB = figB.add_subplot(111)
axB.plot(t_mul, T_mul, c="#ff9f43", lw=2)
axB.plot(t_bor,  T_bor,  c="#c23616", lw=2)
axB.set_xlim(0, 1000)
axB.set_ylim(280, 325)
axB.set_xlabel("Time (fs)")
axB.set_ylabel("Temperature (K)")
axB.set_box_aspect(1)
figB.savefig("Fig3e.pdf", bbox_inches="tight")
plt.close(figB)

# PANEL (d)
ax = axes[1,0]

x, y = load_xy("cavity.dat")

ax.fill_between(x, y, color="#ff6b6b", alpha=0.25)
ax.plot(x, y, color="#c23616", lw=4)
ax.axvline(0.19, linestyle="--", color="black", lw=1)

ax.set_ylim(0.065, 1.1)
ax.set_yticks(Y_TICKS)
ax.set_xlabel("Energy (eV)")
ax.set_ylabel("Abs. (arb. units)")
ax.set_box_aspect(1)

# Save individual panel
figC = plt.figure(figsize=(4,4))
axC = figC.add_subplot(111)
axC.fill_between(x, y, color="#ff6b6b", alpha=0.25)
axC.plot(x, y, color="#c23616", lw=4)
axC.axvline(0.19, linestyle="--", color="black", lw=1)
axC.set_ylim(0.065, 1.1)
axC.set_yticks(Y_TICKS)
axC.set_xlabel("Energy (eV)")
axC.set_ylabel("Abs. (arb. units)")
axC.set_box_aspect(1)
figC.savefig("Fig3d.pdf", bbox_inches="tight")
plt.close(figC)

# PANEL (f)
ax = axes[1,1]

# 19:2
x_a, y_a = load_xy("cavity.dat")
ax.plot(x_a, y_a, lw=4, color="#c23616")
ax.fill_between(x_a, y_a, color="#c23616", alpha=0.15)

# H2O off
x_b, y_b = load_xy("cavity_mul.dat")
ax.plot(x_b, y_b, lw=4, color="#ff9f43")
ax.fill_between(x_b, y_b, color="#ff9f43", alpha=0.15)

ax.set_ylim(0.065, 1.1)
ax.set_yticks(Y_TICKS)
ax.set_xlabel("Energy (eV)")
ax.set_ylabel("Abs. (arb. units)")
ax.set_box_aspect(1)

# Save individual panel
figD = plt.figure(figsize=(4,4))
axD = figD.add_subplot(111)
axD.plot(x_a, y_a, lw=4, color="#c23616")
axD.fill_between(x_a, y_a, color="#c23616", alpha=0.15)
axD.plot(x_b, y_b, lw=4, color="#ff9f43")
axD.fill_between(x_b, y_b, color="#ff9f43", alpha=0.15)
axD.set_ylim(0.065, 1.1)
axD.set_yticks(Y_TICKS)
axD.set_xlabel("Energy (eV)")
axD.set_ylabel("Abs. (arb. units)")
axD.set_box_aspect(1)
figD.savefig("Fig3f.pdf", bbox_inches="tight")
plt.close(figD)


plt.savefig("Fig3_cdef.pdf", bbox_inches="tight")
plt.show()
