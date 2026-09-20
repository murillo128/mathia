# FD-240 — Every subfull point-sampling density retains a macroscopic signed nullspace

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response kernel / arbitrary subfull point density / exact prescribed zeros / signed linear capacity / density-one endpoint
- **Depends on:** FD-225, FD-238, FD-239
- **Classification:** `EXACT-DERIVED + COUNTERMODEL + ALL-SUBFULL-DENSITY-SAMPLING-NULLSPACE + SIGNED-LINEAR-CAPACITY + DENSITY-ONE-ENDPOINT`

## Claim

FD-239 proved a macroscopic signed nullspace for prescribed point samples whose octave density is below the construction threshold

\[
\eta_0=\frac9{\pi^2}-\frac34=0.161890652\ldots .
\]

That threshold is not structural. A pairwise cell construction removes it completely below full density.

Let `S subset N` be any prescribed sampling set. On the dyadic band

\[
B_k=(2^{k-1},2^k]\cap\mathbb N
\]

write

\[
s_k=|S\cap B_k|,
\qquad
\eta=\limsup_{k\to\infty}\frac{s_k}{|B_k|}.
\]

Assume only

\[
\boxed{\eta<1.}
\tag{1}
\]

For the divisor-response operator

\[
(\mathscr A b)(m)
=
\sum_{d\le m}b_d
M\!\left(\left\lfloor\frac md\right\rfloor\right),
\tag{2}
\]

there exists an integer signed sequence `(b_n)` such that

\[
\boxed{|b_n|\le n\qquad(n\ge1),}
\tag{3}
\]

and

\[
\boxed{
(\mathscr A b)(m)=0
\quad
\text{for every }m\in S
\text{ and every }m=2^j.
}
\tag{4}
\]

The response is also controlled between samples:

\[
\boxed{(\mathscr A b)(m)=O(m)\qquad(m\ge1).}
\tag{5}
\]

Despite these exact zeros, `b` retains macroscopic linear-capacity mass. Define

\[
C_\varphi
:=
\sum_{d\ge1}\frac{\mu(d)^2}{d\varphi(d)}
=
\prod_p\left(1+\frac1{p(p-1)}\right)
<\infty .
\tag{6}
\]

Then

\[
\boxed{
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}|b_n|}
     {\sum_{n\in B_k}n}
\ge
\frac{(1-\eta)^2}{6C_\varphi}>0.
}
\tag{7}
\]

Moreover both signs are macroscopic:

\[
\boxed{
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}b_n^+}{\sum_{n\in B_k}n}
\ge
\frac{(1-\eta)^2}{12C_\varphi},
\qquad
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}b_n^-}{\sum_{n\in B_k}n}
\ge
\frac{(1-\eta)^2}{12C_\varphi}.
}
\tag{8}
\]

Thus **no arbitrary point-sampling pattern whose octave density stays bounded away from one can make the divisor response signed-coercive**. The remaining universal density endpoint is full density. This does not classify every proper sampling set of density one; it says that any density threshold strictly below one is impossible.

## Exact response representation

Use the exact inversion from FD-225. Write

\[
b=\mathbf 1*g,
\qquad
b_n=\sum_{d\mid n}g(d).
\tag{9}
\]

Since `mu * 1 = epsilon`,

\[
\mu*b=g.
\]

The first-difference identity for the divisor response is

\[
(\mathscr A b)(m)-(\mathscr A b)(m-1)
=(\mu*b)(m)=g(m).
\]

With response zero at `m=0`, therefore

\[
\boxed{
(\mathscr A b)(m)=Y(m):=\sum_{n\le m}g(n).
}
\tag{10}
\]

So it is enough to construct `g` whose partial sums vanish at all prescribed samples while keeping the divisor sum `b=1*g` large.

## Pairwise zeroing inside every sample cell

Fix one dyadic band and write `N=2^k`, so

\[
B_k=(N/2,N]\cap\mathbb N,
\qquad |B_k|=N/2.
\]

List the points of `S cap B_k` in increasing order and append the right endpoint `N` if it is not already present. Together with the left endpoint `N/2`, these points divide `B_k` into consecutive integer cells. Let `c_k` be the number of nonempty cells. Then

\[
c_k\le s_k+1.
\tag{11}
\]

Inside each cell, pair consecutive integers. If the cell has odd size, leave one integer unpaired. Let `r_k` be the total number of pairs. Since each cell loses at most one integer,

