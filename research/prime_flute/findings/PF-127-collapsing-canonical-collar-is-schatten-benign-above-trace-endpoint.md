# PF-127 — the collapsing canonical collar is Schatten-benign above the trace endpoint

**Status:** `EXACT-DERIVED + BOUNDARY`. PF-060 identifies collapsing short collars as the main reason bounded-geometry localization theorems cannot be imported naively, while PF-112 shows that any non-isometric two-dimensional metric comparison is locally excluded from first-resolvent trace class. The present calculation isolates the corresponding **central hyperbolic collar channel** and shows that collapse itself does not create a stronger obstruction above the trace endpoint: after matching a short prime separator with its shift-clone separator, the transverse constant mode cancels exactly, and for every `r>1` the Dirichlet first-relative-resolvent on any fixed central collar lies in `S_r` with norm tending to zero as the core length pinches. This is a local/two-scale boundary result only; it does not prove the global prime/shift relative resolvent is in `S_r`.

## Claim

Fix `R>0`. For `L>0` with standard collar width `w(L)>R`, let

\[
C_{L,R}=(-R,R)\times \mathbb S^1,
\qquad
 ds_L^2=dr^2+L^2\cosh^2r\,d\theta^2,
\tag{1}
\]

with Dirichlet boundary at `r=+-R` and `theta in R/Z`. Let `L'>0` satisfy `w(L')>R` and

