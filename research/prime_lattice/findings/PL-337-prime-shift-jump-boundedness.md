# PL-337 — Prime shifts are positive atomic jumps, giving uniform `L^infinity` across finite activation ranges

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-CLOSURE + ROUTE-ADVANCE`

**Status:** `COMPACT-APERTURE-LINFTY-BOUND + PRIME-ACTIVATION-LINFTY-GATES-CLOSED + FIRST-PRIME-REFLECTION-ORIENTED + NO-RH-CONSEQUENCE`

## Precise claim

Let `A_a` be Suzuki's fixed-domain localized completed-Weil operator on `I=(-1,1)` used in `PL-291` and `PL-336`. Fix any compact aperture interval

\[
J=[a_-,a_+]\subset(0,\infty)
\tag{PL337-1}
\]

and `M<infinity`. Then there is a constant `C=C(J,M)` such that every real normalized eigenpair

\[
A_a u=\lambda u,
\qquad
a\in J,
\qquad
\|u\|_2=1,
\qquad
|\lambda|\le M,
\tag{PL337-2}
\]

satisfies

\[
\boxed{\|u\|_{L^\infty(I)}\le C.}
\tag{PL337-3}
\]

The constant is uniform through every prime-power source activation contained in `J`, despite the operator-norm discontinuity of the corresponding compressed translations.

The mechanism is exact. For every prime power `n=p^k` with

\[
w_n=\frac{\Lambda(n)}{\sqrt n}>0,
\qquad
h_n(a)=\frac{\log n}{a},
\tag{PL337-4}
\]

let `S_h` denote the one-sided compressed translation on `I`. Suzuki's prime term is

\[
-w_n(S_h+S_h^*)
=w_nD_h-2w_nI,
\qquad
D_h:=2I-S_h-S_h^*.
\tag{PL337-5}
\]

For zero extension `Eu` outside `I`,

\[
\langle D_hu,v\rangle
=
\int_{\mathbb R}
(Eu(x+h)-Eu(x))(Ev(x+h)-Ev(x))\,dx.
\tag{PL337-6}
\]

Thus each rational-prime channel is a **positive atomic jump form plus a scalar compensation**. The scalar truncation `T_t(r)=(r-t)^+` obeys

\[
(r-s)(T_t(r)-T_t(s))
\ge |T_t(r)-T_t(s)|^2,
\tag{PL337-7}
\]

hence

\[
\boxed{
\langle D_hu,T_t(u)\rangle
\ge
\langle D_hT_t(u),T_t(u)\rangle
\ge0.
}
\tag{PL337-8}
\]

Jarohs--Kassmann--Weth prove an `L^infinity` a priori estimate for weak solutions of weakly singular nonlocal equations. The singular part of the one-dimensional logarithmic Laplacian lies in their infinite-jump-mass regime, where arbitrary bounded potentials are allowed. Their truncation proof remains valid after adding any finite positive combination of the atomic forms (PL337-6), because every extra term has the favorable sign (PL337-8). The non-singular logarithmic tail and Suzuki's continuous completion map normalized `L^2` states uniformly into `L^infinity` on a compact aperture interval. This proves (PL337-3).

For the actual simple normalized odd branch at the first source threshold

\[
a_0=\frac12\log2,
\qquad
a_\delta=a_0+\delta,
\]

(PL337-3) discharges the sole remaining hypothesis in `PL-336`. Consequently

\[
S_\delta=O(1),
\qquad
C_\delta\to C_0>0,
\]

and the sharp criterion of `PL-329` gives

\[
\frac{1+S_\delta}{|C_\delta|\sqrt{L_\delta}}
=O(L_\delta^{-1/2})\to0,
\qquad
L_\delta=\log\frac{a_\delta}{\delta}.
\tag{PL337-9}
\]

Therefore the newly active `p=2` reflected correlation of the actual odd branch has the favorable sign for every sufficiently small `delta>0`.

This is a regularity and local sign result, not an RH proof. It closes sup-norm concentration as an obstruction at **every finite prime-power activation on compact aperture ranges**, but later activations can still present independent correlation-sign and branch-ordering problems.

## 1. Every prime-power correlation is a positive jump plus a scalar

Suzuki's arithmetic contribution is a finite sum, at every fixed aperture, of correlations

\[
-2w_n C_{\log n}(u),
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n}>0,
\tag{PL337-10}
\]

supported on prime powers. After the standard unitary rescaling to `I`, the `n`-th contribution is the quadratic form of

\[
P_{n,a}=-w_n(S_{h_n(a)}+S_{h_n(a)}^*).
\tag{PL337-11}
\]

Expanding a translated difference gives

\[
\int_{\mathbb R}|Eu(x+h)-Eu(x)|^2\,dx
=2\|u\|_2^2-2\langle S_hu,u\rangle
=\langle D_hu,u\rangle,
\tag{PL337-12}
\]

and polarization yields (PL337-6). Formula (PL337-5) follows immediately.

This identity also handles source activation exactly. If `h>=2`, the translated copies of `I` have no positive-measure overlap, so `S_h=0` and `D_h=2I`. Therefore

\[
w_nD_h-2w_nI=0.
\tag{PL337-13}
\]

One may consequently include, throughout `J`, every prime power with `log n<=2a_+`; channels not yet active cancel identically as in (PL337-13). There are only finitely many such `n`. The entire prime comb on `J` can thus be written

\[
P_a
=
\sum_{\log n\le2a_+}w_nD_{h_n(a)}
-2\Bigl(\sum_{\log n\le2a_+}w_n\Bigr)I.
\tag{PL337-14}
\]

The first term is a finite positive Dirichlet-form sum and the second is a bounded scalar independent of the activation pattern. This is the structural reason that operator-norm jumps of individual compressed translations do not create an `L^infinity` blow-up mechanism.

The sign `w_n>0` is load-bearing. Reversing a correlation coefficient would replace `+w_nD_h` by a negative jump form and invalidate the truncation argument below.

## 2. The logarithmic principal part has an infinite-mass positive core

Chen--Weth's one-dimensional singular-integral representation, with Fourier symbol `2 log|xi|`, is

\[
L_\Delta u(x)
=
\int_{\mathbb R}
\frac{u(x)1_{\{|x-y|<1\}}-u(y)}{|x-y|}\,dy
+\rho_1u(x).
\tag{PL337-15}
\]

For zero-exterior `u` and `x in I`, write

\[
\frac12L_\Delta
=\mathscr L_0+B_\infty+c_0I,
\tag{PL337-16}
\]

where

\[
\mathscr L_0u(x)
=
\frac12\int_{|x-y|<1}
\frac{Eu(x)-Eu(y)}{|x-y|}\,dy
\tag{PL337-17}
\]

and

\[
B_\infty u(x)
=-\frac12\int_{|x-y|\ge1}
\frac{Eu(y)}{|x-y|}\,dy.
\tag{PL337-18}
\]

The far term satisfies

\[
\|B_\infty u\|_\infty
\le C_I\|u\|_2.
\tag{PL337-19}
\]

The governing density for the positive singular core is

\[
j_0(z)=\frac12\,1_{\{|z|<1\}}\frac1{|z|}.
\tag{PL337-20}
\]

It satisfies the weak-singularity integrability condition

\[
\int_{\mathbb R}\min\{1,|z|^\gamma\}j_0(z)\,dz<\infty
\quad(\gamma>0),
\tag{PL337-21}
\]

but has infinite total mass,

\[
\boxed{\int_{\mathbb R}j_0(z)\,dz=\infty.}
\tag{PL337-22}
\]

Jarohs--Kassmann--Weth, Theorem 1.3, therefore gives for the base equation

\[
\mathscr L_0u=Wu+f
\]

on the fixed bounded interval, with zero exterior data and bounded `W,f`, an estimate of the form

\[
\|u\|_\infty
\le C\bigl(\|f\|_\infty+\|u\|_2\bigr).
\tag{PL337-23}
\]

Their Remark 1.4 explicitly notes that the infinite-mass condition (PL337-22) permits arbitrary bounded potentials `W`.

## 3. The weakly singular truncation proof is stable under the atomic jumps

The published theorem is stated for measurable kernel densities. The compressed prime translations are atomic channels, so they are **not** claimed to be covered literally by that theorem. What transfers is its truncation proof.

Let `w_t=(u-t)^+`. Since `T_t` is monotone and `1`-Lipschitz, (PL337-7) implies (PL337-8). The same inequality applies to the negative truncation after replacing `u` by `-u`.

Suppose more generally that

\[
\left(\mathscr L_0+
\sum_{j=1}^N c_jD_{h_j}\right)u
=Wu+f,
\qquad c_j\ge0.
\tag{PL337-24}
\]

Testing weakly with `w_t` produces the Jarohs--Kassmann--Weth truncation identity for `\mathscr L_0` plus

\[
\sum_jc_j\langle D_{h_j}u,w_t\rangle\ge0.
\tag{PL337-25}
\]

Every lower estimate in their infinite-mass boundedness argument therefore survives unchanged: the added atomic contribution can simply be discarded from below. Repeating for `-u` yields

\[
\boxed{
\|u\|_\infty
\le C\bigl(\|f\|_\infty+\|u\|_2\bigr),
}
\tag{PL337-26}
\]

where `C` depends on the fixed singular kernel, the domain, and a bound for `W`, but not on the lags `h_j`. This lag-independence is precisely what is needed at source activations.

The extension (PL337-26) is elementary Dirichlet-form algebra, not a claimed new PDE theorem. The line-specific point is that the exact von-Mangoldt signs put every Suzuki prime-power channel on the favorable side of this inequality.

## 4. Uniform completed-Weil eigenstate bound on a compact aperture range

On `J`, combine `PL-291`, Suzuki's source formula, and (PL337-14) to write

\[
A_a
=
\mathscr L_0
+
\sum_{\log n\le2a_+}w_nD_{h_n(a)}
+
V_aI
+
B_\infty
+
R_a,
\tag{PL337-27}
\]

where `V_a` collects the scalar logarithmic, aperture, and jump-compensation terms, while `R_a` is the continuous archimedean completion operator. Since `J` is compact and the active source set is finite,

\[
\sup_{a\in J}|V_a|<\infty.
\tag{PL337-28}
\]

The completion kernel is uniformly bounded on the compact `(a,x,y)` range, so

\[
\boxed{
\sup_{a\in J}\|R_a\|_{L^2(I)\to L^\infty(I)}<\infty.
}
\tag{PL337-29}
\]

For an eigenpair (PL337-2), move only the scalar and smoothing terms to the right:

\[
\left(\mathscr L_0+
\sum_{\log n\le2a_+}w_nD_{h_n(a)}\right)u
=W_{a,\lambda}u+f_a,
\tag{PL337-30}
\]

with

\[
\sup_{a\in J,|\lambda|\le M}|W_{a,\lambda}|<\infty,
\tag{PL337-31}
\]

and

\[
f_a=-B_\infty u-R_au.
\tag{PL337-32}
\]

For normalized states, (PL337-19) and (PL337-29) give

\[
\boxed{
\sup_{a\in J}\|f_a\|_\infty<\infty.
}
\tag{PL337-33}
\]

By `PL-289`, completed-Weil eigenstates lie in the logarithmic graph domain and hence in the weak energy space of the singular form (PL337-17). Their zero extension gives exterior datum zero. Applying (PL337-26) to (PL337-30) proves (PL337-3).

No simplicity, parity, or ground-state property is used. Those enter only in downstream RH-facing branch arguments.

## 5. The first-prime conditional gate is now unconditional

`PL-336` reduced the entire first-prime continuation/sign problem for the simple odd branch to

\[
\sup_{0\le\delta\le\delta_0}\|u_\delta\|_\infty<\infty.
\tag{PL337-34}
\]

Norm-resolvent/simple-branch continuity from `PL-330` keeps `lambda_delta` in a compact set. Choose any compact `J` containing `a_0=(1/2)log2` and `a_0+delta_0`. Formula (PL337-3) proves (PL337-34).

The already audited chain in `PL-336` then gives

\[
S_\delta=O(1),
\qquad
|g_\delta(Q)-C_\delta Q^{-1/2}|
\le KQ^{-1}+Ke^{-\eta(Q-R)},
\tag{PL337-35}
\]

\[
C_\delta\to C_0>0.
\tag{PL337-36}
\]

Substitution into the sharp source threshold of `PL-329` yields (PL337-9), so the actual reflected overlap

\[
H_\delta(g_\delta)
=
\int_0^{2\delta}
g_\delta(t)g_\delta(2\delta-t)\,dt
\tag{PL337-37}
\]

satisfies

\[
\boxed{H_\delta(g_\delta)>0}
\tag{PL337-38}
\]

for every sufficiently small `delta>0`.

Thus the hostile half-log boundary layer of `PL-327` cannot occur on the actual branch: it requires source amplitude of order `sqrt(L_delta)`, whereas the exact eigen-equation now gives a uniformly bounded source.

## 6. Adversarial and novelty audit

**The weakly singular boundedness theorem is prior art.** Jarohs--Kassmann--Weth prove the `L^infinity` estimate for weak solutions and explicitly cover arbitrary bounded potentials in the infinite-mass case. Chen--Weth provide the exact logarithmic-Laplacian integral decomposition. No novelty is claimed for either theorem.

**The atomic extension is derived rather than attributed.** The published weakly singular theorem is density-kernel based. Equations (PL337-7)--(PL337-26) are the needed independent check that positive atomic translation channels preserve its truncation estimate.

**No contradiction with `PL-324`.** That finding concerns the folded odd-cone modulus `u -> sgn(x)|u(x)|`, whose Beurling--Deny inequality fails after the first prime event. The present proof uses the ordinary scalar truncation `u -> (u-t)^+` on the full interval. A symmetric prime correlation is a positive jump under this ordinary Markov contraction even though its cross-half folded contribution has the wrong sign for the odd cone.

**No contradiction with `PL-304`.** That result rules out generic `L^p`-to-`BV` and measure-to-`BV` resolvent smoothing. The present estimate gains no derivative or variation. It is a zero-order boundedness theorem for eigen-equations in which all nonsmoothing arithmetic translations remain on the positive Dirichlet-form side.

**The mechanism is not uniquely arithmetic.** Any finite family of symmetric negative-correlation shifts with positive coefficients has the same jump decomposition. The rational-prime content is that Suzuki's canonical coefficients are the positive von-Mangoldt weights and hence satisfy the required sign at every activation. This closes an arithmetic route gate; it does not establish arithmetic rigidity.

**No analytic-continuation shortcut is used.** The proof works entirely with Suzuki's localized Weil operator, the real-space logarithmic Laplacian, and weak-solution estimates. No Euler product is evaluated outside absolute convergence and no zero data are inserted by hand.

A targeted literature audit located no source stating this exact completed-Weil compact-aperture closure. Search absence is not treated as broad novelty. The durable contribution is the exact bridge from Suzuki's correlation signs to the weakly singular truncation estimate, plus the resulting discharge of `PL-336`.

## 7. Boundaries and failure modes

**Compact aperture only.** The theorem is uniform on each fixed `J subset (0,infinity)`. The scalar compensation contains a finite sum of active von-Mangoldt weights whose size grows with `a_+`; no aperture-uniform estimate as `a->infinity` is claimed.

**No global odd positivity theorem.** Sup-norm control across all finite activation ranges does not restore the odd-sector Beurling--Deny property after `a=(1/2)log2` and does not determine later signed reflected correlations.

**No simplicity theorem is added.** Boundedness holds for any normalized bounded-eigenvalue family. The first-prime sign consequence uses the simple odd branch already tracked in `PL-330`.

**No quantitative optimal constant.** The downstream first-prime gate only needs `S_delta=O(1)`, so the proof does not optimize the `L^infinity` constant.

**Later activations remain arithmetic sign problems, not regularity problems.** The same jump argument removes sup-norm concentration at every finite source activation, but correlations from several simultaneously active lags can interact. A separate mechanism is required to orient those signed terms or control the lowest odd branch globally.

**Coefficient signs are essential.** A negative jump weight would invalidate the monotone-truncation comparison. Any deformation control must preserve the sign, not merely the support geometry or translation lengths.

## Consequence for `prime_lattice`

The first-prime program no longer stops at the conditional `L^infinity` hypothesis of `PL-336`. More generally, **prime-source activation itself cannot cause normalized completed-Weil eigenstates with bounded eigenvalues to blow up in sup norm on any compact aperture interval**. The exact von-Mangoldt sign turns every moving compressed prime shift into a positive atomic jump plus a harmless scalar, and the infinite-mass logarithmic core supplies the required truncation coercivity.

Combining `PL-337` with `PL-329`, `PL-330`, `PL-332`, `PL-335`, and `PL-336` gives the unconditional local continuation statement (PL337-38). The next live obstacle is therefore not another regularity norm at `p=2`, nor sup-norm control at later source thresholds. It is to understand the **signed multi-prime correlation geometry** after successive activations and whether the source-selected orientation mechanism can propagate without relying on the odd-cone order structure already ruled out by `PL-324`.

## Dependencies and literature anchors

- `PL-291`: exact logarithmic principal operator, graph-domain control, and regular continuous completion on compact aperture intervals.
- `PL-304`: generic `L^p`/measure-to-`BV` no-smoothing control, delimiting what the present result does not imply.
- `PL-324`: exact positive von-Mangoldt correlation weights and the first odd-sector source threshold.
- `PL-329`: sharp source-amplitude criterion orienting the first reflected correlation.
- `PL-330`: norm-resolvent/simple-branch continuity and bounded branch eigenvalues.
- `PL-332`: transport of the source-selected boundary coefficient.
- `PL-335`: positive antisymmetric Hopf lower law at the threshold.
- `PL-336`: reduction of the complete first-prime sign gate to uniform branch `L^infinity` control.
- Source 56 in `research/prime_lattice/SOURCES.md`: Masatoshi Suzuki, *Weil's quadratic form via the screw function*.
- Source 96 in `research/prime_lattice/SOURCES.md`: Huyuan Chen and Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian*.
- Source 97 in `research/prime_lattice/SOURCES.md`: Víctor Hernández-Santamaría, Luis Fernando López Ríos, and Alberto Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*.
- Sven Jarohs, Moritz Kassmann, and Tobias Weth, *Continuity of solutions to equations with weakly singular nonlocal operators*, *Transactions of the American Mathematical Society* **379** (2026), 7097--7128, DOI `10.1090/tran/9675`, published electronically 2 July 2026; Theorem 1.3 and its infinite-mass truncation proof are the boundedness anchor used here.
