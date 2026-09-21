# MI-072 — Gevrey reconstruction pushes rank-coupled anchor recovery to almost-logarithmic radius

**Evidence level:** exact Fourier-reconstruction synthesis from [NB-264](../../findings/NB-264-fixed-power-carrier-locked-shallow-meshes-recover-the-euler-anchor-at-bounded-hilbert-cost.md) and [NB-265](../../findings/NB-265-gevrey-anchor-reconstruction-pushes-shallow-mesh-coercivity-to-almost-logarithmic-rank-radius.md), sharpening the rank-coupled boundary left by NB-263.

For an Euler-normalized resolved carrier with `J=mK` and bounded coefficient `ell^2` norm, the anchor `sum c_j=1` admits an exact reconstruction from carrier-locked shallow Ford samples. NB-264 used a fixed smooth compact extension and obtained coercivity on every fixed-power radius `K^delta`. NB-265 chooses an explicit compact Gevrey plateau of order `s=1+epsilon`, so the reconstruction coefficients satisfy a stretched-exponential tail of the form

`sum_(|n Delta_m|>B) |d_n| <= C exp(-c B^(1/s))`.

The carrier values themselves obey the bounded-Hilbert estimate `|D_n|<=M sqrt(K)`. Taking

`B_K=C_epsilon (log(2+K))^(1+epsilon)`

with a sufficiently large constant makes the reconstruction tail negligible and forces both

`sup_(|n Delta_m|<=B_K) |D_n| >= c`

and

`sum_(|n Delta_m|<=B_K) |D_n| >= c m`.

Thus bounded-cost suppression cannot cover even a fixed superlogarithmic power of the eventual rank. At the live depth `u=log m+O(1)`, the corresponding physical Ford radius is only

`|x|=O_epsilon(m (log K)^(1+epsilon))=o(J)`,

while a cone-aligned matched packet still carries order-one residue mass.

The unresolved boundary is now much narrower than “subpolynomial.” This Gevrey method does not reach the exactly logarithmic radius: a nonzero compactly supported real-analytic plateau is impossible, so `s=1` is not obtained by specialization. More refined non-quasianalytic reconstruction could potentially approach logarithmic scale, but that is not established.

**Boundary.** Bounded resolved `ell^2` cost remains load-bearing. If `||c||_2=M_K` grows, the required radius depends on `log(M_K sqrt K)`. The result is still a matched source/destination-interface obstruction, not a claim about actual zeta-zero locations; total variation, conditioning and the exact Hardy/Nyman projection remain separate costs.