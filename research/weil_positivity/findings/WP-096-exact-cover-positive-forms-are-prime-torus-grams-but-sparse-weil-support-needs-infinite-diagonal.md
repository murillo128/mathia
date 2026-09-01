# WP-096 — Exact cover-positive forms are prime-torus Grams, but sparse Weil support needs an infinite diagonal

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the direct exact-cover-covariant positive-kernel route. The classification below uses the exact critical first-order intertwiner of `WP-093` and the classical Bochner theorem for positive-definite functions on discrete abelian groups. No novelty is claimed for Bochner duality, the infinite prime torus, multiplicative shifts, or multiplicative Toeplitz kernels themselves.

## Claim

`WP-093` left a genuine escape from its finite-band classification: an exact positive cover-covariant form might use position-dependent infinite-range coupling. `WP-094` and `WP-095` then ruled out the simplest additive Toeplitz endpoint and finite-band-plus-endpoint repairs, but explicitly left arbitrary infinite-range kernels open.

That remaining algebraic cone can be classified exactly.

Let

\[
(W_nx)_{nk+r}=n^{-1/2}x_k,
\qquad 0\le r<n,
\tag{1}
\]

be the normalized pointed-cover isometries on `c_00(N_0)`, and let the critical first-order operator from `WP-093` be

\[
(Tx)_j=(j+1)(x_{j+1}-x_j).
\tag{2}
\]

Reindex by the unitary algebraic bijection

\[
Ue_j=\varepsilon_{j+1},
\qquad
B:=UT:c_{00}(\mathbb N_0)\to c_{00}(\mathbb N).
\tag{3}
\]

If

\[
S_n\varepsilon_m=\varepsilon_{nm},
\tag{4}
\]

then the exact `WP-093` intertwining relation becomes

\[
\boxed{BW_n=\sqrt n\,S_nB.}
\tag{5}
\]

Moreover `B` is an algebraic bijection on the finite-support core. Consequently every finite-valued nonnegative Hermitian quadratic form `q` on `c_00(N_0)` satisfying

\[
\boxed{q(W_nx)=nq(x)\quad(n\ge1)}
\tag{6}
\]

is represented uniquely by a finite positive Borel measure `mu` on the infinite prime torus

\[
\widehat{\mathbb Q_+^\times}
\cong \prod_p\mathbb T
\tag{7}
\]

through

\[
\boxed{
q_\mu(x)
=\int_{\widehat{\mathbb Q_+^\times}}
\left|\sum_{m\ge1}(Bx)_m\chi(m)\right|^2d\mu(\chi).
}
\tag{8}
\]

Equivalently, in the `B`-coordinates every exact cover-positive kernel is a **multiplicative Toeplitz kernel**

\[
R_{a,b}=\varphi(a/b),
\tag{9}
\]

where `varphi` is a positive-definite function on the discrete multiplicative group `Q_+^x`, and

\[
\varphi(r)=\int\chi(r)\,d\mu(\chi).
\tag{10}
\]

This proves two things at once.

First, the infinite-range escape is real: exact cover covariance does **not** collapse positivity to the finite-band cone of `WP-093` or the endpoint anchor of `WP-094`. For example, for any integer `d>1` and `|epsilon|<1/2`, the positive density

\[
w_{d,\varepsilon}(\chi)
=1+2\varepsilon\operatorname{Re}\chi(d)
\tag{11}
\]

with respect to prime-torus Haar measure gives

\[
R_{d,\varepsilon}
=I+\varepsilon(S_d+S_d^*)
\ge(1-2|\varepsilon|)I>0,
\tag{12}
\]

and hence a closable nonlocal exact-cover-positive form

\[
q_{d,\varepsilon}(x)
=\langle Bx,R_{d,\varepsilon}Bx\rangle.
\tag{13}
\]

It couples multiplicative scales `m` and `dm`, so in the original additive cover coordinate it has unbounded range and is neither fixed-band nor additive Toeplitz.

