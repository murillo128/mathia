# PL-367 — Pole-neutral `ell^p` divisor filters manufacture every convergence wall in `(0,1)`, so the Hilbert `1/2` wall is sharp but non-arithmetic

**Evidence:** `EXACT-DERIVED + CLASSICAL-HOLDER/ABEL-CONTROL + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-366`.

**Status:** `THE-ELL2-SQUARE-ROOT-WALL-SITS-INSIDE-A-SHARP-BANACH-COEFFICIENT-LADDER-WHOSE-EXPONENT-CAN-BE-CHOSEN-ARBITRARILY-IN-(0,1)-WITHOUT-USING-ZETA-ZEROS`.

## Precise claim

`PL-366` shows that a pole-neutral coefficient filter `c in ell^2` automatically gives

\[
\sum_{n\le x}(c*\mathbf 1)(n)=O(\sqrt x),
\]

so ordinary convergence reaches `Re(s)>1/2` for a generic Hilbert-space reason. The missing sharpness question can be answered, and the answer is stronger than the Hilbert case.

Fix

\[
1<p<\infty,
\qquad
q=\frac{p}{p-1},
\qquad
\theta=\frac1q=1-\frac1p.
\tag{PL367-1}
\]

Let

\[
c=(c_d)_{d\ge1}\in\ell^p(\mathbb N),
\qquad
b=c*\mathbf 1,
\qquad
b_n=\sum_{d\mid n}c_d,
\tag{PL367-2}
\]

and

\[
C(s)=\sum_{d\ge1}c_dd^{-s}.
\tag{PL367-3}
\]

Because `(1/d) in ell^q`, the pole-neutrality functional `C(1)` is absolutely defined. If

\[
C(1)=\sum_{d\ge1}\frac{c_d}{d}=0,
\tag{PL367-4}
\]

then there is a constant `K_p` depending only on `p` such that

\[
\boxed{
S_b(x):=\sum_{n\le x}b_n
=O_p\!\left(x^\theta\|c\|_p\right).
}
\tag{PL367-5}
\]

Consequently `C(s)` is absolutely holomorphic and the ordinary Dirichlet series

\[
B(s)=\sum_{n\ge1}b_nn^{-s}
\tag{PL367-6}
\]

converges locally uniformly throughout

\[
\operatorname{Re}s>\theta.
\tag{PL367-7}
\]

For `Re(s)>1`, absolute Dirichlet multiplication gives `B(s)=zeta(s)C(s)`. Since (PL367-4) removes the simple pole of zeta at `1`, identity theorem then gives

\[
\boxed{
B(s)=\zeta(s)C(s)
\quad\text{for }\operatorname{Re}s>\theta,
}
\tag{PL367-8}
\]

where zeta on the right is its known meromorphic continuation, not a formally continued Euler product.

The exponent is sharp at the level of the coefficient class. For every `1<p<infinity` there exists a pole-neutral

\[
c\in\ell^p\setminus\bigcup_{1\le r<p}\ell^r
\tag{PL367-9}
\]

for which the output has exact ordinary abscissa

\[
\boxed{\sigma_c(B)=\theta=1-1/p.}
\tag{PL367-10}
\]

Thus every prescribed wall `theta in (0,1)` occurs by choosing

\[
p=\frac1{1-\theta}.
\tag{PL367-11}
\]

In particular, `p=2` gives `theta=1/2`, and there are explicit `ell^2` filters for which the `1/2` abscissa is genuinely sharp despite there being no mechanism that constrains the zeta zero divisor. The `1/2` in `PL-366` is therefore not merely an upper-bound artifact: it is a **sharp ambient Hilbert exponent**, which makes it an even stronger negative control for RH interpretations.

## 1. The full `ell^p` residual estimate

The finite rearrangement used in `PL-365` and `PL-366` is independent of the coefficient norm:

\[
S_b(x)
=\sum_{d\le x}c_d\left\lfloor\frac{x}{d}\right\rfloor.
\tag{PL367-12}
\]

Under (PL367-4), subtract the cancelled main term over the full sequence and define

\[
r_x(d)=
\begin{cases}
\lfloor x/d\rfloor-x/d,&d\le x,\\
-x/d,&d>x.
\end{cases}
\tag{PL367-13}
\]

Then

\[
S_b(x)=\sum_{d\ge1}c_dr_x(d).
\tag{PL367-14}
\]

For `q<infinity`,

\[
\begin{aligned}
\|r_x\|_q^q
&\le \sum_{d\le x}1
+x^q\sum_{d>x}d^{-q}\\
&\le x+1+\frac{x}{q-1}.
\end{aligned}
\tag{PL367-15}
\]

Hence

\[
\|r_x\|_q\le K_p x^{1/q}
\tag{PL367-16}
\]

for `x>=1`, and Holder duality gives (PL367-5). No multiplicativity, prime distribution, Mobius cancellation, functional equation, or zero information enters this estimate. The exponent is exactly the growth of the floor-function residual in the dual coefficient norm.

