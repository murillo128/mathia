# PL-422 — Short-AP equidistribution collapses the canonical raw residue Gram below the `p=5` dephasing floor

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

**Parent findings:** `PL-414`, `PL-418`, `PL-419`, `PL-421`.

## Claim

The quantitative escape left by `PL-421` fails for the most direct **uncentered raw residue covariance** produced by short von-Mangoldt windows. Fix

\[
\frac16<\theta\le\frac12,
\qquad h=X^\theta,
\]

and, for each reduced residue `a mod 5`, define on `y in [X,2X]`

\[
P_a(y;h)
:=
\sum_{\substack{y<n\le y+h\\n\equiv a\pmod 5}}\Lambda(n).
\tag{1}
\]

Let

\[
S_X=(\langle P_a,P_b\rangle_{L^2[X,2X]})_{a,b\in(\mathbb Z/5\mathbb Z)^\times}
\tag{2}
\]

and normalize it to the correlation matrix

\[
C_X
:=
D_X^{-1/2}S_XD_X^{-1/2},
\qquad
D_X:=\operatorname{Diag}(S_X).
\tag{3}
\]

Then

\[
\boxed{
C_X\longrightarrow \mathbf 1\mathbf 1^*
\quad\text{in operator norm as }X\to\infty,
}
\tag{4}
\]

and therefore

\[
\boxed{
\lambda_{\min}(C_X)\longrightarrow0.
}
\tag{5}
\]

In particular, for all sufficiently large `X`,

\[
\lambda_{\min}(C_X)<\frac14.
\tag{6}
\]

But `PL-421` proves that exact positive deletion of the ordinary `p=5` Hardy--Littlewood local factor from a raw residue covariance requires precisely

\[
\lambda_{\min}(C_X)\ge\frac14.
\tag{7}
\]

Hence this canonical uncentered source Gram eventually lies **outside** the positive image cone of the `p=5` dephasing map. The obstruction is not weak decorrelation: the raw residue vectors become asymptotically collinear because their common mean `h/4` dominates their fluctuations.

This is a decisive negative only for the uncentered raw covariance in polynomial windows covered below. It does not rule out centered/model-subtracted covariance, zero-side matrices, nonlocal representations, or a different positive lift.

## 1. Short arithmetic progressions force a common leading vector

For the prime-only weighted count write

\[
P_a^{\rm pr}(y;h)
:=
\sum_{\substack{y<p\le y+h\\p\equiv a\pmod5}}\log p.
\tag{8}
\]

Koukoulopoulos defines

\[
E(y,h;q)
=
\max_{(a,q)=1}
\left|
\sum_{\substack{y<p\le y+h\\p\equiv a\pmod q}}\log p
-
\frac{h}{\varphi(q)}
\right|
\tag{9}
\]

and proves an averaged short-AP estimate strong enough for fixed `q=5`: if `h=X^theta`, `theta>=1/6+2 epsilon`, and `Q^2<=h/X^(alpha+epsilon)`, then for every fixed `A` the integral over `y` of the summed error for `q<=Q` is `O_A(Xh/(log X)^A)`. In the range `theta<=1/2` used here his parameter is `alpha=1/6`.

Fix any `theta in (1/6,1/2]` and choose

\[
0<\varepsilon<\frac12\left(\theta-\frac16\right).
\tag{10}
\]

With the fixed choice `Q=5`, the condition

\[
25\le X^{\theta-1/6-\varepsilon}
\tag{11}
\]

holds for all sufficiently large `X`. Consequently, for every `A>=1`, uniformly in the four reduced residues,

\[
\int_X^{2X}
\left|P_a^{\rm pr}(y;h)-\frac h4\right|dy
\ll_{A,\theta}
\frac{Xh}{(\log X)^A}.
\tag{12}
\]

A crude pointwise estimate gives

\[
\left|P_a^{\rm pr}(y;h)-\frac h4\right|
\ll h\log X.
\tag{13}
\]

Combining `L^1` and `L^infinity`,

\[
\begin{aligned}
\left\|P_a^{\rm pr}-\frac h4\right\|_2^2
&\le
\left\|P_a^{\rm pr}-\frac h4\right\|_\infty
\left\|P_a^{\rm pr}-\frac h4\right\|_1\\
&\ll_{A,\theta}
\frac{Xh^2}{(\log X)^{A-1}}
=o(Xh^2),
\end{aligned}
\tag{14}
\]

