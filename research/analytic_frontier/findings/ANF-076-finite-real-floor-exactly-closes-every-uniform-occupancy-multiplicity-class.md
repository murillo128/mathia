# ANF-076 — the finite-real floor exactly closes every uniform-occupancy multiplicity class

**Status:** `EXACT-DERIVED + REAL-MULTIPLICITY + UNIFORM-OCCUPANCY-CLOSURE + AMPLITUDE-OPTIMIZED + CENTRAL-NOTCH-SURVIVOR + HETEROGENEOUS-OCCUPANCY-FRONTIER`. `ANF-017` introduced the finite-real floor

\[
q_{\rm real}(J)
:=
\inf_{\substack{X\subset\mathbb R\\0<|X|<\infty}}
\frac{1}{|X|}E_{\widehat J}(X)
\]

and used one simple support together with its doubled copy as a necessary amplitude-optimized test. `ANF-075` later showed that arbitrarily narrow central notches survive every *fixed* cap on the number of distinct real support sites, leaving support cardinality growing on the reciprocal-notch scale as a possible real-multiplicity obstruction.

There is an exact complementary closure. The `q_real` envelope is not merely necessary for doubled supports: it is **sufficient and sharp for every real multiset having the same multiplicity at every occupied site, with no bound at all on the number or geometry of those sites**.

Let `J>=0` be continuous, even and supported in `[-1,1]`, put

\[
F=\widehat J,
\qquad
C=C(J),
\qquad
q=q_{\rm real}(J),
\tag{1}
\]

and let `t>0` scale the whole spectral shape. Define the uniform-occupancy class

\[
\mathcal U
:=
\{rX:\ X\subset\mathbb R\text{ finite, nonempty and distinct},\ r\in\mathbb N\},
\tag{2}
\]

where `rX` means that every site of `X` occurs with multiplicity exactly `r`. For the affine inequality

\[
s(Z)\ge A|Z|-E_{tF}(Z),
\tag{3}
\]

required only on `Z in U`, the largest admissible intercept is exactly

\[
\boxed{
A_{\mathcal U}(t)
=
\psi(tq),
\qquad
\psi(u):=\min\{1+u,2u\}.
}
\tag{4}
\]

Consequently, if `q>0`, the best simple-critical-zero lower bound allowed by the entire unbounded-support uniform-occupancy class is exactly

\[
\boxed{
\sup_{t>0}\bigl(A_{\mathcal U}(t)-tC\bigr)
=
\max\left\{0,2-\frac{C}{q}\right\}.
}
\tag{5}
\]

Thus the scale-free ratio `C/q_real` from `ANF-017` completely solves this infinite multiplicity family, rather than only furnishing a necessary obstruction.

For every central-notch separator `J_s` supplied by `ANF-034`,

\[
\frac{C(J_s)}{q_{\rm real}(J_s)}<C_{\rm MT}.
\tag{6}
\]

Taking the single amplitude

\[
\boxed{t=q_{\rm real}(J_s)^{-1}}
\tag{7}
\]

and `A=2` therefore proves (3) simultaneously for **every** uniform-occupancy real multiset, at arbitrary support cardinality, while yielding

\[
\boxed{
2-rac{C(J_s)}{q_{\rm real}(J_s)}
>
2-C_{\rm MT}.
}
\tag{8}
\]

Hence large support by itself cannot furnish a shape-level real-multiplicity no-go for the central-notch separator. Combined with `ANF-075`, the remaining real-multiplicity frontier is genuinely **heterogeneous occupancy at growing support cardinality**: a family capable of obstructing the narrowing central-notch mechanism must use multiplicities that vary across sites, and its number of occupied sites cannot remain bounded as the notch narrows.

This does not prove that one common amplitude/intercept already handles the union of all finite-support heterogeneous patterns and all unbounded uniform patterns. Equations (4)--(8) classify the uniform-occupancy family exactly; `ANF-075` separately classifies every fixed support cap. The unresolved problem is the support-uniform heterogeneous envelope.

## 1. Uniform replication has exact quadratic energy scaling

Fix a finite set of distinct real sites

\[
X=\{x_1,\ldots,x_n\},
\qquad n\ge1,
\]

and write

\[
e_J(X):=\frac1nE_F(X).
\tag{9}
\]

For `r>=1`, the multiset `rX` has size `rn`, structure factor `rS_X`, and therefore

\[
\boxed{
E_{tF}(rX)
=t r^2 E_F(X)
=t r^2 n e_J(X).
}
\tag{10}
\]