\[
2r_k
\ge
|B_k|-c_k
\ge
|B_k|-s_k-1.
\tag{12}
\]

Hence, from (1),

\[
\boxed{
r_k\ge \frac{1-\eta-o(1)}4N.}
\tag{13}
\]

For a pair `(a,a+1)` put

\[
t_a=\min\{\varphi(a),\varphi(a+1)\}
\]

and choose a sign `sigma_a in {+1,-1}`. Set

\[
g(a)=\sigma_a t_a,
\qquad
g(a+1)=-\sigma_a t_a.
\tag{14}
\]

Set `g(n)=0` at every unpaired point. Each pair contributes exactly zero total mass, so every cell contributes zero. Inducting from the previous dyadic endpoint gives

\[
Y(m)=0
\]

at every sample point and at every dyadic endpoint. Between boundaries the only possible nonzero partial sum is the first entry of a pair, so

\[
|Y(m)|\le t_a\le \varphi(m)\le m.
\tag{15}
\]

Equations (10), (14), and (15) prove the exact zeros (4) and the all-integer response bound (5), independently of how the signs `sigma_a` are oriented.

The coefficient envelope is also automatic. Since `|g(d)|<=phi(d)`, the elementary identity

\[
\sum_{d\mid n}\varphi(d)=n
\]

gives

\[
|b_n|
\le
\sum_{d\mid n}|g(d)|
\le
\sum_{d\mid n}\varphi(d)
=n,
\]

which proves (3).

## Orienting the pairs to preserve capacity

The signs in (14) can now be chosen to make `b` large without disturbing any response zero.

For `n in B_k`, every proper divisor of `n` is at most `n/2<=N/2`. Therefore the only divisor of `n` lying in the current band is `n` itself. When processing `B_k`, write

\[
b_a=H_a+\sigma_a t_a,
\qquad
b_{a+1}=H_{a+1}-\sigma_a t_a,
\tag{16}
\]

where the two `H` terms depend only on already fixed earlier bands. No sign chosen for one current-band pair affects another coefficient in the same band.

Average the contribution of one pair over its two possible orientations. The identity

\[
\frac{|H+t|+|H-t|}{2}=\max\{|H|,t\}
\]

gives

\[
\frac12\sum_{\sigma=\pm1}
\left(
|H_a+\sigma t_a|
+
|H_{a+1}-\sigma t_a|
\right)
\ge 2t_a.
\tag{17}
\]

Hence one of the two orientations contributes at least `2t_a` to the current-band total variation. Choose that orientation independently for every pair. Then

\[
\boxed{
\sum_{n\in B_k}|b_n|
\ge
2\sum_{\text{pairs }a}t_a.
}
\tag{18}
\]

It remains to show that the paired totients carry quadratic mass even when the unpaired set is adversarial.

The divisor identity

\[
\frac n{\varphi(n)}
=
\sum_{d\mid n}\frac{\mu(d)^2}{\varphi(d)}
\tag{19}
\]

implies

\[
\sum_{n\le x}\frac n{\varphi(n)}
=
\sum_{d\le x}\frac{\mu(d)^2}{\varphi(d)}
\left\lfloor\frac xd\right\rfloor
\le
xC_\varphi.
\tag{20}
\]

The Euler product in (6) converges because its nontrivial factors differ from one by `1/[p(p-1)]`, and the corresponding sum converges by comparison with `sum_{n>=2}1/[n(n-1)]`.

For `n in B_k`, `n>N/2`, so (20) yields

\[
\sum_{n\in B_k}\frac1{\varphi(n)}
\le
\frac2N
\sum_{n\le N}\frac n{\varphi(n)}
\le 2C_\varphi.
\tag{21}
\]

For each pair,

\[
\frac1{t_a}
=
\max\left\{\frac1{\varphi(a)},\frac1{\varphi(a+1)}\right\}
\le
\frac1{\varphi(a)}+\frac1{\varphi(a+1)}.
\]

The pairs are disjoint, hence

\[
\sum_{\text{pairs }a}\frac1{t_a}
\le2C_\varphi.
\tag{22}
\]

Cauchy-Schwarz now gives

\[
\sum_{\text{pairs }a}t_a
\ge
\frac{r_k^2}{\sum 1/t_a}
\ge
\frac{r_k^2}{2C_\varphi}.
\tag{23}
\]

Combining (13), (18), and (23),

