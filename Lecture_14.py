# plot_period_vs_length_powerlaw_with_residuals.py
# Input columns (header optional, commas/tabs/spaces OK):
#   Length   Period   dx   dv
# Interpreted as: length_m, period_s, length_unc_m, period_unc_s

import os, math
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

SAVE_FIG = "T_vs_L_powerlaw_with_residuals.png"
SAVE_TXT = "T_vs_L_fit_report.txt"
USE_ODR_IF_AVAILABLE = True

# ---------- tiny safe formatter ----------
def g(x, d=3):
    return "nan" if not (isinstance(x, (int, float)) and np.isfinite(x)) else f"{x:.{d}g}"

# ---------- robust loader ----------
def load_txt(path):
    rows = []
    with open(path, "r", encoding="utf-8-sig") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            parts = [p for p in s.replace(",", " ").split() if p]
            # try parse first 4 tokens as floats; skip header-ish lines
            nums = []
            ok = True
            for tok in parts[:4]:
                try:
                    nums.append(float(tok))
                except Exception:
                    ok = False
                    break
            if ok and len(nums) == 4:
                rows.append(nums)
    if not rows:
        raise ValueError(
            "No valid numeric rows. Expected 4 columns like:\n"
            "length  period  dx  dv"
        )
    arr = np.asarray(rows, dtype=float)
    L, T, sL, sT = arr[:,0], arr[:,1], arr[:,2], arr[:,3]
    return L, T, sL, sT

# ---------- power-law fit helpers ----------
def odr_powerlaw_fit(L, T, sL, sT):
    try:
        from scipy import odr
    except Exception:
        return None
    mask = np.isfinite(L) & np.isfinite(T) & (L>0) & (T>0)
    if mask.sum() < 3: return None
    L, T, sL, sT = L[mask], T[mask], sL[mask], sT[mask]
    x, y = np.log(L), np.log(T)
    sx = np.where((sL>0)&np.isfinite(sL), sL/L, 0.0)
    sy = np.where((sT>0)&np.isfinite(sT), sT/T, 0.0)
    def f(beta, x): a,b = beta; return a + b*x
    model = odr.Model(f)
    data  = odr.RealData(x, y, sx=sx, sy=sy)
    out   = odr.ODR(data, model, beta0=[np.mean(y), 0.5]).run()
    a, b = out.beta
    cov  = out.cov_beta
    sa, sb = (np.sqrt(np.diag(cov)) if cov is not None else (np.nan, np.nan))
    k, dk = math.exp(a), (math.exp(a)*sa if np.isfinite(sa) else np.nan)
    n, dn = b, (sb if np.isfinite(sb) else np.nan)
    yhat  = f(out.beta, x)
    ss_res = np.sum((y-yhat)**2); ss_tot = np.sum((y-np.mean(y))**2)
    r2 = 1 - ss_res/ss_tot if ss_tot>0 else np.nan
    return {"k":k,"dk":dk,"n":n,"dn":dn,"r2":r2,"mask":mask}

def wls_powerlaw_fit_yonly(L, T, sT):
    mask = np.isfinite(L) & np.isfinite(T) & (L>0) & (T>0)
    if mask.sum() < 3: return None
    L, T, sT = L[mask], T[mask], sT[mask]
    x, y = np.log(L), np.log(T)
    sigma = np.where((sT>0)&np.isfinite(sT), sT/T, np.nan)
    ok = np.isfinite(sigma) & (sigma>0)
    if ok.sum() >= 3:
        x, y, w = x[ok], y[ok], 1/(sigma[ok]**2)
        A = np.vstack([np.ones_like(x), x]).T
        ATA = A.T @ (w[:,None]*A); ATy = A.T @ (w*y)
        a, b = np.linalg.solve(ATA, ATy)
        yhat = A @ np.array([a,b])
        s2 = np.sum(w*(y-yhat)**2)/(len(y)-2)
        cov = s2 * np.linalg.inv(ATA)
        sa, sb = np.sqrt(np.diag(cov))
    else:
        b, a = np.polyfit(x, y, 1)
        yhat = a + b*x
        s2 = np.var(y-yhat, ddof=2)
        Sxx = np.sum((x-np.mean(x))**2)
        sb = math.sqrt(s2/Sxx) if Sxx>0 else np.nan
        sa = math.sqrt(s2*(1/len(x)+(np.mean(x)**2)/Sxx)) if Sxx>0 else np.nan
    k, dk = math.exp(a), (math.exp(a)*sa if np.isfinite(sa) else np.nan)
    n, dn = b, sb
    y_full = np.log(T); y_pred = a + b*np.log(L)
    ss_res = np.sum((y_full - y_pred)**2); ss_tot = np.sum((y_full - np.mean(y_full))**2)
    r2 = 1 - ss_res/ss_tot if ss_tot>0 else np.nan
    return {"k":k,"dk":dk,"n":n,"dn":dn,"r2":r2,"mask":mask}

