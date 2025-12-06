import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Membuat canvas
fig, ax = plt.subplots(figsize=(8,6))

# Controller SDN
ax.add_patch(patches.Rectangle((3,5), 2.5, 1, edgecolor="black", facecolor="#cce5ff", lw=2))
ax.text(4.25, 5.5, "Controller SDN\n(Ryu/ONOS)", ha="center", va="center", fontsize=10, weight="bold")

# Raspberry Pi (Access Point)
ax.add_patch(patches.Rectangle((3,3), 2.5, 1, edgecolor="black", facecolor="#d4edda", lw=2))
ax.text(4.25, 3.5, "Raspberry Pi\n+ OVS + hostapd", ha="center", va="center", fontsize=10, weight="bold")

# Client devices
ax.add_patch(patches.Rectangle((1,1), 2, 1, edgecolor="black", facecolor="#fff3cd", lw=2))
ax.text(2, 1.5, "Client 1", ha="center", va="center", fontsize=9)

ax.add_patch(patches.Rectangle((4,1), 2, 1, edgecolor="black", facecolor="#fff3cd", lw=2))
ax.text(5, 1.5, "Client 2", ha="center", va="center", fontsize=9)

ax.add_patch(patches.Rectangle((7,1), 2, 1, edgecolor="black", facecolor="#fff3cd", lw=2))
ax.text(8, 1.5, "Client 3", ha="center", va="center", fontsize=9)

# Panah hubungan
ax.annotate("", xy=(4.25,5), xytext=(4.25,4), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(3,3.5), xytext=(2,2), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(5.5,3.5), xytext=(5,2), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(7.5,3.5), xytext=(8,2), arrowprops=dict(arrowstyle="->", lw=2))

# Judul
ax.text(4.5, 6.3, "Konsep Arsitektur SDWN Berbasis Raspberry Pi", ha="center", fontsize=12, weight="bold")

ax.axis("off")
plt.show()
