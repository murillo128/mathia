# AF-513 — A fixed-shift prime tail remains uniformly curvature-indistinguishable

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `QUANTITATIVE-OBSTRUCTION` · `DIRICHLET-SOURCE` · `COFINITE-TAIL-DEFORMATION` · `GLOBAL-RELATIVE-PROFILE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P(s)=P_{\mathbb P}(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa(s)=\frac{d^2}{ds^2}\log P(s),
\qquad s>1,
\]

be the rational-prime Dirichlet sum and its log-curvature. Fix an integer shift `h\ge1`. For a cutoff `A>h+3`, define the simple positive-integer source

\[
R_{A,h}
=
\{p\in\mathbb P:p\le A\}
\cup
\{p+h:p\in\mathbb P,\ p>A\}.
\tag{1}
\]

The tail map `p\mapsto p+h` is injective, every shifted generator is larger than `A`, and the retained prefix contains `2,3`; hence `R_{A,h}` is a primitive simple unit-weight source with the same scale anchor `\log2` as the rational primes.

Write

\[
P_{A,h}(s)=\sum_{q\in R_{A,h}}q^{-s},
\qquad
\kappa_{A,h}(s)=\frac{d^2}{ds^2}\log P_{A,h}(s).
\]

Then for every fixed `h\ge1` there is a constant `C_h<\infty` such that, for all sufficiently large `A`,

\[
\boxed{
\sup_{s>1}
\frac{|\kappa_{A,h}(s)-\kappa(s)|}{\kappa(s)}
\le
C_h\frac{1+\log^2 A}{A}.
}
\tag{2}
\]

In particular,

\[
\boxed{
\sup_{s>1}
\frac{|\kappa_{A,h}(s)-\kappa(s)|}{\kappa(s)}
\longrightarrow0
\qquad(A\to\infty),
}
\tag{3}
\]

and therefore

\[
\boxed{
\sup_{s>1}
|\log\kappa_{A,h}(s)-\log\kappa(s)|
\longrightarrow0.
}
\tag{4}
\]

This strengthens AF-511 and AF-512 qualitatively. Those findings changed one remote prime generator. Here **every prime generator beyond the cutoff is moved**. For `h=1`, every shifted tail generator `p+1` is even and composite once `p>2`, so the controls agree with the primes on an arbitrarily long prefix but contain no rational-prime generators at all in the deformed tail.

The controls are also tightly matched at the counting level. If `x>A+h`, then

\[
N_{A,h}(x):=\#\{q\in R_{A,h}:q\le x\}
=\pi(x-h),
\tag{5}
\]

so

\[
|N_{A,h}(x)-\pi(x)|
=\pi(x)-\pi(x-h)
\le h.
\tag{6}
\]

Equation `(6)` is not itself a new discriminator result; AF-368 already establishes that strong integer-counting proximity does not identify the rational primes. The new point is `(2)`: even the complete full-domain relative-curvature profile has no positive provenance wall against this wholesale fixed-shift tail deformation.

## Derivation

Put

\[
D_{A,h}(s)
:=P_{A,h}(s)-P(s)
=
\sum_{p>A}\big((p+h)^{-s}-p^{-s}\big),
\tag{7}
\]

and

\[
\eta_{A,h}(s):=\frac{D_{A,h}(s)}{P(s)}.
\tag{8}
\]

Then

\[
P_{A,h}(s)=P(s)(1+\eta_{A,h}(s))
\]

and

\[
\kappa_{A,h}(s)-\kappa(s)
=
\frac{d^2}{ds^2}\log(1+\eta_{A,h}(s)).
\tag{9}
\]

As in AF-512, split `(1,\infty)` into a fixed boundary neighborhood and a complementary closed right half-line.

### 1. The whole shifted tail is only `O((1+\log^2A)/A)` in the first two source derivatives near `s=1`

Fix `0<\delta<1/2`. For `j=0,1,2`, let

\[
f_{j,s}(x)=\partial_s^j x^{-s}=(-\log x)^j x^{-s}.
\]

For `1<s\le1+\delta`, differentiation in the generator variable gives

\[
|\partial_x f_{j,s}(x)|
\le
C_{\delta,j}(1+\log^2x)x^{-2},
\qquad j=0,1,2.
\tag{10}
\]

The mean-value theorem on `[p,p+h]` therefore yields

\[
|f_{j,s}(p+h)-f_{j,s}(p)|
\le
C_{h,\delta}(1+\log^2p)p^{-2}.
\tag{11}
\]

Summing first over primes and then majorizing by all integers gives

\[
\boxed{
|D_{A,h}^{(j)}(s)|
\le
C_{h,\delta}
\sum_{n>A}\frac{1+\log^2n}{n^2}
\le
C_{h,\delta}\frac{1+\log^2A}{A}
=:C_{h,\delta}E_A
}
\tag{12}
\]

uniformly for `1<s\le1+\delta` and `j=0,1,2`.

Thus moving infinitely many tail atoms still produces a uniformly small perturbation at the convergence boundary because each fixed shift contributes one extra inverse power of generator scale, and those first-order generator differences are summable.

### 2. Prime-zeta boundary growth dilutes the cofinite-tail perturbation

Write `s=1+t`, `L(t)=\log(1/t)`, and `g=\log P`. AF-512 records the classical prime-zeta estimates, after possibly shrinking `\delta`,

\[
P(1+t)\asymp L(t),
\qquad
|g'(1+t)|\ll\frac1{tL(t)},
\qquad
\kappa(1+t)\asymp\frac1{t^2L(t)}.
\tag{13}
\]

In particular,

\[
P(1+t)\kappa(1+t)\asymp t^{-2}.
\tag{14}
\]

Differentiating `(8)` gives

\[
\eta'
=\frac1P(D'-g'D)
\tag{15}
\]

and

\[
\eta''
=
\frac1P
\left[
D''-2g'D'+\big((g')^2-\kappa\big)D
\right],
\tag{16}
\]

where the subscripts `A,h` are suppressed.

Using `(12)`--`(14)`, each term in `(16)` divided by `\kappa` is uniformly bounded as follows:

\[
\frac{|D''|}{P\kappa}
\ll E_A t^2,
\qquad
\frac{|g'D'|}{P\kappa}
\ll E_A\frac{t}{L(t)},
\tag{17}
\]

\[
\frac{\kappa|D|}{P\kappa}
=\frac{|D|}{P}
\ll\frac{E_A}{L(t)},
\qquad
\frac{|g'|^2|D|}{P\kappa}
\ll\frac{E_A}{L(t)^2}.
\tag{18}
\]

Hence

\[
\sup_{1<s\le1+\delta}
\frac{|\eta_{A,h}''(s)|}{\kappa(s)}
\le C_{h,\delta}E_A.
\tag{19}
\]

Equation `(15)` similarly gives

\[
\sup_{1<s\le1+\delta}
\frac{|\eta_{A,h}'(s)|^2}{\kappa(s)}
\le C_{h,\delta}E_A^2,
\tag{20}
\]

and `(12)`--`(13)` give `\sup|\eta_{A,h}|\to0`. Therefore, for large `A`, `|\eta_{A,h}|\le1/2`, and

\[
\frac{d^2}{ds^2}\log(1+\eta)
=
\frac{\eta''}{1+\eta}
-
\frac{(\eta')^2}{(1+\eta)^2}
\tag{21}
\]

implies

\[
\boxed{
\sup_{1<s\le1+\delta}
\frac{|\kappa_{A,h}(s)-\kappa(s)|}{\kappa(s)}
\le C_{h,\delta}E_A.
}
\tag{22}
\]

So the divergence at `s=1` does not restore tail provenance even when the perturbation changes every sufficiently remote prime generator.

### 3. The complementary right half-line is exponentially easier

Set `\sigma=1+\delta`. For `s\ge\sigma`, the same mean-value argument can retain the factor `x^{-s-1}`. For `j\le2`, integral comparison gives

\[
|D_{A,h}^{(j)}(s)|
\le
C_{h,\sigma}A^{-s}(1+\log^2A),
\qquad s\ge\sigma.
\tag{23}
\]

Indeed, the factor `s` arising from `\partial_x x^{-s}` or its logarithmically weighted analogues is canceled at the level of the tail integral by

\[
s\int_A^\infty x^{-s-1}\,dx=A^{-s},
\]

with the first two logarithmic moments contributing only a polynomial in `\log A` and bounded powers of `1/s`.

Since `P(s)\ge2^{-s}` and `g'`, `\kappa` are bounded on `[\sigma,\infty)`, equations `(15)`--`(16)` imply

