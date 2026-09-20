# PL-398 — Fixed-gap lattice meet/join coupling collapses to finite gap-divisor data

**Evidence/status:** `CLASSICAL-ARITHMETIC+EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION`.

**Parent finding:** `PL-397`.

## Claim

`PL-397` leaves open the possibility of coupling its continuation-faithful fixed-gap boundary layer to a genuinely arithmetic observable of the two exponent vectors. The most canonical lattice interaction is their coordinatewise meet/join, equivalently gcd/lcm. For a **fixed** integer gap `d>0`, however, that interaction has an exact finite collapse.

Put

\[
q=r+d.
\]

Then

\[
\gcd(r,q)=\gcd(r,d),
\tag{1}
\]

so in prime-exponent coordinates

\[
v(r)\wedge v(q)
=
 v(\gcd(r,d)).
\tag{2}
\]

Consequently every shared prime coordinate of `r` and `r+d` is one of the finitely many prime coordinates dividing `d`; for `p\nmid d`,

\[
\min\{v_p(r),v_p(r+d)\}=0.
\tag{3}
\]

The join satisfies

\[
v(r)\vee v(q)
=
 v(r)+v(q)-v(\gcd(r,d)),
\tag{4}
\]

and hence

\[
\operatorname{lcm}(r,r+d)
=
\frac{r(r+d)}{\gcd(r,d)}.
\tag{5}
\]

Thus, at fixed additive gap, the **nonadditive overlap correction** carried by meet/join geometry is not a growing high-dimensional prime-lattice interaction. It is a `d`-periodic finite divisor label. Since the leading transition kernel `\mathcal K_d(u)` of `PL-397` is already independent of the center `r`, multiplying it by any meet-only coupling produces only a finite congruence decoration of that universal kernel.

This rules out the route

\[
\text{fixed-gap continuation kernel}
+
\text{gcd/meet (or the lcm overlap correction)}
\longrightarrow
\text{new full prime-lattice RH mechanism}.
\]

The result does **not** rule out arithmetic couplings depending separately on `v(r)` and `v(r+d)`—for example Möbius/von-Mangoldt or divisor data—or regimes in which `d` itself grows and its prime support is no longer fixed.

## 1. The fixed-gap meet is supported only on the gap

Equation (1) is the Euclidean-algorithm identity

\[
\gcd(r,r+d)=\gcd(r,(r+d)-r)=\gcd(r,d).
\]

Taking prime valuations gives, for every prime `p`,

\[
\min\{v_p(r),v_p(r+d)\}
=
\min\{v_p(r),v_p(d)\}.
\tag{6}
\]

In particular, if `p\nmid d`, the right-hand side vanishes. The meet vector therefore belongs to the finite set

\[
\{v(g):g\mid d\}.
\tag{7}
\]

This is stronger than merely saying that the overlap is arithmetically constrained: at fixed `d` the whole common-support pattern, including prime-power depths, has only `\tau(d)` possible values as `r` varies.

For `d=1` the collapse is total:

\[
v(r)\wedge v(r+1)=0
\qquad\text{for every }r.
\tag{8}
\]

So consecutive fixed-gap pairs have no shared prime direction at all. For general fixed `d`, all shared directions are frozen into the finite coordinate set `\{p:p\mid d\}`.

## 2. The join contains no additional overlap beyond the same finite meet

For arbitrary exponent vectors `a,b` one has coordinatewise

\[
a\vee b=a+b-(a\wedge b).
\]

Applying this to `v(r),v(r+d)` and using (2) gives (4). At the scalar level this is exactly (5).

The qualification is important. An arbitrary nonlinear observable of `v(r)\vee v(r+d)` can still depend strongly on `r`, because the join contains the individual prime factors of `r` and `r+d`. What collapses is the **extra pairwise overlap information** supplied by taking a join rather than retaining the two vectors separately. Its correction to the independent sum is exactly `v(\gcd(r,d))`.

The same distinction is transparent in logarithmic energy:

\[
\log\operatorname{lcm}(r,r+d)
=
\log r+\log(r+d)-\log\gcd(r,d).
\tag{9}
\]

`PL-397` already places the fixed-gap transition at

\[
T_r=2\pi r(r+d),
\]

