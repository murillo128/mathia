# ANF-005 — universal signed affine pair certificates pay an exact normalization slack

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + EXTREMAL-REDUCTION`. The finite-configuration inequalities below are elementary necessary conditions for any universal affine pair-count certificate; copositivity is classical terminology. The zeta-specific consequence is that a support-one signed pair kernel cannot preserve Lamzouri's zero-slack normalization while exploiting real-axis sign changes. Any such sign freedom must pay an explicit deterministic slack, and an unconditional improvement beyond Montgomery--Taylor must recover more in the BGSST pair functional than it loses through that slack.

## 1. General affine certificate and its slack

Let `F : C -> C` be an even entire function of real type,

\[
F(-z)=F(z),\qquad F(\bar z)=\overline{F(z)},
\]

and put

\[
d:=F(0)\in\mathbb R.
\]

For a finite multiset `Z` invariant under complex conjugation, let

\[
s(Z):=\#\{z\in Z\cap\mathbb R:m_z=1\}
\]

count its simple real elements, and define the ordered pair energy

\[
E_F(Z):=\sum_{z,s\in Z}F(z-s),
\]

with multiplicities. Suppose there is a real constant `A` such that the universal deterministic inequality

\[
\boxed{s(Z)\ge A|Z|-E_F(Z)}
\tag{1}
\]

holds for every nonempty finite conjugation-invariant multiset `Z`.

Define the **normalization slack**

\[
\boxed{\delta:=1+d-A.}
\tag{2}
\]

Lamzouri's Proposition 2.1 has `F=K^2`, `d=1`, `A=2`, hence `delta=0`. The point of (2) is that `delta` is not merely a choice of parametrization: tiny admissible configurations force it to control exactly how much sign freedom a universal affine certificate can have.

## 2. One- and two-point configurations give exact necessary inequalities

Take first a singleton `Z={0}`. It is one simple real point, so (1) gives

\[
1\ge A-d,
\]

or equivalently

\[
\boxed{\delta\ge0.}
\tag{3}
\]

Now take two distinct simple real points `Z={0,t}`, with `t in R`, `t != 0`. Since `F` is even,

\[
E_F(Z)=2d+2F(t).
\]

Equation (1) therefore gives

\[
2\ge2A-2d-2F(t),
\]

and hence

\[
\boxed{F(t)\ge-\delta\qquad(t\in\mathbb R).}
\tag{4}
\]

The value at `t=0` is already `d`, so the displayed inequality is relevant to distinct points; extending it to zero requires only the separate condition on `d` below.

Next take one nonreal conjugate pair `Z={iy,-iy}`, with `y != 0`. There are no real points and

\[
E_F(Z)=2d+2F(2iy),
\]

because `F` is even and of real type, so `F(iy)` is real. Equation (1) yields

\[
0\ge2A-2d-2F(2iy),
\]

therefore, after reparametrizing the imaginary argument,

\[
\boxed{F(iy)\ge1-\delta\qquad(y\in\mathbb R,\ y\ne0).}
\tag{5}
\]

Finally take a double real point, i.e. `Z` consists of two copies of `0`. Then `s(Z)=0` and `E_F(Z)=4d`, so

\[
0\ge2A-4d.
\]

Using (2),

\[
\boxed{d\ge1-\delta.}
\tag{6}
\]

Thus the same deterministic slack simultaneously pays for negative real-axis values, for loss of the unit lower barrier on the imaginary axis, and for lowering the diagonal normalization.

## 3. Large multiplicities force real translation-Gram copositivity

The two-point tests are not the only universal constraints. Fix distinct real points `x_1,...,x_k` and positive integers `c_1,...,c_k`. For an integer `M>=2`, form a multiset in which `x_j` has multiplicity `M c_j`. There are no simple real elements, while

\[
|Z|=M\sum_jc_j
\]

and

\[
E_F(Z)=M^2\sum_{i,j}c_ic_jF(x_i-x_j).
\]

Applying (1), dividing by `M^2`, and sending `M -> infinity` gives

\[
\boxed{
\sum_{i,j=1}^k c_i c_j F(x_i-x_j)\ge0.
}
\tag{7}
\]

By homogeneity and density this holds for all nonnegative real coefficient vectors. Hence every finite real translation Gram matrix

\[
\bigl(F(x_i-x_j)\bigr)_{i,j}
\]

must be **copositive**.

This is strictly weaker than positive semidefiniteness in general, so (7) does not collapse the signed route back to an ordinary positive-definite kernel. It is nevertheless a genuine configuration-level constraint that any proposed signed affine certificate must satisfy before number theory enters.

## 4. Zero slack forces the full nonnegative admissible class and recovers the Montgomery--Taylor ceiling

Set `delta=0`. Equations (4)--(6) give

\[
F(x)\ge0\quad(x\in\mathbb R),
\qquad
F(iy)\ge1\quad(y\in\mathbb R\setminus\{0\}),
\qquad
d\ge1.
\tag{8}
\]

Assume now that `F` is admissible for the support-one pair-correlation problem: its restriction to the real line is integrable and its Fourier transform is supported in `[-1,1]`. Define the classical pair-correlation functional

\[
M(F):=
\int_{\mathbb R}F(x)
\left(1-\left(\frac{\sin\pi x}{\pi x}\right)^2\right)dx.
\tag{9}
\]

Corollary 14 of Carneiro--Chandee--Littmann--Milinovich applies to **every nonnegative admissible** `R` with `R(0)>=1`, not merely to the particular factorization used in Lamzouri's proof, and gives

\[
M(R)\ge m_{\rm MT}
:=C_{\rm MT}-1
=0.3274992963206\ldots.
\tag{10}
\]

If `d>=1`, apply this to `R=F/d`. Since `M` is linear,

\[
M(F)=dM(F/d)\ge d\,m_{\rm MT}\ge m_{\rm MT}.
\tag{11}
\]

Therefore **every zero-slack universal affine certificate in the full real-axis-nonnegative support-one admissible class is capped by Montgomery--Taylor**. This slightly strengthens the boundary description in `ANF-002`: the relevant extremal theorem itself is not confined to the visibly factorized kernel `K^2`; nonnegative admissible entire functions factor in the reproducing-kernel Hilbert-space proof, and Corollary 14 solves the full one-delta nonnegative class.

This conclusion is independent of the `WI-118` screening argument. `WI-118` says real-axis nonnegativity of a support-one pair kernel forces Fourier-edge taper and therefore loses the critical-lattice boundary alias. Equation (11) says that, even before invoking that matched lattice obstruction, the classical pair-correlation functional already has the exact Montgomery--Taylor floor throughout the nonnegative admissible class.

## 5. For a signed kernel, the improvement criterion is `M(F) + delta < m_MT`

The useful consequence of allowing `delta>0` is that (4) permits real-axis sign changes. The cost is visible directly in the final asymptotic constant.

Write `F=\widehat J` with a real-even support-one profile `J`, under enough regularity for the BGSST evaluation and the standard derivative correction removing the Montgomery weight. Fourier duality gives

\[
C_F
:=J(0)+2\int_0^1\alpha J(\alpha)\,d\alpha
=d+M(F).
\tag{12}
\]

Indeed, the Fourier transform of `(sin(pi x)/(pi x))^2` is the triangle `(1-|alpha|)_+`, so (9) is exactly `C_F-d`.

Applying (1) to the scaled zeta-zero multiset then yields asymptotically

\[
\frac{N_0^s(T)}{N(T)}
\ge A-C_F-o(1)
=1-\delta-M(F)-o(1).
\tag{13}
\]

The Montgomery--Taylor/Lamzouri value is

\[
1-m_{\rm MT}=0.672500703679\ldots.
\]

Consequently a signed affine support-one improvement of this type must satisfy the exact necessary objective inequality

\[
\boxed{M(F)+\delta<m_{\rm MT}.}
\tag{14}
\]

while simultaneously satisfying (3)--(7) and the analytic BGSST admissibility conditions.

This is the clean tradeoff missing from the previous formulation of the live clue. Negative pair values do not come for free: if the universal inequality allows `F` to dip to roughly `-delta`, the deterministic intercept loses exactly the same `delta`. To beat Montgomery--Taylor, the reduction in the pair-correlation functional `M(F)` must be **strictly larger** than that loss.

## 6. What remains genuinely open

Equations (3)--(7) are necessary, not sufficient. In particular, finding a support-one `F` with

\[
M(F)+\delta<m_{\rm MT},
\quad F(x)\ge-\delta,
\quad F(iy)\ge1-\delta,
\]

and copositive real translation Grams would not by itself prove (1). It would only survive the cheapest universal falsifiers. A full counting inequality for arbitrary conjugation-invariant complex multisets would still have to be established.

Conversely, if the constrained Fourier extremal problem already satisfies

\[
M(F)+\delta\ge m_{\rm MT}
\]

for every BGSST-admissible `F` obeying these necessary finite-configuration constraints, then the whole **universal affine signed support-one** route is dead before any more elaborate Hilbert argument is attempted. This is now a precise analytic target.

The result does not apply to a genuinely non-affine/configuration-level counting functional, to matrix order or inertia used before global scalar pair compression, to support beyond one, to finite-`T` joint fluctuation information, or to higher-order zero correlations. Those remain distinct escape routes from `ANF-004`.

## 7. Prior-art and novelty assessment

Lamzouri's Proposition 2.1 supplies the zero-slack example `A=2`, `F=K^2`, `F(0)=1`; his Remark 3.4 points to Corollary 14 of Carneiro--Chandee--Littmann--Milinovich for optimality of the resulting constant. The latter paper defines the full admissible exponential-type class and proves the one-delta extremal theorem (10) for every nonnegative admissible function with value at least one at the origin. No novelty is claimed for those literature results, for Fourier duality in (12), or for the general notion of a copositive matrix.

A targeted prior-art search found the expected broad literature on Delsarte/linear-programming energy bounds and copositive optimization, but no source was located formulating the specific simple-real/conjugation-invariant affine slack tradeoff (2)--(7). Absence of a source is not a priority claim. The durable Mathia contribution is the exact interface reduction: **the signed support-one branch exposed by `ANF-004` has a compulsory deterministic slack, and its first possible improvement is governed by the combined objective `M(F)+delta`, not by `M(F)` alone.**

## 8. Decisive audit boundary

The finite-configuration part would be falsified by a universal inequality of the exact form (1) violating any of (3)--(7); each condition follows from an explicit one-, two-, or high-multiplicity real configuration.

The Montgomery--Taylor consequence would fail if Corollary 14 did not apply to the stated full nonnegative admissible class or if the identity `C_F=d+M(F)` used incompatible Fourier conventions. The primary source states the full nonnegative one-delta problem, and the triangle-transform calculation gives (12) under the conventions used here.

For future progress, the cheapest decisive test is now to solve or sharply bound the necessary constrained extremal problem in (14). A lower bound `M(F)+delta>=m_MT` would close the universal affine signed branch; an explicit strict sub-Montgomery--Taylor candidate would justify the harder next step of proving the full conjugation-invariant counting inequality.