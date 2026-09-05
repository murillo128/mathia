# AF-125 — Fiberwise adaptive resolution yields stratified entropy fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-INGREDIENTS`, `CATEGORY-INDEXED`, `MULTISCALE-FIDELITY`, `STRATIFIED-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-124 controls nonuniform recovery by replacing retained-state-dependent resolution depth with one high-probability scalar envelope. That is robust, but it can be pessimistic when the rough retained fibers are not the information-rich fibers.

The exact next refinement is to keep the resolution cost and the mark entropy coupled **before averaging over the retained state**.

Let `Y` be arbitrary retained side information taking values in a standard Borel space, let

\[
M\in[0,1)^r,
\qquad
D\in[0,1)^q,
\]

and assume exact recovery

\[
D=R(Y,M)
\qquad\text{almost surely}.
\tag{1}
\]

For dyadic depth `m>=0`, write

\[
Q_m(X):=\lfloor 2^mX\rfloor
\tag{2}
\]

coordinatewise. Choose regular conditional laws given `Y=y`, and define the fiberwise quantization entropies

\[
e_M(y,m):=H_2(Q_m(M)\mid Y=y),
\qquad
e_D(y,k):=H_2(Q_k(D)\mid Y=y).
\tag{3}
\]

For each target depth `k>=1`, suppose there is a measurable finite integer-valued fiber-resolution depth

\[
\Phi_k:Y\to\mathbb N
\tag{4}
\]

such that for almost every retained state `y`, whenever two marks in the relevant conditional support satisfy

