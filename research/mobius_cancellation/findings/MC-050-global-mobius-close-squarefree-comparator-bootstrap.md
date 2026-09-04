# MC-050 — Global Möbius closeness self-upgrades to power-aware transfer for exact-support sign comparators

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
f:\mathbb N\to\{-1,0,1\}
\]

be multiplicative, supported exactly on the square-free integers, with

\[
f(p)\in\{-1,+1\}
\qquad\text{for every prime }p.
\tag{1}
\]

Thus `f` is in the standard class of multiplicative functions that resemble Möbius. Write

\[
S_f(x)=\sum_{n\le x}f(n),
\qquad
F(s)=\sum_{n\ge1}\frac{f(n)}{n^s},
\]

and assume for some fixed

\[
0<\alpha<1
\]

that

\[
S_f(x)\ll x^\alpha.
\tag{2}
\]

Let

\[
E=\{p:f(p)=+1\}.
\tag{3}
\]

Since `mu(p)=-1`, the global ordinary pretentious distance from Möbius is

\[
\mathbb D(f,\mu;\infty)^2
=2\sum_{p\in E}\frac1p.
\tag{4}
\]

Under the power-cancellation hypothesis `(2)`, the following are equivalent:

\[
\boxed{
F(1)=0
\quad\Longleftrightarrow\quad
\mathbb D(f,\mu;\infty)<\infty
\quad\Longleftrightarrow\quad
\sum_{p\in E}\frac1p<\infty.
}
\tag{5}
\]

More importantly, either condition in `(5)` **self-upgrades** the weak prime-harmonic relation to power-aware information at every exponent strictly above the observed partial-sum exponent:

\[
\boxed{
\sum_{p\in E}p^{-\sigma}<\infty
\qquad\text{for every }\sigma>\alpha.
}
\tag{6}
\]

The same upgrade holds for the full absolute Dirichlet-convolution kernels between `f` and Möbius. Consequently,

\[
\boxed{
\zeta(s)\ne0
\qquad (\operatorname{Re}s>\alpha),
}
\tag{7}
\]

and for every `epsilon>0`,

\[
\boxed{
M(x)=O_{f,\varepsilon}(x^{\alpha+\varepsilon}).
}
\tag{8}
\]

Thus an exact-square-free-support sign comparator cannot be both **globally ordinarily Möbius-pretentious** and **independently power-cancellative** without transferring essentially the same exponent back to Möbius and forcing the matching zeta zero-free half-plane.

At the RH scale this is decisive. If one fixed such `f` has finite global ordinary distance from Möbius and

\[
S_f(x)=O_\varepsilon(x^{1/2+\varepsilon})
\qquad\text{for every }\varepsilon>0,
\tag{9}
\]

then RH follows. Therefore the exact-support comparator escape left open by `MC-049` cannot be realized merely by dropping complete multiplicativity while retaining finite global ordinary proximity to Möbius.

The mechanism is not a new RH criterion. It is a special positivity bootstrap inside the already studied square-free-supported sign class: the comparator's own power cancellation turns ordinary `1/p` closeness into the stronger prime-power convolution control that generic pretentious theory does not obtain from ordinary distance alone.

## 1. The Möbius comparison has a positive convolution quotient

Because `f` vanishes on every prime power `p^k`, `k>=2`, its Euler factor is

\[
1+f(p)p^{-s}.
\]

Let

\[
h=1*f,
\]

where `1(n)=1`. Then

\[
H(s):=\sum_{n\ge1}\frac{h(n)}{n^s}
=\zeta(s)F(s)
\qquad (\operatorname{Re}s>1).
\tag{10}
\]

Put `z=p^{-s}`. If `p\notin E`, then `f(p)=-1` and

\[
\frac{1-z}{1-z}=1.
\]

If `p\in E`, then `f(p)=+1` and

\[
\frac{1+z}{1-z}
=1+2z+2z^2+2z^3+\cdots.
\tag{11}
\]