so the scalar product `r(r+d)` is already present in the continuation kernel's center. Replacing that scalar product by lcm introduces only the correction `-\log\gcd(r,d)`, which is periodic in `r` with period `d`.

Therefore the lcm route does not uncover a hidden common-prime interaction in the fixed-gap boundary layer. Any genuinely new factor-sensitive content in an lcm-based observable must come from how the observable uses the **individual** factors already present in `r(r+d)`, not from the lattice join itself.

## 3. Every meet-only coupling is exactly a finite congruence observable

Let `F` be any function on the finite divisor-vector set (7), and define

\[
A_d(r)
=
F\!\left(v(r)\wedge v(r+d)\right)
=
F\!\left(v(\gcd(r,d))\right).
\tag{10}
\]

Because `\gcd(r+d,d)=\gcd(r,d)`,

\[
A_d(r+d)=A_d(r).
\tag{11}
\]

Thus the coupling is exactly a function on the finite cyclic residue space `\mathbf Z/d\mathbf Z`. It admits the finite Fourier decomposition

\[
A_d(r)
=
\sum_{j=0}^{d-1}\widehat A_d(j)e^{2\pi i j r/d},
\tag{12}
\]

with no infinite prime-frequency content left in the meet variable.

The residue classes can be grouped more sharply by their gcd with `d`. For every divisor `g\mid d`,

\[
\#\{a\pmod d:\gcd(a,d)=g\}
=
\varphi(d/g).
\tag{13}
\]

Hence one complete period satisfies the exact identity

\[
\frac1d\sum_{a=1}^{d}F(v(\gcd(a,d)))
=
\frac1d\sum_{g\mid d}\varphi(d/g)F(v(g)).
\tag{14}
\]

and therefore, for fixed `d`,

\[
\sum_{r\le X}A_d(r)
=
\frac{X}{d}\sum_{g\mid d}\varphi(d/g)F(v(g))
+O_d(1),
\tag{15}
\]

where the implicit constant depends only on the finitely many values of `F` on divisors of `d`.

The divisor-class grouping in (13)--(14) is classical gcd-sum arithmetic. For example, Tóth's survey records the standard identity

\[
\sum_{a=1}^{d}\gcd(a,d)
=
\sum_{g\mid d}g\,\varphi(d/g),
\]

obtained by exactly this grouping. No novelty is claimed for (1), (13), or this finite harmonic decomposition.

## 4. Interaction with the continuation-faithful fixed-gap kernel

The leading local object isolated in `PL-397` has the form

\[
\mathcal K_d(u),
\]

with `d` fixed and `u` bounded, and contains no dependence on the center `r` after the natural normalization. If the proposed arithmetic rescue is meet-only, the leading coupled local data are therefore

\[
A_d(r)\,\mathcal K_d(u).
\tag{16}
\]

By (11)--(12), all center dependence in (16) is finite periodic residue data. Over many centers the coupling simply gives the finite divisor mixture (14) multiplying the same universal transition profile. There is no new operation involving an unbounded set of prime coordinates, no new Kronecker frequency `\log p`, and no factor-sensitive interaction between primes not already dividing the fixed external parameter `d`.

This supplies a matched control in the sense of the line's canonical mandate: a scalar model carrying the same integer centers together with their residue class modulo `d` reproduces (16) exactly. The prime-exponent realization of the meet adds no further information. This is consistent with `PL-114`, where fixed finite congruence labels likewise reduce under finite harmonic analysis rather than generating an irreducible prime-pair geometry.

The conclusion is deliberately narrower than `PL-114`. Here no Dirichlet-series factorization or continuation of congruence channels is needed: the collapse happens **before** any analytic continuation question, from the exact fixed-gap arithmetic identity (1). `PL-397` supplies the continuation-faithful analytic kernel; the present result says that grafting the canonical lattice overlap onto it does not restore high-dimensional prime geometry.

## 5. Relation to nontrivial shifted arithmetic correlations

This finding must not be confused with the much harder problem of couplings that inspect the two vectors separately. For example,

\[
\Lambda(r)\Lambda(r+d),
\qquad
\mu(r)\mu(r+d),
\qquad
f(v(r))g(v(r+d))
\tag{17}
\]

