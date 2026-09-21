# PL-410 — Finite cusp-jet renormalization pushes every fixed Ramanujan interior below the zero-sensitive scale

**Evidence/status:** `EXACT-DERIVED + INTERNAL-SHARPENING + ROUTE-ADVANCE + REGULATOR-RENORMALIZATION`.

**Parent findings:** `PL-404`, `PL-408`, `PL-409`.

## Claim

`PL-409` showed that the first nonsmooth term of the cubic Abel kernel

\[
K_\eta(x)=|x|e^{-\eta|x|^3}\sin\!\left(\frac\pi6|x|^3\right),
\qquad \eta>0,
\]

creates an explicit `J_8(q)H^{-8}` Ramanujan alias and therefore a `25/28` crossover with the `H^{-7/4}` zero-sensitive layer. That crossover is sharp **without subtraction**, but it is not a terminal regulator barrier. The complete nonsmooth Taylor jet produces an explicit hierarchy of Jordan-totient aliases, and removing finitely many of them pushes the first remaining deterministic background arbitrarily close to the true endpoint `q\asymp H`.

Put

\[
a=\frac\pi6,
\qquad
\lambda=-\eta+ia,
\qquad
k_j=6j+2\quad(j\ge1).
\tag{1}
\]

Then, for every fixed integer `M>=1`,

\[
\boxed{
\widehat K_\eta(\xi)
=\sum_{j=1}^{M} d_{j,\eta}|\xi|^{-k_j}
+O_{\eta,M}(|\xi|^{-k_{M+1}}),
}
\tag{2}
\]

where

\[
c_{j,\eta}
:=\frac{\Im(\lambda^{2j})}{(2j)!},
\qquad
 d_{j,\eta}
:=(-1)^{j+1}
\frac{2(6j+1)!}{(2\pi)^{6j+2}}c_{j,\eta}.
\tag{3}
\]

Equivalently, only the local powers `|x|^(6j+1)` contribute algebraic Fourier tails. The intervening powers `x^(6j-2)` are smooth across the origin and contribute no singular-jet term.

Let

\[
\beta_{j,\eta}:=2\zeta(k_j)d_{j,\eta}.
\tag{4}
\]

Inserting (2) into the exact Poisson formula of `PL-408`--`PL-409` gives, uniformly for `q<=H`,

\[
\boxed{
B_{q,\eta}(H)
=\mathbf 1_{q=1}\widehat K_\eta(0)
+\sum_{j=1}^{M}
\beta_{j,\eta}\frac{J_{k_j}(q)}{H^{k_j}}
+O_{\eta,M}\!\left(\frac{q^{k_{M+1}}}{H^{k_{M+1}}}\right).
}
\tag{5}
\]

Thus every cusp coefficient has a canonical arithmetic image: the `|x|^(6j+1)` jet maps to the Jordan totient `J_(6j+2)(q)`.

For even `k>=8`, define the exact finite sum

\[
S_k(Q)
:=\sum_{q\le Q}
\frac{\mu(q)^2J_k(q)}{\phi(q)^2}.
\tag{6}
\]

If

\[
A_{\eta,\le Q}^{[2]}(H)
=\frac12\sum_{q\le Q}
\frac{\mu(q)^2}{\phi(q)^2}B_{q,\eta}(H)
\]

is the truncated model statistic from `PL-409`, set

\[
\boxed{
\mathcal R_{\eta,M}(H,Q)
:=A_{\eta,\le Q}^{[2]}(H)-W_{1,\eta}
-\frac12\sum_{j=1}^{M}
\beta_{j,\eta}H^{-k_j}S_{k_j}(Q).
}
\tag{7}
\]

Then, uniformly for `2<=Q<=H`,

\[
\boxed{
\mathcal R_{\eta,M}(H,Q)
\ll_{\eta,M}
H^{-(6M+8)}Q^{6M+7}
\{\log\log(3Q)\}^2.
}
\tag{8}
\]

Consequently, for `Q=H^\kappa` with fixed `0<\kappa<1`,

\[
\boxed{
\mathcal R_{\eta,M}(H,H^\kappa)
=o(H^{-7/4})
\quad\text{whenever}\quad
\kappa<1-\frac{3}{4(6M+7)}.
}
\tag{9}
\]

Because the right-hand threshold tends to `1` as `M->infinity`, this has the important finite-order consequence

\[
\boxed{
\text{for every fixed }\kappa<1,
\text{ finitely many explicit cusp counterterms make the whole }
q\le H^\kappa
\text{ interior invisible at }H^{-7/4}.
}
\tag{10}
\]

No infinite renormalization is needed for a fixed fractional interior.