Second, this broader positive cone still cannot carry the finite Weil comb in its most direct sparse way. Suppose one asks for a single finite-valued positive kernel whose off-diagonal multiplicative Fourier data are exactly

\[
\varphi(p^k)
=-\frac{\log p}{p^{k/2}},
\qquad
\varphi(p^{-k})
=-\frac{\log p}{p^{k/2}},
\qquad k\ge1,
\tag{14}
\]

and

\[
\varphi(r)=0
\tag{15}
\]

whenever the reduced rational `r` involves at least two distinct primes. These are precisely the negative prime-power coefficients of the centered finite Weil multiplier, with no mixed-prime Fourier support. Let

\[
C=\varphi(1)=\mu\!\left(\widehat{\mathbb Q_+^\times}\right)<\infty
\tag{16}
\]

be the positive diagonal/self-energy.

For every finite prime set `P`, positivity of the pushed-forward measure on `T^P` forces the **exact** inequality

\[
\boxed{
C\ge D(P):=
2\sum_{p\in P}\frac{\log p}{\sqrt p-1}.
}
\tag{17}
\]

Since `D(P)` diverges as `P` exhausts the rational primes, no finite `C` exists. Therefore

\[
\boxed{
\text{exact cover covariance}
+\text{ordinary positive quadratic form}
+\text{exact sparse finite-Weil Fourier support}
\Longrightarrow
\text{infinite diagonal self-energy}.
}
\tag{18}
\]

Thus the nonlocal cone opened by `WP-095` is large and contains honest closable positive forms, but **the exact Mangoldt/Weil sparsity cannot be inserted into that cone with only a finite scalar diagonal counterterm**. A surviving global mechanism must introduce additional mixed-prime coefficients that are removed only after a nontrivial compression/quotient, couple to a genuinely non-scalar global or archimedean sector before positivity is read out, change the domain/topology so that the finite-measure representation no longer applies, or abandon the exact cover-covariant ordinary-Gram architecture.

## 1. The critical first-order transform conjugates covers to multiplicative shifts

`WP-093` proved, with

\[
V_ne_j=e_{n(j+1)-1},
\tag{19}
\]

that

\[
TW_n=\sqrt n\,V_nT.
\tag{20}
\]

Under the reindexing `Ue_j=epsilon_{j+1}`,

\[
UV_nU^{-1}=S_n,
\tag{21}
\]

which gives (5).

The point that matters for completeness is that `T` is not merely injective on the core: it is an algebraic bijection. If `y in c_00(N_0)`, then

\[
x_j=-\sum_{k\ge j}\frac{y_k}{k+1}
\tag{22}
\]

is again finitely supported and satisfies `Tx=y`. Hence `B=UT` is a bijection between the two finite-support cores.

Given a nonnegative Hermitian form `q`, polarize it to its sesquilinear form and transport it through `B`:

\[
R(y,z):=q(B^{-1}y,B^{-1}z).
\tag{23}
\]

Using (5), the covariance (6) is equivalent to

\[
R(S_ny,S_nz)=R(y,z)
\qquad(n\ge1).
\tag{24}
\]

Writing

\[
r_{a,b}=R(\varepsilon_a,\varepsilon_b),
\tag{25}
\]

we obtain

\[
\boxed{r_{na,nb}=r_{a,b}.}
\tag{26}
\]

This reduction uses only the exact cover geometry already present in Mathia; no zeta function or zero data enter.

## 2. Scale invariance is exactly positive definiteness on `Q_+^x`

Equation (26) implies that `r_{a,b}` depends only on the reduced ratio `a/b`. Indeed, if

\[
a/b=c/d,
\]

write `(a,b)=g(u,v)` and `(c,d)=h(u,v)` with `(u,v)=1`. Scaling both pairs to `(ghu,ghv)` and applying (26) gives

\[
r_{a,b}=r_{c,d}.
\]

Define

\[
\varphi(a/b):=r_{a,b}.
\tag{27}
\]

The kernel positivity of `R` is equivalent to positive definiteness of `varphi` on the discrete abelian group `Q_+^x`. For rational numbers `q_1,...,q_N`, choose a common positive integer denominator `M` so that `m_i=Mq_i in N`. Then

