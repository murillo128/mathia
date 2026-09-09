# WI-212 — every fixed reciprocal-harmonic packet admits a sparse deep off-line screen

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-BARRIER + CLASSICAL-IDENTITY + LITERATURE-CONTEXT`.

WI-210 shows that a dense symmetrized off-line bow cannot be cancelled at all reciprocal harmonics by a local population consisting only of critical-line zeros: Fejer positivity makes the required positive mass scale with the bow population. WI-211 then gives an exact two-pair countermodel in the first full-packet regime `2<d<3`, showing that the forced fresh off-line defect need not have positive density.

The two-harmonic construction is not exceptional. For **every fixed finite number of reciprocal harmonics**, the entire real target moment vector can be completed to a real self-reciprocal polynomial whose roots are exactly a bounded collection of reciprocal-conjugate pairs. In the bow scaling the outer roots have modulus `asymp M`, so the corresponding screening pairs have horizontal depth

\[
a_j=\log M+O(1).
\]

Consequently, for every fixed spacing `d>2`, if

\[
r=\max\{k\in\mathbb N:k<d\},
\]

then a bounded-depth equal-depth bow of `M` selected right-half-plane off-line labels can be cancelled **exactly at all `r` strictly interior reciprocal harmonics** by only `r` further off-line functional-equation pairs. If `M=T^{\vartheta+o(1)}` and

\[
d\vartheta<\frac12,
\]

the screening pairs stay inside the critical strip. Their local count cost is only `2r=O_d(1)` zero labels, which is negligible compared with the Riemann--von Mangoldt excess `(d-2+o(1))m` for a count-saturating bow when `d>2` is fixed.

Thus **adding any fixed number of discrete reciprocal harmonics cannot by itself turn WI-210 into a positive-density defect bootstrap**. The obstruction is algebraic, not numerical: Newton--Girard identities prescribe the first `r` power sums, and self-reciprocal completion supplies the functional-equation pairing at no additional moment cost. A successful bootstrap must charge radial depth, control a continuum or a number of frequencies growing with the bow population, or impose genuinely source-specific arithmetic restrictions on the screen.

This is a matched structural countermodel, not a claim that the constructed zeros occur for `zeta`.

## 1. General finite real moment target

Fix an integer `r>=1`. Let real target moments

\[
p_k(M)\in\mathbb R,
\qquad 1\le k\le r,
\tag{1}
\]

satisfy, as `M->infinity`,

\[
p_1(M)=-aM+O(1),
\qquad a>0,
\tag{2}
\]

and

\[
p_k(M)=O(M)
\qquad(2\le k\le r).
\tag{3}
\]

Define real coefficients `A_1(M),...,A_r(M)` recursively by the Newton relations

\[
A_0:=1,
\qquad
kA_k
=-\sum_{j=0}^{k-1}A_jp_{k-j}
\qquad(1\le k\le r).
\tag{4}
\]

Equivalently, if a monic polynomial has leading coefficients

\[
z^n+A_1z^{n-1}+\cdots+A_rz^{n-r}+\cdots,
\]

then its root power sums through order `r` are exactly the prescribed `p_k`.

Because every `p_k` is real, all `A_k` are real. From (2)--(4), induction gives

\[
\boxed{
A_k(M)=\frac{(aM)^k}{k!}+O(M^{k-1})
}
\qquad(1\le k\le r).
\tag{5}
\]

Indeed, the only contribution of order `M^k` in (4) is `-A_{k-1}p_1`; every term involving `p_j` with `j>=2` is at most `O(M^{k-1})`.

## 2. Self-reciprocal completion preserves the first r moments exactly

Form the degree-`2r` real palindromic polynomial

\[
\boxed{
\begin{aligned}
P_M(z)
={}&z^{2r}+A_1z^{2r-1}+\cdots+A_{r-1}z^{r+1}+A_rz^r\\
&+A_{r-1}z^{r-1}+\cdots+A_1z+1.
\end{aligned}}
\tag{6}
\]

Let its roots, counted with multiplicity, be

\[
\lambda_1,\ldots,\lambda_{2r}.
\]

Newton--Girard identities only use the first `k` leading coefficients to determine the `k`-th power sum. Hence (4) and (6) give the exact identities

\[
\boxed{
\sum_{\nu=1}^{2r}\lambda_\nu^k=p_k(M)
}
\qquad(1\le k\le r).
\tag{7}
\]

The lower half of the palindromic coefficient list therefore imposes the reciprocal symmetry **without changing any of the first `r` moments**.

Since `P_M` has real palindromic coefficients,

\[
P_M(z)=z^{2r}P_M(1/z),
\tag{8}
\]

and its root multiset is closed under both complex conjugation and reciprocal inversion. Once no root lies on the unit circle, the roots can therefore be grouped as

\[
\boxed{
\{\lambda_1,\ldots,\lambda_{2r}\}
=
\{\xi_1,1/\overline{\xi_1},\ldots,
\xi_r,1/\overline{\xi_r}\},
\qquad |\xi_j|>1.
}
\tag{9}
\]

Equation (7) then becomes

\[
\boxed{
\sum_{j=1}^{r}
\left(
\xi_j^k+\overline{\xi_j}^{-k}
\right)
=p_k(M)
}
\qquad(1\le k\le r).
\tag{10}
\]

Writing

\[
\xi_j=q_jz_j,
\qquad q_j>1,
\qquad |z_j|=1,
\tag{11}
\]

turns (10) into

\[
\boxed{
\sum_{j=1}^{r}
(q_j^k+q_j^{-k})z_j^k
=p_k(M).
}
\tag{12}
\]

This is exactly the reciprocal-harmonic contribution of `r` off-line zeros together with their same-ordinate functional-equation mirrors.

## 3. The outer roots are all of size M

It remains to justify the grouping (9) and quantify the radial depth. Scale (6) by `z=Mw`. From (5),

\[
M^{-2r}P_M(Mw)
\longrightarrow
w^rR_r(w)
\tag{13}
\]

locally uniformly, where

\[
R_r(w)
:=w^r+aw^{r-1}+\frac{a^2}{2!}w^{r-2}
+\cdots+\frac{a^r}{r!}.
\tag{14}
\]

Let

\[
E_r(z):=\sum_{j=0}^{r}\frac{z^j}{j!}.
\tag{15}
\]

Then

\[
R_r(w)=w^rE_r(a/w).
\tag{16}
\]

Every zero of `E_r` is nonzero and simple. Nonzero is immediate from `E_r(0)=1`. If `zeta` were a repeated zero, then

\[
E_r(\zeta)=E_r'(\zeta)=E_{r-1}(\zeta)=0,
\]

but

\[
E_r(\zeta)-E_{r-1}(\zeta)=\frac{\zeta^r}{r!}=0,
\]

forcing `zeta=0`, a contradiction. Therefore `R_r` has `r` distinct nonzero roots

\[
w_j=\frac{a}{\zeta_j},
\tag{17}
\]

where `zeta_j` runs over the zeros of `E_r`.

By ordinary continuity of polynomial zeros, or equivalently Rouche's theorem on disjoint small circles around the `w_j`, equation (13) gives `r` roots of `P_M` satisfying

\[
\boxed{
\xi_j=Mw_j+o(M),
\qquad 1\le j\le r.
}
\tag{18}
\]

In particular

\[
|\xi_j|=M|w_j|(1+o(1))>1
\tag{19}
\]

for large `M`. Palindromicity supplies their `r` reciprocal partners, all of modulus `O(M^{-1})`; hence there are no unit-circle roots for sufficiently large `M`, and (9) is valid.

The radial parameters therefore obey

\[
\boxed{
q_j=M|w_j|(1+o(1)),
\qquad
\log q_j=\log M+O_r(1).
}
\tag{20}
\]

The constants `w_j` depend only on `r` and the leading coefficient `a` of the first target moment. Higher target moments affect lower-order root corrections but not the `M`-scale radial law.

## 4. Exact application to a bounded-depth bow

Use the WI-210/WI-211 unfolded normalization. Take an equal-depth selected bow of `M` right-half-plane labels with fixed scaled depth

\[
b_j=dh,
\qquad h>0.
\tag{21}
\]

At the reciprocal harmonics

\[
\alpha_k=\frac{k}{d},
\qquad 1\le k\le r,
\tag{22}
\]

the selected mirror-pair contribution, after rotating away the common bow phase, is

\[
B_k=2M\cosh(kh).
\tag{23}
\]

To cancel it, set

\[
p_k(M):=-B_k=-2M\cosh(kh).
\tag{24}
\]

Conditions (2)--(3) hold with

\[
a=2\cosh h>0.
\tag{25}
\]

Therefore Sections 1--3 construct exactly `r` reciprocal-conjugate pairs satisfying

\[
\boxed{
\sum_{j=1}^{r}
(q_j^k+q_j^{-k})z_j^k
=-2M\cosh(kh)
}
\qquad(1\le k\le r).
\tag{26}
\]

Thus all `r` reciprocal harmonics are screened exactly.

The phases are locally realizable as ordinates. For each `z_j=e^{i\phi_j}`, choose an unfolded ordinate `u_j` with

\[
\exp\!\left(\frac{2\pi i(u_j-x_0)}d\right)=z_j.
\tag{27}
\]

Adding an integer multiple of `d` leaves (27) unchanged, so in a bow interval containing `m->infinity` grid periods one may place each of the finitely many screening ordinates inside the same local interval.

## 5. The screening pairs remain inside the critical strip at small fixed bow powers

Write

\[
M=T^{\vartheta+o(1)},
\qquad L=\log T.
\tag{28}
\]

A screening pair with radial parameter `q_j=e^{a_j}` has

\[
a_j=\log q_j=\log M+O(1)
=\vartheta L+o(L).
\tag{29}
\]

Its right-half-plane real part is therefore

\[
\beta_j
=\frac12+\frac{da_j}{L}
=\frac12+d\vartheta+o(1).
\tag{30}
\]

Hence

\[
\boxed{
d\vartheta<\frac12
}
\tag{31}
\]

implies

\[
\frac12<\beta_j<1
\]

for every screening pair and all sufficiently large `T`. Their functional-equation mirrors lie in `(0,1/2)`.

This is the same horizontal-depth scale found explicitly for `r=2` in WI-211. The self-reciprocal completion shows that it persists for every fixed finite packet.

## 6. Full reciprocal packet and local count budget

For fixed spacing `d`, define

\[
r:=\max\{k\in\mathbb N:k<d\}.
\tag{32}
\]

Equivalently,

\[
r<d\le r+1.
\tag{33}
\]

These are exactly the strictly interior reciprocal harmonics available inside support one. For every fixed `d>2`, one has `r>=2` and the construction above screens the **entire** reciprocal packet with exactly `r` extra off-line pairs, hence `2r` local zero labels.

For a count-saturating bow with `M=m-O(1)`, WI-210 records the remaining Riemann--von Mangoldt label budget

\[
(d-2+o(1))m.
\tag{34}
\]

Since `d>2` and `r` is fixed,

\[
2r=o((d-2)m).
\tag{35}
\]

Thus local counting never converts the finite packet into positive-density amplification. Increasing `d` by a fixed amount merely increases the number of constraints and the number of screening pairs by another fixed amount.

The endpoint `d=2` remains different: there is only one strictly interior harmonic and no positive-density local count excess. This finding does not alter the separate endpoint analysis.

## 7. What this closes

For every fixed `d>2`, the following implication is false using only finite reciprocal-harmonic cancellation, functional-equation symmetry, and local zero count:

\[
\text{dense selected off-line bow}
+\text{cancellation at every interior reciprocal harmonic}
+\text{local zero count}
\Longrightarrow
\text{positive-density fresh off-line defect}.
\tag{36}
\]

The screen can consist of only `r=O_d(1)` additional pairs.

The mechanism is robust at the finite-moment level. It is not tied to solving two special trigonometric equations: **any fixed real moment vector satisfying (2)--(3) has a self-reciprocal completion with the same first `r` moments and with only `r` deep reciprocal-conjugate pairs.**

Therefore a prospective defect-to-zero iteration must use information absent from this finite packet, for example:

- a depth-weighted coercive quantity that makes `q_j\asymp M` expensive;
- control on a continuum of frequencies or on a number of independent samples growing with `M`;
- an arithmetic source identity constraining which self-reciprocal moment completions can occur;
- a theorem coupling one deep screen to a mesoscopic population of additional zeros;
- another invariant not determined by finitely many truncated power sums.

A request to “add one more reciprocal harmonic” does not evade the obstruction unless the number of genuinely controlled constraints itself grows in a way that defeats the finite self-reciprocal completion.

## 8. Prior-art and novelty audit

The algebraic ingredients are classical. Newton--Girard identities recover polynomial coefficients from prescribed power sums. Real self-reciprocal/self-inversive polynomials have root multisets invariant under reciprocal/conjugate symmetry; this is classical polynomial theory, including the literature of Bonsall--Marden and later work on self-inversive zeros. The positive and indefinite truncated moment literature likewise makes clear that finite moment constraints with indefinite directions have qualitatively more flexible realizations than positive unit-circle measures.

A targeted search around prescribed Newton sums, self-reciprocal/self-inversive polynomial completion, truncated trigonometric moments with negative squares, generalized Nevanlinna interpolation, and reciprocal-root power-sum interpolation found these classical ingredients but no source stating the zeta-bow consequence above: palindromically completing the first reciprocal-harmonic moments to obtain an `O(r)` deep off-line screen with `q_j\asymp M`. Absence from that search is not used as a priority claim, and no novelty claim is made.

The exact mathematical delta relative to WI-211 is structural: the explicit `r=2` screen is promoted to an all-fixed-`r` theorem, so **no fixed finite enlargement of the reciprocal packet can restore a density bootstrap**. This closes a whole family of incremental harmonic refinements at once.

## Research consequence

WI-210 remains a valid one-step coercive statement against a critical-line-only complementary reservoir. WI-211 shows that two off-line pairs can absorb the first full two-harmonic packet. WI-212 shows that this sparse deep screening persists for **every fixed finite full reciprocal packet**.

The next viable escape must therefore be non-finite in the relevant sense or must charge radial depth. In particular, continuum-frequency localization and source-fixed depth coercivity are not optional refinements of the finite-harmonic program; they are the first mechanisms in the current interface that are not algebraically defeated by self-reciprocal completion.