# WI-321 — Arbitrary Hilbert-valued channelization cannot contract a scalar Weil semibound

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

**Parent findings:** WI-311, WI-317, WI-320.

WI-320 closes adaptive scalar feedback for the smooth **real** multiwindow localization class developed in WI-311: one short nonnegative test has nonnegative source-exact localization defect for every admissible real localizer, so feeding the same scalar lower semibound into all localized copies cannot strictly improve that scalar constant. A natural apparent escape is to allow complex phases, arbitrarily many auxiliary channels, or positive cross-channel mixing and hope that these carry information unavailable to real scalar windows.

They do not if the channels are only a representation of the same scalar source. Use Hilbert inner products conjugate-linear in the first variable. Let `K` be an arbitrary complex Hilbert space and let

\[
G\in C_c^\infty((-1/2,1/2);K),
\qquad
\int_{\mathbb R}\|G(u)\|_K^2\,du=1.
\tag{1}
\]

The scalar Weil form has a canonical Hilbert-space amplification `Q_K`; a scalar semibound on the support class used by the localized pieces,

\[
Q(h)\ge -c\|h\|_2^2
\tag{2}
\]

automatically amplifies to

\[
Q_K(F)\ge -c\|F\|_{L^2(K)}^2
\tag{3}
\]

for every smooth `K`-valued test in the same support class. The source-exact sliding identity also survives unchanged, with the channel autocorrelation

\[
R_G(a)=\int_{\mathbb R}\langle G(u),G(u+a)\rangle_K\,du.
\tag{4}
\]

On the same short real nonnegative witness used in WI-320, every prime-power term vanishes and Cauchy--Schwarz gives `Re R_G(a)<=1`; hence the localization defect is nonnegative for **every** normalized Hilbert-valued channelization, even when `K` and `G` are selected after the test is known. Thus neither infinitely many channels nor a continuum/direct-integral presentation creates new information if all channels still propagate only the scalar premise (2).

There is a second exact closure. Polarizing (2), for every finite scalar family `h_1,...,h_m` one already has the Loewner Gram inequality

\[
\boxed{
\bigl(B_Q(h_i,h_j)\bigr)_{i,j}
\succeq
-c\bigl(\langle h_i,h_j\rangle\bigr)_{i,j},
}
\tag{5}
\]

where `B_Q` is the Hermitian polarization of `Q`. Therefore fixed positive-semidefinite cross-channel metrics, positive matrix contractions, and Hilbert-space reparametrizations are not genuinely coupled state: they are consequences of the same scalar semibound. A surviving vector/matrix/mode route must propagate an admissible constraint **strictly stronger than (5)**, or introduce prime/mode-dependent information, an indefinite source-justified coupling, or a different decomposition.

No new zero-density or simple-critical-zero proportion is claimed.

## 1. Dimension-free Hilbert amplification of the Weil form

Vincent Liu's frozen source, already used in WI-304 and WI-320, works on arbitrary scalar complex tests

\[
\mathcal D_L=C_c^\infty((-L,L);\mathbb C)
\]

and writes the classical Weil form as

\[
Q(f)=\mathcal P(f)
+\frac1{2\pi}\int_{\mathbb R}A(t)|F_f(t)|^2\,dt
-\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n}\,H_f(\log n),
\tag{6}
\]

where

\[
h_f(a)=\int f(v+a)\overline{f(v)}\,dv,
\qquad
H_f(a)=\operatorname{Re}h_f(a),
\tag{7}
\]

and the pole term `P`, the archimedean symbol `A`, and the finite prime-power sum are the full classical source; no RH assumption enters this identity.

For an arbitrary complex Hilbert space `K` and a smooth compactly supported `K`-valued test `F` in a support class on which (2) holds, define `Q_K(F)` by the same source formula after replacing scalar products by Hilbert products: the archimedean factor becomes `||\widehat F(t)||_K^2`, the pole pairing becomes the corresponding Hilbert inner product, and

\[
h_F(a)=\int_{\mathbb R}\langle F(v),F(v+a)\rangle_K\,dv.
\tag{8}
\]