The simple-real bookkeeping has only two branches:

\[
s(rX)
=
\begin{cases}
n,&r=1,\\
0,&r\ge2.
\end{cases}
\tag{11}
\]

Substituting `r=1` into (3) gives

\[
A\le1+t e_J(X).
\tag{12}
\]

For `r>=2`, equations (10)--(11) give

\[
A\le tr e_J(X).
\tag{13}
\]

Because `e_J(X)>=0` for `J>=0`, the strongest repeated branch is always `r=2`. Therefore a fixed support `X` imposes exactly

\[
A\le
\min\{1+t e_J(X),2t e_J(X)\}
=
\psi(t e_J(X)).
\tag{14}
\]

No higher common multiplicity can strengthen the doubled support. This is true for every finite geometry, not only lattices or two-site configurations.

## 2. Taking the finite-real infimum gives both necessity and sufficiency

By definition,

\[
e_J(X)\ge q
\qquad\text{for every finite distinct real }X.
\tag{15}
\]

Since `psi` is continuous and increasing on `[0,infinity)`, equations (14)--(15) show that

\[
A\le\inf_X\psi(t e_J(X))
=
\psi(tq)
\tag{16}
\]

is necessary for (3) on the whole class `U`.

The same inequality is also sufficient. If

\[
A\le\psi(tq),
\tag{17}
\]

then for every `X`,

\[
A\le\psi(tq)\le\psi(t e_J(X)),
\tag{18}
\]

so both the simple inequality (12) and the doubled inequality `A<=2te_J(X)` hold. Equation (13) for every `r>2` is weaker than the doubled inequality. Hence (3) holds for every `rX in U`.

This proves the exact identity (4), including the case where the infimum defining `q` is not attained. No compactness or minimizing configuration is required.

The result is stronger than the duplicated-lattice envelope of `ANF-013`: the support `X` may be completely irregular and have arbitrarily many sites. It also turns the finite-support argument of `ANF-017` around. There, `X` and `2X` were used to obtain an upper bound on what a shape could achieve. Here the same two branches, after taking the global infimum `q_real`, are shown to be the **complete** constraints for all constant-multiplicity real multisets.

## 3. Amplitude optimization is exactly the `C/q_real` ratio

Assume first that `q>0`. The pair-correlation cost of the scaled spectrum is `tC`, so the best lower bound permitted by the class `U` at amplitude `t` is

\[
B_{\mathcal U}(t)
=
\psi(tq)-tC.
\tag{19}
\]

Put

\[
x=tq,
\qquad
R=\frac{C}{q}.
\tag{20}
\]

`ANF-013`--`ANF-017` give `q<=C`, hence `R>=1`. Equation (19) becomes

\[
B_{\mathcal U}
=
\begin{cases}
(2-R)x,&0<x\le1,\\
1-(R-1)x,&x\ge1.
\end{cases}
\tag{21}
\]

If `1<=R<2`, both branches are maximized at the junction `x=1`, giving

\[
\sup_{t>0}B_{\mathcal U}(t)=2-R.
\tag{22}
\]

If `R>=2`, the supremum is `0`, approached as `t downarrow0`. This proves (5). If `q=0`, equation (4) gives `A_U(t)=0` for every positive `t`, so again no positive bound is available.

At the nontrivial optimum `t=1/q`, equation (4) gives

\[
A_{\mathcal U}=2.
\tag{23}
\]

There is also a direct verification that is useful for auditing. Since `te_J(X)>=1`, a simple support satisfies

\[
2n-tne_J(X)\le n=s(X),
\tag{24}
\]

while for every `r>=2`,

\[
2rn-tr^2ne_J(X)
=rn\bigl(2-rte_J(X)\bigr)
\le0=s(rX).
\tag{25}
\]

Thus a single amplitude simultaneously handles every geometry, every support cardinality and every common occupancy.

## 4. Central-notch separators survive arbitrary support under uniform occupancy

`ANF-034` constructs central-notch spectra

\[
J_s=J_{\rm MT}-s\phi_\eta\ge0
\tag{26}
\]

for which the finite-real separation is uniform and strict:

\[
q_{\rm real}(J_s)
>
\frac{C(J_s)}{C_{\rm MT}}.
\tag{27}
\]

In particular `q_real(J_s)>0`, and (27) is equivalent to (6). Applying the exact uniform-occupancy optimization (5) therefore gives

\[
\sup_t B_{\mathcal U}(t)
=
2-rac{C(J_s)}{q_{\rm real}(J_s)}
>
2-C_{\rm MT}.
\tag{28}
\]

