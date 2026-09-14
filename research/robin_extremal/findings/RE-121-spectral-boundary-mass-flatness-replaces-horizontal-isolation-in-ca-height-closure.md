# RE-121 — spectral boundary-mass flatness replaces horizontal isolation in CA-height closure

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + BOUNDARY-LAYER-DECOMPOSITION + LAPLACE-STIELTJES-ENVELOPE + SPECTRAL-FLATNESS-CONDITIONAL + ALL-ORDERS-HEIGHT-CLOSURE + HYPOTHESIS-WEAKENING + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume RH is false with a finite **attained** zero edge

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad c:=1-\Theta,
\tag{1}
\]

but do **not** assume the horizontal isolation hypothesis used in `RE-120`. Choose once and for all a fixed `sigma_0` with

\[
\frac12<\sigma_0<\Theta
\tag{2}
\]

in the off-critical range of `RE-112`, so that

\[
\sum_{\Re\rho\ge\sigma_0}\frac1{1+|\Im\rho|}<\infty.
\tag{3}
\]

Let `C` range over sufficiently large regular CA states and put

\[
Y:=\log C,
\qquad
\nu:=\log Y,
\qquad
B_\Theta(C):=Y^c\nu\,(e^{h(C)}-1).
\tag{4}
\]

For every fixed integer `K>=0`, the full high-strip zero source splits exactly at algebraic resolution into the attained edge hierarchy of `RE-120` plus a damped subedge term:

\[
\boxed{
B_\Theta(C)
=
\mathcal E_K(\nu)+\mathcal S_K(\nu)
+O_{\Theta,\sigma_0,K}(\nu^{-K-1}),
}
\tag{5}
\]

where

\[
\mathcal E_K(u)
:=J_0(u)+\sum_{k=1}^{K}\frac{(-1)^k k!}{u^k}J_k(u)
\tag{6}
\]

is the edge-only expansion from `RE-120`, and

\[
\boxed{
\mathcal S_K(u)
:=
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\beta:=\Re\rho<\Theta}}
 e^{-(\Theta-\beta)u}e^{i\gamma u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right],
\qquad \gamma:=\Im\rho .
}
\tag{7}
\]

Thus horizontal isolation in `RE-120` was sufficient only because it makes `mathcal S_K` exponentially small. It is not necessary. The exact replacement is a rate condition on the **weighted amount of zero spectrum approaching the edge**.

Define the positive weight

\[
w(\rho)
:=
\frac1{|\rho|\,|1-\rho|}
+
\frac1{|1-\rho|^2},
\tag{8}
\]

the cumulative near-edge mass

\[
\boxed{
W(t)
:=
\sum_{\substack{\sigma_0\le\Re\rho<\Theta\\
0<\Theta-\Re\rho\le t}}
w(\rho),
}
\tag{9}
\]

and its Laplace--Stieltjes envelope

\[
\boxed{
L(u)
:=
\sum_{\sigma_0\le\Re\rho<\Theta}
 w(\rho)e^{-(\Theta-\Re\rho)u}
=
\int_{(0,\Theta-\sigma_0]}e^{-ut}\,dW(t).
}
\tag{10}
\]

The measure is finite. Indeed `w(rho)<<_(Theta,sigma_0)(1+|gamma|^2)^(-1)`, and the ordinary Riemann--von Mangoldt zero count already makes that weight summable; (3) is stronger than needed for (9), but remains load-bearing in deriving the uniform high-strip expansion (5).

For every fixed `K`,

\[
\boxed{
|\mathcal S_K(u)|\ll_{\Theta,\sigma_0,K}L(u)
\qquad(u\ge1).
}
\tag{11}
\]

Moreover, for every real `A>0`, positivity of the measure gives the elementary rate equivalence

\[
\boxed{
W(t)=O(t^A)\ (t\downarrow0)
\quad\Longleftrightarrow\quad
L(u)=O(u^{-A})\ (u\to\infty).
}
\tag{12}
\]

Consequently, if

\[
W(t)=O(t^{K+1}),
\tag{13}
\]

then the `RE-120` edge-only expansion through order `K` remains valid with the same error **without any fixed horizontal zero gap**:

\[
\boxed{
B_\Theta(C)
=
J_0(\nu)
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{\nu^k}J_k(\nu)
+O(\nu^{-K-1}).
}
\tag{14}
\]

In particular, the full fixed-order closure of `RE-120` holds under the strictly weaker absolute spectral-flatness condition

\[
\boxed{
W(t)=O_A(t^A)
\quad\text{for every fixed }A>0,
}
\tag{15}
\]

even if subedge zero real parts accumulate at `Theta` and no horizontal gap exists.

Conversely, an algebraic CA-height anomaly forces quantitative mass into the shrinking boundary layer. If for some fixed `K` and some `0<=A<K+1` there is an unbounded regular-CA sequence on which

\[
\left|B_\Theta(C)-\mathcal E_K(\nu)\right|
\ge c_0\nu^{-A},
\tag{16}
\]

then along that sequence

