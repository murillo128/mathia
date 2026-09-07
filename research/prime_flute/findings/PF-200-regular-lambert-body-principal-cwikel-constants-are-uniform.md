# PF-200 — regular Lambert-body principal Cwikel constants are uniform

**Status:** `LITERATURE+DERIVED + ENDPOINT-LOCALIZATION + POSITIVE/BOUNDARY`. PF-197 identifies the compactly localized two-dimensional relative gradient form as a matrix-valued critical `Q C P` problem, PF-198 shows that fixed-width Lambert localization preserves the prime-summable `L log L` coefficient budget, and PF-199 proves that two-sided finite-color reassembly creates no window-count loss. PF-199 still left its local critical constants under the conditional envelope `K_{n,j} <= C(1+a_n)^m`. For the **regular Lambert-body principal pieces** that condition can be sharpened to `m=0`: after recentering the fixed-width windows, the exact-area PF-191 comparison metrics form a uniformly elliptic `C^1` family, localized resolvents have a uniform `L^2 -> H^1` gradient bound by standard interior elliptic regularity, and Ponge's torus reduction makes the critical Cwikel constant depend only on the corresponding order-zero renormalized factors. Thus the principal body family has a uniform local weak-`S_1` constant and its global counting budget is bounded directly by `sum_n d_n(1+a_n)/cosh(a_n) < infinity`.

The scope is deliberately narrower than the full relative resolvent. Module-interface/cuff pieces, true-short-collar transition pieces, off-diagonal resolvent tails, cutoff/commutator and smoothing remainders, and the endpoint conservative splice remain separate gates. No global weak-`S_1` theorem, scattering statement, determinant, resonance statement, or RH consequence is claimed.

## Claim

