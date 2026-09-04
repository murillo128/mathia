# MC-051 — Real square-free amplitudes preserve the Möbius comparator positivity bootstrap

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
f:\mathbb N\to[-1,1]
\]

be multiplicative and supported on the square-free integers, so that

\[
f(p^k)=0\qquad(k\ge2)
\]

for every prime `p`. Assume that for some fixed

\[
0<\alpha<1
\]

one has

\[
S_f(x):=\sum_{n\le x}f(n)\ll x^\alpha.
\tag{1}
\]

Write

\[
F(s)=\sum_{n\ge1}\frac{f(n)}{n^s}.
\]

Since `mu(p)=-1`, the ordinary prime-level pretentious distance from Möbius is

\[
\mathbb D(f,\mu;\infty)^2
=\sum_p\frac{1+f(p)}p.
\tag{2}
\]

Under `(1)`, the following are equivalent:

\[
\boxed{
F(1)=0
\quad\Longleftrightarrow\quad
\mathbb D(f,\mu;\infty)<\infty
\quad\Longleftrightarrow\quad
\sum_p\frac{1+f(p)}p<\infty.
}
\tag{3}
\]

Moreover, either condition in `(3)` self-upgrades to power-aware control at every exponent above the observed summatory exponent:

\[
\boxed{
\sum_p\frac{1+f(p)}{p^\sigma}<\infty
\qquad(\sigma>\alpha).
}
\tag{4}
\]

The upgrade extends to an absolutely summable inverse convolution kernel, and consequently

\[
\boxed{
M(x)=O_{f,\varepsilon}(x^{\alpha+\varepsilon})
\qquad(\varepsilon>0),
}
\tag{5}
\]

and

\[
\boxed{
\zeta(s)\ne0
\qquad(\operatorname{Re}s>\alpha).
}
\tag{6}
\]

Thus the exact `f(p)=+-1` sign hypothesis in `MC-050` is not load-bearing. The obstruction survives throughout the larger real square-free-supported unit-ball class `f(p) in [-1,1]`. Allowing a fixed comparator to attenuate its prime amplitudes, while retaining finite global ordinary Möbius distance and an independently proved power bound, does not create a cheaper route: the comparator estimate still transfers essentially the same exponent to Möbius and forces the matching zeta zero-free half-plane.

At the RH scale, if one fixed such `f` has finite global ordinary distance from Möbius and

\[
S_f(x)=O_\varepsilon(x^{1/2+\varepsilon})
\qquad\text{for every }\varepsilon>0,
\tag{7}
\]

then RH follows.

The result is stored as a line-specific extension of the classical nonnegative-Dirichlet-series/Landau mechanism, with no standalone novelty claim.

## 1. The quotient `1*f` remains coefficientwise nonnegative

Set

\[
h=1*f,
\]

where `1(n)=1`. Since `f` is square-free-supported, its Euler factor is

\[
1+f(p)z,
\qquad z=p^{-s},
\]

and hence

\[
H(s):=\zeta(s)F(s)
=\prod_p\frac{1+f(p)p^{-s}}{1-p^{-s}}
\qquad(\operatorname{Re}s>1).
\tag{8}
\]

At each prime,

\[
\frac{1+f(p)z}{1-z}
=1+(1+f(p))z+(1+f(p))z^2+\cdots.
\tag{9}
\]

Because `-1<=f(p)<=1`,

\[
1+f(p)\ge0.
\]

Therefore

\[
\boxed{h(n)\ge0\quad\text{for every }n,}
\tag{10}
\]

with the exact local rule

\[
h(p^k)=1+f(p)\in[0,2]
\qquad(k\ge1).
\tag{11}
\]

In particular `h(n)<=2^omega(n)<=d(n)`, so its Dirichlet series has finite abscissa of convergence and Landau's theorem for nonnegative Dirichlet coefficients applies.

Also,

\[
f=\mu*h,
\tag{12}
\]

because `mu*1` is the convolution identity.

This identifies the actual structural hypothesis behind `MC-050`: not the discreteness of the prime signs, but coefficientwise positivity of the zeta quotient created by real square-free-supported amplitudes bounded below by `-1`.

## 2. Finite ordinary Möbius distance forces `F(1)=0`

The bound `(1)` gives, by partial summation,

\[
F(s)=s\int_1^\infty S_f(x)x^{-s-1}\,dx
\tag{13}
\]

throughout `Re(s)>alpha`. Thus `F` is holomorphic there, in particular at `s=1`.

Assume

\[
\sum_p\frac{1+f(p)}p<\infty.
\tag{14}
\]

For real `sigma>1`, write

