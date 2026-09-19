# NB-225 — Sublinear shells admit Bellotti-compatible phase-aligned Ford packets

**Date:** 2026-09-19  
**Status:** `DERIVED + NEGATIVE/METHOD-BOUNDARY + ZETA-SPECTRAL-MATCHED-CONTROL + PHASE-ALIGNED-ZERO-PACKET + EXACT-FORD-SCALE + SUBLINEAR-LOG-SHELL + NB-223/NB-224-SHARPENING + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-224` shows that widening the logarithmic source shell to `H=Theta(X)` narrows the vertical residue carrier to `Theta(1/X)` and lets Bellotti's local disk count reach the exact Ford denominator with a constant positive Euler gap. The remaining question is whether this linear width is merely a convenient sufficient choice or reflects a real limitation of the current zero-population input.

At the level of the explicit-formula route used in `NB-223`--`NB-224`, the linear width is sharp. At exact Ford scale, every genuinely sublinear carrier width `H=o(R)` admits an abstract packet of near-one zeros that simultaneously respects the Vinogradov--Korobov zero-free depth, Bellotti's fixed-depth and growing near-one zero-density bounds, Bellotti's local `O(K)` disk count, and ordinary local zero counting, while contributing order one to the **signed** smoothed residue carrier. The packet can moreover be placed so that all carrier phases agree.

This does **not** assert that the actual zeta zeros contain such packets. It proves a logical insufficiency statement: the currently used population bounds, even taken together, cannot by themselves close the exact-Ford endpoint for a sublinear logarithmic shell. Any such improvement needs information absent from those hypotheses, such as phase-sensitive zero correlations or a stronger joint estimate coupling horizontal depth to the `1/H` vertical carrier window.

## 1. Exact-Ford scaling and the general shell carrier

Keep the one-sided shell of `NB-224`. Fix `r>0` and a nonzero `phi>=0` in `C_c^infinity((0,1))`, and for

\[
1\le H=H(X)\le C X
\]

put

\[
\sigma_X=1+\frac rX,
\qquad
h_{X,H}(u)=\frac1H\phi\!\left(\frac{u-X}{H}\right).
\tag{1}
\]

Its Fourier carrier is

\[
L_{X,H}(v)
=e^{iXv}F(Hv),
\qquad
F(z)=\int_0^1\phi(y)e^{izy}\,dy,
\tag{2}
\]

with `F(0)>0`. A zero `rho=beta+i gamma` contributes at

\[
v_\rho=(\gamma-t)+i(\sigma_X-\beta).
\tag{3}
\]

Write, as in `NB-223`--`NB-224`,

\[
Q=\log(10+|t|),
\qquad
L=\log Q,
\qquad
R=Q^{2/3}L^{1/3},
\qquad
Y=\frac XR.
\tag{4}
\]

The exact Ford regime is `Y=Theta(1)`, equivalently

\[
Q\asymp \frac{X^{3/2}}{(\log X)^{1/2}}.
\tag{5}
\]

For the matched control below, take a coupled sequence with

\[
Y\longrightarrow Y_*\in(0,\infty)
\tag{6}
\]

and assume the shell is genuinely sublinear relative to the local-zero scale,

\[
\boxed{\frac HR\longrightarrow0.}
\tag{7}
\]

Since `R asymp X` in (6), condition (7) is exactly `H=o(X)` at the Ford endpoint.

`NB-224` derives from Bellotti's Lemma 2.4 the general weighted population estimate

\[
C_t(K)
:=
\sum_{\substack{\rho:\ R(1-\beta)\le K}}
(1+H|\gamma-t|)^{-A}
\ll K+\frac RH,
\tag{8}
\]

valid in the local-disk range `1<=K<<L`. The extra `R/H` term is the number of Bellotti-scale vertical disks needed to cover one carrier window of width `1/H`. The construction below shows that this term is not an artifact of the covering argument.

## 2. A phase-aligned packet saturates the missing vertical population

Set

\[
J=\frac RH\longrightarrow\infty,
\qquad
M=\left\lfloor\min\{J^{1/2},L\}\right\rfloor.
\tag{9}
\]

Then `M->infinity`, `M<=L`, and `M/J->0`. Define the horizontal depth

\[
K=\frac{\log M}{Y}.
\tag{10}
\]

Thus

\[
K\longrightarrow\infty,
\qquad
K\ll\log L\ll L.
\tag{11}
\]

Choose a fixed positive integer `q`, large if necessary only to make the implied local-spacing constant harmless, and consider the simple zero packet

\[
\rho_j
=
1-\frac KR
+i\left(t+\frac{2\pi qj}{X}\right),
\qquad
1\le j\le M.
\tag{12}
\]

The ordinate spacing is a fixed multiple of `1/X`, hence also a fixed multiple of `1/R` because `X/R->Y_*`. More importantly,