This is basis independent. To see both existence and compatibility with the finite-dimensional definition, let `K_F` be the closed span of the ranges of `F` and its derivatives. It is separable, because each derivative has compact image and there are only countably many derivatives. Choose an orthonormal basis `(e_j)` of `K_F`, put `F_j=\langle e_j,F\rangle`, and let `P_N` project onto the first `N` basis vectors. Then

\[
Q_K(P_NF)=\sum_{j=1}^N Q(F_j).
\tag{9}
\]

The vector Fourier transform satisfies

\[
\widehat{P_NF}(t)=P_N\widehat F(t),
\]

so `||\widehat{P_NF}(t)||<=||\widehat F(t)||`. Smooth compact support gives rapid decay of the Hilbert norm of `\widehat F(t)`, enough to dominate the logarithmically growing archimedean symbol. The pole evaluations converge directly, and the prime sum is finite. Hence dominated convergence in (6) gives

\[
Q_K(P_NF)\longrightarrow Q_K(F),
\qquad
\|P_NF\|_2\longrightarrow\|F\|_2.
\tag{10}
\]

Applying the scalar premise (2) to the finitely many coordinates in (9) and passing to the limit proves (3). Thus the scalar semibound tensorizes with the identity on **every** auxiliary Hilbert space; finite channel number was never a load-bearing hypothesis.

This also handles nonseparable ambient spaces. Every individual smooth compactly supported `K`-valued test lives in the separable closed subspace `K_F`, so no uncountable-coordinate summation is needed.

## 2. The source-exact sliding identity is also dimension free

For scalar

\[
f\in C_c^\infty((-L,L);\mathbb C)
\]

define

\[
F_y(u):=G(u)f(u+y)\in K.
\tag{11}
\]

Bochner--Fubini gives the exact norm identity

\[
\int_{\mathbb R}\|F_y\|_{L^2(K)}^2\,dy
=\|f\|_2^2.
\tag{12}
\]

The two relevant autocorrelations are

\[
h_f(a)=\int f(v+a)\overline{f(v)}\,dv,
\qquad
R_G(a)=\int\langle G(u),G(u+a)\rangle_K\,du.
\tag{13}
\]

The channel factorization is basis free:

\[
\int_{\mathbb R} h_{F_y}(a)\,dy
=R_G(a)h_f(a).
\tag{14}
\]

Equation (14) can be inserted directly into the scalar source (6). Equivalently, approximate `G` by normalized finite-rank projections and pass to the limit in the already proved finite-dimensional identity. Because `G` is smooth and compactly supported, those projections converge in every needed `L^2` derivative norm. Near `a=0`, normalized autocorrelations satisfy `1-Re R_G(a)=O(a^2)` and `Im R_G(a)=O(a)` uniformly along the finite-rank approximants; the same smooth expansion for `h_f` makes the real product in (16) `O(a^2)`. Hence the apparent `1/a` singularity of the continuous source remains uniformly integrable.

The resulting exact identity is

\[
Q(f)=\int_{\mathbb R}Q_K(F_y)\,dy-\mathcal E_G(f),
\tag{15}
\]

with

\[
\begin{aligned}
\mathcal E_G(f)
={}&\int_0^{2L}K_0(a)
\operatorname{Re}\!\left((1-R_G(a))h_f(a)\right)\,da\\
&+\sum_{\log n<2L}
\frac{2\Lambda(n)}{\sqrt n}
\operatorname{Re}\!\left((1-R_G(\log n))h_f(\log n)\right),
\end{aligned}
\tag{16}
\]

where

\[
K_0(a)=
\frac{2e^{-a/2}}{1-e^{-2a}}-4\cosh(a/2).
\tag{17}
\]

Thus allowing an infinite or continuum channel space does not alter the source correction. All channel geometry reaches the defect through the single scalar matrix coefficient `R_G`.

## 3. One short witness defeats every Hilbert-valued channelization

Let `rho>1` be the real root of

\[
\rho^3-\rho-1=0
\]

and put

\[
h_0=\log\rho.
\]

WI-320 derives exactly

\[
K_0(a)>0\quad(0<a<h_0),
\qquad
h_0<\log2.
\tag{18}
\]

Choose

\[
0<d<\min\{2L,h_0\}
\tag{19}
\]

