# FD-216 — Logarithmically growing Euler coherence remains horizon-locally blind

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** growing-prime multiplicative coherence / switched root-filter countermodel / deterministic prefix rounding / finite-horizon representation boundary
- **Depends on:** FD-215
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + GROWING-EULER-COHERENCE + HORIZON-LOCAL-COUNTERMODEL + DETERMINISTIC-ROUNDING`

## Claim

`FD-215` shows that every fixed finite collection of exact Möbius Euler relations can be absorbed by the all-integer switched blind construction. Its constants were deliberately non-uniform in the selected prime set. That non-uniformity does not begin as soon as the number of imposed Euler factors tends to infinity.

Let

\[
\alpha=\frac43\log_2\frac{1+\sqrt5}{2}
\approx0.9256558848408232,
\qquad
\beta=\alpha-\frac12
\approx0.4256558848408232,
\tag{1}
\]

and keep the period-three depth schedule

\[
q_j=(0,3,3,0,3,3,\ldots),
\qquad
q(n)=q_{\lfloor\log_2n\rfloor}.
\tag{2}
\]

For every fixed

\[
0<c<\frac1{2\log 2}\approx0.7213475204,
\tag{3}
\]

consider the blind-profile horizons

\[
N_m=3\,2^{3m-1},
\qquad
k_m=\lfloor c\log N_m\rfloor,
\tag{4}
\]

where `log` in (3)--(4) is the natural logarithm. Let `P_m` be the first `k_m` primes. Then, for all sufficiently large `m`, there is a deterministic sequence

\[
\xi^{(m)}_n\in\{-1,0,1\},
\qquad
(\xi^{(m)}_n)^2=\mu(n)^2,
\qquad
\xi^{(m)}_1=1,
\tag{5}
\]

such that

\[
\boxed{
\xi^{(m)}_{pn}=-\xi^{(m)}_n
\quad
(p\in P_m,\ p\nmid n).
}
\tag{6}
\]

Writing

\[
X_m(N)=\sum_{n\le N}\xi^{(m)}_n,
\qquad
\mathcal C_{q(n)}^{X_m}(n)=(T-I)^{q(n)+1}X_m(n),
\tag{7}
\]

one has, with

\[
\gamma_c=\max\{\beta,c\log2\}<\frac12,
\tag{8}
\]

the horizon-uniform bounds

\[
\boxed{
\sup_{N_m\le n\le2N_m}
|\mathcal C_{q(n)}^{X_m}(n)|
\le N_m^{\gamma_c+o(1)},
}
\tag{9}
\]

while at the explicit blind point

\[
\boxed{
|X_m(N_m)|=N_m^{\alpha-o(1)}.
}
\tag{10}
\]

Thus a source can obey exact Möbius Euler-factor coherence at **Theta(log N)** prescribed primes, with the number of constrained primes tending to infinity, and still be super-square-root at the target horizon while the Farey-derived switched root filter is actually sub-square-root there.

For each fixed `m`, the same source satisfies the stronger non-uniform all-integer estimate

\[
\mathcal C_{q(n)}^{X_m}(n)=O_{P_m}(n^\beta+1).
\tag{11}
\]

The construction is a **finite-horizon family of sources**, not one source satisfying an increasing nested family of Euler laws at all scales. That distinction is exact: if one fixed squarefree ternary source with `xi_1=1` obeys (6) for nested prime sets whose union is all primes, then the source is identically Möbius. Consequently (4)--(10) quantify how far the switched observation remains blind under scale-growing *finite* multiplicative coherence; they do not produce a Möbius counterexample or settle the global infinite-prime limit.

## 1. Expose the finite-prime costs in `FD-215`

Use the `FD-215` profile with an explicit amplitude parameter,

\[
A_\varepsilon(x)=\varepsilon a_{j(x)}h(t(x)),
\tag{12}
\]

where the period-three recurrence gives

\[
\mathcal C_{q(n)}^{A_\varepsilon}(n)=0
\qquad(n\ge1),
\tag{13}
\]

and at (4)

\[
|A_\varepsilon(N_m)|\asymp \varepsilon N_m^\alpha.
\tag{14}
\]

The regularity used in `FD-215` is

\[
|A_\varepsilon(x)|\ll\varepsilon x^\alpha,
\qquad
|A_\varepsilon'(x)|\ll\varepsilon x^{\alpha-1}
\tag{15}
\]

on each smooth piece, with the same one-sided control at dyadic breakpoints.

For a finite prime set `P`, write

\[
C_\alpha(P)=\prod_{p\in P}(1-p^{-\alpha})^{-1},
\qquad
\delta(P)=\frac1{\zeta(2)}\prod_{p\in P}\frac{p}{p+1},
\tag{16}
\]

and

\[
G_s(P)=\prod_{p\in P}(1+p^{-s})
\qquad(s>0).
\tag{17}
\]

The finite Euler Green primitive

\[
U_P(x)=\sum_{s\in\langle P\rangle}A_\varepsilon(x/s)
\tag{18}
\]

still satisfies exactly

\[
D_PU_P=A_\varepsilon,
\qquad
D_P=\prod_{p\in P}(I-S_p),
\qquad
(S_pF)(x)=F(x/p).
\tag{19}
\]

The point of keeping the products explicit is that the `FD-215` estimates become

\[
|U_P(x)|\ll\varepsilon C_\alpha(P)x^\alpha
\tag{20}
\]

and, for `w_n=U_P(n)-U_P(n-1)`, on every dyadic block `X<=n<=2X`,

\[
\sup |w_n|
+
\sum |w_{n+1}-w_n|
\ll
\varepsilon C_\alpha(P)X^{\alpha-1}.
\tag{21}
\]

No fixed-`P` big-O is hidden from this point onward.

## 2. A uniform squarefree-core discrepancy

Let

\[
g_P(n)=\mu(n)^2\mathbf1_{(n,\prod_{p\in P}p)=1},
\qquad
Q_P(x)=\sum_{n\le x}g_P(n).
\tag{22}
\]

There is an elementary uniform estimate

\[
\boxed{
Q_P(x)=\delta(P)x+O\!\left(\sqrt x\,G_{1/2}(P)\right).
}
\tag{23}
\]

To see this without a sieve theorem, define a multiplicative function `h_P` by the local rules

\[
h_P(p)=-1,\ h_P(p^j)=0\ (j\ge2),\quad p\in P,
\tag{24}
\]

and

\[
h_P(p^2)=-1,\ h_P(p^j)=0\ (j\ne0,2),\quad p\notin P.
\tag{25}
\]

Then, coefficient by coefficient,

\[
g_P=1*h_P.
\tag{26}
\]

The support of `|h_P|` consists of integers `ab^2` with `a|prod_(p in P)p` and `b` squarefree using no selected prime. Hence

\[
\sum_{d\le x}|h_P(d)|
\le
\sqrt x\sum_{a\mid\prod P}a^{-1/2}
=
\sqrt x\,G_{1/2}(P),
\tag{27}
\]

and the same decomposition gives

\[
x\sum_{d>x}\frac{|h_P(d)|}{d}
\ll
\sqrt x\,G_{1/2}(P).
\tag{28}
\]

Finally

\[
\sum_{d\ge1}\frac{h_P(d)}d
=
\prod_{p\in P}(1-p^{-1})
\prod_{p\notin P}(1-p^{-2})
=
\delta(P),
\tag{29}
\]

so summing `g_P=1*h_P` proves (23).

Choose a sufficiently small absolute `kappa>0` and set

\[
\boxed{
\varepsilon_P=\kappa\frac{\delta(P)}{C_\alpha(P)}.
}
\tag{30}
\]

Equation (21) then makes `|w_n|<=delta(P)` after shrinking `kappa` once, uniformly in `P`. Define

\[
b_n=\delta(P)^{-1}g_P(n)w_n,
\qquad
B_P(N)=\sum_{n\le N}b_n.
\tag{31}
\]

Summation by parts with (21) and (23) yields

\[
\boxed{
B_P(N)-U_P(N)
\ll
G_{1/2}(P)N^\beta+O(1),
}
\tag{32}
\]

because `beta=alpha-1/2>0`. The cancellation of `delta(P)` and `C_alpha(P)` in (32) is the first useful uniformity gain from the amplitude choice (30).

## 3. Replace random rounding by deterministic prefix balancing

The `sqrt(N log N)` rounding error in `FD-215` is not intrinsic. The following scalar lemma is enough.

If `t_j in [-1,1]`, there are signs `eta_j in {-1,+1}` such that

\[
\left|\sum_{i\le J}(\eta_i-t_i)\right|\le1
\qquad(J\ge1).
\tag{33}
\]

Indeed, if the current error is `E in [-1,1]`, choose `eta=+1` when `E<=t` and `eta=-1` when `E>t`. In the first case `E+1-t` remains in `[-1,1]`; in the second `E-1-t` does too.

Apply this to the values `b_n` on the squarefree `P`-coprime core, after changing the single value `b_1` to `1`. That finite modification costs only `O(1)` and permits `eta_1=1`. Thus one obtains deterministic core signs with

\[
Y_P(N)=B_P(N)+O(1)
\qquad\text{for every }N.
\tag{34}
\]

Extend the signs through the exact selected Euler cube exactly as in `FD-215`: if the squarefree integer `n` is uniquely `n=dm`, with `d|prod_(p in P)p` and `m` squarefree and coprime to every selected prime, put

\[
\xi_n=\mu(d)\eta_m,
\tag{35}
\]

and put `xi_n=0` on nonsquarefree integers. Then

\[
\xi_{pn}=-\xi_n
\qquad(p\in P,\ p\nmid n)
\tag{36}
\]

exactly, and

\[
X_P(N)=
\sum_{d\mid\prod P}\mu(d)
Y_P\!\left(\left\lfloor\frac Nd\right\rfloor\right).
\tag{37}
\]

This deterministic replacement is already a strict strengthening of the fixed-prime construction: for fixed `P` it removes the random `sqrt(N log N)` term entirely.

## 4. The complete uniform error ledger

Insert (32) and (34) into (37). The squarefree-projection error is bounded by

\[
N^\beta G_{1/2}(P)
\sum_{d\mid\prod P}d^{-\beta}
=
N^\beta G_{1/2}(P)G_\beta(P).
\tag{38}
\]

The deterministic prefix-rounding errors contribute at most `O(2^k)`, where `k=|P|`.

It remains to compare the floored main term with the exact real Euler identity (19). For `d<=N`, the local Lipschitz estimate from (21) gives

\[
\left|
U_P\!\left(\left\lfloor\frac Nd\right\rfloor\right)-U_P(N/d)
\right|
\ll
\varepsilon_PC_\alpha(P)(N/d)^{\alpha-1}.
\tag{39}
\]

Since `d<=N`, each normalized factor `(d/N)^(1-alpha)` is at most one. Summing over at most `2^k` divisors and using (30) gives a further `O(2^k)` contribution. Terms with `d>N` vanish in the real Green representation because the base profile is zero below `1`.

Consequently the complete comparison is

\[
\boxed{
X_P(N)-A_{\varepsilon_P}(N)
\ll
N^\beta G_{1/2}(P)G_\beta(P)+2^k+1.
}
\tag{40}
\]

For fixed `P`, (40) immediately implies

\[
X_P(N)=A_{\varepsilon_P}(N)+O_P(N^\beta+1),
\tag{41}
\]

and the filter in (11) follows from (13), because every selected difference has order at most four.

Equation (40), rather than a generic `O_P`, is the quantitative growing-coherence ledger left open by `FD-215`.

## 5. The first `c log N` primes remain cheap enough

Let `P` be the first `k` primes and write `y=p_k`. The prime number theorem, already anchored for this line in `SOURCES.md`, gives

\[
y=O(k\log k).
\tag{42}
\]

For `0<s<1`, elementary comparison with all integers gives

\[
\log G_s(P)
\le
\sum_{n\le y}n^{-s}
=O_s(y^{1-s}),
\tag{43}
\]

and similarly

\[
\log C_\alpha(P)=O(y^{1-\alpha}).
\tag{44}
\]

There is also a deliberately crude lower bound for the core density that needs no Mertens product theorem:

\[
\delta(P)^{-1}
=\zeta(2)\prod_{p\le y}(1+p^{-1})
\le
\zeta(2)\prod_{2\le n\le y}(1+n^{-1})
\ll y.
\tag{45}
\]

If `k=floor(c log N)`, then (42) gives `y=O(log N log log N)`. Equations (43)--(45) therefore imply

\[
G_{1/2}(P)G_\beta(P)=N^{o(1)},
\qquad
\varepsilon_P=N^{-o(1)}.
\tag{46}
\]

Meanwhile

\[
2^k=N^{c\log2+o(1)}.
\tag{47}
\]

Putting (46)--(47) into (40) gives

\[
X_P(N)-A_{\varepsilon_P}(N)
=
N^{\max\{\beta,c\log2\}+o(1)}.
\tag{48}
\]

For `c` satisfying (3), the exponent in (48) is strictly below `1/2`. The same estimate holds at every fixed multiplicative translate of `N`, so applying the order-at-most-four switched difference yields (9). At the blind points (4), (14), (46) and (48) give

\[
|X_m(N_m)|
\asymp
\varepsilon_{P_m}N_m^\alpha
=
N_m^{\alpha-o(1)},
\tag{49}
\]

which proves (10).

The numerical constant in (3) is **not** claimed to be an optimal threshold. It comes from the crude worst-case `2^k` cost of lifting a bounded prefix discrepancy through the full selected Euler cube and from the equally crude floor replacement. Any structured cancellation across the cube could improve it. What is proved is the existence of an explicit `Theta(log N)` regime, which is already enough to rule out the hypothesis that *every* unbounded growth of Euler coherence destroys the switched blind mode.

## 6. The coherent infinite-prime limit is exactly Möbius

There is a separate quantifier boundary that should not be blurred with (4)--(10). Suppose a **single** sequence `xi_n` satisfies

\[
\xi_n^2=\mu(n)^2,
\qquad
\xi_1=1,
\tag{50}
\]

and suppose there are nested finite prime sets `P_1 subset P_2 subset ...` whose union is all primes such that

\[
\xi_{pn}=-\xi_n
\qquad(p\in P_j,\ p\nmid n)
\tag{51}
\]

for every `j`. For a squarefree `n=p_1...p_r`, choose `j` containing all its prime factors and iterate (51):

\[
\xi_n=(-1)^r=\mu(n).
\tag{52}
\]

On nonsquarefree integers (50) already gives `xi_n=0=mu(n)`. Hence

\[
\boxed{\xi=\mu.}
\tag{53}
\]

So a request for one coherent source satisfying an eventually exhaustive growing family of exact Euler factors is no longer a relaxation of Möbius at all. The nontrivial remaining question is quantitative: which scale-dependent finite packages can be absorbed while retaining a uniform blind estimate, and whether a Farey argument can exploit the genuinely global compatibility that (53) identifies.

## 7. Prior-art and falsification boundary

The scalar prefix-balancing lemma (33) is a one-dimensional controlled-rounding fact and is not claimed as new. The controlled-rounding literature contains stronger matrix and initial-interval rounding statements; for example, B. Doerr, T. Friedrich, C. Klein and R. Osbild, *Rounding of Sequences and Matrices, with Applications* (WAOA 2005, DOI `10.1007/11671411_8`), treats substantially more general rounding constraints. The proof of (33) is included because the exact deterministic constant is what removes the probabilistic error from this construction.

Terence Tao, *A Remark on Partial Sums Involving the Möbius Function*, Bulletin of the Australian Mathematical Society **81** (2010), 343--349, DOI `10.1017/S0004972709000884`, studies Möbius sums over multiplicative semigroups generated by arbitrary prime sets. That is neighboring Euler-semigroup prior art, but it neither supplies nor contradicts the Farey switched-filter construction, the profile preconditioning, or the horizon-growing exact Euler-cube realization here.

No external theorem beyond the prime number theorem is load-bearing in the derivation, and the PNT already has a durable line-local source anchor. The squarefree-core estimate, controlled rounding, Euler inversion and error ledger are proved above, so `SOURCES.md` needs no new dependency.

The main falsification boundaries are:

- the family `xi^(m)` depends on the horizon through `P_m` and `epsilon_(P_m)`; it is not one global source;
- the constant `1/(2 log 2)` is sufficient, not necessary or sharp;
- (9) is a uniform target-scale statement, while (11) is an all-integer statement with constants depending on the finite set `P_m`;
- exact coherence at an eventually exhaustive nested prime family for one fixed source collapses to Möbius by (53), so the present countermodel cannot be passed to the infinite-prime limit by diagonal rhetoric;
- none of these statements bounds the physical Mertens function or advances the Franel--Landau criterion without a new argument using the global Möbius law.

## 8. Consequence for the research line

The finite-versus-global boundary from `FD-215` is now quantitative. The switched Farey root sensor remains blind not merely after fixing any finite number of Euler factors, but after imposing an explicitly **unbounded, logarithmically growing number** of exact factors at each target horizon. Therefore `|P_N| -> infinity` by itself is not the missing discriminator.

At the same time, the single-source lemma (53) shows why the full limit is qualitatively different: once the growing constraints are required coherently on one source and exhaust all primes, there is no countermodel class left; the source is Möbius. The remaining useful question is thus not whether some unspecified amount of multiplicative coherence grows, but whether the physical Farey observable can exploit **global coherence across scales** before the problem has simply become the original Mertens/RH problem in another notation.