\[
|\eta_{A,h}^{(j)}(s)|
\le
C_{h,\sigma}(1+\log^2A)
\left(\frac2A\right)^s,
\qquad j=0,1,2.
\tag{24}
\]

AF-511 supplies the fixed-pair lower envelope

\[
\kappa(s)\ge c_\sigma\left(\frac23\right)^s,
\qquad s\ge\sigma.
\tag{25}
\]

Combining `(21)`, `(24)`, and `(25)` gives, for large `A`,

\[
\frac{|\kappa_{A,h}(s)-\kappa(s)|}{\kappa(s)}
\le
C_{h,\sigma}(1+\log^2A)
\left(\frac3A\right)^s.
\tag{26}
\]

Because `A>3`, the right side decreases with `s`, and therefore

\[
\sup_{s\ge1+\delta}
\frac{|\kappa_{A,h}(s)-\kappa(s)|}{\kappa(s)}
\le
C_{h,\delta}(1+\log^2A)A^{-(1+\delta)}.
\tag{27}
\]

The boundary estimate `(22)` dominates `(27)`, proving `(2)`--`(3)`.

Once the relative error is below `1/2`, positivity of both curvature profiles and `|\log(1+x)|\le2|x|` give `(4)`.

## Fidelity and matched-control audit

The fixed-shift family removes the most important weakness of the AF-511/AF-512 control. A single remote replacement is a finite Euler modification and therefore need not alter the nontrivial-zero question. The deformation `(1)` is instead **infinite in the tail**: for every `A`, all prime generators above `A` are moved.

