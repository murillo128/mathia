# FD-231 — Signed linear-capacity profiles can be uniformly switched-invisible

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response kernel / signed capacity / exact divisor inversion / totient balancing / switched invisibility / positivity boundary
- **Depends on:** FD-230, FD-225, FD-227
- **Classification:** `EXACT-DERIVED + COUNTERMODEL + SIGNED-LINEAR-CAPACITY + TOTIENT-BALANCING + ALL-INTEGER-LOW-RESPONSE + POSITIVITY-BOUNDARY`

## Claim

FD-230 proves that nonnegative divisor-cell occupancies with the natural linear envelope cannot retain a nonvanishing fraction of aggregate capacity on late dyadic bands while their switched response is subquadratic. The nonnegativity hypothesis is not a technical convenience. If the coefficients are allowed to have both signs, the conclusion fails very strongly.

Let

\[
(\mathscr A b)(m)
=
\sum_{d\le m} b_d M\!\left(\left\lfloor\frac md\right\rfloor\right)
\tag{1}
\]

be the exact divisor-response operator of FD-225. There exists an integer sequence `(b_n)` such that

\[
\boxed{|b_n|\le n\qquad(n\ge1),}
\tag{2}
\]

and yet

\[
\boxed{|(\mathscr A b)(m)|\le m\qquad(m\ge1).}
\tag{3}
\]

Consequently, for every fixed `r>=1`,

\[
\boxed{
|(T-I)^r\mathscr A b(m)|\le 3^r m,
}
\tag{4}
\]

where `(TF)(m)=F(2m)`. In particular, for the switched row orders

\[
r_j=q_j+1=(1,4,4,1,4,4,\ldots),
\]

we have at every dyadic sample

\[
\boxed{
|(T-I)^{r_j}\mathscr A b(2^j)|
\le81\,2^j
=o(4^j).
}
\tag{5}
\]

Despite this uniformly first-order response, the signed coefficients retain a fixed positive fraction of the full linear capacity in total variation. If

\[
B_k=[2^k,2^{k+1})\cap\mathbb N,
\]

then

\[
\boxed{
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}|b_n|}
     {\sum_{n\in B_k}n}
\ge
\frac{12}{\pi^2}-1
\approx0.21585.
}
\tag{6}
\]

In fact the positive and negative parts both carry a positive capacity fraction:

\[
\boxed{
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k} b_n^+}
     {\sum_{n\in B_k}n}
\ge
\frac12\left(\frac{12}{\pi^2}-1\right),
}
\tag{7}
\]

and the same bound holds with `b_n^-` in place of `b_n^+`.

Thus no signed analogue of FD-230 can be true if it measures capacity by `sum |b_d|`, by separate positive/negative mass, or merely by the pointwise envelope `|b_d|<=Cd`. The positivity in FD-230 is exactly what converts the immediately preceding dyadic band into a coercive mass term. Once cellwise signs are available, one can preserve order-one total-variation capacity while making the **entire all-integer divisor response** only linear.

This is a statement about signed divisor-cell degrees of freedom, not a new single-source Farey countermodel. A physical prime-flip occupancy is nonnegative. The construction below is realizable as a difference of two feasible nonnegative cell profiles after a common scaling, but a single nonnegative profile remains subject to FD-230. The research consequence is therefore precise: any future intrinsic capacity obstruction must exploit one-sided positive slack or another source-side sign restriction. A norm coercivity argument on signed corrections cannot work.

## 1. Greedy totient signs give an all-integer response of size `O(m)`

Let `phi` denote Euler's totient. Choose signs

\[
\varepsilon_n\in\{-1,+1\}
\]

recursively. Put

\[
Y(0)=0,
\qquad
Y(n)=\sum_{d\le n}\varepsilon_d\varphi(d),
\tag{8}
\]

and at stage `n` choose `epsilon_n` so that `epsilon_n phi(n)` has the sign opposite to `Y(n-1)`; if `Y(n-1)=0`, choose either sign. Then

\[
|Y(n)|
=
\bigl||Y(n-1)|-\varphi(n)\bigr|
\le
\max\{|Y(n-1)|,\varphi(n)\}.
\tag{9}
\]

Since `phi(n)<=n` and the initial value is bounded, induction gives the completely elementary discrepancy bound

