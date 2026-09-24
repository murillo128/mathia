# NB-322 — Growing rational denominators carry logarithmic mixing resonance below quadratic scale

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-316, NB-320, NB-321
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + WEIGHTED-BILINEAR-MIXING + GROWING-RATIONAL-DENOMINATOR + SUBQUADRATIC-RESONANCE + ADJACENT-WITNESS + RANK-ONE-ERROR + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\qquad
T_{n,m}:=P_{U_n}A_m|_{U_n},
\]

let `R_n` be the far-external rank-one operator from `NB-314`, and use the scaled adjacent cancellation

\[
u_n:=g_n-\frac{n-1}{n}g_{n-1}.
\tag{1}
\]

Write

\[
P_n:=n(n-1),
\qquad
G_n(T):=\int_0^T\widetilde F_{u_n}(s)\,ds.
\tag{2}
\]

For an integer `q>=2` satisfying either `q|n` or `q|(n-1)`, put

\[
m_{n,q}:=\frac{P_n}{q},
\qquad
L_q:=\operatorname{lcm}(2,q),
\tag{3}
\]

and define the weighted mixing coefficient

\[
\mathcal E_{n,q}
:=
\left\langle
(\sqrt{m_{n,q}}T_{n,m_{n,q}}-R_n)g_2,u_n
\right\rangle.
\tag{4}
\]

Define the periodic quadratic residue profile

\[
\phi_q(k):=r(q-r),
\qquad
r\equiv k\pmod q,
\quad 0\le r<q,
\tag{5}
\]

and the absolutely convergent arithmetic coefficient

\[
\boxed{
C_q:=\sum_{k\ge1}\frac{(-1)^k\phi_q(k)}{k^2}.
}
\tag{6}
\]

Then `C_q` is strictly negative for every `q>=2`, and in fact

\[
\boxed{|C_q|\ge \frac q{10}.}
\tag{7}
\]

Moreover the rational-period folding of `NB-321` admits a remainder bound uniform in the denominator:

\[
\boxed{
\mathcal E_{n,q}
=
\begin{cases}
-\dfrac{C_q}{4q(n-1)}+\mathcal R_{n,q},&q\mid n,\\[3mm]
\dfrac{C_q(n-1)}{4qn^2}+\mathcal R_{n,q},&q\mid(n-1),
\end{cases}
}
\tag{8}
\]

with

\[
\boxed{
|\mathcal R_{n,q}|
\le
C_R\frac{q^2}{(n-1)^2},
\qquad
C_R:=\frac{2+\zeta(3)/4}{4}<0.576.
}
\tag{9}
\]

Consequently, for every sequence `q=q_n>=2` with `q_n|n` or `q_n|(n-1)` and

\[
q_n=o(\sqrt n),
\tag{10}
\]

one has

\[
\boxed{
\liminf_{n\to\infty} n|\mathcal E_{n,q_n}|\ge\frac1{40}.
}
\tag{11}
\]

Using the adjacent-witness norm estimate from `NB-304`,

\[
\|u_n\|_2^2
\le
\frac{2H_{n-2}+1+\pi^2/18}{n^2},
\tag{12}
\]

and `||g_2||_2^2=\log2/4`, equation (11) implies

\[
\boxed{
\liminf_{n\to\infty}
\sqrt{\log n}\,
\left\|\sqrt{m_{n,q_n}}T_{n,m_{n,q_n}}-R_n\right\|
\ge
\frac1{20\sqrt{2\log2}}.
}
\tag{13}
\]

Thus the logarithmic adjacent resonance of `NB-320`--`NB-321` is not merely a fixed-denominator quadratic skeleton. It survives for denominators tending to infinity as fast as `o(sqrt(n))`. Since

\[
m_{n,q}\asymp \frac{n^2}{q},
\tag{14}
\]

this produces explicit logarithmic obstructions throughout sparse arithmetic scales strictly below quadratic. In particular, for every fixed exponent

\[
\frac32<\alpha<2,
\tag{15}
\]

there are sequences with

\[
m_n=n^{\alpha+o(1)}
\tag{16}
\]

for which the normalized rank-one mixing error in (13) remains at least order `1/sqrt(log n)`.

This remains an absolute rank-one-error obstruction, not an order-one channel, not a lower bound for `beta_(n+1)(m)`, and not a target-occupation statement.

## 1. Rational primitive samples have a universal quadratic residue shape

`NB-321` reduces the boundary term at `m=P_n/q` to samples `G_n(jP_n/q)`. On the two congruence classes used here, those samples have a closed form for every denominator.