on taking, for example, `A>2`.

Thus every reduced residue class has the same leading `L^2` vector:

\[
P_a^{\rm pr}(y;h)
=
\frac h4+o_{L^2}(h\sqrt X).
\tag{15}
\]

The input here is ordinary prime equidistribution in almost all short intervals, not RH, GRH, or a continued Euler product.

## 2. Prime powers do not change the rank-one limit

Equation (1) uses `Lambda`, whereas Koukoulopoulos's error term is written for primes weighted by `log p`. Let

\[
Q_a(y;h)
:=
\sum_{\substack{y<p^k\le y+h\\k\ge2\\p^k\equiv a\pmod5}}
\log p.
\tag{16}
\]

Then `P_a=P_a^pr+Q_a`. The total prime-power weight up to `3X` satisfies the elementary bound

\[
W(X)
:=
\sum_{\substack{p^k\le3X\\k\ge2}}\log p
\ll \sqrt X\log X.
\tag{17}
\]

Therefore, on `y in [X,2X]`,

\[
\|Q_a\|_\infty\ll \sqrt X\log X,
\tag{18}
\]

while Fubini/counting the set of window origins containing a fixed prime power gives

\[
\|Q_a\|_1\le hW(X)\ll h\sqrt X\log X.
\tag{19}
\]

Hence

\[
\|Q_a\|_2^2
\le
\|Q_a\|_\infty\|Q_a\|_1
\ll hX(\log X)^2
=o(Xh^2),
\tag{20}
\]

because `h=X^theta` with fixed `theta>0`. Combining (15) and (20),

\[
\boxed{
P_a(y;h)
=
\frac h4+o_{L^2}(h\sqrt X)
}
\tag{21}
\]

uniformly for `a=1,2,3,4 mod 5`.

## 3. The normalized raw Gram converges to rank one

Let

\[
m_X(y):=\frac h4,
\qquad
r_a:=P_a-m_X.
\tag{22}
\]

Equation (21) says

\[
\|r_a\|_2=o(h\sqrt X),
\qquad
\|m_X\|_2=\frac14h\sqrt X.
\tag{23}
\]

Therefore

\[
\|P_a\|_2
=\frac14h\sqrt X\,(1+o(1)).
\tag{24}
\]

Writing

\[
v_a:=\frac{P_a}{\|P_a\|_2},
\qquad
u_X:=X^{-1/2}\mathbf 1_{[X,2X]},
\tag{25}
\]

we get

\[
\|v_a-\nu_X\|_2\to0
\tag{26}
\]

for each of the four residues. Thus

\[
(C_X)_{ab}
=\langle v_a,v_b\rangle
\to1
\qquad(a,b\in(\mathbb Z/5\mathbb Z)^\times).
\tag{27}
\]

Since the matrix size is fixed,

\[
\|C_X-\mathbf1\mathbf1^*\|_{\rm op}\to0,
\tag{28}
\]

proving (4). Equivalently, the four eigenvalues converge to

\[
(4,0,0,0).
\tag{29}
\]

A one-line Rayleigh witness makes the loss of the lower frame bound explicit. For any two distinct residues `a,b`, set

\[
z=\frac{e_a-e_b}{\sqrt2}.
\tag{30}
\]

Then

\[
z^*C_Xz
=1-\Re(C_X)_{ab}
\longrightarrow0.
\tag{31}
\]

Because `C_X>=0`, this already implies `lambda_min(C_X)->0`.

## 4. Consequence for the `PL-421` positive image cone

`PL-421` identifies normalized insertion of the odd-prime local factor as

\[
\Psi_p(R)
=
\frac{p-2}{p-1}R
+
\frac1{p-1}\operatorname{Diag}(R),
\tag{32}
\]

with exact positive image criterion

\[
S\in\Psi_p(M_{p-1}^+)
\iff
\lambda_{\min}(C_S)\ge\frac1{p-1}.
\tag{33}
\]

At `p=5` the floor is `1/4`. Equations (5)--(6) therefore prove that the raw short-window residue Gram (2) eventually fails the exact local deletion gate:

\[
\boxed{
S_X\notin\Psi_5(M_4^+)
\quad\text{for all sufficiently large }X.
}
\tag{34}
\]