For `h=1`, this gives an especially hard provenance control:

- the source is ordinary, integer-supported, simple, primitive, and unit-weight;
- it agrees exactly with the rational primes below the chosen cutoff;
- its counting function differs from `\pi(x)` by at most one beyond the transition;
- every deformed tail generator is composite;
- its full curvature profile converges to the prime profile in both relative-curvature and log-curvature sup metrics.

Thus neither a long exact prefix, bounded counting discrepancy, nor access to the complete convergence-domain curvature profile creates a positive rational-prime provenance margin in this topology.

The theorem remains a **stability obstruction**, not an exact collision. AF-509 and AF-510 remain intact: complete curvature equality still determines a normalized simple source exactly, and the exact canonical inverse still exists. The new conclusion is that this inverse is discontinuous or arbitrarily ill-conditioned for the declared provenance task along a control sequence that changes the whole remote tail rather than one atom.

## Representation audit

The exact representation tested here is the full-domain prime-anchored relative-curvature seminorm

\[
\|Q-\mathbb P\|_{\mathrm{rel}\,\kappa}
:=
\sup_{s>1}
\frac{|\kappa_Q(s)-\kappa_{\mathbb P}(s)|}
     {\kappa_{\mathbb P}(s)},
\tag{28}
\]

and the closely related scale-invariant log-curvature metric

\[
d_{\log\kappa}(Q,\mathbb P)
:=
\sup_{s>1}|\log\kappa_Q(s)-\log\kappa_{\mathbb P}(s)|.
\tag{29}
\]

These are mathematically natural conditioning topologies for the AF-509 curvature carrier, but they are **modeling choices**, not uniquely canonical source metrics. Nearby stronger representations include source-pullback distances after the AF-510 inverse, atom-indexed or moving-generator observations, and arithmetic marks recording congruence, gcd, factorization, squarefreeness, or other source incidence.