\[
t:=\log(L'/L),
\qquad |t|\le t_0
\tag{2}
\]

for a fixed bounded `t_0`. Use the constant density unitary to place both Dirichlet Laplacians on

\[
\mathcal H_R
=L^2((-R,R)\times\mathbb S^1,\cosh r\,dr\,d\theta),
\]

and write

\[
A_{L,L'}^{(R)}
:=
(\Delta_{L'}^D+1)^{-1}
-(\Delta_L^D+1)^{-1}.
\tag{3}
\]

Then for every `r0>1`,

\[
\boxed{
A_{L,L'}^{(R)}\in\mathcal S_{r0},
\qquad
\|A_{L,L'}^{(R)}\|_{\mathcal S_{r0}}^{r0}
\le
C_{R,r0,t_0}
|t|^{r0}L^{2r0-1}.
}
\tag{4}
\]

Equivalently,

\[
\boxed{
\|A_{L,L'}^{(R)}\|_{\mathcal S_{r0}}
\le
C_{R,r0,t_0}
|t|L^{2-1/r0}.
}
\tag{5}
\]

If `L' != L`, then nevertheless

\[
\boxed{A_{L,L'}^{(R)}\notin\mathcal S_1.}
\tag{6}
\]

Thus the isolated collapsing collar has the same sharp local ideal threshold as PF-112, but its `S_r`, `r>1`, mass is **suppressed**, not amplified, by pinching.

For a PF-004 canonical separator in the exact prime flute whose leftmost prime label is at least `P`, let `L` and `L_+` be the matched prime and exact all-composite shift-clone lengths. PF-109 gives

\[
\left|\log\frac{L_+}{L}\right|=O(P^{-3})
\tag{7}
\]

uniformly even when `L->0`. Hence on every fixed central collar,

\[
\boxed{
\|A_{L,L_+}^{(R)}\|_{\mathcal S_{r0}}
\le
C_{R,r0}P^{-3}L^{2-1/r0}
\longrightarrow0
}
\tag{8}
\]

along every canonical pinching sequence.

## 1. The collapsing mode cancels exactly

The nonnegative Laplacian for (1) is

\[
\Delta_L
=-\partial_r^2-\tanh r\,\partial_r
-\frac{1}{L^2\cosh^2r}\partial_\theta^2.
\tag{9}
\]

The Riemannian density is `L cosh(r) dr dtheta`; multiplying by the constant `L^{1/2}` identifies it unitarily with the common measure used above and leaves (9) unchanged.

Decompose into Fourier modes `exp(2 pi i m theta)`. The `m`-th radial operator is

\[
H_{m,L}
=H_0+
\frac{(2\pi m)^2}{L^2}\operatorname{sech}^2r,
\qquad
H_0=-\partial_r^2-\tanh r\,\partial_r,
\tag{10}
\]

with Dirichlet boundary at `+-R`.

For `m=0`, equation (10) is **independent of `L`**. Therefore

\[
\boxed{
(H_{0,L'}+1)^{-1}-(H_{0,L}+1)^{-1}=0.
}
\tag{11}
\]

This is the operator version of PF-060's fixed-energy collapse observation: the only transverse mode that survives as `L->0` does not remember the core length at all. Consequently the dangerous low-energy channel contributes exactly zero to the relative resolvent of two matched collars.

## 2. Nonzero transverse modes become cheaper as the collar pinches

Put

\[
c_R:=\operatorname{sech}^2R>0.
\]

For `m != 0`,

\[
H_{m,L}+1
\ge
H_0+1+c_R(2\pi m/L)^2.
\tag{12}
\]

After conjugating `H_0` by `(cosh r)^{1/2}`, it is a regular one-dimensional Dirichlet Schrödinger operator on the fixed interval `[-R,R]`. Hence its eigenvalues have the standard quadratic lower bound

\[
\lambda_k(H_0+1)\ge c'_R(1+k^2).
\tag{13}
\]

For any `s>1/2`, (12)--(13) and min-max therefore give

\[
\begin{aligned}
\|(H_{m,L}+1)^{-1}\|_{\mathcal S_s}^s
&\le
C_{R,s}
\sum_{k\ge1}
\left(k^2+(m/L)^2\right)^{-s}\\
&\le
C_{R,s}(L/|m|)^{2s-1}.
\end{aligned}
\tag{14}
\]

The change of the centrifugal potential is

\[
V_m
=(2\pi m)^2
\left(L^{-2}-L'^{-2}\right)
\operatorname{sech}^2r.
\tag{15}
\]

For `|t|<=t_0`,

\[
\|V_m\|_\infty
\le
C_{t_0}|t|(m/L)^2,
\qquad
\|(H_{m,L'}+1)^{-1}\|
\le
C_{R,t_0}(L/|m|)^2.
\tag{16}
\]

The resolvent identity gives

\[
A_m
=(H_{m,L'}+1)^{-1}
V_m
(H_{m,L}+1)^{-1}.
\tag{17}
\]

Using the two-sided ideal property with (14)--(16), for `r0>1`,

\[
\boxed{
\|A_m\|_{\mathcal S_{r0}}^{r0}
\le
C_{R,r0,t_0}|t|^{r0}
(L/|m|)^{2r0-1}.
}
\tag{18}
\]

The Fourier decomposition is orthogonal, so

\[
\|A_{L,L'}^{(R)}\|_{\mathcal S_{r0}}^{r0}
=
\sum_{m\in\mathbb Z}\|A_m\|_{\mathcal S_{r0}}^{r0}.
\tag{19}
\]

The `m=0` summand vanishes by (11), while

\[
\sum_{m\ne0}|m|^{1-2r0}<\infty
\quad\Longleftrightarrow\quad r0>1.
\tag{20}
\]

Equations (18)--(20) prove (4)--(5).

## 3. The trace endpoint remains impossible

The positive estimate above must not be extrapolated to `r0=1`. If `L' != L`, the two metric tensors in (1) differ on every interior open patch. A cutoff supported away from the Dirichlet boundary therefore sees exactly the PF-112 principal-symbol obstruction: the localized first relative resolvent is a classical order `-2` operator in dimension two with nonzero principal symbol, and its singular values have `c/j` asymptotics.

Thus (6) follows from the already-audited Birman--Solomyak/critical pseudodifferential input of PF-112. The divergence at `r0=1` in (20) is the separated-variable reflection of the same two-dimensional microlocal boundary.

The important distinction is quantitative. For every fixed `r0>1`, the right-hand side of (4) tends to zero with `L`; at `r0=1`, trace class fails for every nonzero metric change no matter how small `L` is.

## 4. Application to the exact prime/shift pinching channel

PF-060 showed that the prime flute contains collars with core length tending to zero and that such collapse destroys uniform local-volume/bounded-geometry hypotheses. That made collapsing necks a plausible place for the global `S_r`, `r>1`, conjecture in `CLUE-shift-clone-sharp-schatten-threshold.md` to fail.

PF-109 supplies the missing matched-control input. For every PF-004 canonical separator in a tail starting at `P`, the exact prime and shift-clone lengths satisfy the uniform logarithmic estimate (7). Inserting `t=log(L_+/L)` into (5) gives (8).

Therefore the canonical short-neck channel behaves in the **opposite** direction from a Schatten obstruction:

```text
pinching L -> 0
    -> m=0 collapse mode: exact relative cancellation
    -> m != 0 modes: energy ~ m^2/L^2
    -> relative S_r mass <= C |log(L_+/L)| L^(2-1/r)
    -> tends to zero for every r>1
```

This does not sum the entire surface and does not control the interfaces between collar and pant body. It does show that a counterexample to global `S_r` membership cannot consist merely of concentrating test functions in the **central canonical collapsing collars** and invoking the loss of injectivity radius.

## 5. Consequence for the accepted Schatten clue

The accepted clue had three broad possible sources of failure: cusps, zero-systole/collapsing regions, or infinite gluing. PF-125 already makes the two metrics exactly isometric sufficiently deep in every cusp. PF-127 now removes the pure central-collar collapse model as a second standalone obstruction.

The unresolved global gate is consequently narrower:

\[
\boxed{
\text{pant-body pieces}
+
\text{collar/body commutators and overlap}
+
\text{infinite summation}
\quad\Longrightarrow?\quad
\mathcal S_r,\ r>1.
}
\tag{21}
\]

A positive proof still needs a global decomposition or heat/pseudodifferential estimate whose constants survive the complete infinite-type geometry. A negative proof must exhibit a mechanism not present in the isolated collar model above -- for example a nonlocal interaction among many thin regions or an interface term whose singular values fail to inherit the `L^{2r-1}` suppression.

No determinant or RH conclusion follows. Even a future positive global classification would hold for the exact all-composite shift control and therefore cannot by itself be a primality selector.

## 6. Prior-art and novelty audit

No novelty is claimed for hyperbolic collar coordinates, Fourier decomposition, the one-dimensional Dirichlet eigenvalue estimate, the resolvent identity, or the critical local `S_1` obstruction. PF-060 already records the standard collar operator and collapse of nonzero transverse modes; PF-112 already anchors the order-`-2` singular-value boundary to classical Birman--Solomyak theory.

Directed searches around degenerating hyperbolic collars, resolvent Schatten classes, and spectral degeneration found the classical large literature on eigenvalue behavior under pinching (including Burger and later sharp collar-degeneration work), but no source that supplies the project-specific **relative** estimate (4) for matched core lengths or its composition with PF-109's all-composite control. The durable Mathia content is therefore the elementary but useful bridge

\[
\boxed{
\text{PF-109 multiplicative clone matching}
+
\text{exact collar Fourier model}
\Longrightarrow
\text{canonical collapse is }S_r\text{-benign for all }r>1.
}
\]

This is a boundary result for the ongoing global operator classification, not a new general theorem about degenerating hyperbolic surfaces.

## 7. Audit / falsification core

A later review can check the claim through the following finite chain:

1. verify the collar metric and Laplacian (1), (9), already used in PF-060;
2. remove the constant density factor `L` and decompose into Fourier modes to obtain (10);
3. check the exact `m=0` cancellation (11);
4. on the fixed interval use `sech^2 r >= sech^2 R` and the Dirichlet quadratic eigenvalue bound to obtain (14);
5. write the exact potential difference (15), use `L'/L=e^t`, and prove (16);
6. apply the resolvent identity and the Schatten ideal property to get (18);
7. sum the orthogonal Fourier blocks and note that `sum m^(1-2r0)` converges exactly for `r0>1`;
8. use PF-112, not the divergent upper estimate, for the rigorous non-`S_1` statement;
9. use PF-109 only at the final prime/shift specialization (7)--(8);
10. do not infer the global `S_r` class until collar/body gluing and the infinite decomposition are controlled.

A refutation would have to break the common-measure Fourier decomposition, the fixed-interval eigenvalue comparison, the Schatten block summation, or PF-109's uniform log-length bound. A failure of a later global decomposition would not refute PF-127; it would identify the remaining nonlocal/interface mechanism explicitly excluded by (21).