Hence

\[
\boxed{
h(n)\ge0\quad\text{for every }n,}
\tag{12}
\]

with the exact local rule

\[
h(p^k)=
\begin{cases}
2,&p\in E,\ k\ge1,\\
0,&p\notin E,\ k\ge1.
\end{cases}
\tag{13}
\]

Equivalently,

\[
H(s)
=R_E(s)
:=\prod_{p\in E}\frac{1+p^{-s}}{1-p^{-s}}
\qquad (\operatorname{Re}s>1).
\tag{14}
\]

The coefficient sequence is harmlessly divisor-bounded: if all prime factors of `n` lie in `E`, then `h(n)=2^{\omega(n)}<=d(n)`, and otherwise `h(n)=0`. Thus its Dirichlet series has a finite abscissa of convergence and Landau's nonnegative-coefficient theorem applies.

Also, since `mu*1` is the convolution identity,

\[
f=\mu*h.
\tag{15}
\]

The reverse kernel `k=h^{-1}` has at each `p\in E`

\[
\sum_{j\ge0}k(p^j)z^j
=\frac{1-z}{1+z}
=1-2z+2z^2-2z^3+\cdots,
\tag{16}
\]

and is trivial away from `E`. Therefore

\[
\boxed{|k(n)|=h(n)\quad\text{for every }n.}
\tag{17}
\]

This positivity/absolute-symmetry is the special structure absent from a generic pair of ordinarily pretentious multiplicative functions.

## 2. Global ordinary Möbius closeness is equivalent to the zero at `s=1`

The bound `(2)` implies by partial summation that `F(s)` is holomorphic throughout

\[
\operatorname{Re}s>\alpha,
\tag{18}
\]

so in particular `F(1)` is a genuine analytic value.

Assume first that the global distance in `(4)` is finite. Then

\[
\sum_{p\in E}\frac1p<\infty.
\]

For real `sigma>1`, equation `(14)` gives

\[
F(\sigma)=\frac{R_E(\sigma)}{\zeta(\sigma)}.
\tag{19}
\]

Since

\[
\log\frac{1+p^{-1}}{1-p^{-1}}
=\frac2p+O\!\left(\frac1{p^2}\right),
\tag{20}
\]

`R_E(sigma)` tends to a finite strictly positive limit as `sigma->1+`. The pole of zeta at `1` therefore gives

\[
F(\sigma)\to0.
\]

By `(18)`,

\[
F(1)=0.
\tag{21}
\]

Conversely, assume `(2)` and `(21)`. The only pole of `zeta(s)` in `Re(s)>alpha` is its simple pole at `1`, and the zero `(21)` cancels it. Hence

\[
H(s)=\zeta(s)F(s)
\tag{22}
\]

is holomorphic on the whole half-plane `Re(s)>alpha`.

But the Dirichlet coefficients of `H` are nonnegative by `(12)`. Landau's theorem says that the finite abscissa of convergence of a Dirichlet series with nonnegative coefficients is a singular point. Since `(22)` has no singularity anywhere in `Re(s)>alpha`, that abscissa is at most `alpha`. In particular the series for `H` converges at `s=1`, and `(13)` gives

\[
2\sum_{p\in E}\frac1p
\le
\sum_{n\ge1}\frac{h(n)}n
<\infty.
\tag{23}
\]

This proves `(5)`.

The forward implication resembles the elementary Euler-ratio half of `MC-049`; the reverse implication uses the same classical nonnegative-coefficient Landau mechanism that underlies the adjacent Aymone/Venturini zero-free literature, now made exact for the square-free-supported Möbius-comparator quotient `(11)`.

## 3. Comparator cancellation bootstraps `1/p` closeness to every `p^{-sigma}` above `alpha`

The Landau argument gives more than `(23)`. Since the abscissa of convergence of `H` is at most `alpha`, for every fixed

\[
\sigma>\alpha
\]