\[
\boxed{
W\!\left(\frac{(A+1)\log\nu}{\nu}\right)
\gg_{c_0,K}
\nu^{-A}.
}
\tag{17}
\]

This sharpens the qualitative boundary layer isolated in `RE-120`: a lower-order failure is not merely associated with zeros somewhere in a strip of width `O(log nu/nu)`; it requires a definite amount of **weighted near-edge zero mass** there.

## 1. Keeping the complete high strip removes the gap hypothesis

The isolation assumption in `RE-120` was used only to replace every subedge zero by an exponentially small remainder. Instead retain all zeros with `beta>=sigma_0` explicitly.

The truncated Riemann--von Mangoldt formula used in `RE-112`--`RE-113`, together with the zero-density estimate behind (3), gives a uniformly summable high-strip expansion. The zeros below `sigma_0` contribute after `x^Theta` normalization

\[
O\!\left(x^{\sigma_0-\Theta}(\log x)^A\right),
\tag{18}
\]

while the omitted high-strip ordinate tail is bounded by the tail of (3). The same density estimate gives that tail a negative power of the truncation height. With `x=e^u`, both errors are therefore `O_M(u^{-M})` for every fixed `M`.

For a regular CA state let `Z` be the exact chamber parameter from `RE-119`, so `Y=Phi(Z)`, and put `u=log Z`. Repeating the selector calculation of `RE-120` without deleting the subedge zeros yields

\[
Z^c u\log\frac{\log Z}{\log Y}
=
\sum_{\Re\rho\ge\sigma_0}
\frac{e^{-(\Theta-\beta)u}e^{i\gamma u}}{\rho}
+O_M(u^{-M}).
\tag{19}
\]

All nonlinear selector terms contain an additional factor `Z^-c=e^{-cu}` and hence remain smaller than every inverse power of `u`.

For the reciprocal-Mertens coordinate, the exact single-zero identity from `RE-120` remains

\[
E_\rho(Z)
=
Z^{\rho-1}
\int_0^\infty
\frac{e^{-(1-\rho)s}}{u+s}\,ds.
\tag{20}
\]

Expanding `u/(u+s)` through order `K` and using the same integration-by-parts remainder bound as `RE-120` gives

\[
Z^c u E(Z)
=
\sum_{\Re\rho\ge\sigma_0}
 e^{-(\Theta-\beta)u}e^{i\gamma u}
\sum_{k=0}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
+O_K(u^{-K-1}).
\tag{21}
\]

The remainder is summable because its single-zero bound is

\[
\ll_{\Theta,K}\frac{u^{-K-1}}{1+|\gamma|},
\tag{22}
\]

and (3) applies. The ordinary prime-power/tax terms remain exponentially small exactly as in `RE-120`.

Adding (19) and (21), the `k=0` coefficient combines as

\[
\frac1\rho+\frac1{1-\rho}
=
\frac1{\rho(1-\rho)}.
\tag{23}
\]

Separating `beta=Theta` from `beta<Theta` gives `mathcal E_K+mathcal S_K`. The coefficient functions are uniformly Lipschitz: after one derivative the worst high-strip coefficient is `O((1+|gamma|)^(-1))`, again summable by (3). Since `u-nu=O(e^{-cu})`, replacing the selector phase `u` by the actual CA phase `nu`, and `Z^c u` by `Y^c nu`, changes the result by `O_M(nu^-M)` for every fixed `M`. This proves (5).

## 2. A positive boundary measure controls every fixed algebraic order

For fixed `K` and `u>=1`, the bracket in (7) obeys

\[
\left|
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right|
\ll_{\Theta,K} w(\rho).
\tag{24}
\]

Here `|1-rho|>=1-Theta=c`, so every fixed higher power of `(1-rho)^-1` is bounded by a `K`-dependent multiple of `|1-rho|^-2`. Taking absolute values in (7) proves (11).

The transform relation (10) is now a standard positive Laplace--Stieltjes situation, but no Tauberian theorem is needed. Let `D:=Theta-sigma_0`. If `W(t)<=Ct^A` for sufficiently small `t`, integration by parts gives

\[
L(u)
=e^{-uD}W(D)+u\int_0^D e^{-ut}W(t)\,dt
=O(u^{-A}).
\tag{25}
\]

Conversely, for `t>0`,

\[
L(1/t)
\ge
\sum_{0<\Theta-\beta\le t}w(\rho)e^{-(\Theta-\beta)/t}
\ge e^{-1}W(t),
\tag{26}
\]

so `L(u)=O(u^-A)` implies `W(t)=O(t^A)`. This proves (12). The same argument works with `o` in place of `O`.

Equations (5), (11), and (12) immediately prove (14)--(15). A genuine fixed horizontal gap is only the extreme special case in which `W(t)=0` for all sufficiently small `t`.

## 3. Algebraic failure forces quantitative near-edge mass

Let

\[
R_K(\nu):=B_\Theta(C)-\mathcal E_K(\nu).
\tag{27}
\]

From (5) and (11),

\[
|R_K(\nu)|
\ll_K L(\nu)+\nu^{-K-1}.
\tag{28}
\]

If (16) holds with `A<K+1`, then for large values on that sequence