\[
\boxed{|Y(n)|\le n.}
\tag{10}
\]

Now define

\[
\boxed{
b_n
=
\sum_{d\mid n}\varepsilon_d\varphi(d).
}
\tag{11}
\]

The classical identity

\[
\sum_{d\mid n}\varphi(d)=n
\tag{12}
\]

immediately yields the cellwise capacity bound (2).

The point of the choice (11) is that it is exactly the FD-225 inverse. Write

\[
g(n)=\varepsilon_n\varphi(n).
\]

Then `b=1*g` in Dirichlet-convolution notation. Expanding the Mertens kernel in (1),

\[
\begin{aligned}
(\mathscr A b)(m)
&=
\sum_{d\le m}b_d
\sum_{a\le m/d}\mu(a)\\
&=
\sum_{n\le m}(\mu*b)(n)\\
&=
\sum_{n\le m}(\mu*1*g)(n)\\
&=
\sum_{n\le m}g(n)\\
&=Y(m),
\end{aligned}
\tag{13}
\]

because `mu*1` is the convolution identity. Equation (10) therefore proves (3) for **every integer sample**, not merely on the dyadic grid.

Applying one fixed dilation difference gives

\[
\begin{aligned}
|(T-I)^rY(m)|
&\le
\sum_{j=0}^{r}\binom rj|Y(2^jm)|\\
&\le
m\sum_{j=0}^{r}\binom rj2^j\\
&=3^r m,
\end{aligned}
\tag{14}
\]

which proves (4)--(5). Hence the signed profile is much more invisible than required by the FD-230 hypothesis: its response is first-order at all integer scales while its natural capacity is quadratic in aggregate.

## 2. The profile still carries a fixed total-variation fraction of linear capacity

The current coefficient `epsilon_n phi(n)` is the largest-divisor term in (11). All proper divisors together have absolute mass at most

\[
\sum_{\substack{d\mid n\\d<n}}\varphi(d)
=n-\varphi(n)
\tag{15}
\]

by (12). Therefore, independently of how the greedy signs were chosen,

\[
\boxed{
|b_n|
\ge
2\varphi(n)-n.
}
\tag{16}
\]

The right side may be negative for individual `n`, which causes no problem when summing because the left side is nonnegative. For `x->infinity`, the elementary totient summatory asymptotic used already in FD-227 is

\[
\sum_{n\le x}\varphi(n)
=
\frac{3}{\pi^2}x^2+O(x\log x).
\tag{17}
\]

For completeness, (17) follows directly from

\[
\varphi(n)
=n\sum_{d\mid n}\frac{\mu(d)}d
\]

by reversing the sums; the main coefficient is `1/(2 zeta(2))=3/pi^2` and the elementary floor error contributes `O(x log x)`. No external cancellation estimate is involved.

Summing (16) over `x<=n<2x` gives

\[
\begin{aligned}
\sum_{x\le n<2x}|b_n|
&\ge
2\sum_{x\le n<2x}\varphi(n)
-
\sum_{x\le n<2x}n\\
&=
\left(
\frac{18}{\pi^2}-\frac32+o(1)
\right)x^2.
\end{aligned}
\tag{18}
\]

Meanwhile

\[
\sum_{x\le n<2x}n
=
\left(\frac32+o(1)\right)x^2.
\tag{19}
\]

Dividing (18) by (19) and taking `x=2^k` proves (6). The numerical constant is strictly positive because `12/pi^2>1`.

This lower bound is deliberately robust. It uses no probabilistic signs, no density theorem for special integers and no cancellation property of the chosen `epsilon_n`. The same signs that make the response small automatically retain a positive fraction of total-variation capacity because the self-divisor totient term cannot be swallowed, on average, by all proper-divisor totients.

## 3. Both signs occur at capacity scale

The total-variation statement could in principle hide a nearly one-sided profile. Here it does not. Let

\[
B(x)=\sum_{n\le x}b_n.
\tag{20}
\]

From `b=1*g`,

\[
B(x)
=
\sum_{d\le x}g(d)
\left\lfloor\frac xd\right\rfloor.
\tag{21}
\]

Partial summation with `Y(t)=sum_(d<=t)g(d)` gives

