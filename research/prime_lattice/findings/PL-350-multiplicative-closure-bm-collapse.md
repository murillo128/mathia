# PL-350 — Multiplicative closure forces source-selected log frequencies into rank one or full form-core collapse

**Evidence:** `EXACT-DERIVED + CLASSICAL-BM + DECISIVE-NEGATIVE`

**Status:** `MULTIPLICATIVE-RANK-TWO-FORCES-SUPERLINEAR-LOG-COUNT + INFINITE-BM-DENSITY-FOR-ANY-CROSS-DIRECTION-CLOSED-FAMILY + FINITE-BM-DENSITY-COLLAPSES-TO-ONE-EXPONENT-RAY`

## Precise claim

`PL-349` leaves a sharply defined escape from the endpoint-modulation collapse: a genuinely intermediate source-selected frequency family `Lambda` must have finite exterior Beurling--Malliavin density. For the Prime-Lattice source there is a natural extra requirement one might try to preserve while thinning the frequencies: **multiplicative closure** of the selected integers.

That requirement is already too strong as soon as more than one independent exponent direction survives.

Let `S` be a nontrivial multiplicative submonoid of the positive integers and define

\[
\Lambda_S:=\{\log n:n\in S\}\subset[0,\infty).
\tag{PL350-1}
\]

Then exactly one of the following structural regimes occurs.

### Rank at least two

If `S` contains multiplicatively independent integers `a,b>1`, equivalently `v(a),v(b)` are linearly independent over `Q`, then

\[
D_{BM}^*(\Lambda_S)=\infty.
\tag{PL350-2}
\]

Consequently, for every finite aperture `A>0`, the endpoint modulations

\[
u_{A,n}(x)=u_A(x)e^{i(\log n)x},\qquad n\in S,
\tag{PL350-3}
\]

form a core for the localized completed Weil form `Q_W^A`. Their unrestricted finite Gram positivity is therefore again exactly full localized Weil positivity, not an intermediate arithmetic criterion.

### Rank one

If `S` contains no multiplicatively independent pair, then there is a primitive integer `b>1` and an additive submonoid `K\subset\mathbb N_0` such that

\[
S=\{b^k:k\in K\}.
\tag{PL350-4}
\]

Writing `g=gcd(K\setminus\{0\})`, the normalized monoid `K/g` is cofinite in `\mathbb N_0`. Hence `Lambda_S` differs only by finitely many points from the half-lattice

\[
(g\log b)\,\mathbb N_0.
\tag{PL350-5}
\]

Its Beurling--Malliavin density and the form-core aperture of `PL-349` are therefore

\[
\boxed{
D_{BM}^*(\Lambda_S)=\frac1{g\log b},
\qquad
A_{\rm core}(\Lambda_S)=\frac{\pi}{g\log b}.
}
\tag{PL350-6}
\]

As in `PL-349`, no claim is made about completeness exactly at the critical aperture.

Thus a multiplicatively closed source selection has no genuinely intermediate finite-BM regime that still retains two independent prime/exponent directions:

\[
\boxed{
\text{multiplicative closure + cross-direction exponent geometry}
\Longrightarrow D_{BM}^*=\infty.
}
\tag{PL350-7}
\]

Finite BM density under multiplicative closure is possible only after the source collapses to one rational exponent ray.

## 1. Two exponent directions already give quadratic frequency counting

Assume `a,b in S` are multiplicatively independent and put

\[
\alpha=\log a,\qquad \beta=\log b.
\]

Multiplicative closure gives

\[
a^m b^n\in S
\qquad(m,n\in\mathbb N_0),
\]

and therefore

\[
m\alpha+n\beta\in\Lambda_S.
\tag{PL350-8}
\]

All these frequencies are distinct. Indeed,

\[
m\alpha+n\beta=m'\alpha+n'\beta
\]

would imply

\[
a^{m-m'}=b^{n'-n},
\]

which is impossible for a nonzero integer relation when `a` and `b` are multiplicatively independent.

The number of lattice points in the first-quadrant triangle

\[
\{(m,n)\in\mathbb N_0^2:m\alpha+n\beta\le R\}
\]

satisfies the elementary estimate

\[
\#\{(m,n):m\alpha+n\beta\le R\}
=
\frac{R^2}{2\alpha\beta}+O(R).
\tag{PL350-9}
\]

Hence

\[
N_{\Lambda_S}(R)
:=\#(\Lambda_S\cap[-R,R])
\gg R^2,
\qquad
\frac{N_{\Lambda_S}(R)}R\longrightarrow\infty.
\tag{PL350-10}
\]

`PL-348` proved directly from Paley--Wiener--Schwartz and Jensen that any real frequency set with this superlinear counting is complete on every finite interval, even in the Sobolev topology needed for the completed Weil form. `PL-349` then identifies infinite completeness radius with

\[
D_{BM}^*(\Lambda_S)=\infty.
\]

This proves (PL350-2) and the form-core statement.

The geometric mechanism is worth isolating. Multiplicative closure fills a two-dimensional positive cone in exponent space, while the energy projection

\[
E(v)=\langle v,(\log p)_p\rangle=\log n
\]