Use PF-191's exact-area Lambert comparison on a tail module of depth `a=a_n` with target parameter `a'=a+d`, and PF-198's fixed-width longitudinal cover. A **regular body window** means one fixed-width window together with a slightly larger fixed-buffer window whose recentered chart lies in one of the smooth Lambert-body coordinate families used by PF-191. As in PF-199, a fixed number of module-end/cuff/interface windows may instead be left to the separate interface remainder; the claim below concerns the two-sided principal family `B_{n,j}` built from the remaining regular windows.

Let

\[
R_k=(\Delta_k+1)^{-1},
\qquad k\in\{g,h\},
\tag{1}
\]

where `g` is the source metric and `h` is the exact-area pulled-back target metric on the local body chart. Choose fixed-profile cutoffs

\[
\chi_{n,j}\prec\chi'_{n,j}\prec\eta_{n,j}
\tag{2}
\]

with support separations independent of `n,j,a_n`. After the finite block-bundle enlargement of PF-197 and transport of the recentered chart to one fixed torus chart, write the compactly localized order-`-1` factors as

\[
P_{n,j}=\chi_{n,j}\,dR_g\,\chi'_{n,j},
\qquad
Q_{n,j}=(\chi_{n,j}\,dR_h\,\chi'_{n,j})^*,
\tag{3}
\]

with harmless fixed-rank zero-order metric/bundle identifications absorbed into the notation. Let `C_{n,j}` be PF-198's localized matrix coefficient and let

\[
B_{n,j}
=M_{\eta_{n,j}}Q_{n,j}M_{C_{n,j}}P_{n,j}M_{\eta_{n,j}}
\tag{4}
\]

be the two-sided principal piece of PF-199.

Then there is a constant `K_0`, independent of `n`, `j`, and `a_n` on the tail, such that

\[
\boxed{
q(B_{n,j})
\le K_0\,\|C_{n,j}\|_{L\log L}.
}
\tag{5}
\]

Here `q` is PF-199's weak-trace counting quasi-norm. Consequently PF-198, PF-196 and PF-199 give

\[
\boxed{
\sum_{n,j}q(B_{n,j})
\le C\sum_n
\frac{d_n(1+a_n)}{\cosh a_n}
<\infty,
}
\tag{6}
\]

and the finite-color two-sided sum of all regular Lambert-body principal pieces belongs to `S_{1,infinity}` with no Lambert-depth loss in the local Cwikel constant.

Equation (6) removes PF-199's conditional factor `(1+a_n)^m` for this principal body family. It does **not** identify that sum with the full relative resolvent.

## 1. The recentered exact-area metric family has uniform local ellipticity and `C^1` control

PF-191 uses the area coordinate

\[
y=\sinh\rho,
\tag{7}
\]

in which the source hyperbolic metric and area are

\[
\boxed{
g
=\frac{dy^2}{1+y^2}+(1+y^2)d\tau^2,
\qquad d\mu=dy\,d\tau.}
\tag{8}
\]

The source metric is therefore independent of the Lambert parameter. On the finite branch the exact-area triangular transport is

\[
\tau'=\psi(\tau)=\operatorname{arsinh}(\lambda\sinh\tau),
\qquad
y'=\frac{y}{\psi'(\tau)},
\tag{9}
\]

with

\[
\lambda=\frac{\sinh(a+d)}{\sinh a}.
\tag{10}
\]

Put

\[
p=\psi',
\qquad
q=(\log p)',
\qquad
e=p^2-1.
\tag{11}
\]

PF-191 gives the exact formulas

\[
\boxed{
e(\tau)
=\frac{\lambda^2-1}{1+\lambda^2\sinh^2\tau},
\qquad
q(\tau)
=\frac{(1-\lambda^2)\tanh\tau}
{1+\lambda^2\sinh^2\tau},}
\tag{12}
\]

and

\[
\boxed{
h
=\frac{(dy-yq\,d\tau)^2}{p^2+y^2}
+(p^2+y^2)d\tau^2.}
\tag{13}
\]

For fixed sufficiently small `d_0`, all tail parameters satisfy `0<=d<=d_0` and `1<=lambda<=lambda_0`. The functions

\[
(1+\lambda^2\sinh^2\tau)^{-1}
\quad\text{and}\quad
\tanh\tau(1+\lambda^2\sinh^2\tau)^{-1}
\tag{14}
\]

have globally bounded derivatives of every fixed finite order, uniformly for `lambda` in this compact interval. Since `lambda^2-1=O(d)`, (12) gives in particular

\[
\|e\|_{C^1(0,\infty)}+
\|q\|_{C^1(0,\infty)}
\le C d.
\tag{15}
\]

PF-191/PF-179 also give a uniform upper bound for the relevant Lambert `y`-width. Therefore (13) and its inverse are uniformly elliptic and uniformly `C^1` on every recentered fixed-width body chart.

The outer branch is easier: PF-179's area-preserving transport there is an exact hyperbolic isometry, so `h=g`. The one moving Lambert corner is treated in PF-179/PF-191 on a fixed recentered bounded-geometry patch. Its relative Moser correction is performed on one fixed reference domain with fixed support separation and an `I+O(d)` differential bound. Choosing the fixed-domain interpolation/divergence solver once gives the same finite `C^1` control required below. A fixed number of windows touching later cuff/interface/true-short-collar assembly corrections may instead be excluded from the present principal family and retained in the already explicit remainder gate.

Thus, for the regular body windows used here, there are constants `c,C,L` independent of `n,j` such that in the recentered chart

\[
c|\xi|^2\le k^{ab}(x)\xi_a\xi_b\le C|\xi|^2,
\qquad
\|k^{ab}\|_{C^1}\le L,
\qquad k\in\{g,h\}.
\tag{16}
\]

This is the precise uniformity needed for the next step; no global bounded-geometry assertion about the complete flute is being made.

## 2. Fixed-buffer localized gradient resolvents have a uniform `L^2 -> H^1` bound

Let `U\Subset U'` be the fixed nested recentered windows corresponding to `chi_{n,j}\prec chi'_{n,j}`. For

\[
u=R_k f,
\tag{17}
\]

we have

\[
(\Delta_k+1)u=f.
\tag{18}
\]

The resolvent energy identity gives a uniform global first-order estimate,

\[
\|u\|_{L^2(k)}+\|du\|_{L^2(k)}
\le C\|f\|_{L^2(k)}.
\tag{19}
\]

On `U'`, (16) puts (18) into a uniformly elliptic divergence-form equation whose leading coefficients have a uniform `C^1` bound. The standard interior difference-quotient `H^2` estimate on the fixed pair `U\Subset U'` therefore gives

\[
\|u\|_{H^2(U)}
\le C\left(
\|f\|_{L^2(U')}+\|u\|_{H^1(U')}
\right)
\le C\|f\|_{L^2},
\tag{20}
\]

where the constant depends only on the fixed support separation and the constants in (16), not on `n,j,a_n`. Multiplication by the fixed-profile cutoffs preserves this uniformity. Hence

\[
\boxed{
\|\chi_{n,j}dR_k\chi'_{n,j}\|_{L^2\to H^1}
\le C,
\qquad k\in\{g,h\}.
}
\tag{21}
\]

This is the only elliptic-regularity input needed for the quantitative Cwikel constant. It is the standard interior `H^2` estimate for second-order uniformly elliptic equations (e.g. the difference-quotient theorem in Chapter 6 of L. C. Evans, *Partial Differential Equations*, 2nd ed., AMS, 2010). No new elliptic-regularity theorem is claimed.

Each doubly localized resolvent factor in (3) is a compactly supported order-`-1` pseudodifferential operator in the local chart: this is the standard local elliptic-parametrix statement, with the global Green correction smoothing after both variables are localized. Ponge's local reduction therefore applies to these factors.

## 3. Ponge's torus reduction exposes the constant

Let

\[
\Lambda=(1+\Delta_{\mathbb T^2})^{1/2}
\tag{22}
\]

on the fixed torus chart used in Ponge's local proof, with the fixed finite-rank bundle handled componentwise. For a transported local order-`-1` pair `P,Q`, the algebraic factorization

\[
\boxed{
Q M_u P
=(Q\Lambda)
\big(\Lambda^{-1}M_u\Lambda^{-1}\big)
(\Lambda P)
}
\tag{23}
\]

is exact. The torus Cwikel--Solomyak estimate used by Ponge gives

\[
\|\Lambda^{-1}M_u\Lambda^{-1}\|_{1,\infty}
\le C_{\mathbb T^2,E}\|u\|_{L\log L}.
\tag{24}
\]

The weak ideal property then yields

\[
\|Q M_u P\|_{1,\infty}
\le
C_{\mathbb T^2,E}
\|Q\Lambda\|_{\mathcal B(L^2)}
\|\Lambda P\|_{\mathcal B(L^2)}
\|u\|_{L\log L}.
\tag{25}
\]

This makes quantitative what PF-197 left implicit in the notation `C_{PQ}`: for the local torus reduction, it is enough to bound the two order-zero renormalized factors.

Under the fixed recentering/trivialization, the `H^1` norm is equivalent to the graph norm of `Lambda` by one fixed constant. Equation (21) therefore gives

\[
\|\Lambda P_{n,j}\|\le C,
\qquad
\|Q_{n,j}\Lambda\|
=\|\Lambda Q_{n,j}^*\|
\le C.
\tag{26}
\]

The coordinate, zero-extension and finite bundle-identification maps in Ponge's compact-support reduction are the same fixed maps after recentering, so they introduce no `n`- or `a_n`-dependent constant. Combining (25)--(26) proves (5).

This argument uses precisely the mechanism behind Ponge's local Cwikel estimate; it does not strengthen the general theorem. The new deduction is that the PF-191/PF-198 family satisfies its quantitative local hypotheses with a uniform constant.

## 4. The critical coefficient budget now sums with `m=0`

PF-198 gives on each module

\[
\sum_j\|C_{n,j}\|_{L\log L}
\le
C\frac{d_n(1+a_n)}{\cosh a_n}.
\tag{27}
\]

PF-196 proves the exact prime/shift summability

\[
\sum_n
\frac{d_n(1+a_n)^k}{\cosh a_n}<\infty
\qquad\text{for every fixed }k.
\tag{28}
\]

The present uniform bound needs only `k=1`. Hence

\[
\sum_{n,j}q(B_{n,j})
\le
K_0\sum_{n,j}\|C_{n,j}\|_{L\log L}
\le
C\sum_n\frac{d_n(1+a_n)}{\cosh a_n}<\infty.
\tag{29}
\]

PF-199's two-sided fixed-color theorem then turns (29) into the weak-`S_1` statement for the sum of the regular principal pieces without multiplying by the `O(a_n)` number of windows.

Thus the analytic frontier moves from

\[
\text{``prove a polynomial bound for the local Ponge constants''}
\tag{30}
\]

to

\[
\boxed{
\text{``control the nonprincipal/off-diagonal/interface remainder.''}
}
\tag{31}
\]

The local matrix endpoint theorem, coefficient fragmentation, finite-color counting, and principal-family constant are no longer independent obstructions on the regular Lambert bodies.

## 5. What remains outside the theorem

The two-sided outer cutoffs in (4) are essential. The full relative gradient form contains terms in which at least one localized resolvent factor connects `supp C_{n,j}` to the complement of the fixed enlarged window. Equation (21) gives no summable singular-value estimate for those off-diagonal pieces by itself.

Likewise, the present proof does not absorb:

- commutators created when cutoffs are inserted into the resolvent/parametrix identity;
- smoothing errors whose individual smoothness does not yet come with a prime-summable trace norm;
- physical cuff/body transmission and module-end pieces deliberately left in the PF-199 interface remainder;
- PF-183's true-short-collar transition/slab terms and their endpoint conservative interpolation;
- the final source/target identification terms required to turn the local form into one global first-relative-resolvent operator.

A finite number of exceptional head modules can always be absorbed into a finite constant, but an infinite family of interface or off-diagonal pieces cannot be dismissed this way. They need their own summable trace/weak-trace estimate or a separate finite-color critical decomposition.

In particular, (29) is **not** evidence that the full first relative resolvent is weak trace class. It proves only that one previously conditional component of that program is now unconditional.

## Prior-art and novelty audit

Raphaël Ponge, *Weyl's Laws and Connes' Integration Formulas for Matrix-Valued `L log L`-Orlicz Potentials*, Mathematical Physics, Analysis and Geometry 25 (2022), article 10, DOI `10.1007/s11040-022-09422-9`, is S20 in `research/prime_flute/SOURCES.md`. Its Proposition 3.13 is the general matrix-valued `Q u P` weak-trace theorem; Lemma 3.9 and Remark 3.11 supply the compact-support/noncompact local reduction used by PF-197. Ponge explicitly derives the manifold theorem from the torus Cwikel--Solomyak estimate, so the factorization (23) and ideal bound (25) are an unpacking of the classical proof mechanism, not a new Cwikel theorem.

The underlying torus endpoint is classical Cwikel--Solomyak theory; see also F. Sukochev and D. Zanin, *Cwikel-Solomyak estimates on tori and Euclidean spaces*, arXiv:2008.04494. Standard interior `H^2` regularity for uniformly elliptic divergence-form operators with `C^1` leading coefficients is textbook PDE theory; Evans' Chapter 6 difference-quotient proof records the dependence on the fixed nested domains and the operator coefficients. No novelty is claimed for either input.

A targeted search for uniform Cwikel constants for pseudodifferential families and bounded-family critical weak-trace estimates found the expected general Cwikel/Sobolev literature but no source that performs the prime-flute-specific exact-area Lambert recentering or combines it with PF-196/PF-198's arithmetic summability. Search absence is not used as a novelty theorem.

The project-specific contribution is the quantitative bridge: the explicit PF-191 exact-area metric formulas plus the fixed-window PF-198 cover give uniform local elliptic constants, which make the order-zero norms in (25) uniform, which removes PF-199's remaining depth-dependent constant for the regular body principal family.

## Falsification and boundary checks

A later adversary can audit PF-200 by:

1. differentiating (12) and verifying the uniform `C^1` bounds in (15) for `lambda` in a fixed compact interval;
2. inserting those bounds into (13) and checking uniform ellipticity on the uniformly bounded Lambert `y`-range;
3. checking that the PF-179/PF-191 recentered corner correction is performed on one fixed bounded-geometry reference patch and can be kept in the same uniform `C^1` class, or excluding those fixed corner windows into the interface remainder;
4. applying the standard fixed-buffer interior `H^2` estimate to `(Delta_k+1)u=f` and verifying that its constants depend only on the uniform ellipticity/coefficient bounds and support separation;
5. checking that the doubly localized `dR_k` factor is a compactly supported order-`-1` pseudodifferential operator modulo a smoothing kernel, so Ponge's local torus reduction applies;
6. verifying the exact factorization (23), the torus critical estimate (24), and the uniform order-zero bounds (26);
7. combining the resulting `K_0` with PF-198's Orlicz budget and PF-199's finite-color counting theorem to obtain (29);
8. refusing any upgrade to the full relative resolvent until every omitted off-diagonal, commutator, smoothing, interface, collar and splice term has a separately proved prime-summable endpoint budget.

PF-200 is refuted or must be narrowed if a supposedly regular body window cannot be embedded in the fixed recentered chart with the uniform support buffer assumed in (2), if the exact-area target coefficients lose the uniform `C^1` bound needed in (20), or if the transported localized resolvent factors fail to admit the fixed-torus order-zero norm control in (26). A failure confined to the explicitly excluded interface/splice family would not refute PF-200; it would realize its stated remaining boundary.