\[
e^{iX(\gamma_j-t)}
=e^{2\pi i qj}
=1.
\tag{13}
\]

So the packet is not merely large in absolute residue mass: its moving-shell phases are exactly aligned.

At `rho_j`,

\[
X(\sigma_X-\beta_j)
=r+\frac{XK}{R}
=r+YK
=r+\log M.
\tag{14}
\]

Therefore

\[
e^{-X(\sigma_X-\beta_j)}
=\frac{e^{-r}}{M}.
\tag{15}
\]

The scaled argument of `F` tends uniformly to zero across the whole packet. Indeed,

\[
H|\gamma_j-t|
\le
\frac{2\pi qHM}{X}
=
\frac{2\pi q}{Y}\frac MJ
=o(1),
\tag{16}
\]

while

\[
H(\sigma_X-\beta_j)
=
\frac{r}{YJ}+\frac KJ
=o(1).
\tag{17}
\]

Hence

\[
F(Hv_{\rho_j})=F(0)+o(1)
\tag{18}
\]

uniformly in `j`. Combining (13)--(18),

\[
L_{X,H}(v_{\rho_j})
=
\frac{e^{-r}F(0)+o(1)}{M},
\tag{19}
\]

with the same asymptotic phase for every `j`. Consequently,

\[
\boxed{
\sum_{j=1}^{M}L_{X,H}(v_{\rho_j})
=e^{-r}F(0)+o(1).
}
\tag{20}
\]

Thus a packet whose cardinality tends to infinity can remain fully coherent after the shell smoothing and contribute a non-vanishing constant at exact Ford scale.

The choice `M<=J^(1/2)` is deliberately conservative. It makes the complete packet live deep inside one `1/H` carrier window and keeps both real and imaginary arguments of `F` in an `o(1)` neighborhood of the origin. No tail estimate or delicate profile optimization is involved.

## 3. The packet is compatible with every population input currently used at the endpoint

The point of (12) is not that it models the actual zeta zeros. It is that none of the population theorems used in `NB-223`--`NB-224` excludes it.

### Vinogradov--Korobov zero-free depth

The packet has

\[
R(1-\beta_j)=K\to\infty.
\tag{21}
\]

Hence it lies safely to the left of every fixed Vinogradov--Korobov zero-free boundary `A_0/R` for all sufficiently large `X`.

### Bellotti fixed-depth near-one count

Bellotti's fixed-`A` theorem counts zeros with

\[
R(1-\beta)\le A
\]

for a fixed `A`. Since `K->infinity`, the packet eventually contributes zero zeros to every such fixed-depth region.

### Bellotti growing near-one density

For every fixed `alpha>0`,

\[
K\ll\log L=o(L^\alpha),
\tag{22}
\]

while the packet has only

\[
M\le L
\tag{23}
\]

points. Bellotti's Theorem 1.1 permits, at depths bounded by `L^alpha`, a population of size

\[
\exp(BL^\alpha)\,O(L^\alpha),
\tag{24}
\]

which dominates `M`. If a tested horizontal threshold lies below `K`, the packet contributes no zeros at all. Hence the packet satisfies every fixed-`alpha<1` instance of that theorem asymptotically.

### Bellotti local disk count

A disk centered on the `1`-line with radius `K'/R` either misses the packet horizontally when `K'<K`, or intersects a vertical segment of length `O(K'/R)` when `K'>=K`. The packet spacing is

\[
\frac{2\pi q}{X}
\asymp_{Y_*,q}
\frac1R,
\tag{25}
\]