\[
R_f(\sigma)
:=\prod_p\frac{1+f(p)p^{-\sigma}}{1-p^{-\sigma}}.
\tag{15}
\]

Uniformly for `f(p) in [-1,1]`,

\[
\log\frac{1+f(p)/p}{1-1/p}
=\frac{1+f(p)}p+O\!\left(\frac1{p^2}\right).
\tag{16}
\]

Hence `(14)` makes `R_f(sigma)` tend to a finite strictly positive limit as `sigma->1+`. From `(8)`,

\[
F(\sigma)=\frac{R_f(\sigma)}{\zeta(\sigma)}.
\]

The pole of zeta at `1` gives `F(sigma)->0`; holomorphy from `(13)` then gives

\[
F(1)=0.
\tag{17}
\]

No zeta zero-free region to the left of `1` is used in this direction.

## 3. `F(1)=0` forces power-aware prime control

Conversely, assume `(1)` and `(17)`. Since the simple zeta pole at `1` is cancelled by the zero of `F`,

\[
H(s)=\zeta(s)F(s)
\tag{18}
\]

is holomorphic throughout `Re(s)>alpha`.

The coefficients of `H` are nonnegative by `(10)`. Landau's theorem says that the finite abscissa of convergence of a Dirichlet series with nonnegative coefficients is a singular point of the represented function. Since `(18)` has no singularity anywhere in `Re(s)>alpha`, the abscissa of convergence of the Dirichlet series for `H` is at most `alpha`.

Therefore, for every fixed `sigma>alpha`,

\[
\sum_{n\ge1}\frac{h(n)}{n^\sigma}<\infty.
\tag{19}
\]

Taking only prime terms and using `(11)` proves `(4)`. Taking `sigma=1` also proves the reverse implication in `(3)`:

\[
\sum_p\frac{1+f(p)}p
\le
\sum_{n\ge1}\frac{h(n)}n
<\infty.
\tag{20}
\]

Thus the comparator's own power cancellation turns a merely ordinary prime-harmonic relation into the stronger scale-sensitive relation that generic pretentious theory cannot infer from ordinary distance alone.

## 4. The inverse kernel is dominated by the positive quotient

Let

\[
k=h^{-1}
\]

under Dirichlet convolution. From `(9)`, its local generating factor is

\[
\frac{1-z}{1+f(p)z}.
\tag{21}
\]

For `k>=1`, the prime-power coefficients are

\[
k(p) = -(1+f(p)),
\tag{22}
\]

and for `j>=2`,

\[
k(p^j)=-(1+f(p))(-f(p))^{j-1}.
\tag{23}
\]

Hence, since `|f(p)|<=1`,

\[
|k(p^j)|
=(1+f(p))|f(p)|^{j-1}
\le 1+f(p)
=h(p^j).
\tag{24}
\]

Both `h` and `k` are multiplicative, so

\[
\boxed{|k(n)|\le h(n)\quad\text{for every }n.}
\tag{25}
\]

Combining `(19)` and `(25)`,

\[
\boxed{
\sum_{n\ge1}\frac{|k(n)|}{n^\sigma}<\infty
\qquad(\sigma>\alpha).
}
\tag{26}
\]

For the sign-valued class of `MC-050`, this domination is an equality. The present calculation shows that equality was unnecessary; one-sided absolute domination is enough for exponent transfer.

## 5. The comparator exponent transfers back to the Mertens function

From `(12)` and `h*k=epsilon`,

\[
\mu=f*k.
\tag{27}
\]

Therefore

\[
M(x)
=\sum_{d\le x}k(d)S_f(x/d).
\tag{28}
\]

Using `(1)`, for every `epsilon>0`,

\[
\begin{aligned}
|M(x)|
&\ll_f x^\alpha
\sum_{d\le x}\frac{|k(d)|}{d^\alpha}\\
&\le
x^{\alpha+\varepsilon}
\sum_{d\ge1}\frac{|k(d)|}{d^{\alpha+\varepsilon}}.
\end{aligned}
\tag{29}
\]

The final series is finite by `(26)`, proving `(5)`.

This transfer is fixed-comparator rather than uniform. The implied constant may depend strongly on `f` and `epsilon`; as in `MC-050`, scale-dependent families whose prime perturbation moves with `x` are not controlled by the statement.

## 6. The same quotient forces a zeta zero-free half-plane

For `sigma>alpha`, `(19)` gives absolute convergence of the multiplicative Dirichlet series for `H`. Consequently its Euler product converges absolutely there. Every local factor

\[
\frac{1+f(p)p^{-s}}{1-p^{-s}}
\tag{30}
\]

