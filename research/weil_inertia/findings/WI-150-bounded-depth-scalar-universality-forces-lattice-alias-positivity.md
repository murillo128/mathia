# WI-150 — bounded-depth compact-spectrum scalar universality forces lattice-alias positivity

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE`. WI-149 shows that bounded off-line depth forces Gaussian-smoothed positivity for a universal Lamzouri-form scalar kernel, but pointwise consequences for a moving family there require regularity because the Gaussian microscope has finite resolution. The fixed-period binomial probes below give a complementary exact statement for compactly supported spectral profiles: they recover point samples without any derivative bound, at the unavoidable cost of sampling the entire harmonic lattice through that point.

Let `B>0`, let `phi : R -> R` be continuous and real-even, with

\[
\int_{\mathbb R}\phi(t)\,dt=1,
\qquad
\operatorname{supp}\phi\subset[-S,S]
\tag{1}
\]

for some finite `S>0`, and define

\[
H(z)=\int_{\mathbb R}\phi(t)e^{-2\pi i zt}\,dt.
\tag{2}
\]

Suppose the Lamzouri-form scalar inequality

\[
s(\mathcal Z)\ge 2|\mathcal Z|-\sum_{z,w\in\mathcal Z}H(z-w)
\tag{3}
\]

holds for every nonempty finite conjugation-invariant multiset `Z` contained in `|Im z|<=B`. Then, for every `a>0` and every `0<b<B`, one necessarily has the exact lattice-alias inequality

\[
\boxed{
\sum_{n\in\mathbb Z}
\phi(na)\cosh^2(2\pi bna)\ge0.
}
\tag{4}
\]

The sum is finite because of (1). Passing `b\uparrow B` therefore also gives

\[
\boxed{
\sum_{n\in\mathbb Z}
\phi(na)\cosh^2(2\pi Bna)\ge0.
}
\tag{5}
\]

This is an exact bounded-depth interpolation between WI-146 and WI-147--WI-149. A fixed negative spectral value cannot be repaired by arbitrary remote positive mass under the full universal finite-multiset hypothesis: for these probes, its compensating mass must appear at the distinguished point `0` or at exact integer harmonics of the tested radius.

## 1. Exact spectral form inherited from Lamzouri universality

As in WI-149, for a finite conjugation-invariant multiset `Z` put

\[
S_{\mathcal Z}(t)=\sum_{z\in\mathcal Z}e^{-2\pi i tz}.
\tag{6}
\]

Compact support makes all Fourier--Laplace manipulations below absolute. Conjugation invariance gives

\[
Q_H(\mathcal Z)
:=\sum_{z,w\in\mathcal Z}H(z-w)
=
\int_{\mathbb R}\phi(t)|S_{\mathcal Z}(t)|^2\,dt.
\tag{7}
\]

For a multiset with no real elements, `s(Z)=0`, so (3) implies

\[
Q_H(\mathcal Z)\ge2|\mathcal Z|.
\tag{8}
\]

This is exactly the finite spectral interface already isolated in WI-149 from Lamzouri's Proposition 2.1. No zeta asymptotic, pair-correlation theorem, Gram representation, or positivity assumption on `phi` is used after (8).

## 2. Fixed-period binomial probes converge to a Dirac comb

Fix `a>0`, `0<b<B`, and an integer `m>=1`. For each `0<=j<=m`, give the horizontal location `j/a` multiplicity `binom(m,j)` and put conjugate points

\[
\frac ja+ib,
\qquad
\frac ja-ib
\tag{9}
\]

with that multiplicity. Denote the resulting multiset by `Z_m`. It has no real points, lies in the allowed strip, and

\[
|\mathcal Z_m|=2^{m+1}.
\tag{10}
\]

Its horizontal exponential polynomial is

\[
P_m(t)
=
\sum_{j=0}^{m}\binom mj e^{-2\pi i tj/a}
=
(1+e^{-2\pi i t/a})^m,
\tag{11}
\]

so

\[
|P_m(t)|^2
=4^m\cos^{2m}\!\left(\frac{\pi t}{a}\right).
\tag{12}
\]

The conjugate-pair factor gives

\[
S_{\mathcal Z_m}(t)
=2\cosh(2\pi bt)P_m(t),
\tag{13}
\]

hence (7)--(8) imply

\[
\int_{\mathbb R}
\phi(t)\cosh^2(2\pi bt)
\cos^{2m}\!\left(\frac{\pi t}{a}\right)dt
\ge2^{-m}.
\tag{14}
\]

Let

\[
C_m:=\binom{2m}{m},
\qquad
K_m(u):=
\frac{4^m}{aC_m}
\cos^{2m}\!\left(\frac{\pi u}{a}\right).
\tag{15}
\]

The elementary beta integral gives

\[
\int_{-a/2}^{a/2}
\cos^{2m}\!\left(\frac{\pi u}{a}\right)du
=
\frac{aC_m}{4^m},
\tag{16}
\]

so `K_m` has mass one on every period. It is also an approximate identity at the lattice `a Z`. Indeed, for fixed `0<delta<a/2`, on `delta<=|u|<=a/2`,

\[
\cos^2\!\left(\frac{\pi u}{a}\right)
\le q_\delta
:=
\cos^2\!\left(\frac{\pi\delta}{a}\right)<1.
\tag{17}
\]

Since the central binomial coefficient is the largest of the `2m+1` coefficients in `(1+1)^{2m}`,

\[
C_m\ge\frac{4^m}{2m+1}.
\tag{18}
\]

Consequently the `K_m`-mass outside `(-delta,delta)` in one period is at most

\[
(2m+1)q_\delta^m\longrightarrow0.
\tag{19}
\]

For

\[
f_b(t):=\phi(t)\cosh^2(2\pi bt),
\tag{20}
\]

continuity and compact support now allow the real line to be split into finitely many centered period cells. Equations (16)--(19) give the exact comb limit

\[
\frac{4^m}{aC_m}
\int_{\mathbb R}f_b(t)
\cos^{2m}\!\left(\frac{\pi t}{a}\right)dt
\longrightarrow
\sum_{n\in\mathbb Z}f_b(na).
\tag{21}
\]

Multiplying (14) by `4^m/(aC_m)` gives a right-hand side

\[
\frac{2^m}{aC_m}
\le
\frac{2m+1}{a2^m}
\longrightarrow0.
\tag{22}
\]

Taking `m\to\infty` in (14) therefore proves (4). Since the lattice sum is finite, continuity in `b` proves (5).

## 3. Exact outer-support restriction and exponential screening cost

Because `phi` is even, (5) reads

\[
\phi(0)
+
2\sum_{n\ge1}
\phi(na)\cosh^2(2\pi Bna)
\ge0,
\tag{23}
\]

where only `na<=S` can contribute. Several rigid consequences are immediate.

First, choosing `a>S` leaves only the central term and gives

\[
\boxed{\phi(0)\ge0.}
\tag{24}
\]

Second, if

\[
\frac S2<a<S,
\tag{25}
\]

then every harmonic `na` with `n>=2` lies outside the spectral support. Hence

\[
\boxed{
\phi(a)
\ge
-\frac{\phi(0)}{2\cosh^2(2\pi Ba)}.
}
\tag{26}
\]

Thus a fixed outer-shell negative dip `phi(a)<=-delta<0` forces the exact central compensation

\[
\phi(0)
\ge
2\delta\cosh^2(2\pi Ba)
\ge
\boxed{
\frac{\delta}{2}e^{4\pi Ba}.
}
\tag{27}
\]

For a moving compact-spectrum family with strip depth `B_T`, the same statement requires no Lipschitz or derivative control. If `phi_T(0)<=M` uniformly and a fixed `a` remains in the outer half of the support, then

\[
\boxed{
\phi_T(a)
\ge
-\frac{M}{2\cosh^2(2\pi B_Ta)}
\ge
-2M e^{-4\pi B_Ta}.
}
\tag{28}
\]

This is stronger than the `O(B_T^{-1/2})` regularity-based pointwise control of WI-149 on the outer half of a compact spectrum, and it removes WI-149's uniform Lipschitz hypothesis there. The price is geometric rather than analytic: once `a<=S/2`, higher harmonic aliases re-enter and can screen the target point.

## 4. Harmonic repair is the only remaining fixed-period screening channel

Equation (23) also quantifies the surviving screening mechanism. Let

\[
w_n(a):=\cosh^2(2\pi Bna).
\tag{29}
\]

If `phi(a)<0`, then (23) implies

\[
2\sum_{\substack{n\ge2\\na\le S}}
w_n(a)\,\phi_+(na)
\ge
2w_1(a)[-\phi(a)]-\phi(0),
\tag{30}
\]

where `phi_+=max(phi,0)`. Therefore, whenever

\[
-\phi(a)>
\frac{\phi(0)}{2w_1(a)},
\tag{31}
\]

there must exist at least one integer harmonic `na`, `n>=2`, inside the support with `phi(na)>0`. A negative value beyond the central-screening budget cannot be repaired by positive mass at an unrelated spectral location for this family of tests; it requires positive mass on an exact harmonic alias.

This does **not** prove pointwise positivity throughout `[-S,S]`. For inner radii, the finite family of higher aliases in (23) is a genuine escape route. It is the compact-spectrum bounded-depth analogue of the remote-repair phenomenon in WI-146, but with the repair locations rigidified from arbitrary remote support to the arithmetic lattice generated by the tested point.

## 5. Relationship to the neighboring barriers

WI-146 shows that one- and two-point Lamzouri tests alone admit remote positive spectral repair. WI-147 proves that compact-spectrum universality with unrestricted off-line depth forces full pointwise Fourier positivity. WI-148 obtains the same pointwise conclusion for sufficiently fast spectral tails under unbounded depth. WI-149 keeps depth bounded and consequently gets Gaussian-smoothed positivity; pointwise control for moving profiles there needs uniform regularity.

The present fixed-period limit resolves a different tradeoff. It keeps the physical depth bounded and obtains exact point samples, but positivity is imposed only on the **periodized lattice sum** (4), not on each sample separately. For points in the outer half of compact support there are no higher aliases, so the periodized constraint collapses to the pointwise floor (26). Deeper inside the support, harmonic screening remains possible.

WI-123 and WI-125 also contain Bragg/alias language, but their object is different: they analyze periodic off-line matrix cells and the alias channels available to the Weil-form compression. Here the object is the scalar Fourier profile in Lamzouri's universal finite-multiset inequality. No matrix-equivalence claim between the two alias mechanisms is made.

## 6. Prior-art audit and novelty boundary

The primary zero-side source is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), especially Proposition 2.1. The scalar interface (3)--(8) is the same literature-backed abstraction already audited in WI-145--WI-149.

Jorge Buescu, A. C. Paixão and A. Symeonides, *Complex Positive Definite Functions on Strips*, Complex Analysis and Operator Theory 11 (2017), 627--649, DOI `10.1007/s11785-015-0527-y`, characterize genuinely positive-definite holomorphic strip kernels by positive Fourier--Laplace measures. As noted in WI-149, that hypothesis controls arbitrary finite quadratic forms and therefore does not supply the present conclusion from the weaker coefficient-one census inequality.

The cosine-power approximate identity on the circle, the central-binomial normalization (16), and its periodized Dirac-comb limit are classical Fourier-analysis ingredients. A targeted audit of the current `weil_inertia` corpus, the positive-definite strip literature, and nearby copositive-kernel literature found no direct theorem deriving the lattice-alias constraint (4), the outer-half floor (26), or the exponential central-spike cost (27) from bounded-depth Lamzouri-form universality. This is the novelty boundary used for persistence, not a claim of mathematical priority.

## 7. Scope and next falsification test

The strongest assumption remains universality over **all** conjugation-invariant finite multisets in the strip. Actual zeta zero configurations are far more structured. A zeta-specific scalar inequality valid only on realizable zero configurations could evade the binomial probes, and proving such a restriction would be genuinely new arithmetic/spectral information rather than a scalar-kernel optimization.

Compact spectral support is also essential to the exact finite alias sum used here. With tails, (4) needs a justified infinite periodization and the exponentially growing `cosh^2` weights make tail control nontrivial; WI-149 is the safer bounded-depth statement in that regime.

No new unconditional zero proportion is claimed. The result closes a narrower signed-kernel escape: **for a compact-spectrum scalar profile subject to the full bounded-strip Lamzouri census, a fixed outer-half negative dip costs an exponentially large central spike as the available off-line depth grows, and an inner negative dip beyond that central budget must be screened on exact harmonic aliases.** The next useful test is whether the arithmetic normalization and prime-side admissibility of candidate signed profiles can bound `phi(0)` and the harmonic positive budget strongly enough to turn (23) into an outright no-go for the remaining inner-support negative mass.