# MC-090 — GCD-sieve retention preserves the unsifted Huxley--Watt top mode

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-088` and `MC-089` show that deleting annular pairs with a shared moving prime can make a support-supercritical **omitted** block recursively cheap. The complementary retained carrier does not inherit that scale reduction from the same divisor sieve.

Let

\[
z(x)=\lfloor x\rfloor+\frac12-x,
\qquad
M(N)=\sum_{n\le N}\mu(n),
\qquad
H(N)=\sum_{n\le N}\frac{\mu(n)}n,
\]

and define the complete Huxley--Watt sawtooth form

\[
Q_1(N)
:=
\sum_{m,n\le N}
\mu(m)\mu(n)
 z\!\left(\frac{N^2}{mn}\right).
\tag{1}
\]

For a prime `p<=N`, put `X=N/p` and

\[
\nu_p(a):=\mu(a)\mathbf 1_{p\nmid a},
\qquad
Q_p(X)
:=
\sum_{a,b\le X}
\nu_p(a)\nu_p(b)
 z\!\left(\frac{X^2}{ab}\right),
\tag{2}
\]

with real cutoffs interpreted by `a,b<=floor(X)` as in `MC-089`.

Consider the complete retained form obtained by deleting pairs for which both coordinates are divisible by `p`:

\[
R_{N,p}
:=
\sum_{\substack{m,n\le N\\\neg(p\mid m\ \&\ p\mid n)}}
\mu(m)\mu(n)
 z\!\left(\frac{N^2}{mn}\right).
\tag{3}
\]

Then exactly

\[
\boxed{
R_{N,p}=Q_1(N)-Q_p(N/p).
}
\tag{4}
\]

Thus the prime deletion contributes a lower-scale correction, but the unsifted top-scale Huxley--Watt block `Q_1(N)` survives with coefficient exactly `1`. The same Euler-factor deletion that made the omitted block cheap cannot, by termwise recursive reduction, make the retained block cheap.

This is not peculiar to one prime. Let `w(g)` be any arithmetic mask applied only through `gcd(m,n)`, and write its divisor-basis coefficients

\[
a(d):=\sum_{e\mid d}\mu(d/e)w(e),
\qquad
w(g)=\sum_{d\mid g}a(d).
\tag{5}
\]

Define

\[
R_{N,w}
:=
\sum_{m,n\le N}
\mu(m)\mu(n)w(\gcd(m,n))
 z\!\left(\frac{N^2}{mn}\right).
\tag{6}
\]

For square-free `d` put

\[
\nu_d(a):=\mu(a)\mathbf 1_{(a,d)=1},
\qquad
Q_d(N/d)
:=
\sum_{a,b\le N/d}
\nu_d(a)\nu_d(b)
 z\!\left(\frac{(N/d)^2}{ab}\right).
\tag{7}
\]

Then finite divisor inversion gives the exact decomposition

\[
\boxed{
R_{N,w}
=
w(1)Q_1(N)
+
\sum_{\substack{2\le d\le N\\ d\ \mathrm{squarefree}}}
 a(d)Q_d(N/d).
}
\tag{8}
\]

In particular, **every gcd-sieve retention mask with `w(1) != 0` carries the unsifted top block with coefficient `w(1)`**. Any algebraic linear combination of such masks that cancels this coefficient also cancels the corresponding unsifted scale-doubling target coefficient. Therefore a divisor-sieve escape cannot both remove the top mode algebraically and retain the target merely by recombining independently bounded lower-scale blocks.

For the one-prime annular carrier of `MC-089`, this gives an especially sharp form. Let

\[
\mathcal A_N=\{(m,n):m,n\le N,\ mn>N\},
\]

let `E_{N,p}` be the common-`p` omitted annular block, and let

\[
P_N(E_{N,p})
=
N^2H(N)^2-\frac12M(N)^2
+
\sum_{\substack{(m,n)\in\mathcal A_N\\(m,n)\notin E_{N,p}}}
\mu(m)\mu(n)z\!\left(\frac{N^2}{mn}\right)
\tag{9}
\]

be the retained source-coupled statistic. If

\[
L_{N,p}^{\rm ret}
:=
\sum_{\substack{m,n\le N\\mn\le N\\\neg(p\mid m\ \&\ p\mid n)}}
\mu(m)\mu(n)z\!\left(\frac{N^2}{mn}\right),
\tag{10}
\]

then `|L_{N,p}^{ret}|=O(N log N)` and the square Huxley--Watt identity gives

\[
\boxed{
P_N(E_{N,p})
=
2M(N)-M(N^2)
-Q_p(N/p)
-L_{N,p}^{\rm ret}.
}
\tag{11}
\]

Under a prior exponent

\[
M(x)=O(x^\beta),
\qquad
\frac12<\beta<1,
\tag{12}
\]

`MC-089` proves uniformly in `p`

\[
Q_p(N/p)=O_\beta((1+N/p)^{2\beta}).
\tag{13}
\]

Hence for a moving prime `p=N^{\delta+o(1)}`, `0<delta<1/2`,

\[
\boxed{
P_N(E_{N,p})
=
-M(N^2)
+O_\beta\!\left(
N^\beta+N\log N+N^{2\beta(1-\delta)}
\right).
}
\tag{14}
\]

The common-prime projection has therefore moved the omitted arithmetic into a lower-scale term while leaving the desired doubled Mertens value as the unique top-power component of the retained carrier.

Consequently, if `1/2<alpha<beta` and

\[
\delta>1-\frac\alpha\beta,
\tag{15}
\]

then, under the prior bound (12),

\[
\boxed{
P_N(E_{N,p})=O(N^{2\alpha})
\quad\Longleftrightarrow\quad
M(N^2)=O(N^{2\alpha})
}
\tag{16}
\]

along that moving-prime family. Equation (16) does not invalidate the contraction ledger of `MC-089`; it identifies exactly where its new arithmetic theorem must live. A sub-old-exponent estimate for the retained statistic is already an improved Mertens estimate up to terms known to be lower order under the old exponent. It cannot be supplied by recursively bounding the p-sifted correction separately.

## 1. Exact one-prime decomposition

The omitted **complete-square** common-`p` block is

\[
\sum_{\substack{m,n\le N\\p\mid m,\ p\mid n}}
\mu(m)\mu(n)
 z\!\left(\frac{N^2}{mn}\right).
\tag{17}
\]

Only square-free multiples of `p` contribute. Writing `m=pa`, `n=pb`, both factors `mu(p)=-1` cancel and `(a,p)=(b,p)=1` is forced. Therefore (17) is exactly

\[
Q_p(N/p).
\tag{18}
\]

Subtracting it from the full square form proves (4). No Huxley--Watt evaluation, floor-alignment argument, asymptotic estimate, or analytic continuation is needed for this identity.

There is a second useful way to see the same cancellation. Since

\[
\mu(n)\mathbf 1_{p\mid n}=\mu(n)-\nu_p(n),
\]

the retained tensor weight is

\[
\mu\otimes\mu
-(\mu-\nu_p)\otimes(\mu-\nu_p)
=
\mu\otimes\nu_p
+\nu_p\otimes\mu
-\nu_p\otimes\nu_p.
\tag{19}
\]

Expanding `nu_p` by the Euler-deletion stack from `MC-088` makes all mixed top/lower layers cancel. The `(0,0)` unsifted layer remains once, while only layers with positive p-adic depth remain with negative sign. Equation (4) is the compressed exact statement of that cancellation.

## 2. General gcd-mask decomposition

Equation (5) is ordinary Möbius inversion on the divisor lattice. Substitute it into (6) and interchange the finite sums:

\[
R_{N,w}
=
\sum_{d\le N}a(d)
\sum_{\substack{m,n\le N\\d\mid m,\ d\mid n}}
\mu(m)\mu(n)
 z\!\left(\frac{N^2}{mn}\right).
\tag{20}
\]

If `d` is not square-free, the inner sum vanishes because every contributing `m,n` would have square factor. For square-free `d`, write `m=da`, `n=db`. Nonzero Möbius weight forces `(a,d)=(b,d)=1`, and

\[
\mu(da)\mu(db)
=
\mu(d)^2\mu(a)\mu(b)
=
\mu(a)\mu(b).
\tag{21}
\]

The inner sum is therefore exactly `Q_d(N/d)`, proving (8).

At `d=1`, equation (5) gives `a(1)=w(1)`. This proves the top-mode statement with no assumption on the remaining divisor coefficients. For the common-prime retention mask

\[
w_p(g)=1-\mathbf 1_{p\mid g},
\]
one has only `a(1)=1` and `a(p)=-1`, recovering (4).

For a finite set of primes `S`, the mask retaining pairs with no common prime from `S` is

\[
w_S(g)=\mathbf 1_{(g,\prod_{p\in S}p)=1}
=
\sum_{\substack{d\mid g\\d\mid\prod_{p\in S}p}}\mu(d),
\tag{22}
\]

so

\[
R_{N,w_S}
=
\sum_{d\mid\prod_{p\in S}p}\mu(d)Q_d(N/d).
\tag{23}
\]

Again the `d=1` unsifted block occurs with coefficient `1`. Adding more common-prime exclusions changes the lower divisor layers but does not remove the top layer termwise.

## 3. Passage back to the annulus

The complete retained square decomposes into its low-product and annular pieces:

\[
R_{N,p}
=
L_{N,p}^{\rm ret}
+
W_N^{\rm ret}(E_{N,p}).
\tag{24}
\]

The number of ordered pairs with `mn<=N` is `O(N log N)`, and `|z|<=1/2`, so

\[
L_{N,p}^{\rm ret}=O(N\log N)
\tag{25}
\]

uniformly in `p`.

The square Huxley--Watt identity recorded through `MC-S24` is

\[
Q_1(N)
=
2M(N)-M(N^2)
-N^2H(N)^2
+\frac12M(N)^2.
\tag{26}
\]

Adding the source coarse term `N^2H(N)^2-M(N)^2/2` to (4) and subtracting the low-product retained piece gives (11).

This is equivalent to the earlier `MC-087` identity

\[
P_N(E_{N,p})
=
2M(N)-M(N^2)-I_N-T_{N,p},
\]
because the full low-product piece splits into retained and common-`p` parts, while `MC-089` has `T_{N,p}=Q_p(N/p)-J_p(N/p)`. The `J_p` terms cancel across the two descriptions. The new form is useful because it exposes the top/lower scale separation directly.

## 4. Conditional equivalence at the proposed improved exponent

Assume (12) and take `p=N^{delta+o(1)}`. Equation (13), the low-product bound (25), and `M(N)=O(N^beta)` give (14).

Now fix `1/2<alpha<beta` and impose (15). Then

\[
2\beta(1-\delta)<2\alpha,
\]

while `beta<1<2alpha`, so both `N^beta` and `N log N` are also `O(N^{2alpha})`. Equation (14) becomes

\[
P_N(E_{N,p})=-M(N^2)+O(N^{2\alpha}),
\tag{27}
\]

which proves the two directions in (16).

Thus the moving-prime complement is genuinely recursively cheaper, but the retained carrier is not a separately easier p-sifted object at the requested improved exponent. Any proof of its sub-old-exponent bound must create cancellation involving the surviving top mode itself.

## 5. Prior art and novelty boundary

The Huxley--Watt square identity and its sawtooth matrix decomposition are prior art from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function* (2018), recorded as `MC-S24`. Ordinary divisor Möbius inversion and common-divisor sieve decompositions are classical.

A targeted literature search around the Huxley--Watt identity, p-sifted/common-prime Möbius bilinear forms, and gcd-sieve variants recovered the source paper and standard sieve/inclusion-exclusion language, but no basis for claiming a separate new theorem under the formulation above. **No novelty claim is made.**

The durable line-specific content is the obstruction obtained by applying those classical mechanisms to the exact `MC-089` survivor: divisor-only retention leaves the unsifted source carrier with nonzero coefficient. The complement reduction and the retained-estimate problem are therefore structurally asymmetric.

## 6. Boundary and decisive continuation

This result does **not** prove that the retained statistic cannot be estimated. It rules out only the natural idea that the same divisor/Euler-factor scale reduction which controls the omitted common-prime block will also control the retained carrier after termwise decomposition.

Several possibilities remain outside the obstruction:

- a genuinely joint estimate in which `Q_1(N)` cancels against lower divisor layers before absolute values or separate bounds are taken;
- a mask depending on more than `gcd(m,n)` or on non-divisor source geometry;
- a bilinear/frequency estimate acting directly on the retained annulus rather than recursively evaluating each divisor block;
- a recurrence whose target is not obtained from a linear combination with the same unsifted coefficient;
- an arithmetic theorem that controls the top/lower coupled difference without independently controlling `Q_1(N)`.

For gcd-sieve constructions, however, the first test is now exact: compute the divisor-basis coefficient of `d=1`. If it is nonzero, the unsifted Huxley--Watt top mode survives. If a linear combination is chosen to make that coefficient zero, verify that the scale-doubling target has not been canceled at the same time.

## Consequence for the research line

`MC-088`--`MC-089` solved a real half of the accepted annular clue: a support-supercritical common-prime complement can be made recursively cheap on arbitrary scales. `MC-090` shows that the mirror-image strategy does not solve the other half. The retained common-prime sieve is the full top-scale source carrier minus a lower-scale correction.

The live question is therefore narrower: **find a coupled arithmetic estimate that acts on the surviving unsifted top mode together with the lower divisor layers, rather than attempting to bound the retained object by the same termwise p-adic recursion used for the complement.**