are not functions of `v(r)\wedge v(r+d)` alone. Their difficulty is not removed by (1). `PL-075` and `PL-169` already identify fixed-lag von-Mangoldt/ratios-type couplings with classical shifted-prime and additive-correlation problems, so merely inserting such a weight would not itself constitute a new mechanism either; one would still need an independently controlled sign, positivity, trace, or zero-sensitive consequence.

The present negative result is useful because it separates these two cases sharply. **Common-factor geometry is easy and finite at fixed gap; separate-vector arithmetic remains genuinely nontrivial.** The next continuation-aware coupling should therefore use information that survives after quotienting out the finite meet data.

## 6. Continuation and novelty audit

No identity valid only for `Re(s)>1` is transported here. Equations (1)--(15) are finite arithmetic identities. Their use in (16) is conditional only on the already-stored continuation-faithful asymptotics of `PL-397`, which came from the exact incomplete-gamma representation rather than from a formally continued Euler product.

The arithmetic ingredients themselves are classical. A representative literature anchor is:

- **László Tóth**, “A Survey of Gcd-Sum Functions,” *Journal of Integer Sequences* **13** (2010), Article 10.8.1, https://cs.uwaterloo.ca/journals/JIS/VOL13/Toth/toth10.pdf. The survey records the classical grouping of gcd values by divisors, including `P(n)=\sum_{k=1}^n\gcd(k,n)=\sum_{g\mid n}g\varphi(n/g)`.

Targeted novelty checks against gcd/lcm-sum literature and the line's own `PL-016`, `PL-030`, `PL-114`, `PL-169`, and `PL-397` found no basis for claiming a new number-theoretic theorem. The durable content is the **route restriction** specific to the current frontier: one explicit escape proposed by `PL-397`—using gcd/lcm overlap as the missing factor-sensitive coefficient—reduces at fixed additive gap to a finite congruence decoration.

## 7. Adversarial boundaries and falsification tests

1. **Fixed `d` is essential.** If `d=d(r)` grows, the set of prime coordinates dividing `d` may grow and the finite-alphabet argument is no longer uniform. Such a regime must first rederive the saddle/transition asymptotics; `PL-397` assumes fixed `d`.

2. **Meet-only is essential.** Equation (2) does not collapse `v(r)` or `v(r+d)` separately. A coupling using separate Möbius, von-Mangoldt, divisor, residue, or other data can retain difficult shifted arithmetic.

3. **Do not overstate the lcm conclusion.** `G(\operatorname{lcm}(r,r+d))` can vary nonperiodically with `r`. The exact statement is that the join's correction to `v(r)+v(r+d)` is the finite periodic meet (2), and that `\operatorname{lcm}/[r(r+d)]=1/\gcd(r,d)` is periodic.

4. **Finite congruence data are arithmetic, but not a new full-lattice interaction.** The primes dividing `d` are genuine arithmetic information. The negative conclusion is a matched-control statement: at fixed `d`, the same coupling is reproduced by a finite residue label and does not use an unbounded collection of exponent coordinates.

5. **The result is leading-order only when attached to `PL-397`.** Subleading `O(r^{-1})` transition terms can correlate with the periodic weight. They do not change the exact support statement (3), but no all-orders factorization or zero-blindness is claimed.

6. **No RH consequence follows.** Neither (14) nor the coupled kernel (16) supplies a sign theorem, positivity principle, zero-location constraint, trace identity, or cancellation estimate. A future construction could still combine the periodic meet factor with an independent zero-sensitive component; that extra component would carry the substantive burden.

## Research consequence

The continuation-faithful fixed-gap boundary layer remains a legitimate place to test arithmetic couplings, but **gcd/meet and the genuinely pairwise part of lcm/join should no longer be treated as promising sources of the missing geometry**. At fixed `d`, their overlap content is exactly the finite divisor pattern of `d` and is harmonically equivalent to a finite congruence label.

A viable next step must therefore obtain factor sensitivity from information not determined by the meet: a separately oriented Möbius/von-Mangoldt/divisor observable on `r` and `r+d`, an operator acting nontrivially on their two full exponent vectors, or a newly derived growing-gap regime in which the prime support of the gap itself enters the continuation kernel. In every case the arithmetic input must still produce an independently controlled sign, cancellation, positivity, trace, or zero-sensitive mechanism rather than merely decorating the universal kernel.