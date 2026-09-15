# PL-318 — Bounded logarithmic forcing still permits the moving-diagonal obstruction

**Evidence:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE/SOURCE-GATE-NARROWING`

**Status:** `BOUNDED-LOG-POISSON-SOURCE-INSUFFICIENT + STATE-SOURCE-COUPLING-STILL-OPEN`

## Precise claim

`PL-314`--`PL-317` isolate the endpoint condition needed to pass from the finite-order Green problem to the rank-one corner law. In the logarithmic coordinate

\[
Q=-\log\frac{1-x}{2},
\]

the sufficient condition is `Qm(Q)->0`; weighted `L^1`, all logarithmic Fourier moments, every subcritical Sobolev exponent, and even the critical zero-extension space `H^{1/2}` are not enough, whereas any fixed supercritical zero-extension gain is sufficient.

A natural remaining shortcut is to use the **zero-order equation itself**: perhaps being a genuine Dirichlet solution of the logarithmic Laplacian with bounded forcing rules out the sparse `1/Q` saturation used in `PL-314`--`PL-316`. It does not.

Fix an outer point `r>0`. There exists a nonnegative endpoint profile `u`, supported near the right endpoint of `I=(-1,1)` and extended by zero to `R`, such that

\[
\boxed{L_\Delta u\in L^\infty(I),}
\tag{PL318-1}
\]

while, writing

\[
u(1-2e^{-Q})=m(Q),
\]

one has

\[
\boxed{
m\in L^1(0,\infty),\qquad
m(Q)=O(Q^{-1}),\qquad
\limsup_{Q\to\infty}Qm(Q)>0.
}
\tag{PL318-2}
\]

Moreover the same fixed `m` can be chosen so that along a sequence `s_n downarrow 0`, the normalized Green transfer of `PL-314`,

\[
\mathcal A_s[m](r)
=\frac1s\int_0^\infty m(q/s)\,d\mu_{s,r}(q),
\tag{PL318-3}
\]

stays a fixed positive distance from the rank-one candidate

\[
e^{-r}\int_0^\infty m(Q)\,dQ.
\tag{PL318-4}
\]

Thus **bounded logarithmic-Poisson forcing does not imply the moving-tail suppression needed by `PL-314`**. The remaining completed-Weil route must use the special state-source relation in its eigen-equation, not merely boundedness of the zero-order right-hand side or the standard boundary regularity theory for `L_\Delta`.

The construction can be multiplied by an arbitrarily small positive scalar. Hence there is no norm-small bounded-source version of the missing qualitative implication either.

## 1. Sparse `1/Q` profile synchronized with the Green diagonal

Let `mu_{s,r}` be the positive stretched Green measure of `PL-310`, so

\[
\mu_{s,r}\Longrightarrow
\mu_r
=e^{-r-q}\mathbf 1_{0<q<r}\,dq+e^{-2r}\delta_r.
\tag{PL318-5}
\]

Choose

\[
\chi\in C_c^\infty((-1,1)),
\qquad 0\le\chi\le1,
\qquad \chi=1\text{ on }[-1/2,1/2].
\]

Fix `kappa>0`. Choose numbers `epsilon_n in (0,1/4)` with

\[
\sum_n\epsilon_n<\infty
\tag{PL318-6}
\]

and total sum as small as required below. We recursively choose `Q_n to infinity` so rapidly that

\[
\sum_n\frac1{Q_n}<\infty,
\qquad
\inf_n \epsilon_nQ_n^2>0,
\tag{PL318-7}
\]

the intervals

\[
J_n=[Q_n(1-\epsilon_n),Q_n(1+\epsilon_n)]
\tag{PL318-8}
\]

are pairwise disjoint, and, with

\[
s_n=\frac r{Q_n},
\tag{PL318-9}
\]

one has

\[
\boxed{
\mu_{s_n,r}
\bigl((r-r\epsilon_n/2,r+r\epsilon_n/2)\bigr)
\ge\frac34e^{-2r}.
}
\tag{PL318-10}
\]

This selection is legitimate. For each fixed `epsilon_n`, the open interval in (PL318-10) contains the atom at `r`; the Portmanteau theorem applied to (PL318-5) therefore gives the lower bound for all sufficiently small `s`. We then choose `Q_n=r/s_n` large enough to satisfy that threshold together with the separation and summability requirements.

Set

\[
W_n=\epsilon_nQ_n,
\qquad
m_n(Q)=\frac{\kappa}{Q_n}
\chi\!\left(\frac{Q-Q_n}{W_n}\right),
\qquad
m(Q)=\sum_nm_n(Q).
\tag{PL318-11}
\]

Because the supports are disjoint,

\[
\int_0^\infty m(Q)\,dQ
=\kappa\|\chi\|_{L^1}\sum_n\epsilon_n<\infty.
\tag{PL318-12}
\]

On `J_n`, `Q/Q_n<=1+epsilon_n`, so

\[
\sup_Q Qm(Q)\le\frac54\kappa\|\chi\|_\infty,
\tag{PL318-13}
\]

whereas at each center

\[
\boxed{Q_nm(Q_n)=\kappa.}
\tag{PL318-14}
\]

This proves (PL318-2): the profile obeys the natural critical envelope `O(1/Q)` but not the little-`o` tail needed in `PL-314`.

## 2. The physical profile has bounded logarithmic Laplacian

Write the physical distance from the right endpoint as

\[
\delta=1-x,
\qquad
Q(\delta)=\log\frac2\delta,
\]

and define, after taking `Q_1` large enough that the support lies in `0<delta<1/8`,

\[
g(\delta)=m(Q(\delta))
\quad(\delta>0),
\qquad
g(\delta)=0\quad(\delta\le0),
\tag{PL318-15}
\]

with `g=0` also away from the displayed endpoint support. Put `u(x)=g(1-x)`.

Three elementary quantities control the singular integral. First,

\[
M_0:=\sup_{0<\delta<1/8}
\log(2/\delta)|g(\delta)|<\infty
\tag{PL318-16}
\]

by (PL318-13). Second, on the `n`-th bump,

\[
\delta|g'(\delta)|
=|m'(Q)|
\le
\frac{\kappa\|\chi'\|_\infty}
{Q_nW_n}
=
\frac{\kappa\|\chi'\|_\infty}
{\epsilon_nQ_n^2},
\]

so (PL318-7) gives

\[
M_1:=\sup_{\delta>0}\delta|g'(\delta)|<\infty.
\tag{PL318-17}
\]

Third, the logarithmic Jacobian gives the exact identity

\[
L:=\int_0^{1/8}\frac{|g(z)|}{z}\,dz
=\int_{\log16}^{\infty}|m(Q)|\,dQ<\infty.
\tag{PL318-18}
\]

These three bounds imply a uniform Dini estimate. For `0<delta<1/8`, split

\[
D_g(\delta)
:=\int_{|h|<1}
\frac{|g(\delta+h)-g(\delta)|}{|h|}\,dh
\tag{PL318-19}
\]

at `|h|=delta/2`. On `|h|<delta/2`, the mean-value theorem and (PL318-17), with `delta+h` comparable to `delta`, give a bound `C M_1`. On `delta/2<=|h|<1`, the `g(delta)` contribution is at most

\[
C|g(\delta)|\log(2/\delta)\le C M_0.
\]

For the shifted term put `z=delta+h`. When `z<=delta/2`, `|z-delta|>=delta/2` and `2/delta<=1/z`; when `z>=3delta/2`, `|z-delta|>= z/3`. Since `g=0` for `z<=0`, these two regions contribute at most `C L`. Hence

\[
\boxed{
\sup_{0<\delta<1/8}D_g(\delta)
\le C(M_0+M_1+L)<\infty.
}
\tag{PL318-20}
\]

Points with `delta>=1/8` are separated from the endpoint support after increasing `Q_1` if necessary, so their local singular integrals are uniformly bounded as well.

Chen--Weth's one-dimensional integral representation is

\[
L_\Delta g(\delta)
=c_1\int_{\mathbb R}
\frac{g(\delta)\mathbf1_{|h|<1}-g(\delta+h)}{|h|}\,dh
+\rho_1g(\delta).
\tag{PL318-21}
\]

The local part is absolutely bounded by (PL318-20); the `|h|>=1` part is bounded by `\|g\|_{L^1}`, and the scalar term is bounded. Therefore

\[
\boxed{\|L_\Delta u\|_{L^\infty(I)}<\infty.}
\tag{PL318-22}
\]

The same construction also lies in the zero-exterior logarithmic energy space. Indeed,

\[
\int|g'(\delta)|\,d\delta
=\int|m'(Q)|\,dQ
=\kappa\|\chi'\|_{L^1}\sum_n\frac1{Q_n}<\infty,
\tag{PL318-23}
\]

so the zero extension is compactly supported `W^{1,1}`; `PL-315` already records that such profiles have every logarithmic Fourier moment and every `H^alpha`, `alpha<1/2`. Thus (PL318-22) is not merely a formal pointwise calculation: `u` is an admissible zero-exterior weak Dirichlet state with bounded right-hand side `f=L_Delta u`.

## 3. The moving Green atom still produces an order-one defect

At `s=s_n`, if

\[
|q-r|<r\epsilon_n/2,
\]

then

\[
\left|\frac q{s_n}-Q_n\right|
<\frac{\epsilon_nQ_n}{2}
=\frac{W_n}{2}.
\]

Hence `chi=1` there and

\[
m(q/s_n)=\frac\kappa{Q_n}
=\frac{\kappa}{r}s_n.
\tag{PL318-24}
\]

Positivity of `mu_{s_n,r}` and (PL318-10) give

\[
\boxed{
\mathcal A_{s_n}[m](r)
\ge
\frac{3\kappa}{4r}e^{-2r}.
}
\tag{PL318-25}
\]

On the other hand, (PL318-12) gives

\[
e^{-r}\int_0^\infty m(Q)\,dQ
=
\kappa e^{-r}\|\chi\|_{L^1}
\sum_n\epsilon_n.
\tag{PL318-26}
\]

Choose the summable `epsilon_n` initially so that

\[
\|\chi\|_{L^1}\sum_n\epsilon_n
<\frac{e^{-r}}{4r}.
\tag{PL318-27}
\]

Then the rank-one candidate in (PL318-26) is smaller than `kappa e^{-2r}/(4r)`, while (PL318-25) is at least three times that value. Therefore (PL318-4) fails along `s_n` by a fixed positive gap.

This is the same diagonal mechanism as `PL-314`, but it now survives the additional constraint that the physical profile itself solves a logarithmic Dirichlet Poisson equation with bounded forcing.

## 4. Why this narrows the completed-Weil gate

The current completed-Weil program reaches the zero-order logarithmic operator through a highly structured eigen-equation: the source is not an arbitrary bounded function but is tied back to the state by the finite active prime-power shifts, the archimedean completion term, and the scalar eigenvalue relation. `PL-291` already shows that this coupling bootstraps actual eigenstates through every logarithmic Fourier scale, while `PL-315` proves that the resulting generic all-log regularity is still insufficient for the moving-diagonal limit.

The present construction closes one more generic shortcut. Even adding the equation

\[
L_\Delta u=f,
\qquad f\in L^\infty,
\tag{PL318-28}
\]

does not force `Qm(Q)->0`. Hence the missing tail law cannot be obtained merely by citing bounded-source boundary regularity for the logarithmic Laplacian, by observing that the zero-order right-hand side is bounded, or by combining those facts with the regularity already recorded in `PL-291`--`PL-317`.

A useful next theorem must exploit a **source-specific relation absent from (PL318-28)**: for example a genuine boundary asymptotic forced by the completed-Weil state-source coupling, monotonicity or one-sided structure of the actual ground state, a cancellation identity involving the finite prime-power channels, or a direct estimate of the samples `m(r/s)/s`. Once such a tail theorem exists, the scalar corner-to-outer compatibility of `PL-313` becomes available; the separate rational-prime sign problem still remains.

## Prior-art and novelty audit

The logarithmic-Laplacian formula (PL318-21) is classical. Chen--Weth (source 96 in `research/prime_lattice/SOURCES.md`) establish the singular-integral realization and Dirichlet framework. Hernández-Santamaría--López Ríos--Saldaña (source 97) prove the optimal generic bounded-source boundary estimate

\[
|u(x)|\le C\,\ell(\operatorname{dist}(x,\partial I))^{1/2},
\qquad
\ell(t)\asymp |\log t|^{-1},
\]

and show that this `1/sqrt(log)` scale is sharp in the positive torsion/Hopf setting. The present profile is fully consistent with that theorem: its sparse peaks are only `O(1/log)`, hence smaller than the generic upper scale, and its bounded forcing is not assumed nonnegative.

A targeted literature audit around bounded-source logarithmic-Laplacian boundary regularity, log-Hölder/Dini regularity, and zero-order integral kernels found the established generic boundary laws and classical regularity theory but no theorem excluding sparse `1/log` saturation for sign-indefinite bounded forcing, nor a result coupling such saturation to the `Q=r/s` Green observation scale. Search absence is not treated as broad novelty evidence. The durable claim is line-local and exact: the explicit profile above simultaneously has bounded `L_Delta`, violates `Qm(Q)->0`, and retains the `PL-314` moving-diagonal defect.

## Adversarial controls

1. **This is not a counterexample to the actual completed-Weil eigenbranch.** The constructed bounded forcing is defined as `f=L_Delta u` and is free to change sign. It need not satisfy the state-dependent prime-power/completion relation of the localized Weil operator.
2. **There is no conflict with the sharp Hopf law.** Source 97's lower boundary law uses positivity/supersolution hypotheses. Here only boundedness of the forcing is tested, and the profile lies below the generic `1/sqrt(Q)` upper envelope.
3. **The result is stronger than a regularity counterexample but weaker than a source-coupled one.** `PL-315`--`PL-316` already show that large ambient regularity classes permit the obstruction. `PL-318` adds compatibility with the principal zero-order PDE, but deliberately does not encode the arithmetic lower operator.
4. **The construction uses one fixed profile.** Only the observation orders `s_n` vary. There is no `s`-dependent forcing hidden in `u`.
5. **No necessity is claimed for `Qm(Q)->0`.** As in `PL-314`, weaker averaged anti-concentration or source-structured estimates may suffice. The claim is only that bounded logarithmic forcing does not provide such a condition automatically.
6. **No RH or sign conclusion is obtained.** This is a route-narrowing theorem at the analytic matching gate. Rational-prime specificity remains downstream.

## Consequence for the research line

The zero-order frontier is now more specific. Passing from `PL-315`'s broad function classes to the actual principal PDE does **not** kill the moving atom: a bounded logarithmic-Poisson source still admits a fixed `O(1/Q)` endpoint profile with sparse order-one samples after the `1/s` normalization. Therefore the next productive pass should not seek another generic bounded-source estimate for `L_Delta`.

The falsifiable target is the full completed-Weil state-source coupling. It must force either `m=o(1/Q)`, an equivalent anti-concentration law, or a direct cancellation of the moving diagonal. Without one of those genuinely source-specific statements, the rank-one corner balance of `PL-313` cannot yet be applied to the actual branch.

## Sources

- Huyuan Chen, Tobias Weth, “The Dirichlet problem for the logarithmic Laplacian,” *Communications in Partial Differential Equations* **44**(11) (2019), 1100–1139. DOI: https://doi.org/10.1080/03605302.2019.1611851. arXiv: https://arxiv.org/abs/1710.03416. Source 96 in `research/prime_lattice/SOURCES.md`.
- Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, “Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian,” *Discrete and Continuous Dynamical Systems* **45**(1) (2025), 1–36. DOI: https://doi.org/10.3934/dcds.2024084. arXiv: https://arxiv.org/abs/2401.18033. Source 97 in `research/prime_lattice/SOURCES.md`.
- `PL-310`: stretched Green-measure limit and diagonal atom.
- `PL-313`: compact-corner rank-one transfer.
- `PL-314`: `L^1(dQ)` failure and sufficient `Qm(Q)->0` tail criterion.
- `PL-315`--`PL-317`: sharp generic regularity controls around the moving-tail gate.