\[
\sum_{n\in B_k}|b_n|
\ge
\frac{(1-\eta-o(1))^2}{16C_\varphi}N^2.
\tag{24}
\]

Finally

\[
\sum_{n\in B_k}n
=\frac38N^2+O(N),
\]

so (24) proves (7).

## Both signs remain macroscopic

The construction also prevents the total variation from hiding almost entirely in one sign. From (10) and (15), `Y(m)=O(m)`. Since `b=1*g`,

\[
\sum_{n\le x}b_n
=
\sum_{d\le x}g(d)\left\lfloor\frac xd\right\rfloor.
\tag{25}
\]

Discrete summation by parts gives

\[
\sum_{n\le x}b_n
=
Y(x)
+
\sum_{d<x}Y(d)
\left(
\left\lfloor\frac xd\right\rfloor
-
\left\lfloor\frac x{d+1}\right\rfloor
\right).
\tag{26}
\]

Using `|Y(d)|<=d` and

\[
\sum_{d<x}d
\left(
\left\lfloor\frac xd\right\rfloor
-
\left\lfloor\frac x{d+1}\right\rfloor
\right)
=O(x\log x),
\]

we obtain

\[
\sum_{n\le x}b_n=O(x\log x).
\tag{27}
\]

Thus the signed sum over `B_k` is `O(N log N)=o(N^2)`, whereas (24) gives total variation `Omega(N^2)`. If `P_k=sum_{B_k}b_n^+` and `Q_k=sum_{B_k}b_n^-`, then

\[
P_k+Q_k=\sum_{B_k}|b_n|,
\qquad
P_k-Q_k=o(N^2).
\]

Each sign therefore carries asymptotically half of the lower-bound mass, proving (8).

## Consequence for switched sampling

Because every dyadic endpoint is included among the exact zeros, any switched stencil built from dyadic response values also vanishes identically on this sequence. In particular the orders used in the current switched scheduler satisfy

\[
((T-I)^r\mathscr A b)(2^j)=0
\qquad(r=1,4).
\]

More generally, adding any prescribed point samples of octave density strictly below one cannot remove the macroscopic signed kernel.

This sharpens the frontier left by FD-239. The previous constant `eta_0` came from paying for one pivot of potentially full totient size in every sample cell. Pairwise cancellation pays only one **unpaired location**, with zero coefficient, per cell. The unsampled fraction itself supplies a linear number of disjoint pairs, and the reciprocal-totient estimate forces those pairs to retain quadratic aggregate amplitude.

The density-one endpoint is qualitatively different. If every integer response coordinate is sampled, (10) makes the transform injective: `Y(m)=0` for every `m` implies `g(m)=0`, hence `b=0`. The present theorem does **not** show that every proper sampling set of density one is coercive; it only closes the possibility of a universal signed-coercivity threshold at any fixed density below one.

## Scope and falsification boundary

This remains a signed countermodel, not a physical nonnegative reservoir filling and not a source satisfying the full arithmetic coherence of Möbius. FD-230/232 already show why that distinction matters: positivity can destroy large signed blind directions even when response information alone cannot see them.

The result is therefore negative evidence specifically against **pointwise divisor-response sampling as the missing coercive ingredient**. To improve the Farey route one must now use at least one of:

- a near-full-density or structurally stronger response constraint whose omitted set shrinks relative to each octave;
- a genuinely non-pointwise observable carrying information not reducible to selected coordinates of `mathscr A b`;
- positivity or source-side arithmetic coherence that excludes the signed kernel.

A useful next test is the density-one-but-not-full regime: characterize which sparse omitted sets still permit macroscopic signed capacity. A positive result there would push point-sampling failure all the way to a quantitative codimension criterion; a negative result would identify the first genuine response-side rigidity threshold.

## Prior-art boundary

A targeted check for one-dimensional balancing with prescribed zeros, Dirichlet/Mobius convolution kernels, and totient-weighted discrepancy found only the generic balancing and convolution identities underlying the proof, not a theorem matching this divisor-response statement with arbitrary prescribed subfull-density zeros and macroscopic signed capacity. No external result is load-bearing here: the exact transform identity, pairwise construction, reciprocal-totient bound, and capacity estimate are all derived above. Accordingly no new source entry is required.

The claim of this finding is limited to the exact Farey/Mertens divisor-response model used in this research line; no general novelty claim is made for the elementary balancing devices themselves.