\[
\left[\varphi(q_i/q_j)\right]_{i,j}
=
\left[r_{m_i,m_j}\right]_{i,j}
\succeq0.
\tag{28}
\]

Conversely a positive-definite `varphi` makes (9) a positive kernel.

The group `Q_+^x` is the free abelian group on the rational primes,

\[
\mathbb Q_+^\times\cong\bigoplus_p\mathbb Z,
\tag{29}
\]

so its compact Pontryagin dual is the infinite prime torus `prod_p T`. Bochner's theorem for discrete abelian groups gives a unique finite positive measure `mu` with (10). Substitution into the finite matrix sum proves (8).

Conversely, for any finite positive measure `mu`, multiplication of the character polynomial by `chi(n)` gives

\[
\sum_m(S_ny)_m\chi(m)
=\chi(n)\sum_my_m\chi(m),
\tag{30}
\]

up to the harmless reciprocal-character convention. Since `|chi(n)|=1`, (8) is invariant under `S_n`, and (5) restores (6). This proves the classification in both directions.

The total mass is not an adjustable hidden infinity:

\[
\mu(\widehat{\mathbb Q_+^\times})
=\varphi(1)
=R(\varepsilon_1,\varepsilon_1)
=q(B^{-1}\varepsilon_1).
\tag{31}
\]

For a finite-valued form on the algebraic core, it is finite.

## 3. Explicit nonlocal closable survivors

Haar measure gives `varphi(r)=1_{r=1}` and therefore

\[
q_{\rm Haar}(x)=\|Bx\|^2=\|Tx\|^2,
\tag{32}
\]

the critical `WP-093` energy.

Now fix `d>1`. Because the character `chi(d)` is nontrivial,

\[
1-2|\varepsilon|
\le w_{d,\varepsilon}
\le1+2|\varepsilon|.
\tag{33}
\]

Its only nonzero Fourier coefficients away from the identity are at `d` and `d^{-1}`, both equal to `epsilon`. Hence (12) follows and

\[
(1-2|\varepsilon|)\|Tx\|^2
\le q_{d,\varepsilon}(x)
\le(1+2|\varepsilon|)\|Tx\|^2.
\tag{34}
\]

Since the critical `WP-093` form is closable, this norm equivalence makes `q_{d,epsilon}` closable with the same form domain after closure.

In output coordinates `y=Bx`,

\[
q_{d,\varepsilon}(x)
=\sum_m|y_m|^2
+2\varepsilon\operatorname{Re}
\sum_m\overline{y_{dm}}y_m.
\tag{35}
\]

The coupling `m <-> dm` has unbounded additive separation as `m` grows. Therefore `WP-093`'s fixed-band theorem, `WP-094`'s additive block-Toeplitz endpoint theorem, and `WP-095`'s finite-band-plus-endpoint obstruction do not apply to it.

This is also a matched universality control. Nothing in (11)-(35) distinguishes a prime `d=p` from a composite `d`. For every `d>1`, `S_d` is a pure unilateral shift of countably infinite multiplicity: the wandering subspace is spanned by integers not divisible by `d`. Consequently the abstract spectrum of

\[
I+\varepsilon(S_d+S_d^*)
\]

is the same interval `[1-2|epsilon|,1+2|epsilon|]` for every `d`. Exact covariance and ordinary positivity create a large nonlocal cone, but not a prime-power discriminator by themselves.

## 4. Exact finite-prime positivity threshold for sparse Weil coefficients

Assume now (14)-(16). Let `P` be a finite set of primes and push `mu` forward to the coordinate torus

\[
\mathbb T^P.
\]

Its Fourier coefficient at the exponent vector `alpha in Z^P` is

\[
\varphi\!\left(\prod_{p\in P}p^{\alpha_p}\right).
\tag{36}
\]

Because all mixed-prime coefficients vanish and each one-prime tail is geometrically summable, these Fourier coefficients are absolutely summable. Therefore Fourier uniqueness identifies the pushforward with the continuous density