maps its `O(R^2)` lattice points into distinct frequencies below height `R`. Any exponent subsemigroup containing two rationally independent rays therefore overwhelms the `O(R)` zero budget of a nonzero compactly supported Fourier transform. No prime number theorem, zeta zero, or Euler product is involved.

More generally, `d` multiplicatively independent generators yield `\gg R^d` distinct log frequencies. The obstruction begins already at `d=2`.

## 2. Finite density forces a single exponent ray

Suppose instead that `S` has no multiplicatively independent pair. Choose any `a>1` in `S` and write

\[
v(a)=d u,
\]

where `u` is a primitive nonnegative integer vector, meaning that the gcd of its nonzero coordinates is one. Every `n in S` is multiplicatively dependent with `a`, so

\[
v(n)=q_n u
\]

for some nonnegative rational `q_n`. Since `v(n)` is integral and `u` is primitive, `q_n` must in fact be an integer. If `b` is the integer with `v(b)=u`, then every element of `S` is a power of `b`.

Define

\[
K:=\{k\in\mathbb N_0:b^k\in S\}.
\tag{PL350-11}
\]

Multiplicative closure of `S` is exactly additive closure of `K`. Let `g` be the gcd of its positive elements. A standard elementary fact about additive submonoids of `\mathbb N_0` says that `K/g` is a numerical semigroup: it contains every sufficiently large nonnegative integer. One quick proof is to choose finitely many elements of `K` already having gcd `g`; the submonoid they generate has finite complement in `g\mathbb N_0`, and it is contained in `K`.

Therefore there is `k_0` such that

\[
gk\in K\qquad(k\ge k_0),
\]

so `Lambda_S=(\log b)K` differs finitely from `(g\log b)\mathbb N_0`. Finite modifications do not change Beurling--Malliavin density. The half-lattice `h\mathbb N_0` has exterior BM density `1/h`, equivalently completeness radius `2\pi/h`; this is the arithmetic-progression case of the classical Beurling--Malliavin theorem recorded as source 104 and used in `PL-349`. Taking `h=g\log b` gives (PL350-6).

This rank-one alternative can still be incomplete on sufficiently large apertures, but it has discarded the very cross-prime geometry that motivated a Prime-Lattice source selection. It is an ordinary one-frequency semigroup up to finitely many missing modes.

## 3. Prior-art and novelty audit

The load-bearing analytic ingredient is not new: source 104 and `PL-349` give the Beurling--Malliavin completeness-radius theorem, while `PL-348` already established the easier superlinear-counting obstruction needed for the rank-at-least-two case. The rank-one classification uses only unique factorization plus the elementary numerical-semigroup fact that an additive submonoid of `\mathbb N_0`, after dividing by its gcd, is eventually cofinite.

A targeted literature audit on 18 September 2026 for Beurling--Malliavin density of logarithms of multiplicative semigroups and for exponential systems with frequencies `m alpha+n beta` did not locate this exact Prime-Lattice route classification. That absence is **not** treated as evidence of novelty. The mathematical ingredients are classical and the quadratic-count argument is elementary. The durable contribution is the negative consequence for the live `PL-349` intermediate-sufficiency route: multiplicative closure itself is incompatible with finite BM density once two independent exponent directions are retained.

This is not a new RH criterion and does not make progress on the zero-location step. It removes one natural design principle for constructing the restricted family sought after `PL-349`.

## 4. Adversarial boundaries

1. **Multiplicative closure is essential.** A non-closed source-selected subset may contain points from infinitely many prime directions while still having finite BM density. The theorem does not reject such thinnings.

2. **Multiplicative independence is essential.** Distinct integers such as `4` and `8` lie on the same rational exponent ray. Their closure is rank one and has only linear frequency growth after logarithm.

3. **The conclusion concerns unrestricted linear span of frequency modulations.** Coefficient constraints, nonlinear relations, coupled apertures, matrix-valued source laws, or noncommutative state families can avoid the ordinary BM completeness argument.

4. **Infinite BM density is a density obstruction, not an arithmetic sufficiency theorem.** It says that Gram positivity on the resulting modulation family merely reconstructs full localized Weil positivity. It does not derive RH from less information.

5. **The rank-one density formula is insensitive to finitely many exceptional powers.** The precise small-exponent membership of `S` cannot restore cross-prime information or change the completeness radius.

6. **No analytic continuation is performed here.** All continuation-sensitive zeta information remains inside the completed Weil form inherited from `PL-347`; the present argument only classifies which multiplicatively closed log-frequency sources become complete coordinates for it.

## Research consequence

The finite-BM escape identified in `PL-349` cannot be obtained by taking a source-defined set of integers and then imposing ordinary multiplicative closure while retaining two independent Prime-Lattice directions. Even two such directions generate quadratically many distinct log frequencies, forcing infinite completeness radius and immediate form-core collapse.

A viable intermediate family must therefore **break multiplicative closure at the level of the frequency set**, or retain multiplication only through additional coefficient/coupling laws that are not erased when one passes to unrestricted linear span. Alternatively it must leave the frequency-only endpoint-modulation framework altogether. Within the present framework, rank-one multiplicative families are the only finite-density closed cases, and they reduce to an eventual half-lattice rather than to genuinely multidimensional prime-exponent geometry.