The endpoint `p=1`, `q=infinity`, is `PL-365`: `||r_x||_infinity<=1` gives an `O(1)` remainder. The opposite endpoint `p=infinity` is deliberately excluded: `(1/d)` is not in `ell^1`, so `C(1)` is not a continuous functional on a generic `ell^infinity` coefficient class.

## 2. The same exponent controls the analytic half-plane

For `sigma>theta=1/q`, Holder gives

\[
\sum_{d\ge1}|c_d|d^{-\sigma}
\le
\|c\|_p
\left(\sum_{d\ge1}d^{-q\sigma}\right)^{1/q}
<\infty.
\tag{PL367-17}
\]

Thus `C` is absolutely convergent and holomorphic on `Re(s)>theta`. Separately, (PL367-5) and Abel summation give local uniform convergence of `B` on the same half-plane. These are coefficient estimates, not analytic continuation assumptions.

Only on `Re(s)>1` do we first multiply the two absolutely convergent Dirichlet series:

\[
\sum_{n\ge1}\frac{|b_n|}{n^\sigma}
\le
\zeta(\sigma)
\sum_{d\ge1}\frac{|c_d|}{d^\sigma}
<\infty,
\qquad \sigma>1.
\tag{PL367-18}
\]

This proves `B=zeta C` there. On `Re(s)>theta`, the independently convergent series `B` is holomorphic, while `zeta C` is holomorphic after the removable singularity at `s=1` is filled using `C(1)=0`. Agreement on `Re(s)>1` then proves (PL367-8) by the identity theorem.

A hypothetical zeta zero `rho` with `Re(rho)>theta` is simply inherited by `B(rho)=0`. Nothing in the construction restricts `Re(rho)`.

## 3. Sharp examples for every Banach exponent

Fix `p` and choose a real number

\[
\frac1p<a<1.
\tag{PL367-19}
\]

For `d>=2`, set

\[
c_d=d^{-1/p}(\log d)^{-a},
\tag{PL367-20}
\]

and choose

\[
c_1=-\sum_{d\ge2}\frac{c_d}{d}.
\tag{PL367-21}
\]

The defining series for `c_1` converges. Moreover,

\[
\sum_{d\ge2}|c_d|^p
=
\sum_{d\ge2}\frac1{d(\log d)^{ap}}
<\infty
\tag{PL367-22}
\]

because `ap>1`. For every `r<p`, however,

\[
\sum_{d\ge2}|c_d|^r
=
\sum_{d\ge2}d^{-r/p}(\log d)^{-ar}
=\infty,
\tag{PL367-23}
\]

because `r/p<1`. Thus (PL367-9) holds and the coefficient topology is not an accidental consequence of a stronger `ell^r` assumption.

Now restrict to integer `N`. The `d=1` residual vanishes, and every `c_d` for `d>=2` is positive. Equation (PL367-14) therefore has only non-positive terms:

\[
S_b(N)
\le
-N\sum_{d>N}\frac{c_d}{d}<0.
\tag{PL367-24}
\]

Keeping only `N<d<=2N` gives the explicit lower bound

\[
\begin{aligned}
|S_b(N)|
&\ge
N\sum_{N<d\le2N}
 d^{-1-1/p}(\log d)^{-a}\\
&\ge
2^{-1-1/p}
N^{1-1/p}(\log(2N))^{-a}.
\end{aligned}
\tag{PL367-25}
\]

Together with (PL367-5),

\[
N^\theta(\log N)^{-a}\ll_p |S_b(N)|\ll_p N^\theta.
\tag{PL367-26}
\]

This already forces the exact ordinary abscissa. Indeed, (PL367-5) gives `sigma_c(B)<=theta`. Conversely, suppose the ordinary series converged at a real `sigma<theta`. By the half-plane property of Dirichlet-series convergence, it is enough to consider `0<=sigma<theta`. Put

\[
A_N=\sum_{n\le N}b_nn^{-\sigma}.
\tag{PL367-27}
\]

Convergence makes `A_N` bounded, and discrete Abel summation yields

\[
S_b(N)
=A_NN^\sigma
-\sum_{n<N}A_n\big((n+1)^\sigma-n^\sigma\big)
=O(N^\sigma)
\tag{PL367-28}
\]

(with bounded `S_b` when `sigma=0`). This contradicts the lower bound (PL367-25) because `sigma<theta`. Hence `sigma_c(B)>=theta`, proving (PL367-10).

The choice `a<1` also makes the coefficient Dirichlet series `C` itself have absolute-convergence boundary `theta`: at `sigma=theta` its positive tail is `sum 1/(d (log d)^a)`, which diverges. This is not needed for (PL367-10), but it confirms that the example really sits on the declared coefficient boundary.

## 4. Why this is a stronger control than the isolated `ell^2` bound

The pair `PL-365` / `PL-366` might leave open the interpretation that `1/2` is special because `ell^2` is the canonical coefficient Hilbert space of Dirichlet series. The present ladder separates two statements that should not be conflated.

The first is true and classical in flavor: `ell^2` is distinguished by Hilbert geometry, and under the Bohr transform it is the standard `mathcal H^2` coefficient space. The second does **not** follow: a square-root exponent obtained solely from that norm is not zeta-specific. The identical residual calculation in `ell^p-ell^q` duality produces every exponent `theta in (0,1)`, and the examples above show those exponents are sharp in their respective coefficient classes.