## 1. The full nonsmooth jet

For `r=|x|`,

\[
K_\eta(x)
=r\,\Im e^{\lambda r^3}
=\sum_{k\ge1}
\frac{\Im(\lambda^k)}{k!}r^{3k+1}.
\tag{11}
\]

If `k=2j-1` is odd, then `3k+1=6j-2` is even, so the corresponding local term is the smooth polynomial `x^(6j-2)`. If `k=2j` is even, then

\[
3k+1=6j+1
\]

is odd and the local term is the genuine cusp

\[
c_{j,\eta}|x|^{6j+1}.
\tag{12}
\]

Its `(6j+1)`-st derivative has jump

\[
2c_{j,\eta}(6j+1)!,
\]

so one further distributional derivative contributes that multiple of `delta_0`. With the Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx,
\]

this gives exactly the coefficient (3). Subtracting a smooth cutoff times the first `M` cusp monomials leaves a function whose next derivative jump occurs at order `6M+7`; repeated integration by parts then gives the remainder in (2). The exponential factor makes all away-from-zero derivatives integrable.

For `j=1`, (3)--(4) recover `PL-409`:

\[
d_{1,\eta}=-\frac{105\eta}{16\pi^7},
\qquad
\boxed{\beta_{1,\eta}=-\frac{\pi\eta}{720}}.
\tag{13}
\]

The next coefficient is also explicit:

\[
\boxed{
\beta_{2,\eta}
=\frac{\pi\eta(36\eta^2-\pi^2)}{7776}.
}
\tag{14}
\]

Thus the gap from Fourier order `8` to `14` in `PL-409` is the first instance of a complete ladder

\[
8,14,20,26,\ldots .
\]

## 2. Poisson converts every cusp order into a Jordan totient

The exact single-denominator formula is

\[
B_{q,\eta}(H)
=\sum_{r\mid q}\mu(q/r)
\sum_{m\in\mathbb Z}\widehat K_\eta(Hm/r).
\tag{15}
\]

For `q<=H`, every nonzero argument satisfies `|Hm/r|>=1`. The `j`-th term of (2) therefore contributes

\[
d_{j,\eta}H^{-k_j}
\left(\sum_{m\ne0}|m|^{-k_j}\right)
\left(\sum_{r\mid q}\mu(q/r)r^{k_j}\right).
\]

The two parenthesized factors are `2 zeta(k_j)` and `J_(k_j)(q)`, respectively, proving the finite expansion in (5). The next Fourier remainder gives

\[
H^{-k_{M+1}}
\sum_{r\mid q}r^{k_{M+1}}
\ll
H^{-k_{M+1}}q^{k_{M+1}},
\]

uniformly in the same range.

After multiplication by `mu(q)^2/phi(q)^2` and summation to `Q`,

\[
\sum_{q\le Q}
\frac{\mu(q)^2q^k}{\phi(q)^2}
\ll_k
Q^{k-1}\{\log\log(3Q)\}^2,
\tag{16}
\]

which proves (8).

## 3. The remaining crossover after `M` counterterms

The finite sums in (6) have the same one-pole structure used for `S_8` in `PL-409`. For every fixed `k>=8`,

\[
\sum_{q\ge1}
\frac{\mu(q)^2J_k(q)}{\phi(q)^2q^s}
=\zeta(s-k+2)G_k(s),
\tag{17}
\]

where `G_k` is analytic near `s=k-1` and

\[
C_k:=G_k(k-1)
=\prod_p
\left(1-\frac1p\right)
\left(
1+\frac{p^k-1}{p^{k-1}(p-1)^2}
\right)>0.
\tag{18}
\]

Hence

\[
S_k(Q)\sim \frac{C_k}{k-1}Q^{k-1}.
\tag{19}
\]

Expand (5) one order farther than the number of counterterms in (7). If `beta_(M+1,eta) != 0`, then for every fixed `kappa<1`, with `k=6M+8`,

\[
\boxed{
\mathcal R_{\eta,M}(H,H^\kappa)
\sim
\frac{\beta_{M+1,\eta}C_k}{2(k-1)}
H^{-k+(k-1)\kappa}.
}
\tag{20}
\]

Indeed, the next remainder divided by this term is `O((Q/H)^6 (log log Q)^2)=o(1)`. Therefore the threshold in (9) is sharp whenever the next cusp coefficient is nonzero: at

\[
\kappa
=1-\frac{3}{4(6M+7)}
\tag{21}
\]

the first untreated regulator alias is genuinely of order `H^-7/4`.

For `M=0`, (21) is `25/28`, reproducing `PL-409`. After subtracting only the explicit `J_8` term (`M=1`), the generic next coefficient is (14), so