First suppose `q|n`, so `n=qa`. For `1<=j<=q-1`,

\[
\frac{jP_n}{q}
=ja(n-1)
=(ja-1)n+a(q-j).
\tag{17}
\]

In the block notation of `NB-316`, the remainder `a(q-j)` is exactly the jump location

\[
n-1-(ja-1)=a(q-j).
\]

Therefore equation (15) of `NB-316` gives

\[
\boxed{
G_n\!\left(\frac{jP_n}{q}\right)
=-\frac{n}{2q^2}j(q-j).
}
\tag{18}
\]

Now suppose `q|(n-1)`, so `n=qa+1`. Then

\[
\frac{jP_n}{q}=jan
\tag{19}
\]

is exactly the start of block `ja`. Equation (14) of `NB-316` gives

\[
\boxed{
G_n\!\left(\frac{jP_n}{q}\right)
=\frac{(n-1)^2}{2q^2n}j(q-j).
}
\tag{20}
\]

Because `G_n` has period `P_n`, equations (18)--(20) extend to all integer `j` after replacing `j` by its residue modulo `q`. Thus on either congruence class

\[
G_n(jm_{n,q})=s_{n,q}\phi_q(j),
\tag{21}
\]

where

\[
s_{n,q}
=
\begin{cases}
-\dfrac{n}{2q^2},&q\mid n,\\[2mm]
\dfrac{(n-1)^2}{2q^2n},&q\mid(n-1).
\end{cases}
\tag{22}
\]

The fixed-`q` calculations in `NB-320` and `NB-321` are therefore samples of one denominator-independent residue law.

## 2. The entire boundary sum is one alternating Dirichlet coefficient

Let

\[
K_L(t):=\sum_{\ell\ge0}(t+\ell L)^{-2}.
\tag{23}
\]

The exact first integration by parts from `NB-321` gives the boundary contribution

\[
\mathcal B_{n,q}
=
\frac1{2m_{n,q}}
\sum_{\substack{1\le r<L_q\\r\ {m odd}}}
\left[
G_n((r+1)m_{n,q})K_{L_q}(r+1)
-G_n(rm_{n,q})K_{L_q}(r)
\right].
\tag{24}
\]

Since `L_q` is even, every integer endpoint `j=1,...,L_q` appears once, with sign `(-1)^j`. Substituting (21),

\[
\mathcal B_{n,q}
=
\frac{s_{n,q}}{2m_{n,q}}
\sum_{j=1}^{L_q}
(-1)^j\phi_q(j)K_{L_q}(j).
\tag{25}
\]

Because `q|L_q` and `L_q` is even, unfolding the kernel preserves both the residue modulo `q` and the parity. Hence

\[
\sum_{j=1}^{L_q}
(-1)^j\phi_q(j)K_{L_q}(j)
=
\sum_{k\ge1}\frac{(-1)^k\phi_q(k)}{k^2}
=C_q.
\tag{26}
\]

Using `m_(n,q)=n(n-1)/q` in (25) gives exactly the two main terms in (8).

As checks, `C_2=-\pi^2/8` recovers the half-period coefficient of `NB-320`, while `C_4=-\pi^2/4` recovers the quarter-period coefficient of `NB-321`. The next denominator is already nonzero:

\[
C_3=-\frac{4\pi^2}{27},
\tag{27}
\]

so, for example, `3|n` gives

\[
\mathcal B_{n,3}=\frac{\pi^2}{81(n-1)}.
\tag{28}
\]

## 3. No denominator cancels: `C_q<0` uniformly

Put

\[
\Phi_q(z):=\sum_{r=1}^{q-1}r(q-r)z^r.
\tag{29}
\]

A finite geometric differentiation gives

\[
\Phi_q(z)
=
\frac{
(q-1)z-(q+1)z^2+(q+1)z^{q+1}-(q-1)z^{q+2}
}{(1-z)^3}.
\tag{30}
\]

For `0<x<1`, the generating function of the alternating periodic residue sequence is

\[
S_q(x)
:=
\sum_{k\ge1}(-1)^k\phi_q(k)x^k
=
\frac{\Phi_q(-x)}{1-(-x)^q}.
\tag{31}
\]

If `q` is even, every term in the numerator of `Phi_q(-x)` is negative:

\[
\Phi_q(-x)
=-\frac{
(q-1)x+(q+1)x^2+(q+1)x^{q+1}+(q-1)x^{q+2}
}{(1+x)^3}<0.
\tag{32}
\]