\[
L(\nu)\gg\nu^{-A}.
\tag{29}
\]

Set

\[
t_\nu:=\frac{(A+1)\log\nu}{\nu}.
\tag{30}
\]

Splitting the transform at `t_nu` gives

\[
L(\nu)
\le
W(t_\nu)+e^{-\nu t_\nu}W(D)
=
W(t_\nu)+W(D)\nu^{-A-1}.
\tag{31}
\]

Combining (29)--(31) proves (17).

This is deliberately one-sided. A large positive envelope `L(nu)` does **not** force a large actual signed residual `S_K(nu)`: phases can cancel. Therefore non-flat boundary mass is a necessary source for an algebraic failure of the edge-only hierarchy, not a sufficient CA-height anomaly. The finding does not smuggle a Tauberian lower bound through an oscillatory zero sum.

## 4. Stress tests: no-gap spectra can be algebraically visible or invisible

Two abstract coefficient-level controls show that a fixed gap and all-orders closure are genuinely different hypotheses. They satisfy the summability pattern needed above but are **not** claimed to be realizable zero sets of the Riemann zeta function.

First take conjugate pairs with deficits `Delta_n=1/n`, ordinates `gamma_n=2^n`, and hence coefficient-scale weights `w_n asy 4^-n`. There is no horizontal gap, but

\[
W(t)\ll 4^{-1/t},
\tag{32}
\]

which is smaller than every power of `t`. Equation (15) therefore allows the complete edge-only algebraic hierarchy despite spectral accumulation at the edge.

As the opposite control, take `Delta_n=2^-n` and `gamma_n=2^n`. Then again the reciprocal-ordinate sum converges, while `w_n asy4^-n=Delta_n^2`, so

\[
W(t)\asymp t^2
\tag{33}
\]

up to the expected dyadic step oscillation. Correspondingly `L(u)` has exact `u^-2` scale on dyadic phases. Thus a nonisolated high strip can enter at a definite algebraic order while respecting the same basic summability used by the finite-edge argument.

These controls are used only to stress the logical sharpness of the rate classification. Because they are not asserted to be realizable zeta spectra, they are not evidence that the actual zeta source has an independent coordinate or that an algebraic anomaly really occurs.

## 5. Representation audit and evidence boundary

The primitive source retained by (7) is the actual nonedge high-strip zero data `(Theta-beta,gamma,rho)`. The map to `S_K(u)` is a damped oscillatory transform and is highly non-injective at one phase. No information-gain claim is made from the higher-dimensional representation itself.

The positive measure `W` is even coarser: it intentionally discards every phase and keeps only enough source mass to dominate the signed correction. Its purpose is a kill test. If `W` is superpolynomially flat, no fixed algebraic refinement of the CA height can distinguish the nonisolated branch from the isolated-edge hierarchy. If a fixed algebraic discrepancy is nevertheless observed, (17) certifies that the source must contain quantitatively non-negligible zero mass in the corresponding shrinking boundary layer.

Several stronger readings are invalid. Equation (15) is an additional spectral condition and is not known for zeta. The converse direction does not say that failure of (15) produces Robin counterexamples, favorable signs, or even a large `S_K`; oscillatory cancellation can still erase it. Nor does the result justify choosing `K=K(nu)` or summing the factorial Poincare hierarchy. Everything remains fixed-order, as in `RE-120`.

The finding also stays inside the attained finite-edge branch. If the edge is not attained, the obstruction of `RE-113` remains the relevant statement. The separate `Theta=1` branch is untouched.

## 6. Prior-art boundary and research consequence

Laplace--Stieltjes rate comparisons for positive measures belong to classical Abelian/Tauberian theory; modern quantified Ingham--Karamata results are much more general than the elementary estimate (25)--(26). No novelty is claimed for (12). Likewise, the August 2026 work of Broadbent--Fiori--Kadiri--Ng--Wilk supplies recent exact Riemann--Guinand formulas for Mertens sums, and the standard zero kernels underlying (20)--(21) are not new. Recent 2026 Robin/CA work located in the audit concerns explicit counterexample windows, smoothing, or finite verification rather than this hypothetical finite-edge boundary-mass classification.

The line-specific content is the splice: `RE-112` supplies off-critical reciprocal summability, `RE-119` supplies the exact regular-CA selector, and `RE-120` supplies the all-orders Mertens kernel. Retaining rather than deleting the subedge high strip yields (5), after which the positive boundary measure gives a precise weakening of horizontal isolation and the quantitative necessity statement (17). No external theorem is load-bearing, so `SOURCES.md` requires no new anchor.

The finite-edge frontier can therefore be stated more sharply. A fixed horizontal gap is no longer the essential dichotomy. The unresolved source is the **rate of weighted zero accumulation at the right edge**. Superpolynomially flat accumulation is invisible to every fixed algebraic CA-height correction; an algebraically visible failure requires polynomially detectable boundary mass in a `log nu/nu` layer. A closing theorem in the nonisolated branch must therefore constrain that near-edge mass or exploit signed phase information beyond its absolute envelope, rather than merely remove the gap hypothesis.