and a nonzero real nonnegative

\[
f\in C_c^\infty((-L,L))
\]

supported in an interval of diameter strictly smaller than `d`. Then

\[
h_f(a)=\int f(v+a)f(v)\,dv\ge0
\tag{20}
\]

and

\[
h_f(a)=0\qquad(a\ge d).
\tag{21}
\]

Since `d<h_0<log 2`, every prime-power term in (16) vanishes exactly.

Now regard `G` as a unit vector of the Hilbert space `L^2(\mathbb R;K)`. Translation is unitary, so Cauchy--Schwarz gives, in arbitrary Hilbert dimension,

\[
|R_G(a)|\le1,
\qquad
\operatorname{Re}R_G(a)\le1.
\tag{22}
\]

On the chosen real witness,

\[
\operatorname{Re}\!\left((1-R_G(a))h_f(a)\right)
=(1-\operatorname{Re}R_G(a))h_f(a)\ge0.
\tag{23}
\]

Equations (18)--(23) reduce (16) to

\[
\boxed{
\mathcal E_G(f)
=\int_0^d
K_0(a)(1-\operatorname{Re}R_G(a))h_f(a)\,da
\ge0.
}
\tag{24}
\]

The same fixed scalar `f` works for every complex Hilbert space `K` and every normalized smooth `G`. No phase choice, channel cardinality, carrier frequency, direct-sum decomposition, or adaptive selection can make the defect negative on this witness.

Using (3) and (12),

\[
\int_{\mathbb R}Q_K(F_y)\,dy
\ge
-c\int_{\mathbb R}\|F_y\|_2^2\,dy
=-c\|f\|_2^2.
\tag{25}
\]

Combining (15), (24), and (25), a strict uniform contraction from `c` to `c-kappa`, `kappa>0`, would require some admissible channelization with

\[
\mathcal E_G(f)\le-\kappa\|f\|_2^2
\tag{26}
\]

for every nonzero `f`. The witness above violates that necessary condition for all `K,G`. Hence

\[
\boxed{
\text{arbitrary complex Hilbert-valued channelization cannot strictly improve a scalar Weil semibound}
}
\tag{27}
\]

when the only information propagated through the localized pieces is that same scalar semibound.

## 4. Polarization closes fixed positive cross-channel metrics as an escape

There is an equivalent finite-matrix form of the same obstruction that makes the information boundary sharper.

Let `B_Q` be the Hermitian sesquilinear polarization of `Q`. For arbitrary scalar tests `h_1,\ldots,h_m`, define

\[
M_{ij}:=B_Q(h_i,h_j),
\qquad
S_{ij}:=\langle h_i,h_j\rangle_{L^2}.
\tag{28}
\]

For every `z\in\mathbb C^m`,

\[
z^*(M+cS)z
=
Q\!\left(\sum_i z_i h_i\right)
+c\left\|\sum_i z_i h_i\right\|_2^2
\ge0.
\tag{29}
\]

Therefore the scalar semibound (2) is equivalent, over all finite families, to the Loewner statement

\[
\boxed{M\succeq-cS.}
\tag{30}
\]

The converse is already the one-channel case. Thus cross-channel covariance generated only by polarization is not extra state: it is precisely the scalar premise tested simultaneously in several directions.

In particular, for every fixed positive-semidefinite channel weight `W`,

\[
\operatorname{Tr}(WM)
\ge
-c\,\operatorname{Tr}(WS).
\tag{31}
\]

Factorizing `W=C^*C` shows the same fact directly: the weighted cross-channel form is a sum of scalar Weil forms of the mixed channels determined by `C`. Passing to a completion gives exactly the arbitrary-Hilbert amplification of Section 1.

Consequently a **fixed PSD matrix metric with off-diagonal entries is not a surviving coupled-matrix mechanism**. To add information beyond the scalar lower bound, a matrix/vector state must impose constraints not implied by (30): for example source-specific relations among several observables, a prime- or mode-resolved admissible set, an indefinite coupling backed by an independent zero-side inequality, or a genuinely different coercivity/inertia invariant.

## 5. Stress tests and exact boundary

