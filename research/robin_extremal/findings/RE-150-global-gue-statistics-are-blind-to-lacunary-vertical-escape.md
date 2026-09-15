# RE-150 — global GUE statistics are blind to lacunary vertical reciprocal escape

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + RIEMANN-VON-MANGOLDT-COMPATIBLE + GLOBAL-CORRELATION-BLINDNESS + PURE-VERTICAL-ESCAPE + DECISIVE-NEGATIVE + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-149` shows that a strict-subedge Robin atom can be hidden by a product packet lying on exactly one vertical line. That construction deliberately leaves source-specific vertical laws open, including local zero statistics or correlation information. The first natural candidate is the GUE/pair-correlation hierarchy for zeta ordinates.

Global averaged correlation laws are not enough. The `RE-149` packets can be made so lacunary and so small in cardinality relative to their height that they are invisible to every fixed-order random-translation correlation statistic, while their internal phase geometry still hides the scale-maximal Robin atom. The same choice can keep their total contribution inside the classical `O(log T)` remainder allowed by Riemann--von Mangoldt.

Thus even a full fixed-order GUE hierarchy for the ordinates, interpreted in its standard globally averaged sense, does not supply the source-specific vertical control needed after `RE-149`. What is required is local-uniform or target-conditioned information capable of seeing exceptional windows of zero asymptotic sampling density.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad A>0,
\qquad 0<\kappa<\frac12.
\tag{1}
\]

Let `B` be any conjugation-symmetric background spectrum supported on the critical line `Re rho=1/2`, with positive-ordinate counting function satisfying

\[
N_B(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+O(\log T),
\tag{2}
\]

and the local consequence

\[
N_B(t+1)-N_B(t-1)\ll\log(2+t).
\tag{3}
\]

For fixed `k>=1`, put

\[
L_T:=\frac{\log T}{2\pi}
\tag{4}
\]

and for `f in C_c(R^k)` define the random-translation correlation statistic

\[
\mathcal C_{k,T}^{B}(f)
:=
\frac1T
\int_T^{2T}
\sum_{(\tau_1,\ldots,\tau_k)\in B_*^k}
 f\!\left(
 L_T(\tau_1-t),\ldots,L_T(\tau_k-t)
 \right)
\,dt,
\tag{5}
\]

where `B_*^k` denotes ordered tuples of distinct indexed zeros; multiplicities, if present, are treated as distinct indices.

There is a refinement of the `RE-149` construction producing a formal finite-edge spectrum `Z_ctl` such that:

1. its strict-subedge right-half-strip Robin packet still satisfies the pure-vertical hiding conclusion of `RE-149` along phases `U_j->infinity`;
2. after adjoining the background `B`, the total positive-ordinate count still satisfies (2), with only a changed `O(log T)` constant;
3. the augmented local unit count still satisfies (3);
4. for every fixed `k` and every `f in C_c(R^k)`,

\[
\boxed{
\mathcal C_{k,T}^{B\cup Z_{\rm ctl}}(f)
-
\mathcal C_{k,T}^{B}(f)
\longrightarrow0.
}
\tag{6}
\]

Consequently every fixed-order global GUE correlation limit enjoyed by `B` is inherited by the augmented spectrum. The obstruction is not a failure of ordinary one-level density or of globally averaged local statistics; it is concentration in a lacunary sequence of exceptional target windows.

## 1. The RE-149 packet can fit inside the Riemann--von Mangoldt error budget

Use the stage geometry of `RE-149`. At stage `j` there are `2^j` right-half-strip atoms

\[
\rho_{j,S}
=
\beta_j+i\gamma_{j,S},
\qquad
S\subset\{1,\ldots,j\},
\tag{7}
\]

with

\[
\beta_j=\Theta-U_j^{-2},
\qquad
\Gamma_j=U_j^{A/2},
\qquad
\gamma_{j,S}
=
\Gamma_j+
\frac1{U_j}
\sum_{\ell\in S}\omega_{j,\ell}.
\tag{8}
\]

Closing under `rho -> 1-rho` doubles the positive-ordinate stage cardinality, so write

\[
m_j:=2^{j+1}.
\tag{9}
\]

The recursive freedom in `U_j` used by `RE-149` allows us to impose, in addition to all of its tail and hiding requirements,

\[
\Gamma_{j+1}\ge4\Gamma_j,
\qquad
m_j\le \log\Gamma_j,
\qquad
\frac{j\log\Gamma_j}{U_j}\longrightarrow0.
\tag{10}
\]

There is no conflict with `Gamma_j=U_j^(A/2)`: enlarge `U_j` until all three conditions and the original stage conditions hold. Likewise the requirement that a prescribed scaled-radius envelope `W(U)` satisfy `W(U_j)>=j(1+omega_kappa)` remains compatible because `W(U)->infinity`.

The cumulative number of inserted positive-ordinate points below the `j`th stage is geometric:

\[
M_j:=\sum_{n\le j}m_n\ll 2^j\ll\log\Gamma_j.
\tag{11}
\]

If `T` lies between successive stage heights, monotonicity and lacunarity give

\[
M(T):=\#\{\rho\in Z_{\rm ctl}:0<\Im\rho\le T\}
\ll\log T.
\tag{12}
\]

A fixed attained-edge quartet contributes only `O(1)`. Hence adjoining all control points to a background satisfying (2) changes its counting function by at most `O(log T)`. In particular, the classical Riemann--von Mangoldt main term and remainder scale survive unchanged in order.

The whole `j`th packet has absolute vertical diameter

\[
\Delta_j
\ll_\kappa \frac{j}{U_j}.
\tag{13}
\]

By (10), `Delta_j=o(1/log Gamma_j)`. Since `m_j<=log Gamma_j`, inserting a stage into one unit ordinate interval changes its occupancy by only `O(log Gamma_j)`. Thus the local unit bound (3) also survives.

This already sharpens the one-level boundary of `RE-149`: its vertical escape can coexist not merely with an arbitrarily sparse off-critical count, but with a dense critical-line background having the full zeta-scale counting law.

## 2. Fixed-order global correlations cannot see the packet

Fix `k` and `f in C_c(R^k)`. Choose `K>0` such that

\[
\operatorname{supp}f\subset[-K,K]^k.
\tag{14}
\]

Because of `Gamma_(j+1)>=4 Gamma_j`, any dyadic observation interval `[T,2T]`, enlarged by `O(1/log T)` at its endpoints, meets at most one sufficiently high control stage.

Suppose it meets stage `j`. A tuple involving any inserted point contributes to the difference in (6) only when the translation parameter `t` lies within `K/L_T` of that stage. Therefore all such `t` lie in a set `E_{j,T}` of length

\[
|E_{j,T}|
\le
\Delta_j+
\frac{2K}{L_T}
\ll_{K}\frac1{\log T},
\tag{15}
\]

where (13) and the third condition in (10) were used.

For `t in E_(j,T)`, every zero that can occur in a tuple tested by `f` lies in an interval of absolute length `O_K(1/log T)`, hence inside a unit interval for large `T`. Equations (3), (9), and (10) give the uniform occupancy bound

\[
\#\{\hbox{visible indexed points near }t\}
\ll_{K}\log T.
\tag{16}
\]

The absolute difference between the two `k`-tuple sums is therefore at most

\[
O_{f,k}((\log T)^k).
\tag{17}
\]

Integrating only over the exceptional translation set (15) and dividing by `T` yields

\[
\left|
\mathcal C_{k,T}^{B\cup Z_{\rm ctl}}(f)
-
\mathcal C_{k,T}^{B}(f)
\right|
\ll_{f,k}
\frac{(\log T)^{k-1}}{T}
=o(1).
\tag{18}
\]

If no stage meets the enlarged dyadic window, only finitely many old control points can contribute and the same conclusion is easier. This proves (6).

The estimate also survives coincident ordinates created by functional-equation reflection: the two complex zeros are distinct points of the spectrum but may have the same imaginary part. They merely increase the local indexed occupancy by the factor already included in `m_j`.

## 3. Distributional GUE and fixed local moments are equally blind

The blindness is not specific to the correlation functional (5). For a fixed bounded rescaled window, the augmented and background local point configurations differ only when the randomly translated center `t in [T,2T]` lands in a set of measure `O(1/log T)`. Hence the probability of even seeing the exceptional stage is

\[
O\!\left(\frac1{T\log T}\right).
\tag{19}
\]

So any bounded local observable has the same random-translation limiting distribution before and after the graft.

Unbounded fixed moments of local counts remain stable as well. For every fixed `q`, the exceptional window has local occupancy `O(log T)`, and therefore its contribution to the averaged `q`th moment is at most

\[
\frac1T
O\!\left(\frac1{\log T}\right)
O((\log T)^q)
=
O\!\left(\frac{(\log T)^{q-1}}{T}\right)
=o(1).
\tag{20}
\]

Thus strengthening pair correlation to the entire hierarchy of fixed-order random-translation correlations, local-count distributions, or fixed local moments does not price these lacunary target windows. The packet can be arbitrarily pathological conditional on landing at `Gamma_j` while remaining invisible when the observation center is sampled globally.

This is exactly the local-versus-global information loss relevant to `RE-149`: Robin selects the exceptional phase `U_j` and its associated target zero; a GUE statistic samples a typical ordinate location.

## 4. The Robin obstruction survives the dense background

The strict-subedge packet in `RE-149` is taken in the right-half strip `Re rho>=sigma_0>1/2`. The critical-line background therefore contributes no atom to that packet. Its scale-maximal anchor, zero-horizontal-spread product factorization, and exponential hiding estimate are unchanged.

Even if one enlarges the leading coefficient sum to include the background, the background is harmless at the `RE-149` phases. From (2), partial summation gives

\[
\sum_{\tau\in B,\ \tau>0}
\frac1{1+\tau^2}<\infty.
\tag{21}
\]

Every background point has horizontal deficit `Theta-1/2`, so uniformly on the fixed-relative stage window

\[
\sum_{\rho\in B}
|a_{\rho,0}(u)|
\ll
\exp[-(\Theta-1/2)(1-\kappa)U_j]
=o(U_j^{-A}).
\tag{22}
\]

Thus densifying the spectrum to zeta-scale one-level statistics does not purchase cancellation resistance at the active off-critical edge. The only potentially relevant source information must discriminate the exceptional vertical arrangement itself.

## 5. Prior-art boundary

Montgomery's pair-correlation framework and the Rudnick--Sarnak `n`-level program are classical globally averaged statistics. A recent clarification particularly close to the present distinction is Juan Arias de Reyna and Brad Rodgers, *On convergence of points to limiting processes, with an application to zeta zeros* (arXiv:2311.13441): their standard GUE formulation samples a translation center uniformly from a macroscopic interval and tests compactly supported local configurations, and they relate correlation, distributional, and spacing formulations under the usual zeta regularity inputs.

The general fact that a zero-density set of exceptional sampling locations can disappear from an averaged limiting statistic is not claimed as new. The line-specific result here is the exact compatibility with the `RE-149` Robin obstruction: the same lacunary stages can simultaneously retain the pure-vertical product cancellation, fit inside an `O(log T)` Riemann--von Mangoldt perturbation budget, preserve local `O(log T)` occupancy, and contribute `o(1)` to every fixed-order global correlation statistic.

No external correlation theorem is load-bearing in the proof: equations (15)--(20) directly estimate the perturbation. The literature audit therefore bounds the novelty claim but does not add a new theorem dependency to `SOURCES.md`.

## 6. Boundary and research effect

This is still a matched-control statement. It does **not** assert that actual zeta zeros realize the vertical subset-product packets, nor that GUE is proved for zeta in the full form used above. It does not preserve an Euler product, a zeta explicit formula, determinant identities tied to the actual zero set, or a local law uniform in the observation center.

Those exclusions are the point. `RE-149` left a generic "correlation theorem" among the possible source-specific ways to control vertical escape. The present result separates two meanings of correlation. A theorem averaged over ordinate centers, even through every fixed order, cannot exclude a lacunary sequence of exceptional Robin-selected windows. To close this channel one needs information with a uniform or conditioned quantifier, for example a bound valid around **every** sufficiently high off-critical target, a large-deviation estimate strong enough to exclude all exceptional centers rather than almost all centers, or an explicit-formula/Euler-product coupling that directly penalizes the required phase packet.

Therefore the next vertical target should not be another global pair-correlation or GUE asymptotic. It must control the target-conditioned local configuration

\[
\{\rho:
|\Re\rho-\beta_0|\ll U^{-1},
\quad
|\Im\rho-\gamma_0|\lesssim R(U)/U
\}
\tag{23}
\]

with a quantifier strong enough to survive selection of the exceptional scale-maximal atom. Global typical-zero statistics do not supply that quantifier.