so such a disk contains at most `O_{Y_*,q}(K')` packet points. Taking `q` as a sufficiently large fixed integer makes this compatible with any fixed implied constant in the `O(K')` local-disk law. Thus the packet obeys the same local population scaling as Bellotti's Lemma 2.4 throughout its range `K'<<L`.

### Ordinary local zero counting

Finally,

\[
M\le L=o(Q),
\tag{26}
\]

so the packet is far smaller than the classical `O(Q)` allowance in a unit vertical interval. It can also be completed by conjugate and functional-equation-reflected partners without changing the local near-one carrier: the conjugates are remote from `+t`, while the reflected zeros are far from the `1`-line and acquire an exponentially small horizontal shell weight.

Therefore the packet is compatible, as an abstract spectral control, with all of the **population-only** information currently used by the endpoint route.

## 4. Linear width is the sharp threshold for this population-only mechanism

`NB-224` proves that when

\[
H=\theta X\asymp R
\tag{27}
\]

and the Ford constant is chosen small enough, Bellotti's local disk estimate gives a constant positive Euler gap. The packet above proves the complementary method boundary:

\[
\boxed{
H=o(R)
\quad\Longrightarrow\quad
\text{the same population hypotheses permit an order-one coherent residue packet.}
}
\tag{28}
\]

Since `R asymp X` at exact Ford scale, `H=Theta(X)` is therefore not merely a convenient width inside the `NB-224` argument. It is the sharp transition, up to constants, for what can be forced from the present combination of zero-free depth and zero-population bounds **without additional phase information**.

This conclusion is stronger than observing that the upper bound (8) contains `R/H`. A loose covering estimate might conceivably overcount incompatible local configurations. Equations (9)--(26) exhibit a configuration that simultaneously realizes the missing vertical capacity, stays inside every known population allowance, and aligns the actual moving-shell phase. The obstruction is therefore informational rather than a bookkeeping artifact.

A useful way to state the missing theorem is in terms of a genuinely joint local count. For a depth `K/R` and carrier width `1/H`, define schematically

\[
N_t(K;H)
=
\#\left\{
\rho:
R(1-\beta)\le K,
\ |\gamma-t|\lesssim\frac1H
\right\}.
\tag{29}
\]

Population control strong enough to beat the packet would have to exclude, at relevant moving depths, approximately

\[
N_t(K;H)\asymp e^{YK}
\tag{30}
\]

coherently placed zeros, or else supply cancellation among their carrier phases. Bellotti's separate global-density and local-disk estimates do neither in the coupled construction above.

## 5. What is and is not proved

Equation (28) is a **method no-go**, not a statement about the actual zeta zero set. The constructed packet need not be realizable as a local subset of the true zeta zeros, and no claim is made that zeta has such clustering. The result instead identifies exactly what the present theorems fail to rule out.

It also remains source-side. Even eliminating these packets for the actual zeta function would still not by itself yield a quantitative Nyman--Beurling distance theorem; the destination bridge isolated throughout the line remains separate. Positivity likewise remains relevant only when the small twisted barycenter is converted into the positive Euler-return defect.

The obstruction is representation-sensitive in a useful way. Generic local zero population is not enough because the shell reads both horizontal damping and vertical phase. The arithmetic/spectral advance needed next must therefore couple those two coordinates. Candidates include a stronger short-window near-one zero-density theorem, a pair-correlation/repulsion input strong enough in this near-one regime, or direct cancellation in the signed residue sum. Merely sharpening a global count while discarding the zero phases does not address the matched packet.

## 6. Adversarial checks and prior-art boundary

The packet depth was chosen to grow only like `log M`, and `M<=L`; this is essential. It evades every fixed-depth theorem while remaining tiny compared with the population allowed by Bellotti's growing-density theorem. The phase spacing is `Theta(1/X)=Theta(1/R)`, exactly the scale at which the local `O(K)` disk law permits `Theta(K)` points. The restriction `M<=J^(1/2)` prevents the carrier profile from seeing any nontrivial fraction of its own `1/H` window, so the coherent lower bound in (20) cannot be blamed on a poorly controlled Fourier tail.

A targeted prior-art audit covered Bellotti's near-one zero-density paper, standard smoothed explicit-formula treatments, and searches for local-zero-density/Fourier-window endpoint arguments. Bellotti's Lemma 2.4 is exactly the load-bearing local count; Theorems 1.1--1.2 provide the global population constraints checked above. The audit did not locate the specific matched-control deduction (28), nor the phase-aligned packet (12) showing that linear logarithmic width is sharp for this population-only Ford mechanism. No novelty is claimed for the zero-density theorems, the explicit formula, or Fourier smoothing themselves.

The modern source remains Chiara Bellotti, *A new zero-density estimate for zeta(s) and the error term in the Prime Number Theorem*, Bull. London Math. Soc. 58 (2026), e70442, DOI `10.1112/blms.70442`, arXiv:2508.02041. In particular, Lemma 2.4 proves the `O(K)` local disk count used in the compatibility test. The Vinogradov--Korobov zero-free region and ordinary local zero count are already anchored in `SOURCES.md`; no new external theorem is load-bearing here.

The representation audit separates the generic and zeta-specific claims. The matched packet argument applies to any meromorphic spectral model whose only near-edge information is a Ford-type zero-free strip plus Bellotti-type population upper bounds. Zeta enters because its logarithmic derivative supplies the residue carrier and because the current best near-one theorems have precisely those population forms. The conclusion is therefore not intrinsic Nyman geometry, but it is a source-specific boundary on the only arithmetic endpoint route presently surviving `NB-222`.

## Route consequence

`NB-224` left the minimal shell width as an optimization problem. `NB-225` resolves that question for the current **population-only** route: at exact Ford scale, `H=Theta(X)` is sharp up to constants. Any `H=o(X)` leaves enough unresolved vertical phase capacity to support an order-one Bellotti-compatible coherent packet.

The fixed/sublinear-width endpoint should therefore no longer be attacked by repackaging the same zero counts. A substantive continuation needs new phase-sensitive information about the actual zeta zeros, or a stronger joint depth-versus-window population theorem that rules out the packet geometry before absolute values are taken.