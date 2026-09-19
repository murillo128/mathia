# FD-217 — Linear prime-cutoff Euler coherence remains one-horizon blind

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** macroscopic-prime multiplicative coherence / switched root-filter countermodel / exact reservoir cancellation / one-horizon representation boundary
- **Depends on:** FD-216
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + LINEAR-EULER-CUTOFF + ONE-HORIZON-COUNTERMODEL + EXACT-RESERVOIR-CANCELLATION`

## Claim

`FD-216` shows that at a target horizon one may impose exact Möbius Euler relations at `Theta(log N)` primes while retaining a switched blind mode uniformly across a target-scale interval. If the observation requirement is weakened to the single target horizon itself, the number of exact Euler factors can be increased almost to the full prime prefix.

Keep the period-three switched depth schedule

\[
q_j=(0,3,3,0,3,3,\ldots),
\qquad
q(n)=q_{\lfloor\log_2n\rfloor},
\tag{1}
\]

and write

\[
\mathcal C_{q(n)}^X(n)=(T-I)^{q(n)+1}X(n),
\qquad
(TF)(n)=F(2n).
\tag{2}
\]

Fix any constant

\[
0<\theta<1.
\tag{3}
\]

Then for every sufficiently large integer `N` there is a deterministic sequence

\[
\xi^{(N)}_n\in\{-1,0,1\},
\qquad
(\xi^{(N)}_n)^2=\mu(n)^2,
\qquad
\xi^{(N)}_1=1,
\tag{4}
\]

such that for **every prime up to the linear cutoff**

\[
\boxed{
\xi^{(N)}_{pn}=-\xi^{(N)}_n
\quad
(p\le\theta N,\ p\nmid n),
}
\tag{5}
\]

while, writing

\[
X_N(x)=\sum_{n\le x}\xi^{(N)}_n,
\tag{6}
\]

one has simultaneously

\[
\boxed{
|\mathcal C_{q(N)}^{X_N}(N)|\le4
}
\tag{7}
\]

and

\[
\boxed{
X_N(N)\asymp_\theta \frac{N}{\log N}.
}
\tag{8}
\]

The constrained set therefore has

\[
\pi(\theta N)\sim\theta\frac{N}{\log N}
\tag{9}
\]

exact Euler factors, rather than the logarithmically many factors of `FD-216`, yet the target switched observation can still be bounded while the summatory function is almost linear on the power scale.

This strengthening deliberately trades away the uniformity of `FD-216`: (7) is a **one-horizon** statement, not an all-integer or target-interval blind estimate, and the source is allowed to depend on `N`. The quantifier distinction is the point of the result.

There is also an exact endpoint. If (4)--(5) are required instead for every prime `p<=N`, then necessarily

\[
\xi_n=\mu(n)\qquad(n\le N),
\tag{10}
\]

so `X_N(N)=M(N)`. Thus every fixed fractional cutoff `theta<1` leaves enough one-horizon freedom for (7)--(8), whereas the full cutoff `theta=1` locks the entire target prefix to Möbius.

## 1. Leave only the unconstrained core free

Let

\[
P_N=\{p\text{ prime}:p\le\theta N\},
\qquad
Q_N=\prod_{p\in P_N}p.
\tag{11}
\]

Every squarefree integer has a unique factorization

\[
n=dm,
\qquad
d\mid Q_N,
\qquad (m,Q_N)=1.
\tag{12}
\]

Choose arbitrary signs `eta_m in {-1,+1}` on the squarefree `P_N`-coprime core, with `eta_1=1`, and define

\[
\xi_{dm}=\mu(d)\eta_m
\tag{13}
\]

for squarefree `dm`; put `xi_n=0` on nonsquarefree integers. Then (4) holds automatically, and for every selected prime `p in P_N`,

\[
\xi_{pn}=-\xi_n
\qquad(p\nmid n)
\tag{14}
\]

exactly. Thus all selected Euler factors can be imposed globally while the values of the unselected core remain independent degrees of freedom.

Start with the Möbius core `eta_m=mu(m)` and flip only a finite collection `R` of unselected **core primes** `r>theta N`, changing `eta_r=-1` to `eta_r=+1`. No composite core value is changed. The contribution of a single flipped prime `r` to the summatory error at `x` is then exactly

\[
2\sum_{\substack{d\mid Q_N\\d\le x/r}}\mu(d).
\tag{15}
\]

For the switched depths in (1), the largest sampled point is `16N`. If `r>theta N`, then

\[
\frac{x}{r}<\frac{16}{\theta}
\qquad(x\le16N).
\tag{16}
\]

For sufficiently large `N`, every prime not exceeding `16/theta` already lies in `P_N`. Hence every squarefree `d<=x/r` divides `Q_N`, and (15) becomes the exact small-argument identity

\[
\boxed{
X_N(x)-M(x)
=
2\sum_{r\in R}M\!\left(\left\lfloor\frac xr\right\rfloor\right)
\qquad(x\in\{N,2N,4N,8N,16N\}).
}
\tag{17}
\]

This is the key simplification: after imposing almost all prime Euler laws below the target scale, each remaining prime in a macroscopic reservoir has a fixed finite response vector determined only by the small values of `M`.

## 2. Exact cancellation when `q(N)=0`

Suppose first that the schedule chooses `q(N)=0`. Then

\[
\mathcal C_0^X(N)=X(2N)-X(N).
\tag{18}
\]

Put

\[
a_0=\max\{\theta,2/3\}.
\tag{19}
\]

For any prime

\[
r\in(a_0N,N],
\tag{20}
\]

one has

\[
\left(\left\lfloor\frac Nr\right\rfloor,
\left\lfloor\frac{2N}{r}\right\rfloor\right)=(1,2),
\tag{21}
\]

so, since `M(1)=1` and `M(2)=0`, flipping `r` changes (18) by

\[
2(M(2)-M(1))=-2,
\tag{22}
\]

while increasing `X_N(N)` by `2`.

For any prime

\[
s\in(N,2N],
\tag{23}
\]

the corresponding floors are `(0,1)`, so the same flip changes (18) by `+2` and does not affect `X_N(N)`.

The prime number theorem gives

\[
\#\{r:(20)\}
\sim(1-a_0)\frac N{\log N},
\qquad
\#\{s:(23)\}
\sim\frac N{\log N}.
\tag{24}
\]

Choose

\[
A=\frac{1-a_0}{2}\frac N{\log N}+o\!\left(\frac N{\log N}\right)
\tag{25}
\]

low-reservoir primes to flip. The physical Möbius baseline

\[
b_0(N)=M(2N)-M(N)
\tag{26}
\]

satisfies `b_0(N)=o(N/log N)` by the classical Davenport bound already anchored in `SOURCES.md`. Hence one can choose an integer number `B=A-b_0(N)/2+O(1)` of high-reservoir flips, with `0<=B` below the capacity in (24), such that

\[
|b_0(N)-2A+2B|\le1.
\tag{27}
\]

Equations (17)--(27) prove (7) in the `q=0` bands. Moreover the high flips lie above `N`, while every low flip contributes `+2` to the prefix, so

\[
X_N(N)=M(N)+2A\asymp_\theta\frac N{\log N}.
\tag{28}
\]

## 3. Exact cancellation when `q(N)=3`

Now suppose `q(N)=3`. Then

\[
\mathcal C_3^X(N)
=
X(16N)-4X(8N)+6X(4N)-4X(2N)+X(N).
\tag{29}
\]

Put

\[
a_3=\max\{\theta,16/17\}.
\tag{30}
\]

For a prime

\[
r\in(a_3N,N],
\tag{31}
\]

the five floor quotients are exactly

\[
(1,2,4,8,16),
\tag{32}
\]

and

\[
(M(1),M(2),M(4),M(8),M(16))=(1,0,-1,-2,-1).
\tag{33}
\]

Therefore one low-reservoir flip changes (29) by

\[
2\{1-4(0)+6(-1)-4(-2)+(-1)\}=+4,
\tag{34}
\]

and again increases `X_N(N)` by `2`.

For a prime in the disjoint high reservoir

\[
s\in(16N/15,8N/7],
\tag{35}
\]

the five quotients are

\[
(0,1,3,7,14),
\tag{36}
\]

with

\[
(M(0),M(1),M(3),M(7),M(14))=(0,1,-1,-2,-2).
\tag{37}
\]

Its response is therefore

\[
2\{0-4(1)+6(-1)-4(-2)+(-2)\}=-8,
\tag{38}
\]

and it does not change `X_N(N)`.

The low reservoir contains

\[
(1-a_3+o(1))\frac N{\log N}
\tag{39}
\]

primes and the high reservoir contains

\[
\left(\frac87-\frac{16}{15}+o(1)\right)\frac N{\log N}
=
\left(\frac8{105}+o(1)\right)\frac N{\log N}
\tag{40}
\]

primes. Choose half of the low reservoir, say `A`, so `A asymp_theta N/log N`. The physical baseline

\[
b_3(N)=(T-I)^4M(N)
\tag{41}
\]

is again `o(N/log N)` by the same fixed-scale Davenport estimate. Consequently an integer

\[
B=\frac{b_3(N)+4A}{8}+O(1)
\tag{42}
\]

can be chosen inside the high reservoir for all sufficiently large `N`; note that asymptotically `B=A/2`, while (40) has more than enough capacity because `1-a_3<=1/17`. Choosing the nearest admissible integer gives

\[
|b_3(N)+4A-8B|\le4.
\tag{43}
\]

This proves (7) in the `q=3` bands, and exactly as before

\[
X_N(N)=M(N)+2A\asymp_\theta\frac N{\log N}.
\tag{44}
\]

Together, Sections 2--3 prove the claim for the entire schedule (1).

## 4. The endpoint `theta=1` locks the prefix

The construction above works for every fixed `theta<1` because the interval between `theta N` and `N` contains a macroscopic reservoir of unconstrained primes. At the exact endpoint there is no such freedom.

Suppose a squarefree ternary source with `xi_1=1` satisfies

\[
\xi_{pn}=-\xi_n
\qquad(p\le N,\ p\nmid n).
\tag{45}
\]

If `n<=N` is squarefree, every prime factor of `n` is at most `N`. Writing `n=p_1...p_k` and iterating (45) therefore gives

\[
\xi_n=(-1)^k=\mu(n).
\tag{46}
\]

On nonsquarefree `n`, the support condition already gives `xi_n=0=mu(n)`. Hence (10) follows.

This gives a sharp qualitative one-horizon boundary: **every fixed fractional prime cutoff remains relaxable, while complete prime coverage of the target prefix removes all source freedom below the target.** It does not say how close a cutoff `theta_N -> 1` may approach one while a useful reservoir persists; that shrinking-interval problem would require prime-distribution input beyond the fixed-ratio PNT used here.

## 5. Representation audit and prior-art boundary

Unlike a transform-space extremizer, the countermodel is an explicit arithmetic sequence on all positive integers. It has exactly the Möbius zero set, takes only the physical amplitudes `{-1,0,1}`, and obeys the exact Möbius Euler relation at every selected prime globally. The freedom is also explicit: multiplicativity is **not** imposed between unselected core primes, and the source changes with the target horizon `N`. Therefore this is not a Möbius counterexample and cannot be diagonalized into one fixed globally multiplicative source without a new argument.

The closest general literature located in the prior-art search concerns genuinely multiplicative squarefree functions with prescribed `+/-1` values on primes: Marco Aymone, *A note on multiplicative functions resembling the Möbius function*, arXiv `1908.11014`, and Qingyang Liu, *Multiplicative functions resembling the Möbius function*, arXiv `2205.00972`. Pretentious multiplicative-function theory, beginning for example with Granville--Soundararajan, *Pretentious multiplicative functions and an inequality for the zeta-function*, arXiv `math/0608407`, is also a neighboring framework for measuring prime-by-prime agreement. Those works assume global multiplicativity and do not supply the finite-horizon two-reservoir switched-filter cancellation above. I did not find this exact linear-cutoff one-horizon construction in the searched literature.

No new external theorem is load-bearing. The proof uses only fixed-ratio prime counts from the prime number theorem and the unconditional `M(x)<<_A x/log^A x` estimate already anchored in line-local `SOURCES.md`; the remaining identities are finite and proved above. Accordingly `SOURCES.md` needs no new durable dependency.

## 6. Consequence for the research line

`FD-216` left open whether its `Theta(log N)` Euler-coherence budget was merely an artifact of the Green inversion and Euler-cube error ledger. At a single horizon it is: the switched root filter can remain bounded even when exact Möbius Euler laws are imposed at

\[
\Theta\!\left(\frac N{\log N}\right)
\tag{47}
\]

primes, indeed at every prime below any fixed fraction `theta N` of the target.

The result does **not** supersede the stronger uniform statement of `FD-216`; rather, the pair separates two resources. Prime-count coherence can be made almost maximal if one asks for blindness at one target only, while target-interval/all-integer blindness is much more expensive. The endpoint lemma shows why simply increasing the local prime count is the wrong next discriminator: only full coverage of all prime factors below the target literally collapses the relaxed source to Möbius on that prefix.

The remaining useful frontier is therefore even more specifically cross-horizon. A physical argument must force the same source to carry compatible prime information as the horizon moves, or must couple enough neighboring horizons that the free prime reservoirs used here cannot be retuned independently. Merely showing that a large, even linearly cut off, finite set of Euler relations holds at each isolated target does not by itself defeat switched blindness.