**Complex tests are legal.** Liu's frozen manuscript defines the classical source on `C_c^\infty((-L,L);\mathbb C)`. The argument never applies a real-only theorem to complex localized pieces.

**Infinite channel dimension adds no convergence hypothesis beyond smooth compact support.** Every individual `K`-valued test occupies a separable closed subspace. Finite-rank projections converge source by source, with the archimedean integral dominated by rapid Fourier decay. The proof therefore covers separable and nonseparable ambient Hilbert spaces alike.

**The imaginary autocorrelation is retained until the decisive witness.** For a general complex `f`, the defect is (16), not `(1-Re R_G)H_f`; imaginary parts of `R_G` and `h_f` may interact. The simplification occurs only for the real nonnegative short witness.

**The pole and archimedean terms are not omitted.** They are already included in the audited source kernel `K_0`. The proof uses its exact positive interval, not a prime-only surrogate.

**Every arithmetic atom vanishes exactly.** The witness diameter is below `h_0<log2`, while every prime-power lag is at least `log2`. No asymptotic density or truncation estimate is used.

**Adaptive Hilbert spaces are allowed.** `K` itself may vary with the chosen localizer and may be selected after observing the test. The same scalar witness works pointwise for every choice.

**Positive matrix cross terms are covered only when they are consequences of the scalar premise.** Equation (30) closes the canonical polarized Loewner amplification and every positive contraction of it. A stronger matrix theorem with additional arithmetic restrictions is outside the result and remains potentially useful.

**Indefinite or source-specific couplings remain outside.** A sign-indefinite channel functional does not follow from (30) merely because it is formally writable. It needs a separate source-valid inequality. Likewise a localization rule that destroys the factorization (14) requires a new exact source identity.

The finding is therefore a no-go for representational enlargement of scalar feedback, not a no-go for non-scalar information and not an RH result.

## 6. Prior art and novelty audit

The load-bearing source identity is literature-backed by Vincent Liu, **Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function**, frozen source commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`. Its manuscript explicitly defines the classical Weil form for arbitrary complex smooth tests and gives the scalar sliding-localization defect used in WI-304/WI-320. The frozen source was checked directly for the domain, pole term, archimedean integral, finite prime-power truncation, and localization identity before using it here.

Hilbert-space tensor amplification, finite-rank approximation, polarization of semibounded Hermitian forms, Bochner--Fubini, and Cauchy--Schwarz are classical functional analysis. The arbitrary-`K` passage does not claim a new tensor-product theorem. A targeted search around Hilbert/vector-valued IMS localization, semibounded quadratic-form amplification, matrix-valued Weil forms, and vector-valued Weil localization located the generic Hilbert/tensor machinery but no source stating the Weil-specific all-channel obstruction (24)--(27) or using the prime-free positive bump to close it. Search absence is not a priority claim.

Within the local `weil_inertia` corpus, WI-144 concerns positive-Hilbert/Frobenius **support-one tail-sign** lifts, while WI-154--WI-155 concern matrix one-delta/Loewner Lamzouri kernels. WI-317--WI-320 concern source-exact scalar localization. The present claim is distinct: it proves that arbitrary Hilbert multiplicity and the canonical polarized Loewner Gram structure add no information to that scalar-feedback architecture.

The Mathia contribution recorded here is therefore narrow and exact: the WI-320 short witness and the audited source identity are dimension-free once the scalar form is amplified correctly, and the canonical matrix Gram bound is already equivalent to the scalar semibound.

## 7. Consequence for the Weil-inertia program

The scalar-localization no-go is not an artifact of real windows, finite channel number, or diagonal coordinates. Arbitrary Hilbert multiplicity and fixed positive cross-channel mixing leave the information content unchanged.

This sharpens the surviving `vector/matrix/mode-dependent state` route. A useful state must reduce the admissible set beyond what scalar semiboundedness plus polarization already imposes. Merely adding channels, allowing a continuum of channels, applying unitary/positive mixing, or retaining the canonical Gram matrix cannot create the missing defect-to-zero contraction.

The RH-facing target is therefore genuinely information-theoretic rather than representational: find a source-justified invariant whose localized constraints are strictly stronger than (30), or a different inertia/coercivity mechanism that does not bootstrap the same scalar lower bound through copies of itself.