The geometry is the opposite of the decorrelation target proposed after `PL-421`. Before centering, the dominant deterministic mean makes the four residue vectors increasingly parallel, so the lower Riesz bound collapses rather than approaching the identity-Gram regime.

This matters directly to the current source-transfer architecture. A positive representation cannot rescue exact `p=5` deletion merely by keeping the full **raw** residue covariance instead of its diagonal energies: the canonical raw matrix occupies the wrong side of the exact positive image boundary asymptotically.

The only immediate way to remove this obstruction is to remove or neutralize the common rank-one mode before applying the criterion. But that is no longer the raw covariance problem: it returns the line to the centered/model-subtracted residual gate isolated in `PL-418`, where positivity is not automatic.

## 5. Prior-art and novelty audit

The analytic input is classical prior art:

- **Dimitris Koukoulopoulos**, “Primes in short arithmetic progressions,” *International Journal of Number Theory* **11**(5) (2015), 1499--1521, DOI `10.1142/S1793042115400035`, arXiv:1405.6592. Theorem 1.2 supplies the averaged short-AP equidistribution used in (12), with the `1/6` threshold in the range `theta<=1/2`.
- Classical and later work on primes in short arithmetic progressions studies variances and mean-square errors of the residue counts. No novelty is claimed here for equidistribution, the passage from `L^1` plus a crude supremum to `L^2`, or the observation that uncentered variables with a dominant common mean are nearly collinear.

Targeted searches around short-interval residue covariance, Gram spectra, and arithmetic-progression variance did not locate the line-specific consequence (34). The durable contribution is therefore narrow and derived: combining the established short-AP theorem with the exact `PL-421` dephasing image cone **falsifies the canonical uncentered raw-residue realization of the required `1/4` lower frame bound**.

This is not a new theorem about the distribution of primes and is not an RH result.

## 6. Adversarial audit and scope limits

1. **The theorem is averaged in the window origin.** The covariance (2) is also an average over origins `y in [X,2X]`, so this is the correct mode of convergence for the proposed raw Gram. No pointwise-in-`y` equidistribution is inferred.

2. **The `L^2` upgrade is legitimate but deliberately crude.** It uses only the theorem's arbitrarily strong logarithmic `L^1` saving and the trivial `O(h log X)` supremum. No unproved variance asymptotic is inserted.

3. **Prime powers are explicitly controlled.** Their `L^2` mass is `o(Xh^2)` for every fixed polynomial window `h=X^theta`; the passage from prime sums to `Lambda` therefore does not create the rank-one limit.

4. **The range is not extrapolated below `1/6`.** The conclusion proved here is for every fixed `theta in (1/6,1/2]`. It includes the `theta=2/5` polynomial window relevant to the current source construction, but says nothing about logarithmic or sub-`X^(1/6)` windows.

5. **Centering can change the spectrum completely.** The finding does not claim that the centered vectors `P_a-h/4` have collapsing Gram spectrum. Their covariance is precisely where short-interval variance and Dirichlet-character information live. That is a different object and remains open for the current positivity program.

6. **The positive image criterion is representation-specific.** Equation (34) falsifies the canonical raw covariance route through `Psi_5`; it does not exclude another positive representation of the local repair.

7. **No analytic continuation or zero localization is used.** The argument is entirely on the prime/source side. It cannot by itself imply anything about zeros in the critical strip.

### Decisive audit test

The claim can be falsified only by breaking one of its exact bridges: either the fixed-modulus short-AP estimate does not imply (12) in the stated `theta` range, the prime-power estimate (20) fails, or the matrix tested in the source-transfer construction is not the uncentered Gram (2). If (1)--(3) are the intended raw residue covariance, the spectral collapse follows deterministically from (21).

## Consequence for the line

The `PL-421` question “can the actual raw arithmetic residue matrix satisfy the `1/4` dephasing floor?” has a negative answer for the canonical polynomial short-window Gram:

\[
\boxed{
\lambda_{\min}(C_X)\to0<\frac14.
}
\tag{35}
\]

So the next viable positivity question is no longer raw cross-residue decorrelation. It must either **center/subtract the common source mode and prove positivity for the residual matrix**, or change the representation so exact local-factor removal is not inverse dephasing on this uncentered Gram. That returns the load-bearing problem to the residual/model-subtracted order issue already isolated by `PL-418`, rather than supplying a shortcut around it.