The optimal scale for this subfamily is the global one in (7); it does not depend on `|X|`, on the positions of the sites, or on their common multiplicity.

This removes two tempting continuations of `ANF-075`. First, taking more and more equally occupied sites cannot eventually reveal a new real obstruction: the exact `q_real` floor has already absorbed that entire limit. Second, replacing long duplicated lattices by irregular but still uniformly doubled clouds also adds no new shape-level information. Their normalized simple-support energy is already one of the configurations entering `q_real`.

The obstruction left by `ANF-075` must therefore exploit the integer weight vector itself. For a general real multiset with support `X={x_1,...,x_r}` and unequal multiplicities `k_i`, the energy is

\[
E_F(k;X)
=
\sum_{i,j}k_i k_jF(x_i-x_j),
\tag{29}
\]

whereas `q_real` controls only the special coefficient vector `(1,...,1)`. Positive spectral density makes the Gram matrix positive semidefinite, but that alone does not compare arbitrary positive integer vectors with the uniform vector strongly enough to reduce (29) to `q_real`. `ANF-074` closes this weighted problem when there are at most two support sites; `ANF-075` closes every fixed support cap after narrowing the notch. The first unclassified real regime is therefore a genuinely weighted, growing-dimensional stability problem.

## 5. Interaction with the reciprocal-width frontier

`ANF-075` proves that for every prescribed support cap `R`, sufficiently narrow central notches survive **all** multiplicity vectors on at most `R` sites while retaining a strict Montgomery--Taylor improvement. Its scalable width condition is

\[
\eta_R
=3R-\sqrt{9R^2-3}
=\frac1{2R}+O(R^{-3}).
\tag{30}
\]

Hence any family intended to furnish a uniform real-multiplicity no-go against the narrowing notch must already have support cardinality growing on the reciprocal-width scale. The present finding adds an independent requirement: unbounded support is still insufficient if the multiplicity vector remains constant.

Accordingly, a decisive real-only attack should no longer spend effort on larger equal-double lattices, equal-occupancy irregular clouds, or any other constant replication of a simple support. It should study weighted Gram energies with both

\[
r\to\infty
\qquad\text{and}\qquad
(k_1,\ldots,k_r)\not\propto(1,\ldots,1),
\tag{31}
\]

with `r` coupled to `eta^{-1}` if the goal is to obstruct the entire narrowing family.

This is a classification of the remaining falsifier geometry, not a proof that such heterogeneous configurations exist or that they kill the central notch. The next useful scalar object would be a **weighted finite-real floor** or a support-uniform stability inequality that retains the simple-point penalty while optimizing over nonconstant positive integer weights. Any such proposal must reduce to (4) on the uniform ray and to `ANF-074` on two support sites.

## 6. Prior art, audit, and evidence boundary

Uniform particle replication and quadratic pair-energy scaling are elementary features of classical many-particle systems, and positive-type stability is part of the Fisher--Ruelle/Sütő framework already neighboring `ANF-018`. A targeted current literature check found the expected general stability and bounded-potential clustering literature, including classical work where multiply occupied sites occur, but no external theorem is needed for (4)--(5). No novelty is claimed for the fact that pair energies scale quadratically under common replication.

The Mathia-specific content is the exact interaction with the affine simple-real count and the already isolated finite-real floor: the same `q_real` that was previously used as a necessary shape test is now proved to be a complete amplitude-optimized invariant for the entire unbounded-support uniform-occupancy class. Existing stability anchors in `SOURCES.md` are sufficient; no new load-bearing source is added.

The audit has four load-bearing steps:

1. `E_F(rX)=r^2E_F(X)` is exact because the structure factor is multiplied by `r`.
2. `s(rX)=|X|` only for `r=1`, and is zero for every `r>=2`; therefore the repeated branch is strongest at `r=2` when `e_J(X)>=0`.
3. `J>=0` gives `e_J(X)>=0`, and the definition of `q_real` gives `e_J(X)>=q` uniformly over all finite distinct real supports.
4. `ANF-034` supplies the strict ratio `C(J_s)/q_real(J_s)<C_MT`; no numerical estimate or attainment of `q_real` is assumed.

The finding does **not** establish the universal affine certificate, improve the unconditional zeta-zero proportion, or imply RH. It settles one infinite real-multiplicity subclass exactly. Heterogeneous real occupancies of growing support, nonreal multi-pair configurations, and richer pre-compression information carriers remain outside the theorem.