\[
\begin{aligned}
w_P(\theta)
&=C
-2\sum_{p\in P}(\log p)
\sum_{k\ge1}p^{-k/2}\cos(k\theta_p)\\
&=C+\sum_{p\in P}(\log p)
\left(1-P_{p^{-1/2}}(\theta_p)\right),
\end{aligned}
\tag{37}
\]

where

\[
P_r(\theta)
=\frac{1-r^2}{1-2r\cos\theta+r^2}
=1+2\sum_{k\ge1}r^k\cos(k\theta)
\tag{38}
\]

is the circle Poisson kernel.

Each summand in (37) is minimized at `theta_p=0`, independently of the others. Since

\[
P_r(0)=\frac{1+r}{1-r},
\tag{39}
\]

we get

\[
\min_{\theta\in\mathbb T^P}w_P(\theta)
=C-2\sum_{p\in P}
\frac{\log p}{\sqrt p-1}.
\tag{40}
\]

Thus positivity of the measure is equivalent, on this exact finite-prime Fourier support, to

\[
\boxed{C\ge D(P).}
\tag{41}
\]

This is not merely a necessary estimate. If `C>=D(P)`, the density (37) is pointwise nonnegative, so it explicitly gives a positive finite-prime carrier. The obstruction is entirely in the all-prime limit.

To see divergence without any prime-number-theorem input, for every prime `p>=2`,

\[
\frac{\log p}{\sqrt p-1}\ge\frac1p,
\tag{42}
\]

and Euler's theorem gives

\[
\sum_p\frac1p=\infty.
\tag{43}
\]

Hence

\[
D(P)\longrightarrow\infty
\tag{44}
\]

along any exhaustion of the primes. Equations (31) and (44) contradict a finite diagonal `C`.

The obstruction is therefore stronger than saying that the obvious zero-diagonal Weil multiplier is indefinite. Even after allowing an arbitrary positive scalar self-energy at the identity, **the exact sparse prime-power coefficients force that self-energy to diverge**.

## 5. Relation to earlier obstructions

This result changes the boundary left by several earlier findings rather than duplicating them.

- `WP-093` classified only fixed finite-band exact-cover-positive operators and found the critical weighted-difference ray. The present Bochner transport classifies **all algebraic nonnegative exact-cover-covariant forms on the finite-support core** after the same critical first-order conjugacy.
- `WP-094` considered additive block-Toeplitz infinite-range forms and found only a singular endpoint anchor. Equation (35) is multiplicative Toeplitz after `B` and gives explicit closable infinite-range survivors outside that hypothesis.
- `WP-095` showed that adding the endpoint anchor to a finite-band positive energy cannot regularize it. The present cone proves that the remaining nonlocal escape was mathematically real, then identifies a different obstruction to the exact sparse Weil carrier.
- `WP-022` found the correct critical finite-Weil coefficients inside the radial score of one specific product-Poisson family, but its canonical Fisher norm diverges at `sigma=1/2`. Equation (41) assumes no Fisher/statistical geometry: it is forced by positive definiteness of **any** exact-cover-positive Gram kernel with the prescribed sparse Fourier coefficients.
- `WP-039` rules out putting Mangoldt support directly into a translation-invariant **Markov/Dirichlet generator symbol**, whose zero set must be a subgroup. The present kernels are ordinary positive-definite Gram kernels, not conditionally-negative Markov symbols; they have many nontrivial survivors, so the obstruction and surviving cone are different.
- `WP-005` shows that a positive finite coefficient measure becomes indefinite under the exact Weil autocorrelation lift. Here the obstruction appears earlier inside the pointed-cover geometry: the direct multiplicative positive kernel cannot carry the exact negative prime-power Fourier comb with finite diagonal mass.

## 6. Prior art and novelty audit

No novelty is claimed for the abstract ingredients of the classification.