\[
\boxed{
\eta\ne\frac\pi6
\quad\Longrightarrow\quad
\text{next crossover }\kappa=\frac{49}{52}.
}
\tag{22}
\]

There is also a useful tuned exception. If

\[
\eta=a=\frac\pi6,
\]

then `lambda=a(-1+i)` and

\[
\lambda^{2j}=(-2ia^2)^j.
\]

Thus `c_(j,eta)=0` for every even `j`. In particular `beta_(2,a)=0`, while `beta_(3,a) != 0`. After subtracting the `J_8` alias, the next nonzero Fourier order is then `20`, not `14`, and its zero-scale crossover is

\[
\boxed{
\kappa=1-\frac{3}{4\cdot19}=\frac{73}{76}.
}
\tag{23}
\]

This tuning does not erase the zeta-zero layer: `PL-404` proves that the Mellin transform of the cubic Abel weight is nonzero at every nontrivial-zero pole for every fixed `eta>0`, including `eta=pi/6`.

## 4. Prime-exponent interpretation

The sums `S_k(Q)` remain supported on square-free denominators. Hence

\[
q\le H^\kappa
\quad\Longleftrightarrow\quad
v(q)\in\{0,1\}^{(\mathcal P)},
\qquad
\langle v(q),(\log p)_p\rangle\le\kappa\log H.
\]

The counterterms in (7) are therefore not arbitrary analytic subtractions. Each is an explicit multiplicative weight on the same square-free exponent-lattice energy ball,

\[
J_k(q)=q^k\prod_{p\mid q}(1-p^{-k}).
\]

Equation (10) says that the apparent sequence of fractional interior barriers is generated by the local archimedean cusp jet and can be removed to any prescribed finite depth. What cannot be reached by this argument is the actual endpoint `q\asymp H`, where `Q/H` is no longer small and the six-order separation between successive cusp terms no longer makes the remainder subordinate.

## 5. Novelty and adversarial audit

The ingredients behind (2)--(5) are standard: Taylor expansion at an isolated cusp, distributional derivative jumps, repeated integration by parts, Poisson summation, Jordan totients and a one-pole Tauberian argument. None is claimed as a new harmonic-analysis theorem.

The line-specific delta is the **all-finite-order composition** of those facts for the already-fixed cubic Abel/Ramanujan statistic. Targeted literature searches for the cubic Abel kernel together with Ramanujan/Jordan-totient Poisson aliases, and repository searches for the resulting `49/52` or general `6M+7` crossover, located no direct prior occurrence. `PL-409` contains only the first `J_8` term and the `O(|xi|^-14)` remainder, while explicitly leaving subtraction as a possible escape. Equations (2)--(23) turn that escape into a quantitative finite renormalization scheme.

Several limits are essential.

1. **This remains model-side.** No actual-prime source replacement is proved. The prime-variance threshold of `PL-407` and the signed prime/model bridge remain independent arithmetic obstacles.

2. **`M` is fixed before `H->infinity`.** Equation (10) allows `M` to depend on a prescribed fixed `kappa<1`, but gives no uniform control as `kappa->1` with `H`, and constructs no infinite counterterm series.

3. **The exact finite sums `S_k(Q)` are the counterterms.** Replacing them only by their leading Tauberian asymptotics would introduce a new remainder that has not been shown small enough at the zero-sensitive scale.

4. **Special coefficient zeros only improve the bound.** Sharpness at the nominal threshold requires `beta_(M+1,eta) != 0`. The choice `eta=pi/6` is an explicit example where the generic `49/52` term vanishes and the next barrier jumps to `73/76`.

5. **The full endpoint is not renormalized away.** When `Q\asymp H`, successive terms are no longer separated by a factor `(Q/H)^6=o(1)`. The `H^-1` boundary contribution and the `H^-7/4` zero layer of the full singular-series model therefore remain genuinely endpoint phenomena.

## Consequence for the line

The `25/28` obstruction of `PL-409` is the first untreated archimedean cusp alias, not a fundamental moving-boundary limit. After exact finite cusp-jet subtraction, **every fixed fractional square-free energy interior can be pushed below the RH-sensitive `H^-7/4` resolution**. The model-side target therefore sharpens again: the nonrenormalizable region is the true moving endpoint `q/H=Theta(1)`, not any fixed power `q<=H^kappa`.

This makes the next arithmetic question cleaner. A source-faithful prime/model comparison should be aimed directly at the signed `q\asymp H` endpoint (or at an equivalent prime-variance functional), with the explicit regulator jet removed first. Improving control of another fixed fractional interior without this subtraction would only rediscover a removable archimedean background.