If `q` is odd,

\[
\Phi_q(-x)
=-\frac{
(q-1)x(1-x^{q+1})+(q+1)x^2(1-x^{q-1})
}{(1+x)^3}<0.
\tag{33}
\]

The denominator in (31) is positive in both cases, so `S_q(x)<0` throughout `(0,1)`. Since

\[
\frac1{k^2}
=
\int_0^1x^{k-1}(-\log x)\,dx,
\]

absolute convergence allows termwise integration and gives

\[
C_q
=
\int_0^1\frac{-\log x}{x}S_q(x)\,dx<0.
\tag{34}
\]

The same formula gives a denominator-uniform lower bound. On `0<x<=1/2`, if `q` is even,

\[
-S_q(x)
\ge
\frac{8}{27}(q-1)x,
\tag{35}
\]

while for odd `q>=3`,

\[
-S_q(x)
\ge
\frac{20}{81}(q-1)x.
\tag{36}
\]

Using

\[
\int_0^{1/2}(-\log x)\,dx
=\frac{1+\log2}{2}>\frac45
\tag{37}
\]

and the elementary bounds `q-1>=q/2` for even `q>=2` and `q-1>=2q/3` for odd `q>=3`, equations (34)--(37) imply the convenient common estimate

\[
|C_q|\ge\frac q{10},
\tag{38}
\]

which proves (7). No fixed rational denominator can make the first-order boundary functional vanish on these two congruence subsequences.

## 4. The folding remainder is uniform enough for growing denominators

The exact remainder after the first integration by parts is

\[
\mathcal R_{n,q}
=-\frac1{2m_{n,q}^2}
\sum_{\substack{1\le r<L_q\\r\ {m odd}}}
\int_{rm_{n,q}}^{(r+1)m_{n,q}}
G_n(s)K_{L_q}'(s/m_{n,q})\,ds.
\tag{39}
\]

For each selected interval define

\[
H_{n,q,r}(s)
:=
\int_{rm_{n,q}}^sG_n(y)\,dy.
\tag{40}
\]

The second-primitive estimate established in `NB-321` is denominator-free at this stage:

\[
\|H_{n,q,r}\|_\infty\le\frac{n^2}{2},
\tag{41}
\]

because every interval has length `m_(n,q)<=P_n`. Integrating (39) by parts once more therefore gives

\[
|\mathcal R_{n,q}|
\le
\frac{n^2}{4m_{n,q}^2}
\left(
\sum_{\substack{1\le r<L_q\\r\ {m odd}}}
|K_{L_q}'(r+1)|
+
\sum_{\substack{1\le r<L_q\\r\ {m odd}}}
\int_r^{r+1}|K_{L_q}''(t)|\,dt
\right).
\tag{42}
\]

The apparent dependence on the number of folded cells disappears when the kernel is unfolded. Since `L_q` is even, the endpoints `r+1` run through all even residue classes, and therefore

\[
\sum_{\substack{1\le r<L_q\\r\ {m odd}}}
|K_{L_q}'(r+1)|
=
2\sum_{k\ge1,\ 2\mid k}\frac1{k^3}
=
\frac{\zeta(3)}4.
\tag{43}
\]

Likewise the second-derivative integrals unfold onto a subset of `[1,infinity)`:

\[
\sum_{\substack{1\le r<L_q\\r\ {m odd}}}
\int_r^{r+1}|K_{L_q}''(t)|\,dt
\le
6\int_1^\infty t^{-4}\,dt
=2.
\tag{44}
\]

Since

\[
\frac{n^2}{m_{n,q}^2}
=
\frac{q^2}{(n-1)^2},
\tag{45}
\]

substitution of (43)--(45) into (42) gives (9).

This is the step that allows `q` to move. The `O_q(n^-2)` remainder in `NB-321` was sufficient for fixed denominators but hid exactly the dependence needed to decide whether the rational skeleton survives below a fixed quadratic ratio.

## 5. The resonance reaches every polynomial exponent above `3/2`

Suppose now that `q=q_n` divides `n` or `n-1` and `q=o(sqrt(n))`. From (7)--(9), the boundary main term has magnitude asymptotic to at least `1/(40n)`, while

\[
n|\mathcal R_{n,q}|
\ll\frac{q^2}{n}\to0.
\tag{46}
\]

More precisely, in either congruence class,

\[
\liminf n|\mathcal B_{n,q}|\ge\frac1{40},
\tag{47}
\]