The conclusion changes under such enrichments. For example, parity immediately separates the `h=1` shifted tail from the rational primes, while a pullback metric that directly prices generator displacement can also keep the controls apart. Those alternatives are not contradicted by `(2)`.

The representation-invariant core is narrower: **exact injectivity of a compression does not imply robust provenance recovery, and even changing an entire remote tail can be invisible in a natural full-profile topology.** Any repair must strengthen the retained representation or weaken the target discriminator; it cannot be obtained merely by observing the same curvature carrier closer to `s=1`.

## Prior art and novelty assessment

The ingredients surrounding this statement are classical, and no novelty is claimed for shifted primes, prime-zeta asymptotics, or inverse-Laplace ill-conditioning.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187–202, DOI `10.1007/BF01933420`, is a classical source for the prime zeta function used in AF-509--AF-512.
- Adolf Hildebrand, **“Additive and Multiplicative Functions on Shifted Primes,”** *Proceedings of the London Mathematical Society* (3) 59 (1989), 209–232, DOI `10.1112/plms/s3-59.2.209`, is representative prior art for the arithmetic study of the shifted-prime sequence `p+1`. That literature studies arithmetic functions on shifted primes, not the curvature-compression stability statement `(2)`.
- AF-511 audits the neighboring inverse-Laplace and Prony stability literature, including Dong (1993), Plonka--Tasche (2014), Maréchal--Triki--Lee (2024), and Katz--Diab--Batenkov (2024). Those works establish the broader fact that exponential-source inversion can be severely ill-conditioned.
- AF-368 already shows that logarithmic integer-counting proximity does not identify the rational-prime source, so `(6)` is used here only as a matched-control property, not as a new finding.

A targeted search for fixed shifts of the prime tail combined with prime-zeta/log-prime-zeta curvature and full-domain relative stability did not expose a standard theorem equivalent to `(2)`. The durable Arithmetic Fidelity delta is therefore intentionally specific and carries `NO-NOVELTY-CLAIM`: the exact estimate `(2)` upgrades the one-atom obstruction of AF-511/AF-512 to a source family whose **entire sufficiently remote prime tail is changed**.

## Boundaries and failure modes

- **The shift is fixed.** Constants may depend on `h`. No uniform theorem for shifts `h=h(A)` growing with the cutoff is claimed.
- **No zero-divisor conclusion is asserted.** Unlike AF-511/AF-512's finite replacement, `(1)` is an infinite Euler-data deformation. The present proof neither preserves nor classifies the analytic continuation, functional equation, or zero set of any Euler product associated with `R_{A,h}`.
- **Exact curvature fidelity remains rigid.** The controls approach but never equal the prime curvature profile. AF-509/AF-510 are not contradicted.
- **The topology is explicit.** Stronger source-aware metrics or independent arithmetic incidence marks may separate these controls.
- **Counting proximity is not enough.** Equation `(6)` deliberately reuses a weakness already exposed abstractly by AF-368; it is not evidence that all density-matched controls behave the same way under other transforms.
- **The source class is simple integer-supported unit weight.** The theorem does not need generalized nonintegral Beurling generators, arbitrary weights, or a rescaling gauge.

## Research consequence

AF-512 showed that moving the same curvature observation all the way to the convergence boundary does not recover a positive provenance margin for one remote prime replacement. Equation `(2)` now closes a stronger escape: the failure is not an artifact of changing only finitely many Euler generators.

A full fixed-shift tail can be arithmetically very different while remaining uniformly invisible to the retained curvature profile. In particular, `h=1` replaces every sufficiently large rational prime by a composite integer and still converges to the rational-prime curvature in the strongest relative full-domain topology studied in AF-511--AF-513.

The next useful repair question is therefore sharper. Any proposed source-aware topology or arithmetic lift should be tested against `(R_{A,h})` and should identify **which additional incidence survives this tail deformation and why that incidence is relevant to the eventual arithmetic target**. Merely enlarging the curvature observation domain, retaining a longer finite prime prefix, or matching the prime counting function more closely cannot answer that question.