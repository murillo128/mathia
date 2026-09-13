# MI-018 — One-signed first crossings expose a quantitative source-tail budget for screened gaps

**Evidence level:** exact on the one-signed branch of a hypothetical first unrestricted Suzuki crossing through WI-272. WI-270 gives the general cut tariff using the classical Hilbert--Carleman inequality, WI-271 forces arithmetic overlap across gaps at least as wide as `h_0=log rho`, and WI-272 extends that conclusion below `h_0` whenever the remaining positive archimedean tail is too small to pay firstness. No theorem makes the actual first null mode one-signed or proves RH.

WI-269 gives the exact source-ground-state transform at a first crossing: multiplier energies form a positive-semidefinite signed-source Laplacian, while the archimedean source changes sign once at `h_0`. WI-270 sharpens that structure when the null mode `v` is one-signed. For almost every cut, a positive proper-aperture firstness cost must be paid either by positive prime-power crossing overlap or by bilateral short-range mass in the region where the archimedean source is positive.

For a genuine internal support gap `(alpha,beta)` of width `L`, a smooth multiplier can transition entirely through the zero region and split the mode into exact left and right pieces. WI-271 observes that when `L>=h_0`, every cross-gap archimedean edge has nonpositive source weight, so the continuous source cannot finance the strictly positive side-mode energy. The von-Mangoldt source must then carry the balance and some active prime-power lag has `C_v(log n)>0`.

WI-272 shows that `h_0` is not a hard boundary. Put

`B(L) = integral_L^{h_0} w(h) dh`

for `0<L<h_0`, and `B(L)=0` for `L>=h_0`. The positive cross-gap continuous term is a convolution pairing between the two side modes. Young's `L^1*L^2 -> L^2` inequality bounds it by

`B(L) sqrt(M_L M_R)`.

Consequently the prime cross-gap mass satisfies

`P_gap >= max(lambda_(r_L) M_L, lambda_(r_R) M_R) - B(L) sqrt(M_L M_R)`.

Complete prime screening therefore requires simultaneously

`B(L) >= lambda_(r_L) sqrt(M_L/M_R)` and `B(L) >= lambda_(r_R) sqrt(M_R/M_L)`,

so in particular

`B(L)^2 >= lambda_(r_L) lambda_(r_R)`.

The two inequalities also pin the admissible mass ratio; a screened gap cannot escape merely by moving almost all mass to one side. Since `B(L)` vanishes quadratically as `L` approaches `h_0` from below, every fixed proper-aperture margin has a strict exclusion collar below the sign-change scale. WI-271 is the zero-tail endpoint of this continuous tariff, not a separate mechanism.

The remaining one-signed geometry is correspondingly sharper: a completely screened first mode must avoid any gap whose positive source tail is too small, and must maintain enough short-range mass/coupling to pay firstness everywhere. The scalar tail estimate itself cannot exclude arbitrarily narrow gaps because `w(h)~1/(2h)` and hence `B(L)` diverges logarithmically as `L` tends to zero. Progress in that regime needs the full cut/null-equation family, more local information about the mode, or a sharper source-conditioned operator norm rather than another total-mass estimate.

**Boundary.** The one-signed assumption and the genuine separating gap are load-bearing. WI-272 does not force a gap to exist, does not make the first null mode one-signed, and does not transfer to sign-changing cross-gap products. The sign-changing branch remains governed by WI-269's PSD/nodal compensation law.