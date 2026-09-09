# PF-244 — one-sided seam domination does not imply separated Poisson smoothing

**Status:** `EXACT-DERIVED + ABSTRACT-COUNTERMODEL + DECISIVE-NEGATIVE/PROOF-STRATEGY-OBSTRUCTION + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing|PF-243]] reduces the high-high shear correction to a sharply localized question: does a seam-normalized Robin Poisson solution gain more than one scaled tangential derivative when it is observed a fixed positive `X`-distance from its forcing boundary? [[research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer|PF-238]] supplies an important surviving fact about the actual complete-lift seam, namely one-sided form domination by the matched first-order seam. That fact is enough for the diagonal dressed crossing estimate, but it is **not enough by itself** for PF-243's separated Poisson smoothing.

There is an explicit product half-strip model with all of the following features at once:

- a positive compact-resolvent tangential operator `K`;
- a positive invertible nonlocal seam `Q` satisfying the one-sided first-order form bound `Q <= C K`;
- compact inverse for the matched seam `K` but noncompact inverse for `Q`, paralleling the soft-seam spectral-type mismatch isolated in [[research/prime_flute/findings/PF-237-complete-lift-seam-spectral-type-blocks-direct-matched-normalizer-comparison|PF-237]];
- the same normalized Robin variational energy contraction used in PF-243;
- an exactly diagonal interior, so propagation by a fixed positive distance is exponentially smoothing in the `K` modes;

and nevertheless the separated source-to-bulk map fails

\[
F_d K^R P_Z\in\mathcal B(H)
\]

for **every** `R>0`, every fixed high cutoff `Z`, and every fixed observation distance `d>0`.

The failure mechanism is precise. The square root `Q^{1/2}` can send a sparse high-`K` input into one fixed low mode **before** the interior propagation acts. Fixed-distance propagation then damps that leaked component only by a constant. Thus spatial separation cannot manufacture tangential smoothing from one-sided form order alone.

This is not a counterexample to the canonical prime-flute seam and does not refute PF-243's estimates (20)--(21). It rules out a proof that uses only PF-238's form domination, positivity/energy contraction, and source separation. A positive PF proof must use additional structure of the **actual** seam relative to `K_a`: microlocal/spectral locality, commutator control, a pseudodifferential boundary calculus compatible with the endpoint compactification, or a finite physical trace realization that removes the bad high-to-low leakage channel.

## Claim

Let

\[
H=\ell^2(\{0,1,2,\ldots\}),
\qquad
Ke_0=e_0,
\qquad
Ke_n=n e_n\quad(n\ge1).
\tag{1}
\]

Then `K>=I` and `K^{-1}` is compact. Choose

\[
N_j=2^j,
\qquad
c_j=\frac1j,
\qquad
v=\sum_{j\ge2}c_j e_{N_j},
\qquad
V=\|v\|<\infty.
\tag{2}
\]

Let

\[
A=|e_0\rangle\langle v|+|v\rangle\langle e_0|,
\qquad
0<\varepsilon V<\frac14,
\tag{3}
\]

and define

\[
S=I+\varepsilon A,
\qquad
Q=S^2.
\tag{4}
\]

Then `S=Q^{1/2}` is positive and boundedly invertible, and

\[
0<Q\le (1+\varepsilon V)^2 I
\le (1+\varepsilon V)^2K.
\tag{5}
\]

In particular `Q` satisfies a uniform one-sided form domination by the first-order matched model `K`. Since `Q` itself is boundedly invertible on an infinite-dimensional space, `Q^{-1}` is noncompact, while `K^{-1}` is compact.

On the product half-strip `x>0`, consider the energy

\[
q[u]=\int_0^\infty
\left(\|u'(x)\|_H^2+\|Ku(x)\|_H^2\right)dx
\tag{6}
\]

and, for normalized boundary source `f in H`, the Robin variational problem

\[
q[u,z]+\langle S u(0),S z(0)\rangle
=\langle f,S z(0)\rangle.
\tag{7}
\]

Its decaying solution is

\[
u_f(x)=e^{-xK}a_f,
\qquad
(K+Q)a_f=Sf.
\tag{8}
\]

The usual variational test `z=u_f` gives the same normalized contraction currency as PF-243:

\[
q[u_f]+\|S a_f\|^2\le\|f\|^2.
\tag{9}
\]

For fixed `d>0`, define the separated energy observation

\[
F_df
:=K e^{-dK}(K+Q)^{-1}Sf.
\tag{10}
\]

This is the exact tangential-energy analogue of observing one PF-243 Poisson leg a fixed positive distance from its forcing boundary. Let

\[
P_Z=\mathbf1_{(Z,\infty)}(K).
\tag{11}
\]

Then, for every `R>0` and every fixed `Z,d>0`,

\[
\boxed{F_dK^RP_Z\text{ is unbounded}.}
\tag{12}
\]

Thus no positive smoothing order follows from (5), positivity, (9), and fixed source separation, even though the interior itself is exactly separable and exponentially smoothing mode by mode.

## 1. The seam has exactly the one-sided information available to the abstract argument

Because `e_0` is orthogonal to `v`,

\[
\|A\|=V,
\tag{13}
\]

so (3) gives

\[
(1-\varepsilon V)I\le S\le(1+\varepsilon V)I.
\tag{14}
\]

This proves positivity and bounded invertibility of `S` and `Q`. Equation (5) then follows from `K>=I`.

The comparison is deliberately one-sided. It says only that the seam energy is no harder than a first-order `K` seam. It gives no information about how `S=Q^{1/2}` moves spectral mass between distant `K` bands. That missing information is exactly what the countermodel exploits.

The compactness mismatch is also exact. If `Q^{-1}` were compact, then

\[
I=Q Q^{-1}
\]

would be compact, impossible on infinite-dimensional `H`. Hence the model retains the qualitative `compact matched inverse / noncompact soft inverse` distinction from PF-237 without importing any geometry from that finding.

## 2. The normalized Robin problem is an energy contraction

For a decaying solution of the product equation

\[
-u''+K^2u=0,
\tag{15}
\]

with boundary value `a`, one has `u(x)=e^{-xK}a` and the boundary energy operator is exactly `K`. Therefore (7) reduces to (8).

Testing (7) with `u_f` gives

\[
q[u_f]+\|Sa_f\|^2
=\langle f,Sa_f\rangle.
\tag{16}
\]

Since `\|Sa_f\|` is one summand of the left energy norm, Cauchy--Schwarz yields (9). Thus the failure below is not caused by loss of coercivity, an ill-posed Robin problem, or an unbounded normalized solution operator.

## 3. A sparse high input leaks into one fixed low mode before propagation

Fix `n=N_j`. Write

\[
a=(K+Q)^{-1}Se_n=a_0e_0+a_\perp.
\tag{17}
\]

Since

\[
A^2=V^2|e_0\rangle\langle e_0|+|v\rangle\langle v|,
\tag{18}
\]

the equation `(K+Q)a=Se_n` splits as

\[
\left(2+\varepsilon^2V^2\right)a_0
+2\varepsilon\langle v,a_\perp\rangle
=\varepsilon c_j,
\tag{19}
\]

and

\[
B a_\perp+2\varepsilon v a_0=e_n,
\qquad
B:=K_\perp+I+\varepsilon^2|v\rangle\langle v|.
\tag{20}
\]

Put

\[
D:=K_\perp+I,
\qquad
h:=\langle v,D^{-1}v\rangle.
\tag{21}
\]

The rank-one resolvent formula gives

\[
\langle v,B^{-1}e_n\rangle
=\frac{c_j}{(n+1)(1+\varepsilon^2h)},
\qquad
\langle v,B^{-1}v\rangle
=\frac{h}{1+\varepsilon^2h}.
\tag{22}
\]

Substituting `a_\perp=B^{-1}(e_n-2\varepsilon v a_0)` into (19) yields the exact scalar identity

\[
\begin{aligned}
&\left(
2+\varepsilon^2V^2
-\frac{4\varepsilon^2h}{1+\varepsilon^2h}
\right)a_0\\
&\qquad=
\varepsilon c_j
\left(
1-\frac{2}{(n+1)(1+\varepsilon^2h)}
\right).
\end{aligned}
\tag{23}
\]

The coefficient on the left is positive because it is the Schur complement of the positive operator `K+Q`. For `n=N_j>=4`, the parenthesis on the right is at least `1/2`, while the positive left coefficient is at most `2+\varepsilon^2V^2`. Hence

\[
\boxed{
a_0\ge
\frac{\varepsilon c_j}{2(2+\varepsilon^2V^2)}.
}
\tag{24}
\]

The key point is that this low-mode amplitude is proportional to `c_j`, not to an exponentially small function of the high input frequency `n`.

## 4. Fixed-distance propagation cannot repair pre-propagation leakage

For every fixed `Z`, all sufficiently large `N_j` lie in `P_ZH`. By linearity, (24) applied to the source `K^Re_{N_j}=N_j^Re_{N_j}` gives a low-mode component of `F_dK^Re_{N_j}` of size at least

\[
\frac{e^{-d}\varepsilon}{2(2+\varepsilon^2V^2)}
\,c_jN_j^R.
\tag{25}
\]

Here the factor `e^{-d}` is exactly the propagation of the fixed mode `e_0`; the exponentially small factor `e^{-dN_j}` never appears because `S` moved part of the source to `e_0` before propagation.

With `c_j=1/j` and `N_j=2^j`,

\[
\boxed{
c_jN_j^R=\frac{2^{jR}}j\longrightarrow\infty}
\qquad(R>0).
\tag{26}
\]

Equations (25)--(26) prove (12).

The same construction works with a smooth observation cutoff supported in any fixed interval `[d,d+delta]`: the low `e_0` component has a fixed positive `L^2` energy there. Thus the obstruction is not an artifact of sampling at one point in `x`.

## 5. What this rules out in the PF-243 route

PF-243 correctly notes that source separation alone is not yet smoothing. PF-244 makes the missing logical ingredient exact: even if the interior is a perfect product and even if the normalized Robin solution is an energy contraction, a nonlocal seam can defeat every polynomial tangential gain by **high-to-low spectral leakage at the forcing boundary**.

Therefore the chain

\[
Q^{\rm act}\le C Q^{\rm mat}
+\text{ positivity}
+\text{ fixed }X\text{-separation}
\quad\Longrightarrow\quad
\text{PF-243 (20)--(21)}
\tag{27}
\]

is false as an abstract implication.

A successful proof for the actual prime-flute seam must add a statement that excludes the mechanism in (23)--(26). Natural sufficient forms include quantitative decay of

\[
P_{\le M}(Q^{\rm act})^{1/2}P_{>N}
\tag{28}
\]

in the `K_a` spectral decomposition, iterated `K_a`-commutator estimates, a pseudodifferential/off-diagonal kernel description that survives the `tau<->theta` endpoint compactification, or a finite closed-cuff/physical trace realization in which the complete-lift translation channel is absent. PF-242's locality of the **shear multiplier** does not supply any of these seam statements.

The countermodel also explains why PF-238 and PF-237 fit together without contradiction. One-sided form domination controls energy size and was enough for PF-238's diagonal inverse-crossing factorization; it does not control the spectral direction in which the seam square root sends a high-frequency source.

## 6. Prior-art and novelty audit

No novelty is claimed for rank-one resolvent formulas, product half-strip Poisson kernels, or the general fact that quadratic-form order does not impose pseudodifferential locality. The calculation above is self-contained and imports no external theorem.

The closest positive regularity literature reinforces the boundary of the claim rather than closing the PF estimate. Große and Nistor, *Uniform Shapiro-Lopatinski conditions and boundary value problems on manifolds with bounded geometry*, Potential Analysis 53 (2020), 407--447, DOI `10.1007/s11118-019-09774-y`, arXiv:1703.07228, obtain uniform Robin regularity from strong ellipticity together with a uniform boundary regularity condition in bounded geometry. Grubb, *Local and nonlocal boundary conditions for mu-transmission and fractional elliptic pseudodifferential operators*, Analysis & PDE 7 (2014), 1649--1682, DOI `10.2140/apde.2014.7.1649`, arXiv:1403.7140, and *Green's formula and a Dirichlet-to-Neumann operator for fractional-order pseudodifferential operators*, Communications in Partial Differential Equations 43 (2018), 750--789, DOI `10.1080/03605302.2018.1475487`, arXiv:1611.03024, obtain Poisson/DtN mapping structure under explicit pseudodifferential ellipticity/symbol hypotheses.

Those results do not say that one-sided form domination of an arbitrary nonlocal Robin seam implies off-diagonal tangential smoothing. Conversely PF-244 does not challenge those theories: its seam is deliberately allowed to violate their microlocal locality assumptions. The project-specific delta is the exact calibration of **which surviving PF seam information is insufficient for the live PF-243 gate**.

## 7. Falsification and boundary checks

1. **Not an actual-seam counterexample.** `Q` in this model is an abstract bounded nonlocal seam. PF-244 does not show that the PF-205/PF-235 complete-lift seam has the leakage in (24).
2. **No claim that PF-243 is false.** The separated estimates may still hold because the actual seam has translation/pseudodifferential structure absent from the countermodel.
3. **The obstruction is not interior mode mixing.** The interior is exactly diagonal in `K`; all bad mixing occurs in `Q^{1/2}` before propagation.
4. **The obstruction survives arbitrary positive separation.** Increasing `d` changes only the fixed factor `e^{-d}` on the leaked low mode.
5. **The form bound is genuinely satisfied.** Equation (5) is stronger than a merely asymptotic one-sided estimate, yet gives no spectral off-diagonal control.
6. **The normalized energy bound is genuinely satisfied.** Equation (9) rules out an explanation based on unbounded Robin amplification.
7. **The compactness mismatch is only a calibration.** Matching PF-237's compact/noncompact inverse pattern does not make this abstract seam geometrically equivalent to the actual complete lift.
8. **No RH-level conclusion follows.** Weak-trace reassembly, physical `P/H` recoupling, finite-pant completion, wave/scattering theory, determinants/resonances, prime/clone separation, zeta zeros, and RH remain outside the result.

## Consequences for the research line

The current high-high shear frontier remains PF-243's accepted separated-Poisson question, but its proof obligation is now narrower. **Uniform interior ellipticity plus fixed propagation distance plus PF-238's one-sided seam domination cannot close it.** The next positive step must establish an actual-seam high-to-low locality theorem relative to `K_a`, or move to a physical finite trace realization where such locality can be proved directly.

This is a useful negative result because it prevents a generic Robin-regularity argument from being mistaken for the missing estimate. Any future proof of PF-243 (20)--(21) should identify explicitly which property of the canonical seam forbids the rank-two leakage mechanism above.