is nonzero for `Re(s)>alpha`: because `alpha>0`, one has `|p^{-s}|<1`, and therefore `|f(p)p^{-s}|<1`.

Thus

\[
H(s)\ne0
\qquad(\operatorname{Re}s>\alpha).
\tag{31}
\]

But `(18)` holds throughout that half-plane by analytic continuation. If zeta had a zero `rho` with `Re(rho)>alpha`, then

\[
H(\rho)=\zeta(\rho)F(\rho)=0,
\]

contradicting `(31)`. This proves `(6)`.

At the RH-scale hypothesis `(7)`, fix any `eta>0` and apply the result with `alpha=1/2+eta`. Zeta is zero-free in `Re(s)>1/2+eta`; letting `eta->0` excludes every zero strictly to the right of the critical line, and the functional-equation symmetry gives RH.

## 7. Falsification controls and surviving escape classes

The generalization closes one immediate boundary left open by `MC-050`. Replacing the exact prime signs `+-1` by smaller **real** amplitudes does not evade the positivity bootstrap. The local identities `(9)` and `(24)` show why: real values in `[-1,1]` preserve both nonnegativity of `1*f` and absolute domination of its inverse.

Several nearby changes are genuinely outside the claim.

First, complex prime phases need not make `1+f(p)` nonnegative real. Landau's coefficient-positivity step then disappears, so this finding does not classify complex square-free-supported comparators.

Second, changing the prime-power support changes the local quotient itself. The formula `(9)` uses `f(p^k)=0` for `k>=2`; a comparator with nonzero prime-square data may have signed quotient coefficients or a different inverse-kernel threshold.

Third, finite **global** ordinary distance is essential. A moving terminal-prime perturbation can be close at each finite scale while its global comparator is not fixed; `MC-045`--`MC-048` already show why one-scale pretentious control does not transfer a fixed power exponent uniformly.

Fourth, dropping the independent power bound `(1)` removes the analytic continuation of `F` past `1` and therefore removes the Landau bootstrap. Ordinary global distance by itself still does not transfer power cancellation for generic multiplicative functions, consistent with Jung--Lemke Oliver (`MC-S7`).

Finally, the theorem is an obstruction to a **single comparator summatory estimate**. It does not rule out signed bilinear identities, multiscale relations, cancellation between several auxiliary functions, or structures whose useful information is not representable by finite ordinary distance plus one partial-sum exponent.

## 8. Prior art and novelty boundary

The standard literature on multiplicative functions "resembling the Möbius function" uses the square-free-supported sign class `f(p)=+-1`. Marco Aymone, *A note on multiplicative functions resembling the Möbius function*, Journal of Number Theory 212 (2020), 113--121, DOI `10.1016/j.jnt.2019.10.025`, arXiv `1908.11014`, explicitly works in that sign-valued class and studies cancellation and zero-free consequences. `MC-S16` records the later Klurman--Mangerel--Pohoata--Teräväinen discrepancy theorem for the same square-free-supported sign setting.

The nonnegative-Dirichlet-series/Landau mechanism used here is classical. `MC-S33` records Aymone's adjacent theorem for **completely multiplicative real** functions with small partial sums, where positivity of a related convolution is used to obtain prime control and a zeta zero-free region. `MC-049` already identified the corresponding global Liouville-close obstruction in that completely multiplicative class. `MC-050` specialized the positivity bootstrap to square-free-supported prime signs and obtained direct absolute convolution transfer back to Möbius.

A targeted search across the square-free-supported Möbius-resembling literature, real bounded multiplicative functions, small partial sums, and zeta zero-free arguments found these neighboring mechanisms but did not establish the exact `[-1,1]` square-free-supported extension `(3)`--`(6)` as a named theorem. Absence from that search is not evidence of novelty. The durable result is therefore classified only as a **Mathia-specific structural extension**: it identifies the minimal local inequality behind `MC-050` and removes prime-sign discreteness as a possible escape hatch.

## Consequence for the research line

The comparator frontier is now narrower than `MC-050` stated. For fixed square-free-supported real comparators, the strategically relevant divide is not `f(p)=+-1` versus attenuated prime values. It is **positive versus nonpositive quotient structure**.

Any next comparator proposal that keeps `f(p) in [-1,1]`, finite global ordinary Möbius distance, and an independently provable power exponent should be rejected immediately as a relocation of the Mertens/RH burden: equations `(19)`--`(29)` force that exponent back to Möbius. A genuinely different route must break at least one of those load-bearing inputs or exploit a multi-object relation that is not reducible to one globally close auxiliary partial sum.