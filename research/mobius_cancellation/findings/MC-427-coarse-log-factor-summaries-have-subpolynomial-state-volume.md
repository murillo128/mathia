# MC-427 — Coarse logarithmic factor summaries have subpolynomial state volume

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · CLASSICAL-INGREDIENTS · FRONTIER-ADVANCE · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-426` leaves open unbounded additive per-prime data, with exact logarithmic factor size as the most natural example. Unboundedness alone is not enough. If an additive statistic has only moderately growing **total mass after quantization**, then the same factorization channel still has subpolynomial state volume.

Let `n<=X` be squarefree, write `r=omega(n)`, and consider all ordered active factorizations

\[
n=u_1\cdots u_d,
\qquad 1\le d\le r,
\qquad u_j>1.
\tag{1}
\]

Fix a dimension `m`. For each prime `p|n` and coordinate `1<=ell<=m`, let

\[
w_\ell(p)\ge0,
\qquad
W_\ell(n):=\sum_{p\mid n}w_\ell(p),
\tag{2}
\]

and choose a quantization mesh `eta_ell>0`. Retain a factor only through

\[
Q_\ell(u)
:=
\left\lfloor
\frac{1}{\eta_\ell}
\sum_{p\mid u}w_\ell(p)
\right\rfloor.
\tag{3}
\]

Put

\[
L_\ell:=\left\lfloor\frac{W_\ell(n)}{\eta_\ell}\right\rfloor.
\tag{4}
\]

Then the total number `N(n)` of distinct retained words

\[
\bigl(Q(u_1),\ldots,Q(u_d)\bigr)
\tag{5}
\]

across **all active depths** satisfies the exact combinatorial upper bound

\[
\boxed{
N(n)
\le
r\prod_{\ell=1}^m
\binom{L_\ell+r}{r}.
}
\tag{6}
\]

Consequently,

\[
\boxed{
\log N(n)
\le
\log r
+
r\sum_{\ell=1}^m
\left[1+\log\!\left(1+\frac{L_\ell}{r}\right)\right].
}
\tag{7}
\]

For squarefree `n<=X`, the elementary primorial/factorial bound gives

\[
r\le (1+o(1))\frac{\log X}{\log\log X}.
\tag{8}
\]

Hence, for fixed `m`, every family for which

\[
L_\ell
\le
\frac{\log X}{\log\log X}
(\log X)^{o(1)}
\qquad(1\le\ell\le m)
\tag{9}
\]

has

\[
\boxed{N(n)=X^{o(1)}}
\tag{10}
\]

uniformly for squarefree `n<=X`.

The important specialization is logarithmic factor size. Take

\[
w(p)=\log p,
\qquad
Q_\eta(u)=\left\lfloor\frac{\log u}{\eta}\right\rfloor.
\tag{11}
\]

Since `W(n)=log n<=log X`, every mesh satisfying

\[
\eta^{-1}=(\log X)^{o(1)}
\tag{12}
\]

still yields only

\[
\boxed{N_\eta(n)=X^{o(1)}}.
\tag{13}
\]

Thus fixed precision, poly-`log log X` precision, and more generally every sub-power-of-`log X` refinement of factor log-size cannot produce polynomially many retained factor states. A factor-size escape from `MC-426` must use genuinely increasing precision.

The converse capacity requirement is quantitative. If the scalar log-size words alone are claimed to provide at least `X^delta` distinct states for some fixed `delta>0`, then `(6)` forces

\[
\boxed{
\eta^{-1}
\ge
(\log X)^{\delta-o(1)}.
}
\tag{14}
\]

So polynomial state exponent `delta` requires at least inverse-`(log X)^delta` logarithmic resolution, up to subpower factors. Equivalently, the retained size channel must carry on the order of `delta log log X` growing precision bits before polynomial state capacity is even combinatorially possible.

This is a **necessary information-capacity condition only**. It does not show that inverse-polylogarithmic resolution produces useful cancellation, independent Fourier channels, or a better bound for `M(x)`.

## Exact counting argument

At a fixed depth `d`, define

\[
q_{\ell,j}=Q_\ell(u_j).
\tag{15}
\]

Because the prime factors of squarefree `n` are partitioned among the active blocks and every `w_ell(p)` is nonnegative,

\[
\sum_{j=1}^d q_{\ell,j}
\le
\left\lfloor
\frac{1}{\eta_\ell}
\sum_{p\mid n}w_\ell(p)
\right\rfloor
=L_\ell.
\tag{16}
\]

The number of nonnegative integer `d`-tuples with total at most `L_ell` is the stars-and-bars count

\[
\binom{L_\ell+d}{d}.
\tag{17}
\]

Ignoring compatibility between different coordinates only enlarges the state set, so the number of retained words at depth `d` is at most

\[
\prod_{\ell=1}^m\binom{L_\ell+d}{d}.
\tag{18}
\]

Summing over `1<=d<=r` and using monotonicity in `d` proves `(6)`. The standard estimate

\[
\binom{L+r}{r}
\le
\left(e\left(1+\frac{L}{r}\right)\right)^r
\tag{19}
\]

then proves `(7)`.

For squarefree `n`, if `r=omega(n)` then `n` is at least the product of the first `r` primes. The crude inequalities `p_j>=j+1` already give `(r+1)!<=n<=X`; Stirling therefore yields `(8)` without any prime-number theorem.

The function

\[
t\mapsto t\left[1+\log\left(1+\frac{L}{t}\right)\right]
\tag{20}
\]

is increasing for positive `t`. We may therefore replace `r` by the upper scale

\[
R_X=(1+o(1))\frac{\log X}{\log\log X}
\tag{21}
\]

in `(7)` for a uniform upper bound. Under `(9)`, each logarithm in `(7)` is `o(log log X)`, so the whole right side is `o(log X)`, proving `(10)`.

For `(11)`, one has `L<=log X/eta`. Condition `(12)` gives

\[
\frac{L}{R_X}
\ll
\frac{\log\log X}{\eta}
=(\log X)^{o(1)},
\tag{22}
\]

which proves `(13)`.

Finally suppose `N_\eta(n)>=X^delta`. Combining this with `(6)`, `(19)`, and `(21)` gives

\[
\delta\log X
\le
(1+o(1))\frac{\log X}{\log\log X}
\left[
1+\log\left(1+\frac{(1+o(1))\log\log X}{\eta}\right)
\right].
\tag{23}
\]

Hence

\[
\log\left(1+\frac{\log\log X}{\eta}\right)
\ge
(\delta-o(1))\log\log X,
\tag{24}
\]

which is equivalent to `(14)` after absorbing the `log log X` factor into `(log X)^{o(1)}`.

## Relation to the current frontier

`MC-425` showed that remembering only one Möbius-sign bit per factor cannot turn growing factor depth into polynomial source complexity. `MC-426` generalized that obstruction to every fixed-dimensional additive statistic whose prime-local increments are uniformly bounded.

Exact factor magnitude is the first obvious escape because `log u=sum_(p|u) log p` is additive but has unbounded prime increments. The present result separates **unbounded weight** from **usable retained precision**. Coarsely quantized logarithmic size is still compressed by conservation of total logarithmic mass: the factor blocks merely redistribute a total budget `log n<=log X` among at most `omega(n)` positions.

The surviving size-based route is therefore narrower. It must retain factor magnitude at inverse-polylogarithmic or finer logarithmic resolution, or use exact factor identities, and must then demonstrate that this growing precision survives coefficient manipulations and positive/quadratic closure as cancellation-relevant information rather than as a high-cardinality label space.

There is also a shell version. If product values range over a short shell containing at most `Delta+O(1)` integers and the retained state includes the product value, then under `(12)` the total quantized-log factor state count is at most

\[
(\Delta+O(1))X^{o(1)}.
\tag{25}
\]

Thus coarse logarithmic size does not amplify the shell exponent already bounded in `MC-424`.

## Prior art and novelty boundary

The ingredients are classical. Ordered factorization counting is a long-standing `factorisatio numerorum` problem; Don Coppersmith and Moshe Lewenstein, *Constructive Bounds on Ordered Factorizations*, SIAM Journal on Discrete Mathematics **19** (2005), 301–303, DOI `10.1137/S0895480104445861`, explicitly studies the number of ordered products with factors greater than one. `MC-426` already records the still earlier squarefree-factorization combinatorics of R. D. James. Stars-and-bars, the binomial estimate `(19)`, and the factorial bound on `omega(n)` are elementary.

A targeted literature search on ordered/multiplicative factorizations, additive arithmetic summaries, and logarithmic factor-size encodings found extensive prior art on counting raw factorizations and multiplicative partitions, but no reason to treat `(6)` as a new standalone number-theoretic theorem. No novelty is claimed for the counting ingredients or quantization argument.

The durable contribution here is only the **mechanism-specific frontier consequence**: the `MC-426` escape through unbounded log-size data still has subpolynomial retained state volume at every sub-power-of-`log X` precision, and a claimed polynomial factor-size channel must explicitly pay the growing precision threshold `(14)`.

## Limits and decisive test

- **Nonnegativity is load-bearing.** Signed additive weights can cancel in the total and require a bound on positive/negative variation rather than only the final sum.
- **Fixed retained dimension is load-bearing.** A dimension growing with `X` can evade `(10)` and must be priced jointly with precision.
- **Quantization is part of the claim.** Exact real values `log u` determine `u` exactly, so exact logarithmic size is effectively an exact factor identity and lies outside the coarse-state conclusion.
- **Polynomial capacity is not analytic usefulness.** Passing `(14)` only avoids this counting obstruction; it does not provide a character-sum estimate, a Möbius correlation theorem, or a positive-kernel gain.
- **The squarefree hypothesis matches nonzero Möbius support.** For nonsquarefree inputs the depth bound must use total prime multiplicity or another explicit factor-complexity parameter.
- **Shell multiplication in `(25)` is only an upper bound.** Different products can collide after quantization; such collisions make the retained family smaller.
- **No zero information is imported.** The argument is finite combinatorics and the elementary size identity `sum_(p|n) log p=log n` on squarefree `n`.

A proposed factor-size escape now has a direct admission test: state the actual logarithmic mesh (or equivalent number of retained bits), compute its state capacity using `(6)`, and only then ask whether those states survive the analytic architecture. Fixed or slowly growing precision cannot be credited as polynomial source bandwidth.