# ---------- main ----------
def main():
    root = Tk(); root.withdraw()
    path = filedialog.askopenfilename(
        title="Select TXT with 4 columns (Length Period dx dv)",
        filetypes=[("Text files","*.txt *.dat *.csv"), ("All files","*.*")]
    )
    if not path: return

    # Load
    L, T, sL, sT = load_txt(path)

    # Fit
    res = odr_powerlaw_fit(L, T, sL, sT) if USE_ODR_IF_AVAILABLE else None
    if res is None:
        res = wls_powerlaw_fit_yonly(L, T, sT)
    if res is None:
        raise RuntimeError("Not enough valid points to fit.")

    k, dk, n, dn, r2, mask = res["k"], res["dk"], res["n"], res["dn"], res["r2"], res["mask"]

    # Smooth curve & residuals
    Lmin, Lmax = np.nanmin(L[mask]), np.nanmax(L[mask])
    Lfit = np.linspace(Lmin, Lmax, 400)
    Tfit_curve = k * (Lfit ** n)
    residuals = T[mask] - (k * (L[mask] ** n))

    # Figure with residuals
    fig = plt.figure(figsize=(8.5,7))
    gs = fig.add_gridspec(2,1, height_ratios=[3,1], hspace=0.10)
    ax  = fig.add_subplot(gs[0,0])
    rax = fig.add_subplot(gs[1,0], sharex=ax)

    ax.errorbar(L, T, xerr=sL, yerr=sT, fmt='+', capsize=3, lw=1, label="data")
    ax.plot(Lfit, Tfit_curve, '-', label="power-law fit")
    ax.set_ylabel("Period, $T$ (s)")
    ax.set_title("Length vs. Period (power-law fit)\n$T = k L^{n}$")
    ax.legend(loc="best")

    # Put equation on the plot (upper-left)
    eq = f"$T = ({g(k,3)} \\pm {g(dk,2)})\\,L^{{{g(n,3)}}}$\n$\\,\\,\\,\\,\\,\\,\\,\\,\\pm\\,{g(dn,2)}$"
    ax.text(0.02, 0.95, eq + f"\n$R^2_{{\\log}} = {g(r2,3)}$",
            transform=ax.transAxes, va="top", ha="left",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="0.7"))

    # Residuals
    rax.axhline(0, lw=1, alpha=0.8)
    rax.errorbar(L[mask], residuals, xerr=sL[mask], yerr=sT[mask], fmt='+', capsize=3, lw=1)
    rax.set_xlabel("Length, $L$ (m)")
    rax.set_ylabel("Residuals\n$T - T_{fit}$ (s)")

    fig.tight_layout()

    # Save outputs
    out_dir = os.path.dirname(path)
    fig_path = os.path.join(out_dir, SAVE_FIG)
    fig.savefig(fig_path, dpi=220)

    # Print and save a small text report (so you can't miss it)
    line = (f"Fit (log–log):  T = ({g(k,6)} ± {g(dk,3)}) · L^({g(n,4)} ± {g(dn,3)})"
            f"   R^2(log) = {g(r2,4)}")
    print(line)
    with open(os.path.join(out_dir, SAVE_TXT), "w", encoding="utf-8") as f:
        f.write(line + "\n")

    print(f"Saved figure: {fig_path}")
    print(f"Saved report: {os.path.join(out_dir, SAVE_TXT)}")
    plt.show()

if __name__ == "__main__":
    main()
