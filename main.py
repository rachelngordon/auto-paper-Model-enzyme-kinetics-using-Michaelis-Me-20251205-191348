# ==== main.py ====
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Parameters for Michaelis-Menten kinetics
    Km = 0.5  # Michaelis constant
    Vmax = 1.0  # Maximum velocity

    # Substrate concentration range: 0 to 10*Km
    S = np.linspace(0, 10 * Km, 200)
    # Michaelis-Menten equation
    v = (Vmax * S) / (Km + S)

    # --- Experiment 1: Saturation curve ---
    plt.figure()
    plt.plot(S, v, label='Michaelis-Menten')
    plt.xlabel('Substrate concentration [S]')
    plt.ylabel('Reaction velocity v')
    plt.title('Michaelis-Menten saturation curve')
    plt.legend()
    plt.grid(True)
    plt.savefig('velocity_vs_substrate.png')
    plt.close()

    # --- Experiment 2: Lineweaver-Burk plot ---
    # Exclude zero substrate to avoid division by zero
    mask = S > 0
    S_nz = S[mask]
    v_nz = v[mask]
    inv_S = 1.0 / S_nz
    inv_v = 1.0 / v_nz

    # Linear regression on double-reciprocal data
    slope, intercept = np.polyfit(inv_S, inv_v, 1)
    Vmax_est = 1.0 / intercept
    Km_est = slope * Vmax_est

    # Plot data and fitted line
    inv_S_fit = np.linspace(inv_S.min(), inv_S.max(), 200)
    inv_v_fit = slope * inv_S_fit + intercept
    plt.figure()
    plt.scatter(inv_S, inv_v, color='blue', label='Data')
    plt.plot(inv_S_fit, inv_v_fit, color='red', label='Fit')
    plt.xlabel('1/[S]')
    plt.ylabel('1/v')
    plt.title('Lineweaver-Burk plot')
    plt.legend()
    plt.grid(True)
    plt.savefig('lineweaver_burk.png')
    plt.close()

    # Primary numeric answer: estimated Vmax from the double-reciprocal fit
    print('Answer:', Vmax_est)

if __name__ == '__main__':
    main()