\[
B(x)
=
Y(x)
+
\sum_{d<x}Y(d)
\left(
\left\lfloor\frac xd\right\rfloor
-
\left\lfloor\frac{x}{d+1}\right\rfloor
\right).
\tag{22}
\]

Using `|Y(d)|<=d` and the monotonicity of the floor quotient,

\[
|B(x)|
\le
x+
\sum_{d<x}d
\left(
\left\lfloor\frac xd\right\rfloor
-
\left\lfloor\frac{x}{d+1}\right\rfloor
\right)
=
O(x\log x),
\tag{23}
\]

because the last weighted telescoping sum is bounded by `sum_(d<=x) floor(x/d)=O(x log x)`.

Hence on every dyadic band

\[
\sum_{x\le n<2x}b_n
=O(x\log x)
=o(x^2).
\tag{24}
\]

Write the positive and negative band masses as

\[
P(x)=\sum_{x\le n<2x}b_n^+,
\qquad
N(x)=\sum_{x\le n<2x}b_n^-.
\]

Then

\[
P(x)+N(x)=\sum_{x\le n<2x}|b_n|,
\qquad
P(x)-N(x)=O(x\log x).
\tag{25}
\]

Combining (18)--(19) with (25) proves (7) and its negative-part analogue. Thus the construction contains genuinely macroscopic positive and negative cell mass on every late dyadic band. The cancellation is not produced by a sparse exceptional set.

## 4. What this does and does not mean for the prime reservoirs

FD-226 gives scale-adapted prime cells whose available occupancy is asymptotically proportional to `d`. The coefficient law (2) therefore has exactly the right pointwise **signed** scale for those cells. After multiplying `(b_d)` by any sufficiently small fixed fraction of the common reservoir scale, `b_d^+` and `b_d^-` fit separately inside the corresponding positive cell capacities. Equations (6)--(7) say that neither side becomes aggregate-capacity sparse.

However, a physical prime-flip construction relative to the Möbius source records a **nonnegative number of flipped primes** in each cell. The signed vector `(b_d)` is therefore not itself such an occupancy. It can be interpreted source-side as the difference between two feasible reservoir fillings, but not as one filling without adding a positive offset. Adding an offset changes the divisor response, and FD-230 shows that a nonnegative offset retaining a fixed late-band capacity fraction cannot itself remain switched-subquadratic.

This representation distinction is essential. The result does **not** reverse FD-230, does not extend the earlier squarefree ternary source countermodels, and does not show that the physical Mertens correction can actually be absorbed beyond the current Vinogradov--Korobov depth. It instead closes a tempting proof route: one cannot hope to establish the missing capacity obstruction by proving a lower bound for `mathscr A` on signed linear-capacity vectors, even if the norm sees total variation separately on every dyadic band. Such vectors can have macroscopic norm and uniformly tiny response.

The remaining physical question is consequently one-sided. A successful obstruction must quantify the **positive slack** required to realize the signed Mertens correction inside one nonnegative occupancy profile, or exploit an equivalent source-side restriction. FD-230 supplies coercivity for the positive profile; the present finding shows why that coercivity disappears immediately after passing to signed corrections.

## 5. Prior-art boundary and verdict

The ingredients are classical and elementary: `sum_(d|n) phi(d)=n`, `mu*1=epsilon`, the average order of `phi`, and one-dimensional greedy sign balancing. The prior-art search found the expected divisor-transform and totient material but no external theorem is load-bearing: all identities and estimates needed above are derived directly. No novelty claim is made for greedy discrepancy balancing, Euler's totient identity, Dirichlet inversion or the totient summatory asymptotic.

The research-specific point is their combination with the exact FD-225 divisor-response map. It constructs an explicit signed linear-capacity direction with all-integer response `O(m)`, while preserving a fixed positive fraction of both positive and negative capacity mass on every asymptotic dyadic band.

**Verdict.** FD-230 is genuinely a positivity theorem, not a hidden norm-coercivity theorem. Signed divisor-cell corrections have large, explicit blind directions even under the strongest natural linear envelope and even when their positive and negative masses are each macroscopic. The next capacity argument must remain one-sided and source-realizable: the unresolved issue is how much nonnegative reservoir slack is forced by the particular signed correction needed to cancel the physical Mertens baseline.