For `p=2`, choose any `1/2<a<1` in (PL367-20). Then

\[
c_d=d^{-1/2}(\log d)^{-a}
\quad(d\ge2)
\tag{PL367-29}
\]

with the pole-neutral `c_1` from (PL367-21) lies in `ell^2` but in no `ell^r` for `r<2`, and its filtered output satisfies

\[
\sigma_c(B)=\frac12.
\tag{PL367-30}
\]

Thus `PL-366`'s square-root upper bound cannot be uniformly improved to `O(x^{1/2-delta})` over the pole-neutral `ell^2` class for any fixed `delta>0`. The obstruction is already present in a one-sign coefficient tail plus one scalar pole-cancelling coefficient; it is unrelated to prime cancellation.

## 5. Prior-art and novelty audit

No theorem-level novelty is claimed for the analytic ingredients. Holder duality, Abel summation, the half-plane property of ordinary Dirichlet-series convergence, and the factorization of a Dirichlet product in its absolute-convergence region are classical. `PL-365` already records Wintner-type mean-value control for divisor convolutions, and `PL-366` records the Hedenmalm-Lindqvist-Seip `mathcal H^2` background.

The literature audit covered Wintner/generalized mean-value formulas for Dirichlet convolution, Bohr-Cahen abscissa formulas, coefficient spaces for ordinary Dirichlet series, and Hardy spaces of Dirichlet series. The individual estimates belong to standard analysis. No source located in that audit turns the coefficient `ell^p` ladder into an RH mechanism; this finding does not claim the ladder as a new theorem of analytic number theory.

The durable delta is the **sharp route classification** left open by `PL-366`. That finding intentionally made no sharpness claim and only established the universal Hilbert upper bound. Here the same residual is computed in its full dual Banach scale and explicit pole-neutral examples attain every resulting abscissa. Therefore a vertical boundary obtained from a bare coefficient norm plus the single condition `C(1)=0` can be placed anywhere in `(0,1)` by changing the ambient exponent. A mechanism that genuinely singles out `1/2` must contain information not reducible to this coefficient-topology choice.

One distinction is essential. For `p!=2`, the coefficient condition `c in ell^p` is **not** being identified with the canonical Hardy space `mathcal H^p` on the infinite torus. Those norms are different outside the Hilbert case. The present no-go therefore applies to diagonal coefficient-Banach regularity, not to every nonlinear or non-diagonal Hardy-space phenomenon.

## 6. Adversarial boundaries

1. **Pole neutrality remains imposed, not source-forced.** The relation `C(1)=0` is one scalar cancellation chosen to remove zeta's pole. The prime lattice itself has not forced it.

2. **The ladder is a control family, not a canonical arithmetic hierarchy.** Choosing `p` after choosing a desired exponent would be exactly the sort of post-hoc function-space tuning prohibited by the research mandate. Its value is falsificatory: it shows why such an exponent is not evidence by itself.

3. **Nested coefficient classes must be handled by the best available exponent.** A particular sequence may belong to several `ell^p` spaces and then inherit the strongest corresponding bound. The sharp examples (PL367-20) avoid this ambiguity by lying in `ell^p` and in no smaller `ell^r`.

4. **No `ell^infinity` endpoint is claimed.** At `p=infinity`, pole evaluation at `1` is not generically continuous and the tail in the dual `ell^1` residual norm diverges.

5. **This says nothing directly about Mobius cancellation.** The Mobius sequence is not in any finite `ell^p` coefficient class, so the argument does not imply a Mertens bound or RH.

6. **Zeros are transported, not localized.** Equation (PL367-8) inherits every zeta zero lying in the available half-plane. There is no positivity, self-adjointness, functional equation, trace identity, or target-relative condition forcing those zeros to the critical line.

7. **The coefficient-one source is still not a vector in `mathcal H^2`.** As in `PL-365` and `PL-366`, `b=c*1` is a coefficientwise divisor-filter readout. No claim is made that an arbitrary `ell^p` filter acts boundedly on the formal zeta source in a Hilbert space.

## 7. Prime-lattice consequence

The filter chain now has an exact continuum of ambient cancellation scales:

\[
\boxed{
 c\in\ell^p,\ C(1)=0
 \quad\Longrightarrow\quad
 S_{c*1}(x)=O_p\!\left(x^{1-1/p}\right),
 \qquad 1\le p<\infty,
}
\tag{PL367-31}
\]

with `p=1` interpreted by `PL-365`, and with the exponent sharp for every `1<p<infinity` by Section 3.

Accordingly, the next viable filter mechanism cannot use a coefficient norm merely because its dual exponent happens to produce the RH scale. It must supply an **independently source-forced condition** that is sensitive to the rational-prime system and violated by hypothetical off-line zeros — for example a functional-equation constraint, a target-relative quotient/model-space condition, a canonical signed form, or another global relation that survives the Helson/Beurling and programmability controls already recorded in this line.