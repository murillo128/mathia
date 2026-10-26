# MI-067 — Fixed gap correlations determine the high-band rank spectrum, not its residue split

**Evidence level:** supported synthesis of [FD-346](../../findings/FD-346-classical-gap-correlations-separate-high-band-farey-transport.md). The input is the classical fixed-lag gap-correlation asymptotic as persisted there; this is neither a new arithmetic estimate nor an RH consequence.

For genuine Farey order `Q`, put `N=sum_(q<=Q) phi(q)`, `D_k=x_k-k/N`, and periodic gaps `g_k=x_(k+1)-x_k`. Write `S_r=sum_k g_k g_(k+r)`. The leading scaled correlations are

`(Q^2/log Q)S_0 -> 12/pi^2`, `(Q^2/log Q)S_1 -> 6/pi^2`, and `(Q^2/log Q)S_r -> 0` for each fixed `r>=2`.

If `G_j` and `F_j` are the unitary periodic Fourier coefficients of `g` and `D`, the positive gap measure `(Q^2/log Q)sum_j |G_j|^2 delta_(2pi j/N)` therefore converges weakly to `(6/pi^3)(1+cos theta)dtheta`. Fixed trigonometric polynomials and bounded total mass suffice; no estimate uniform in growing lag is used. Discrete integration gives

`G_j=(exp(2pi i j/N)-1)F_j` for `j!=0`.

Its inverse squared multiplier is bounded only away from frequency zero. Reflection gives `d_(2j)^2=2|F_j|^2` for the orthonormal sine coefficients `d_m` of `D`, while odd `d_m` vanish. Hence, for every fixed `0<alpha<1`,

`(Q^2/log Q)sum_(m/N>=alpha) d_m^2 delta_(m/N) => (6/pi^2)cot^2(pi x/2) dx` on `[alpha,1]`.

This identifies a tail of size `log Q/Q^2`; it gives no uniform shrinking-band limit and no control of the full Franel energy near the singular frequency.

For the reflected four-defect `BCA` reassembly at prime order `p`, let `B={m:N/2<=m<N}`, `b=1/(2p)`, and use the exact dictionary `y=CD+w`: `C` is the periodic half-shift and `w` is the balanced step, zero at the midpoint. The half-shift preserves every source intensity, while `||Pi_B w||^2=O(p^-2)`. Thus

`||Pi_B y||^2 ~ (6I/pi^2)log(p)/p^2`, `I=2/pi-1/2`,

and `TV(pi^B(y),pi^B(D))=O((log p)^(-1/2))`. Here `pi^B` normalizes squared sine coefficients inside `B`. The source dominates this band, even though transport dominates the full energy.

The projected right-endpoint transport `a` has only `m=2 mod 4` coefficients `2b sqrt(2/N)cos(pi m/N)cot(pi m/(2N))`. Its band energy is `~J/(2p^2)`, `J=4/pi-5/4`. Under `m -> m/N`, the two conditional laws have different weak densities:

`f(x)=cot^2(pi x/2)/I`, `f_a(x)=cos^2(pi x)cot^2(pi x/2)/J`, `1/2<=x<=1`.

Because the extra weight `cos^2(pi x)` is strictly increasing, the event `[1/2,3/4]` has strictly less mass under `f_a`. FD-346 obtains `liminf TV(pi^B(y),pi^B(a))>=0.2989471621...`. This proves nonconvergence even after stitch projection; a diverging coefficient-error ratio alone would not prove it after separate energy normalization. See the [Visual comparison](../../../visual_exploration/mind/intuition/MI-071-farey-spectral-transfer-pays-relative-energy-and-rank-variation.md) for the exact finite dictionary.

The inherited fraction `sum_(m in B,4|m)d_m^2 / ||Pi_B y||^2` is still unknown. Weak convergence cannot split interlaced mesh classes. Since `m=2j`, separating `m=0 mod 4` from `m=2 mod 4` inserts `(-1)^j` in the gap measure, requiring scaled correlations `S_(N/2+r)` at fixed offsets `r`, not the fixed lags above. The unresolved half-period correlation is a finer source question; it is no longer needed to reject the projected comparator.