one has

\[
\sum_{n\ge1}\frac{h(n)}{n^\sigma}<\infty.
\tag{24}
\]

Applying `(13)` to the prime terms proves `(6)`. Applying `(17)` gives simultaneously

\[
\boxed{
\sum_{n\ge1}\frac{|k(n)|}{n^\sigma}
=
\sum_{n\ge1}\frac{h(n)}{n^\sigma}
<\infty
\qquad(\sigma>\alpha).
}
\tag{25}
\]

Thus the comparator's own power cancellation has converted a priori ordinary global proximity,

\[
\sum_{p\in E}p^{-1}<\infty,
\]

into the full absolute convolution control at all exponents above `alpha`. In the language audited in `MC-047`, the missing power-aware information is not an additional independent hypothesis for this particular comparator class: positivity of `1*f` forces it once `(2)` is known.

This does **not** contradict Jung--Lemke Oliver (`MC-S7`). Their central warning is that ordinary pretentiousness does not transfer power cancellation for general multiplicative functions. The implication here uses two special facts simultaneously: exact Möbius square-free support makes the quotient `(11)` coefficientwise nonnegative, and the proposed comparator already satisfies a power bound strong enough to continue `F` left of `1`. Without either input, Landau cannot perform the upgrade.

## 4. The upgraded kernel transfers the exponent back to Möbius

From `(15)` and `(16)`,

\[
\mu=f*k.
\tag{26}
\]

Therefore

\[
M(x)
=
\sum_{d\le x}k(d)S_f(x/d).
\tag{27}
\]

Using `(2)`, for every `epsilon>0`,

\[
\begin{aligned}
|M(x)|
&\ll_f x^\alpha
\sum_{d\le x}\frac{|k(d)|}{d^\alpha}\\
&\le
x^{\alpha+\varepsilon}
\sum_{d\ge1}\frac{|k(d)|}{d^{\alpha+\varepsilon}}.
\end{aligned}
\tag{28}
\]

The final series is finite by `(25)`, proving `(8)`.

This is stronger than a mere zero-divisor fidelity statement. The comparator estimate itself transfers back to the actual Mertens function with only an arbitrarily small exponent loss. The transfer constant may depend strongly on `f` and `epsilon`; no uniform claim over a scale-dependent family is made.

## 5. The same positivity bootstrap forces a zeta zero-free half-plane

Equation `(24)` implies that the Euler product `(14)` converges absolutely and locally uniformly throughout `Re(s)>alpha`. Every local factor

\[
\frac{1+p^{-s}}{1-p^{-s}}
\]

is nonzero there because `alpha>0` gives `|p^{-s}|<1`. Hence

\[
R_E(s)\ne0
\qquad(\operatorname{Re}s>\alpha).
\tag{29}
\]

On `Re(s)>1`, equations `(10)` and `(14)` give

\[
\zeta(s)F(s)=R_E(s).
\]

Both sides are holomorphic on `Re(s)>alpha`, so uniqueness of analytic continuation gives the same identity throughout that half-plane. If `rho` were a zeta zero with `Re(rho)>alpha`, then the left side would vanish at `rho`, while `(29)` says the right side does not. This contradiction proves `(7)`.

Equivalently, the positive convolution quotient cannot mask a zeta zero once the comparator's power cancellation has forced its Euler product to converge at that zero's real part.

For the RH-scale statement `(9)`, fix any `eta in (0,1/2)` and apply the result with

\[
\alpha=\frac12+\eta.
\]

Then zeta is zero-free in `Re(s)>1/2+eta`. Letting `eta` tend to zero excludes every zero strictly to the right of the critical line; the functional-equation symmetry excludes zeros strictly to the left. Thus RH follows.

## 6. Matched controls and boundaries

Several existing controls show exactly what this finding does and does not rule out.