so (11) follows. Dividing by `||g_2||_2||u_n||_2` and using (12) gives (13).

The polynomial-scale consequence is explicit. Fix any

\[
\frac32<\alpha<2,
\qquad
\theta:=2-\alpha\in(0,1/2).
\tag{48}
\]

Let `q_k=k`, choose

\[
r_k:=\left\lceil k^{1/\theta-1}\right\rceil,
\qquad
n_k:=q_kr_k.
\tag{49}
\]

Then `q_k|n_k`,

\[
q_k=n_k^{\theta+o(1)}=o(\sqrt{n_k}),
\tag{50}
\]

and

\[
m_{n_k,q_k}
=\frac{n_k(n_k-1)}{q_k}
=n_k^{2-\theta+o(1)}
=n_k^{\alpha+o(1)}.
\tag{51}
\]

Equation (13) therefore supplies a logarithmic operator-error obstruction at every exponent in `(3/2,2)`. Fixed `q` includes the quadratic endpoint `alpha=2`. The present argument does not reach `q asymp sqrt(n)` and therefore makes no claim at the `n^(3/2)` endpoint or below it.

## 6. Adversarial checks and prior-art boundary

Several quantifier distinctions are essential.

First, (13) is an absolute lower bound for `||sqrt(m)T-R||`; it tends to zero like a logarithm and is tiny relative to `||R_n||`, which is at least order `sqrt(n)` by `NB-314`. It therefore does not contradict rank-one behavior in any relative sense and does not supply an order-one post-core channel.

Second, the moving-denominator theorem uses the special congruence subsequences `q|n` or `q|(n-1)`. These are sufficient to prove resonant scales at every exponent above `3/2`, but they do not classify arbitrary near-rational quadratic ratios. The exact arithmetic coefficient (6) concerns the first boundary term; condition `q=o(sqrt(n))` is where the uniform second-order remainder proved here is guaranteed to be negligible. A sharper treatment of that remainder could extend the denominator range, and the numerical size of the remainder is not used as evidence for such an extension.

Third, everything remains source-side. The witness `u_n` says nothing about occupation by the first-free Ford datum, finite-section excess, the Nyman distance, or RH.

A fresh prior-art audit confirms that rational arithmetic in fractional-part autocorrelation is classical. Báez-Duarte, Balazard, Landreau and Saias, *Étude de l'autocorrélation multiplicative de la fonction partie fractionnaire* (Ramanujan J. 9 (2005), 215--240; arXiv:math/0306251), show in particular the special behavior of the multiplicative autocorrelation at rational points. Balazard and Martin, *Sur l'autocorrélation multiplicative de la fonction partie fractionnaire et une fonction définie par J. R. Wilton* (arXiv:1305.4395), develop the continued-fraction/Wilton structure, while Bettin--Conrey cotangent sums give another classical rational boundary connected to Nyman--Beurling. Accordingly, no novelty is claimed for the generic fact that rational fractional-part correlations have arithmetic structure.

The line-local contribution proved here is narrower: the rank-one-subtracted finite-section projected-dilation coefficient for the adjacent witness collapses to the specific alternating residue series `C_q`; that coefficient never vanishes on the two canonical congruence subsequences; and the folding remainder is uniform enough to let `q` grow as `o(sqrt(n))`, producing logarithmic operator-error obstructions at every polynomial scale `n^(alpha+o(1))` with `3/2<alpha<=2`. The material located in the audit did not expose this finite-section statement. This is a prior-art boundary from the sources reviewed, not a claim of bibliographic novelty.

No external theorem is load-bearing for the proof, so no durable source dependency is added to `SOURCES.md`.

## Classification and next discriminator

This is a rigorous positive structural finding and a method boundary. `NB-321` left open whether fixed denominators other than `q=2,4` could cancel and treated `q` as fixed. The present result removes both limitations on the two canonical congruence subsequences: every denominator has a nonzero first-order coefficient, and the resonance survives while `q=o(sqrt(n))`.

The next discriminator is the `q`-dependence of the **actual** second-order folding error. The bound (9) loses two powers of `q` through a uniform second-primitive supremum, while direct cancellation inside the weighted remainder is not used. A proof of `o(1/n)` remainder for `q` substantially larger than `sqrt(n)` would push the same logarithmic skeleton toward the linear regime; a counterexample or matching lower remainder near `q asymp sqrt(n)` would instead identify a genuine `n^(3/2)` transition for this adjacent channel. Near-rational and irrational ratios remain separate after that exact-rational problem.