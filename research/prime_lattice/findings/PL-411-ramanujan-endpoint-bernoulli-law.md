# PL-411 — The full cubic Ramanujan endpoint is an independent-prime probability law whose continued Mellin transform carries the zeta-zero divisor

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + STRUCTURAL-REFACTORIZATION + ENDPOINT-LOCALIZATION`.

**Parent findings:** `PL-404`, `PL-405`, `PL-408`, `PL-410`.

## Claim

The full, untruncated Ramanujan source used in `PL-404` admits an exact reorganization that is stronger than the moving-denominator language of `PL-408`--`PL-410`. After the divisor Möbius transform in the exact Poisson formula is summed over **all** Ramanujan denominators, every odd divisor channel cancels and the surviving even channels form a positive probability measure on the odd square-free prime-exponent lattice.

Let

\[
K_\eta(x)=|x|e^{-\eta |x|^3}\sin\!\left(\frac\pi6|x|^3\right),
\qquad
P_\eta(x):=\sum_{k\in\mathbb Z}\widehat K_\eta(kx),
\tag{1}
\]

and let `A_eta^[2](H)` be the full singular-series statistic of `PL-404`. Define, for odd square-free `m`,

\[
\boxed{
\nu(m)
:=C_2\prod_{p\mid m}\frac1{p(p-2)},
}
\qquad
C_2:=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right),
\tag{2}
\]

and put `nu(m)=0` otherwise. Then

\[
\boxed{
2A_\eta^{[2]}(H)
=\sum_{m\ge1}\nu(m)
P_\eta\!\left(\frac{H}{2m}\right).
}
\tag{3}
\]

Moreover,

\[
\boxed{\sum_{m\ge1}\nu(m)=1.}
\tag{4}
\]

Thus the full model source is exactly an expectation

\[
\boxed{
2A_\eta^{[2]}(H)
=\mathbb E\left[
P_\eta\!\left(\frac{H}{2M}\right)
\right]
}
\tag{5}
\]

for a canonical random odd square-free integer `M`.

The law is not merely multiplicative: its prime coordinates are independent. If

\[
M=\prod_{p>2}p^{X_p},
\qquad X_p\in\{0,1\},
\]

then the `X_p` are independent Bernoulli variables with

\[
\boxed{
\mathbb P(X_p=1)=\frac1{(p-1)^2},
\qquad
\mathbb P(X_p=0)=1-\frac1{(p-1)^2}.
}
\tag{6}
\]

Since `sum_p (p-1)^(-2)<infinity`, only finitely many coordinates are occupied almost surely, so this is literally a probability measure on the finite-support square-free exponent lattice.

Its Mellin transform

\[
N(s):=\mathbb E(M^{-s})
=\sum_{m\ge1}\frac{\nu(m)}{m^s}
\tag{7}
\]

converges absolutely for `Re(s)>-1` and satisfies

\[
\boxed{
N(s)
=rac{C_2}{1+2^{-s-2}}
\frac{\zeta(s+2)}{\zeta(2s+4)}
\mathcal G(s+1),
}
\tag{8}
\]

where

\[
\mathcal G(u)
=\prod_{p>2}\left(
1+\frac{2}{(p-2)(p^{u+1}+1)}
\right).
\tag{9}
\]

The product in (9) is absolutely convergent in the range needed below, and (8) supplies meromorphic continuation to `Re(s)>-2` subject to the displayed zeta divisor and the elementary local factors.

If

\[
F(u):=\sum_{k\ge1}\frac{\mathfrak S(k)}{k^u}
\tag{10}
\]

is the classical singular-series Dirichlet series of Goldston--Suriajaya, then their factorization gives the exact identity

\[
\boxed{
N(s)=2^s\frac{F(s+1)}{\zeta(s+1)}.
}
\tag{11}
\]

Hence the probability law is not a new analytic continuation of the singular series: it is a precise positive factor extracted from the classical continuation. Its usefulness for this line is that it places the entire moving square-free endpoint in one fixed prime-coordinate probability space.

Two consequences are immediate and load-bearing.

First,

\[
\boxed{
\operatorname*{Res}_{s=-1}N(s)=\frac12,
}
\tag{12}
\]

and therefore

\[
\boxed{
\mathbb P(M>X)\sim\frac1{2X}.
}
\tag{13}
\]

Second, the nontrivial-zero divisor in (8) occurs at

\[
2s+4=\rho,
\qquad
\boxed{s=\frac\rho2-2}.
\tag{14}
\]

Under RH these singularities lie on

\[
\boxed{\Re s=-\frac74,}
\tag{15}
\]

which is exactly the zero-sensitive exponent already obtained in `PL-404`. This does **not** by itself prove an RH criterion for `N`: accidental numerator/local-factor cancellation must not be silently excluded. What is exact is that the same zeta-zero denominator which drives the Goldston--Suriajaya explicit formula is now located wholly in the continued Mellin transform of a positive square-free prime-lattice law.

Finally, this probability law explains why the finite cusp-jet renormalization of `PL-410` cannot simply be globalized term by term. One has

\[
\boxed{
\mathbb E(M^a)<\infty\iff a<1.
}
\tag{16}
\]

The first cubic cusp term would require the eighth moment, and every cusp moment `8,14,20,...` is infinite. Fixed fractional interiors admit finite counterterms because the corresponding moments are truncated; the true endpoint is exactly where this moment expansion ceases to be integrable.

## 1. Reindexing the exact Ramanujan--Poisson formula

`PL-408` proved, for each Ramanujan denominator `q`,

\[
B_{q,\eta}(H)
=\sum_{r\mid q}\mu(q/r)
P_\eta(H/r),
\tag{17}
\]

with

\[
2A_\eta^{[2]}(H)
=\sum_{q\ge1}
\frac{\mu(q)^2}{\phi(q)^2}B_{q,\eta}(H).
\tag{18}
\]

The reindexing below is absolutely legitimate. The Poisson sum `P_eta(x)` is bounded on `(0,infinity)`: as `x->infinity` it tends to `widehat K_eta(0)`, while Poisson summation gives

\[
P_\eta(x)=x^{-1}\sum_{n\in\mathbb Z}K_\eta(n/x),
\tag{19}
\]

which tends rapidly to zero as `x->0` because `K_eta(0)=0` and `K_eta` has exponential cubic decay. Also

\[
\sum_{q\ge1}\frac{\mu(q)^2\tau(q)}{\phi(q)^2}<\infty.
\]

Substitute (17) into (18) and group by `r`. Since `mu(q)^2` forces `q` square-free, write `q=rd` with `(r,d)=1`. The coefficient of `P_eta(H/r)` is

\[
C(r)
=\frac{\mu(r)^2}{\phi(r)^2}
\sum_{\substack{d\ge1\\(d,r)=1}}
\frac{\mu(d)\mu(d)^2}{\phi(d)^2}
=\frac{\mu(r)^2}{\phi(r)^2}
\prod_{p\nmid r}
\left(1-\frac1{(p-1)^2}\right).
\tag{20}
\]

If `r` is odd, the product contains the `p=2` factor

\[
1-\frac1{(2-1)^2}=0,
\]

so

\[
\boxed{C(r)=0\qquad(r\text{ odd}).}
\tag{21}
\]

If `r=2m` with `m` odd and square-free, then `phi(2m)=phi(m)` and

\[
C(2m)
=C_2\prod_{p\mid m}
\frac{1}{(p-1)^2}
\left(1-\frac1{(p-1)^2}\right)^{-1}
=C_2\prod_{p\mid m}\frac1{p(p-2)}.
\tag{22}
\]

This is exactly `nu(m)` and proves (3).

## 2. The coefficient is exactly a product Bernoulli probability

For every odd prime `p`, put

\[
q_p:=\frac1{(p-1)^2}.
\]

Then

\[
1-q_p
=\frac{p(p-2)}{(p-1)^2},
\qquad
\frac{q_p}{1-q_p}
=\frac1{p(p-2)}.
\tag{23}
\]

Since

\[
C_2=\prod_{p>2}(1-q_p),
\]

the product Bernoulli mass of a finite support `S` is

\[
\prod_{p\in S}q_p
\prod_{p\notin S}(1-q_p)
=C_2\prod_{p\in S}\frac1{p(p-2)}.
\tag{24}
\]

Identifying `m=prod_(p in S)p` gives (2), (4), and (6). Equivalently,

\[
C_2\prod_{p>2}\left(1+\frac1{p(p-2)}\right)=1.
\tag{25}
\]

This also makes the moment threshold transparent. For real `a`,

\[
\mathbb E(M^a)
=\prod_{p>2}\left(1-q_p+q_pp^a\right).
\tag{26}
\]

The logarithm converges exactly when

\[
\sum_p q_pp^a
\asymp\sum_p p^{a-2}
\]

converges, namely for `a<1`. This proves (16).

## 3. Mellin continuation and exact relation to the classical singular-series Dirichlet series

From (2), initially for `Re(s)>-1`,

\[
N(s)
=C_2\prod_{p>2}
\left(1+\frac{p^{-s}}{p(p-2)}\right)
=C_2\prod_{p>2}
\left(1+\frac1{(p-2)p^{s+1}}\right).
\tag{27}
\]

Use

\[
\frac{\zeta(s+2)}{\zeta(2s+4)}
=\prod_p(1+p^{-s-2}).
\tag{28}
\]

For `p>2`, the quotient between the local factor in (27) and `1+p^{-s-2}` is

\[
\frac{1+((p-2)p^{s+1})^{-1}}
     {1+p^{-s-2}}
=1+\frac{2}{(p-2)(p^{s+2}+1)},
\tag{29}
\]

which is the `p`-factor of `mathcal G(s+1)`. Removing the `p=2` factor in (28) gives (8).

Goldston--Suriajaya prove, for their singular-series Dirichlet series,

\[
F(u)
=\frac{4C_2}{2^{u+1}+1}
\frac{\zeta(u)\zeta(u+1)}{\zeta(2u+2)}
\mathcal G(u),
\tag{30}
\]

with meromorphic continuation beyond the original half-plane of convergence. Replacing `u` by `s+1` and comparing with (8) gives (11) exactly.

The source is:

D. A. Goldston and A. I. Suriajaya, “A singular series average and the zeros of the Riemann zeta-function,” *Acta Arithmetica* **200** (2021), 71--90, DOI `10.4064/aa200821-24-2`, arXiv:`2007.16099`. Their equation (2.2) is (30), and their explicit formula supplies the classical zero-dependent continuation background. No novelty is claimed for that analytic factorization.

## 4. The heavy tail has exact leading constant `1/2`

At `s=-1`, only `zeta(s+2)` has the leading pole relevant here. From (8),

\[
\operatorname*{Res}_{s=-1}N(s)
=rac{C_2\mathcal G(0)}{(1+2^{-1})\zeta(2)}.
\tag{31}
\]

For each `p>2`,

\[
\left(1-\frac1{(p-1)^2}\right)
\left(1+\frac{2}{(p-2)(p+1)}\right)
=\frac1{1-p^{-2}}.
\tag{32}
\]

Hence

\[
C_2\mathcal G(0)
=\prod_{p>2}(1-p^{-2})^{-1}
=\frac34\zeta(2),
\]

and (12) follows.

For a standard Tauberian extraction, define

\[
D(z):=N(z-2)
=\sum_{m\ge1}\frac{m^2\nu(m)}{m^z}.
\tag{33}
\]

The coefficients are nonnegative, `D` converges for `Re(z)>1`, and (8) shows that on `Re(z)>=1` it has only the simple pole at `z=1`, with residue `1/2`. Wiener--Ikehara therefore gives

\[
\sum_{m\le X}m^2\nu(m)\sim\frac X2.
\tag{34}
\]

Partial summation then yields

\[
\sum_{m>X}\nu(m)
=-\frac1{X^2}\sum_{m\le X}m^2\nu(m)
+2\int_X^\infty
\frac{1}{t^3}\left(\sum_{m\le t}m^2\nu(m)\right)dt
\sim\frac1{2X},
\tag{35}
\]

proving (13).

Thus the true `m asymp H` endpoint is not an artifact of the cubic regulator: it is the natural scale of a fixed probability law with tail index one.

## 5. The archimedean filter and the arithmetic law factor exactly

Set

\[
\Phi_\eta(y)
:=P_\eta\!\left(\frac1{2y}\right).
\tag{36}
\]

Poisson summation and `K_eta(0)=0` give

\[
\Phi_\eta(y)
=4y\sum_{n\ge1}K_\eta(2ny).
\tag{37}
\]

For `Re(s)>0`, its Mellin transform is therefore

\[
\begin{aligned}
\mathcal M\Phi_\eta(s)
&=4\sum_{n\ge1}
\int_0^\infty y^sK_\eta(2ny)\,dy\\
&=2^{1-s}\zeta(s+1)\widehat w_\eta^{[2]}(s+1),
\end{aligned}
\tag{38}
\]

where `widehat w_eta^[2]` is the Mellin transform fixed in `PL-404`.

Combining (11) and (38) gives the exact cancellation

\[
\boxed{
N(s)\,\mathcal M\Phi_\eta(s)
=2F(s+1)\widehat w_\eta^{[2]}(s+1).
}
\tag{39}
\]

The factor `zeta(s+1)` introduced by the Poisson/archimedean comb cancels the `1/zeta(s+1)` separating `N` from the classical singular-series Dirichlet series. The critical zero-sensitive denominator `1/zeta(2s+4)` is therefore carried by the continued Mellin transform of the square-free probability law, while the chosen cubic kernel supplies only the archimedean Mellin multiplier which decides how those singularities are read out.

As a consistency check, at `s=-1`,

\[
\mathcal M\Phi_\eta(-1)
=4\zeta(0)\widehat w_\eta^{[2]}(0)
=-2W_{0,\eta}.
\tag{40}
\]

Together with `Res_(s=-1)N(s)=1/2`, the residue of the product in (39) is `-W_(0,eta)`. Since (3) is `2A`, this recovers exactly the deterministic correction

\[
-\frac{W_{0,\eta}}{2H}
\]

in `PL-404`.

Likewise the denominator in (8) places the nontrivial-zero singularities at (14). Under RH their real part is `-7/4`, matching the `PL-404` error scale without introducing a new affine “explanation” of the critical line.

## 6. Relation to `PL-410`: why the endpoint resists finite cusp moments

For small `y`, equivalently large `H/(2m)`, the high-frequency expansion of `PL-410` gives formally

\[
\Phi_\eta(y)
=\widehat K_\eta(0)
+\sum_{j\ge1}\beta_{j,\eta}(2y)^{6j+2}+\cdots.
\tag{41}
\]

A global term-by-term average of (41) against `nu` would require

\[
\mathbb E(M^{6j+2}),
\]

but every such moment is infinite by (16). Therefore the failure of the finite cusp-jet hierarchy at `m/H=Theta(1)` is not merely that successive powers become numerically comparable. The probability-law representation gives a sharper obstruction:

\[
\boxed{
\text{the global cusp expansion asks for moments which do not exist.}
}
\tag{42}
\]

This is fully compatible with `PL-410`. On a fixed fractional interior the effective moments are truncated and finitely many exact cusp counterterms push the regulator aliases below `H^-7/4`; once the full probability tail is restored, those same polynomial moments diverge and the endpoint must be treated nonperturbatively.

## 7. Novelty and adversarial audit

The analytic singular-series factorization and its zeta-zero explicit formula are classical prior art. Goldston--Suriajaya equation (2.2) already contains the factors `zeta(u)zeta(u+1)/zeta(2u+2)` and `mathcal G(u)`, and their theorems already identify the `x^(m-3/4)` zero scale under RH. Equation (11) is therefore an algebraic refactorization of established material, not a new continuation theorem.

The exact ingredients used to derive the probability law are also elementary once `PL-408` is available: absolute reindexing, the `p=2` Möbius factor, the twin-prime constant, and an Euler product. Targeted searches around the prime-pair singular series, its Ramanujan tail, the coefficient `1/[p(p-2)]`, and the Goldston--Suriajaya factorization did not locate this exact **independent-Bernoulli endpoint representation** as a stated mechanism. The durable delta claimed here is consequently narrow: (3)--(6), (11), (13), and (39)--(42) give a line-specific structural factorization of the already-established `PL-404`--`PL-410` model endpoint. No claim is made that the underlying number-theory factors are new.

Several controls prevent overinterpretation.

1. **This is still the singular-series model, not actual prime data.** The source-replacement/prime-variance obstruction isolated in `PL-405`--`PL-407` is untouched.

2. **The affine location `Re(s)=-7/4` does not force RH.** It is the image of `Re(rho)=1/2` under `s=rho/2-2`. Equation (8) reorganizes the zero divisor but supplies no positivity theorem locating it.

3. **Do not infer an unconditional pole for every individual zero from (8).** Numerator or local-factor cancellation at a particular zero location has not been excluded here. The exact zero-dependent observable remains the full product (39), whose classical counterpart is the Goldston--Suriajaya explicit formula used by `PL-404`.

4. **The probability structure uses the exact prime-pair local factors.** Generic Helson phases or arbitrary multiplicative-frequency systems do not preserve the positive Bernoulli weights in (6). Conversely, this observation alone is not a proof that no generalized-prime system can reproduce an analogous law; it is a rational-prime-specific structure to test, not a uniqueness theorem.

5. **The moment obstruction is genuinely endpoint-specific.** It does not invalidate the finite exact counterterms of `PL-410`, which are defined before the full endpoint reindexing and use truncated finite sums rather than nonexistent global moments.

## Consequence for the line

The surviving model-side object after `PL-410` can now be stated without an `H`-dependent collection of Ramanujan denominators. It is the fixed random exponent vector

\[
X=(X_p)_{p>2},
\qquad
X_p\sim\operatorname{Bernoulli}((p-1)^{-2})
\quad\text{independently},
\tag{43}
\]

with random energy

\[
\log M=\sum_{p>2}X_p\log p.
\tag{44}
\]

The cubic source statistic is an exact scale-dependent readout of this one law through `P_eta(H/(2M))`. Its tail is `1/(2X)`, its positive moments hit a hard wall at order one, and its continued Mellin transform contains the classical `1/zeta(2s+4)` zero divisor. This makes the next model-side question concrete: analyze the endpoint readout or its prime-data replacement **as a heavy-tail prime-coordinate expectation**, rather than trying to extend the finite cusp expansion through a region where the required moments provably diverge.