First, the residue-class exact-support comparators from `MC-005` can have strong qualitative mean cancellation while still possessing large partial sums. They are not globally Möbius-close in `(4)`: their `+1` prime set contains fixed positive-density residue classes, so the reciprocal-prime mass diverges. The new bootstrap therefore does not turn those examples into a contradiction.

Second, the terminal-prime family `nu_X` from `MC-045`--`MC-048` is deliberately scale-dependent. For every frozen `X` its changed-prime set is finite, but the constants in `(24)`--`(28)` deteriorate with `X`; `MC-047` and `MC-048` quantify exactly that nonuniformity. The present theorem is about one fixed comparator with one fixed global prime set, not a family whose perturbation moves with the observation scale.

Third, `MC-049` treated fixed **completely multiplicative** real functions globally close to Liouville and used Aymone's theorem to show that independently proving a power saving already pays the zeta zero-free burden. The present result closes the most immediate boundary left there: exact-square-free-support sign comparators are not completely multiplicative, but their convolution with `1` has a stronger coefficientwise positivity that yields the same strategic obstruction and additionally gives the direct transfer `(8)`.

Fourth, the conclusion depends essentially on finite **global** ordinary distance. Finite one-scale distance, bounded distance along a moving cutoff, or merely `D(f,mu;x)=o(sqrt(log log x))` does not give `(20)` or a fixed Euler product at `1`. The one-scale failures of `MC-045` and the general ordinary-pretentiousness failures in `MC-S7` therefore remain intact.

Finally, the theorem does not cover complex prime values, altered prime-power support, signed quotient kernels without positivity, or comparators whose relation to Möbius is local/multiscale rather than finite global ordinary distance. Those are genuinely different escape categories.

## 7. Prior art and novelty boundary

The exact-square-free-support sign class is established prior art; `MC-S16` anchors the literature around functions of the form `mu^2 g` and their partial-sum rigidity. Ordinary versus power-aware pretentiousness and the need for stronger transfer carriers are established by Jung--Lemke Oliver (`MC-S7`). The use of nonnegative Dirichlet coefficients and Landau's theorem to convert analytic continuation into Euler-factor control is classical; `MC-S33` records a directly adjacent use of that mechanism for small completely multiplicative functions and zeta zero-free regions. `MC-008` already separated analytic zero nonmasking from absolute convolution inversion for a different local Möbius comparator.

A targeted literature search of square-free-supported functions resembling Möbius, modified-character examples, pretentious power cancellation, and auxiliary zero-free arguments found these established neighboring mechanisms and conditional constructions, but no basis for a standalone novelty claim for `(5)`--`(8)`. The result is therefore stored as a **Mathia-specific synthesis and obstruction**, not as a new theorem of analytic number theory.

The line-specific addition is the exact self-bootstrap: in this entire real exact-support sign class, a fixed comparator's own `x^alpha` cancellation plus only ordinary global Möbius proximity forces the positive quotient `1*f` to have abscissa at most `alpha`; that in turn upgrades the relation to power-aware absolute convolution control and transfers the exponent back to Möbius.

## 8. Consequence for the comparator search

After `MC-047`--`MC-049`, one surviving hope was that an exact-support multiplicative comparator might be easier to cancel even if the completely multiplicative Liouville-like route is not. This finding sharply narrows that hope.

A fixed comparator in the full class `(1)` cannot be used as an easier RH-scale proxy if its only claimed bridge to Möbius is finite global ordinary pretentious distance. Once the comparator estimate is strong enough to be useful, the bridge automatically becomes power-aware and returns essentially the same exponent to `M(x)`.

Therefore a genuinely different comparator route must abandon at least one load-bearing ingredient: exact square-free sign support, finite global ordinary Möbius distance, fixed-function global comparison, or the positive convolution quotient. The most plausible remaining escape is not another globally close sign twist, but a signed/bilinear, complex-valued, altered-prime-power, or genuinely local/multiscale mechanism whose information cannot be collapsed to the positive Euler product `(14)`.