\[
Q_{\Phi_k(y)}(m)=Q_{\Phi_k(y)}(m'),
\tag{5}
\]

then

\[
\|R_y(m)-R_y(m')\|_\infty\le 2^{-k},
\qquad
R_y(m):=R(y,m).
\tag{6}
\]

Then for almost every `y`,

\[
\boxed{
 e_D(y,k)
 \le
 \min\left\{
 qk,
 e_M\bigl(y,\Phi_k(y)\bigr)+q
 \right\}.
}
\tag{7}
\]

Consequently the global conditional quantization profile obeys

\[
\boxed{
E_D(k\mid Y)
\le
B_k
:=
\int
\min\left\{
qk,
 e_M\bigl(y,\Phi_k(y)\bigr)+q
\right\}
\,dP_Y(y).
}
\tag{8}
\]

The quantity `B_k` is a **stratified scale-fidelity budget**. Each retained fiber pays whichever is cheaper: the mark entropy at the resolution actually required by that fiber, or the trivial `qk`-bit target cap. No worst retained-fiber modulus and no common deterministic mark depth is imposed before averaging.

This strictly sharpens the form of AF-124. For every deterministic depth `m`, let

\[
\delta_{k,m}:=\Pr\{\Phi_k(Y)>m\}.
\tag{9}
\]

Then

\[
\boxed{
B_k
\le
E_M(m\mid Y)
+q
+qk\,\delta_{k,m},
}
\tag{10}
\]

so AF-124's profile inequality follows as a coarser envelope of `(8)`.

### Fiberwise asymptotic form

Define the fiberwise repair rate

\[
\rho_R(y)
:=
\limsup_{k\to\infty}
\frac{e_M(y,\Phi_k(y))}{k}
\tag{11}
\]

and the fiberwise upper information dimensions

\[
\overline d_M(y)
:=
\limsup_{m\to\infty}
\frac{e_M(y,m)}{m},
\qquad
\overline d_D(y)
:=
\limsup_{k\to\infty}
\frac{e_D(y,k)}{k}.
\tag{12}
\]

Then `(7)` gives

\[
\boxed{
\overline d_D(y)
\le
\min\{q,\rho_R(y)\}
}
\qquad\text{for almost every }y.
\tag{13}
\]

Since `0<=e_D(y,k)/k<=q`, reverse Fatou applied to the bounded sequence gives the global bound

\[
\boxed{
\overline d(D\mid Y)
\le
\int \min\{q,\rho_R(y)\}\,dP_Y(y).
}
\tag{14}
\]

If in addition the pointwise resolution exponent

\[
c(y):=\limsup_{k\to\infty}\frac{\Phi_k(y)}k
\tag{15}
\]

is finite, then

\[
\rho_R(y)
\le
c(y)\,\overline d_M(y),
\tag{16}
\]

and therefore

\[
\boxed{
\overline d(D\mid Y)
\le
\int
\min\{q,c(y)\overline d_M(y)\}
\,dP_Y(y).
}
\tag{17}
\]

Equation `(17)` is the coupling missing from the scalar `c_R` of AF-124: a fiber is expensive only when it simultaneously requires deep source resolution **and** carries fine-scale mark entropy.

## Derivation

### The entropy bound is fiberwise

Fix `k` and a retained state `y` for which `(1)` and `(6)` hold under the regular conditional law. Put

\[
m_y:=\Phi_k(y).
\tag{18}
\]

Inside one `Q_{m_y}(M)` cell, condition `(6)` says that the image of the conditional mark support under `R_y` has `\ell_\infty` diameter at most `2^{-k}`. Such a set intersects at most two depth-`k` dyadic intervals in each target coordinate, hence at most

\[
2^q
\tag{19}
\]

cells of `Q_k(D)`.

Therefore

\[
H_2(Q_k(D)\mid Y=y,Q_{m_y}(M))\le q.
\tag{20}
\]

The entropy chain rule yields

\[
\begin{aligned}
e_D(y,k)
&\le
H_2(Q_{m_y}(M),Q_k(D)\mid Y=y)\\
&=
e_M(y,m_y)
+H_2(Q_k(D)\mid Y=y,Q_{m_y}(M))\\
&\le
e_M(y,m_y)+q.
\end{aligned}
\tag{21}
\]

Independently, because `D\in[0,1)^q`, the variable `Q_k(D)` has at most `2^{qk}` labels, so

\[
e_D(y,k)\le qk.
\tag{22}
\]

Taking the better of `(21)` and `(22)` proves `(7)`. Integrating the regular conditional entropy identity

\[
H_2(Q_k(D)\mid Y)
=
\int e_D(y,k)\,dP_Y(y)
\tag{23}
\]

proves `(8)`.

Equivalently, the same bound can be realized by a retained-state-dependent keep-or-drop policy. On fibers where `e_M(y,\Phi_k(y))+q<=qk`, retain the adaptive mark label `Q_{\Phi_k(y)}(M)`; on the others use a fixed null symbol and pay the trivial target entropy. Because the decision is already a function of `Y`, it costs no additional selector bit after conditioning on `Y`.

### AF-124 is the common-depth relaxation

Fix a deterministic `m` and split the retained states into

\[
G_{k,m}:=\{y:\Phi_k(y)\le m\},
\qquad
B_{k,m}:=\{y:\Phi_k(y)>m\}.
\tag{24}
\]

On `G_{k,m}`, dyadic refinement monotonicity gives

\[
e_M(y,\Phi_k(y))\le e_M(y,m),
\tag{25}
\]

while on `B_{k,m}` the pointwise budget in `(8)` is at most `qk`. Hence

\[
\begin{aligned}
B_k
&\le
\int_{G_{k,m}}\bigl(e_M(y,m)+q\bigr)\,dP_Y(y)
+
qk\,P_Y(B_{k,m})\\
&\le
E_M(m\mid Y)
+q(1-\delta_{k,m})
+qk\delta_{k,m}\\
&\le
E_M(m\mid Y)+q+qk\delta_{k,m},
\end{aligned}
\tag{26}
\]

which is `(10)`.

Thus AF-124 is not wrong or obsolete. Its scalar high-probability envelope is the convenient bound obtained after discarding the correlation between local regularity and local information content. AF-125 records the exact place where that correlation lives.

### Pointwise resolution growth couples to pointwise information dimension

For fixed `y`, let

\[
c(y)=\limsup_k\frac{\Phi_k(y)}k<\infty.
\tag{27}
\]

If `c(y)=0`, boundedness

\[
e_M(y,m)\le rm
\tag{28}
\]

immediately gives `rho_R(y)=0`.

If `c(y)>0`, then for every `epsilon>0`, all sufficiently large mark depths satisfy

\[
e_M(y,m)
\le
\bigl(\overline d_M(y)+\epsilon\bigr)m.
\tag{29}
\]

Terms for which `\Phi_k(y)` remains below that finite threshold contribute `o(k)`, while the remaining terms obey `(29)`. Taking the limsup gives

\[
\rho_R(y)
\le
c(y)\bigl(\overline d_M(y)+\epsilon\bigr).
\tag{30}
\]

Letting `epsilon` tend to zero proves `(16)`.

Finally divide `(7)` by `k`. The normalized fiberwise target entropy is bounded by `q`, so reverse Fatou is available without any integrability assumption on `c(y)`. This gives `(14)` and then `(17)`.

## Strict finite-strata example

The scalar resolution exponent from AF-124 can lose a real factor even in a two-stratum model.

Let `Y` be Bernoulli with equal masses, and conditionally on either value let

\[
M\sim\operatorname{Unif}[0,1).
\tag{31}
\]

Take a two-coordinate target `D\in[0,1)^2`.

On the first stratum, define

\[
D=(M,0).
\tag{32}
\]

Then depth `k` in `M` resolves depth `k` in `D`, so one may take

\[
\Phi_k(0)=k,
\qquad
 e_M(0,\Phi_k(0))=k,
\qquad
 e_D(0,k)=k.
\tag{33}
\]

On the second stratum, use the standard measurable binary digit-splitting map: away from the null set of ambiguous dyadic expansions, the odd binary digits of `M` form the first target coordinate and the even binary digits form the second. The two coordinates are independent uniform random variables. To determine `k` target bits in both coordinates it is sufficient to know the first `2k` source bits, so

\[
\Phi_k(1)=2k,
\qquad
 e_M(1,\Phi_k(1))=2k,
\qquad
 e_D(1,k)=2k.
\tag{34}
\]

Therefore

\[
\overline d(D\mid Y)
=
\frac12\cdot1+
\frac12\cdot2
=
\frac32.
\tag{35}
\]

AF-124 sees a positive-probability stratum with scale exponent `2`, so its scalar probabilistic limsup is

\[
c_R=2,
\tag{36}
\]

while

\[
\overline d(M\mid Y)=1.
\tag{37}
\]

Its dimension bound is therefore only `2`. In contrast, `(17)` gives

\[
\frac12\min\{2,1\cdot1\}
+
\frac12\min\{2,2\cdot1\}
=
\frac32,
\tag{38}
\]

which is exact.

The improvement is not produced by another global statistic. It comes solely from refusing to separate retained-state-dependent resolution cost from retained-state-dependent information content before averaging.

## Sharpness and falsification controls

### The fiber-resolution certificate must be independently justified

As in AF-124, `\Phi_k` is category data, not a free optimization variable. Inflating it only weakens `(8)`. A meaningful application must derive the depth from a decoder, metric, filtration, symbolic locality rule, boundary/transverse representation, or another independently admissible structure.

If a canonical minimal depth exists, it gives the strongest version of the theorem, but minimality is not required for validity.

### Finite fiber depth is a real hypothesis

AF-125 requires `\Phi_k(y)<\infty` almost surely at each target scale so that an adaptive mark cell is defined fiberwise. If a positive-measure set of fibers has no finite resolution certificate, the adaptive formula does not silently assign those fibers infinite entropy. AF-124's deterministic truncation method remains useful in settings where one wants to tolerate unresolved exceptional fibers directly.

### The result is conditional-measure theory, not an operational coding theorem

The entropies in `(3)` are conditional partition entropies under regular conditional laws. Equation `(8)` does not claim an optimal prefix code, a Wyner--Ziv rate, or a rate-distortion theorem. The keep-or-drop interpretation is only a convenient realization of the entropy inequality once `Y` is already conditioned upon.

### Quantization geometry remains part of the category

Changing coordinates, source metrics, or the refinement filtration can change `\Phi_k` and the local entropy profiles. The result is invariant only after the quantization/refinement category has been declared. An arbitrary reparameterization cannot be used to make a costly decoder appear faithful for free.

### The additive `q` is a boundary-cell constant

The term `q` comes from the fact that a target set of `\ell_\infty` diameter one cell width can cross at most two dyadic cells per coordinate. It is deliberately not optimized. It vanishes after normalization and is irrelevant to the information-dimension conclusion.

### The local profile is stronger than the local slope

Two fibers can have the same `c(y)` and the same information dimension while having very different finite-scale entropy profiles. Equation `(8)`, not `(17)`, is the primary statement. The dimension integral is a first-order corollary and should not replace the full stratified profile when finite-scale distinctions matter.

## Prior-art audit

All mathematical ingredients are classical, and **no standalone novelty claim is made for `(7)`--`(17)`**.

- Alfréd Rényi, **“On the Dimension and Entropy of Probability Distributions,”** *Acta Mathematica Academiae Scientiarum Hungaricae* 10, 193–215 (1959). Role: foundational quantization-entropy definition of information dimension.
- Robert M. Gray and David L. Neuhoff, **“Quantization,”** *IEEE Transactions on Information Theory* 44(6), 2325–2383 (1998), DOI `10.1109/18.720541`. Role: authoritative survey of scalar/vector, fixed/variable-rate, and high-resolution quantization; establishes that adapting quantization resolution and accounting for entropy rather than only cell count are classical concerns.
- Yihong Wu and Sergio Verdú, **“Rényi Information Dimension: Fundamental Limits of Almost Lossless Analog Compression,”** *IEEE Transactions on Information Theory* 56(8), 3721–3748 (2010), DOI `10.1109/TIT.2010.2050803`. Role: direct prior art for information dimension as a fine-scale compression resource and for regularity constraints on decompression.
- Te Sun Han, ***Information-Spectrum Methods in Information Theory***, Springer, Stochastic Modelling and Applied Probability 50 (2003), DOI `10.1007/978-3-662-12066-8`. Role: established asymptotic language for nonuniform sources and probabilistic limsup/liminf quantities rather than uniform or mean-only control.
- Olav Kallenberg, ***Foundations of Modern Probability***, 3rd ed., Springer (2021), DOI `10.1007/978-3-030-61871-1`. Role: standard-Borel regular conditional distributions and conditional probability/entropy framework underlying the fiberwise disintegration.

Targeted searches for random-depth, variable-resolution, adaptive-quantization, conditional-entropy, and information-dimension formulations found the classical quantization and information-spectrum frameworks above, but did not identify `(8)` as a standard named theorem. That absence is not evidence of novelty. Once the retained-state-dependent depth is made explicit, the proof is an elementary conditional-entropy argument plus dyadic cell geometry.

The durable contribution for Arithmetic Fidelity is the exact **organization of the loss budget**: regularity and information content must be coupled on the same retained fiber before averaging. AF-124 had already identified this as the unresolved stratified level; AF-125 closes that level with a pointwise profile bound and shows precisely how the scalar high-probability envelope arises by relaxation.

## Consequences for Arithmetic Fidelity

AF-124's scalar resolution exponent is no longer the end of the multiscale audit. A proposed retained structure `Y` can contain fibers with very different reconstruction geometry, and those fibers should not be charged the same information rate merely because one class is rough.

The correct first question is now fiberwise:

> at target scale `2^{-k}`, how much conditional mark entropy is actually present at the source depth required by this retained state?

Only after answering that question should the costs be averaged. Rare or geometrically rough fibers can be harmless when they carry little fine-scale mark information, while a modest resolution exponent can still be expensive on information-rich fibers.

For later arithmetic applications this is directly usable. If a prime-specific residual is stored in boundary, transverse, marked, spectral, or other retained data whose reconstruction regularity varies across the retained state, a global worst-case modulus can falsely suggest that the lift is prohibitively expensive. Conversely, averaging the entropy first can hide a small but information-dense stratum where the rational-prime discriminator still requires substantial side information. Equation `(8)` forces both quantities to be audited at the same information layer.

The next unresolved question is no longer merely how to average heterogeneous fibers. It is whether natural arithmetic compressions supply an **intrinsic retained-state stratification and resolution certificate** for a prime-specific discriminator, rather than one chosen after the fact to make the entropy budget favorable.