The Hardy space of square-summable Dirichlet series and its Bohr realization on the infinite prime polydisc/torus are classical; the line's `SOURCES.md` already anchors this with Hedenmalm--Lindqvist--Seip (1997). Under coefficient identification, multiplication by a Dirichlet monomial is precisely the multiplicative shift `S_n`. Positive-definite functions on a discrete abelian group and their representation by positive measures on the Pontryagin dual are the classical Bochner theorem. Matrices depending on the ratio `a/b` belong to the classical multiplicative-Toeplitz/Dirichlet-series operator landscape.

The Mathia-specific content is the exact conjunction:

\[
\text{pointed-cover covariance}
\xrightarrow{\;B=UT\;}
\text{multiplicative-shift invariance}
\xrightarrow{\rm Bochner}
\text{prime-torus positive-measure cone},
\tag{45}
\]

followed by the sharp finite-prime positivity threshold (41) for the exact sparse critical Weil coefficients. The result is therefore a **derived classification and obstruction**, not a claim that multiplicative Toeplitz theory or prime-torus harmonic analysis is new.

There is also a strong generalized-prime/universality warning. The representation (8) depends only on a free abelian multiplicative semigroup/group and its character dual. Replacing rational primes by abstract free generators reproduces the same positivity theorem. Rational-prime arithmetic enters (14) only through the externally requested values `log p` and `p^{-1/2}`. Thus even the large positive cone does not itself explain why the Riemann completion, rather than a generalized-prime analogue, should be selected.

## 7. Boundary conditions and surviving routes

Equation (18) is intentionally narrower than a no-go theorem for global Weil positivity. It assumes all of the following:

1. the pointed-cover operators `W_n` and their exact covariance (6);
2. an ordinary finite-valued nonnegative Hermitian quadratic form on the algebraic core;
3. the `WP-093` critical first-order conjugacy, which is algebraically invertible there;
4. a direct prime-torus carrier whose nonidentity Fourier support is **exactly** the one-prime prime-power axes with coefficients (14);
5. no mixed-prime Fourier coefficients available to help positivity.

It does **not** rule out:

- a positive global block form with an infinite-dimensional archimedean/boundary sector whose elimination produces nontrivial mixed-prime corrections before the Weil readout;
- a compression, quotient, cohomological pairing, or indefinite-before-quotient construction in which the sparse Weil comb appears only after a structural operation;
- a domain-changing or renormalized object for which `q(B^{-1}epsilon_1)` is not a finite core value, provided its finiteness and sign are established independently rather than by subtracting (44) by hand;
- abandoning exact pointed-cover covariance in favor of a different Mathia-native global geometry;
- a positive kernel with canonical mixed-prime Fourier data that cancel only after a separately justified global projection.

The last possibility is now especially sharp. Exact cover covariance itself does permit arbitrary positive prime-torus measures. Therefore the next nontrivial escape is **not** merely "try a longer-range kernel". It must explain why a canonical positive measure has the required cross-prime Fourier structure, how a geometric operation removes those mixed terms while retaining the one-prime Weil coefficients, and where the archimedean Gamma and polar terms come from in the same construction.

## Consequence for the research line

The direct pointed-cover positive-form route now has a complete algebraic normal form:

```text
WP-093 critical cover derivative B
    -> multiplicative shifts S_n
    -> arbitrary positive-definite ratio kernel phi(a/b)
    -> finite positive measure on the infinite prime torus
    -> exact cover-positive quadratic form.
```

This is a genuine enlargement over the finite-band and additive-Toeplitz classes: nonlocal closable survivors exist abundantly. But demanding the exact finite Weil prime-power Fourier support with zero mixed-prime terms yields

```text
finite prime set P
    -> positive density exists only with diagonal C >= D(P)
    -> D(P) = 2 sum_{p in P} log(p)/(sqrt(p)-1)
    -> D(P) -> infinity
    -> no finite all-prime positive Gram carrier.
```

Accordingly, **ordinary exact-cover positivity plus sparse Mangoldt support is not the missing global geometry**. Any viable continuation must make cross-prime/global coupling structural before the positivity theorem, rather than add an arbitrary infinite-range kernel and hope that positivity alone selects the Weil comb.
