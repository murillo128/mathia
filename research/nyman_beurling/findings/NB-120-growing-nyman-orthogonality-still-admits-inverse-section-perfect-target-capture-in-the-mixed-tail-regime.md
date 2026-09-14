# NB-120 — growing Nyman orthogonality still admits inverse-section perfect target capture in the mixed-tail regime

**Status:** `EXACT-DERIVED + GROWING-SOURCE-MATCHED-CONTROL + PERIODIC-TAIL-GRAM + JORDAN-TOTIENT-FACTORIZATION + PERFECT-VISIBLE-TARGET-CAPTURE + NEGATIVE/ROUTE-NARROWING + REPRESENTATION-AUDIT`.

`NB-119` proves that any **fixed** family of Nyman annihilation equations

\[
\langle f,g_b\rangle=0,
\qquad 2\le b\le M,
\]

still admits a matched control with perfect visible target capture and retained fraction `Theta_M(1/R)`. That leaves an obvious escape: perhaps one can let the number of exact source equations grow with the cell cutoff and thereby force the repair cost above order `R`.

In the regime where the periodic tails have enough room to mix, this escape also fails. Let `M=M(R)` satisfy

\[
M\longrightarrow\infty,
\qquad
\frac{M^6(1+\log M)}{R}\longrightarrow0.
\tag{1}
\]

Retain the natural-cell objects of `NB-118`--`NB-119`,

\[
V_M=\operatorname{span}\{g_2,\ldots,g_M\},
\qquad
Q_R=P_{\operatorname{span}\{\psi_n:1\le n<R\}},
\qquad
e_R=Q_Re.
\tag{2}
\]

Then for all sufficiently large `R` there is an exact matched control

\[
f_{M,R}\in V_M^\perp,
\qquad
Q_Rf_{M,R}=e_R,
\tag{3}
\]

so its visible target angle is exactly one, while

\[
\boxed{
\frac{\|Q_Rf_{M,R}\|^2}{\|f_{M,R}\|^2}
=
\frac{1+o(1)}{\kappa_\infty R}.
}
\tag{4}
\]

The limiting repair constant is finite, positive, and explicit:

\[
\boxed{
\kappa_\infty
=
12\sum_p
\frac{p^2(\log p)^2}{(p^2-1)^2}
<\infty.
}
\tag{5}
\]

Numerically `kappa_infty` is about `10.614`. Thus a number of **exact** Nyman source equations tending to infinity can still be satisfied while preserving perfect finite target capture at precisely the inverse-section scale. The `M^6 log M << R` condition is only a sufficient mixed-tail regime coming from a deliberately crude uniform conditioning bound; no sharpness is claimed for the exponent `1/6`.

The mechanism becomes transparent because the periodic tail Gram of `NB-119` has an exact arithmetic factorization. If

\[
C_M(i,j)
=
\lim_{R\to\infty}R\,
\langle (I-Q_R)g_i,(I-Q_R)g_j\rangle,
\qquad 2\le i,j\le M,
\tag{6}
\]

then, with `g=gcd(i,j)`,

\[
\boxed{
C_M(i,j)
=
\frac{(i-1)(j-1)}{4ij}
+
\frac{g^2-1}{12ij}.
}
\tag{7}
\]

For the fixed-`M` repair constant of `NB-119`,

\[
\kappa_M
=
a_M^*C_M^{-1}a_M,
\qquad
a_M(b)=\frac{\log b}{b},
\tag{8}
\]

this gives the exact scalar formula

\[
\boxed{
\kappa_M
=
12S_2(M)
-
\frac{36S_1(M)^2}{1+3S_0(M)},
}
\tag{9}
\]

where

\[
S_2(M)=\sum_{2\le n\le M}\frac{\Lambda(n)^2}{J_2(n)},
\quad
S_1(M)=\sum_{2\le n\le M}\frac{\Lambda(n)\varphi(n)}{J_2(n)},
\quad
S_0(M)=\sum_{2\le n\le M}\frac{\varphi(n)^2}{J_2(n)}.
\tag{10}
\]

Here `J_2` is Jordan's totient. Formula `(9)` shows in particular that the matched-control constant does **not** diverge as more Nyman equations are imposed; instead `kappa_M -> kappa_infty`.

## 1. The periodic covariance is a rank-one mean plus a GCD-square kernel

On the `n`th natural cell, `NB-119` gives

\[
\langle g_b,\psi_n\rangle
=
\frac{\{n/b\}}{\sqrt{n(n+1)}}.
\tag{11}
\]

Therefore the first-order tail Gram is the period mean

\[
C_M(i,j)
=
\operatorname*{mean}_{n}
\{n/i\}\{n/j\}.
\tag{12}
\]

Put `g=gcd(i,j)`, `i=ga`, `j=gb`, with `(a,b)=1`. Conditional on the residue `r=n mod g`, the lifts modulo `i` and `j` are independent by the Chinese remainder theorem. Their conditional means are

\[
\frac{a-1}{2a}+\frac{r}{ga},
\qquad
\frac{b-1}{2b}+\frac{r}{gb}.
\tag{13}
\]

Averaging over `r=0,...,g-1` therefore gives the product of the unconditional means plus the covariance of the common residue. Since

\[
\operatorname{Var}\{0,1,\ldots,g-1\}
=\frac{g^2-1}{12},
\tag{14}
\]

we obtain exactly `(7)`.

Define, on indices `2,...,M`,

\[
u_i:=\frac{i-1}{2i},
\qquad
D:=\operatorname{diag}(2,3,\ldots,M),
\qquad
H_{ij}:=\gcd(i,j)^2-1.
\tag{15}
\]

Then

\[
\boxed{
C_M=uu^*+\frac1{12}D^{-1}HD^{-1}.
}
\tag{16}
\]

The second term is a classical GCD-matrix object. Using

\[
\gcd(i,j)^2-1
=
\sum_{\substack{d\mid i\\d\mid j\\d\ge2}}J_2(d),
\tag{17}
\]

let

\[
Z_{n,d}:=\mathbf1_{d\mid n},
\qquad 2\le n,d\le M.
\tag{18}
\]

The divisor-incidence matrix `Z` is unit lower triangular and

\[
\boxed{
H=Z\,\operatorname{diag}(J_2(2),\ldots,J_2(M))\,Z^*.
}
\tag{19}
\]

Thus `H>0` and `C_M>0` for every `M`, recovering and sharpening the positivity argument of `NB-119` without using the enormous common period `lcm(2,...,M)`.

## 2. Möbius inversion diagonalizes the repair constant

Write

\[
K_M:=\frac1{12}D^{-1}HD^{-1},
\qquad
C_M=K_M+uu^*.
\tag{20}
\]

Let

\[
\ell_n:=\log n,
\qquad
v_n:=\frac{n-1}{2}.
\tag{21}
\]

Since `a_M=D^{-1}ell` and `u=D^{-1}v`, the incidence factorization `(19)` makes the relevant quadratic forms diagonal after Möbius inversion. The classical divisor identities

\[
\log n=\sum_{d\mid n}\Lambda(d),
\qquad
n-1=\sum_{\substack{d\mid n\\d\ge2}}\varphi(d)
\tag{22}
\]

say exactly that

\[
Z^{-1}\ell=(\Lambda(n))_{2\le n\le M},
\qquad
Z^{-1}v=\left(\frac{\varphi(n)}2\right)_{2\le n\le M}.
\tag{23}
\]

Hence

\[
a_M^*K_M^{-1}a_M=12S_2(M),
\tag{24}
\]

\[
a_M^*K_M^{-1}u=6S_1(M),
\tag{25}
\]

and

\[
u^*K_M^{-1}u=3S_0(M).
\tag{26}
\]

Applying the Sherman--Morrison formula to `C_M=K_M+uu^*` proves `(9)` exactly.

This identity survives several independent checks. Direct period averaging of `(12)` agrees with `(7)` for every pair `2<=i,j<=7`; direct inversion of `C_M` agrees with `(9)` to machine precision for every `2<=M<=20`; and `M=2` recovers

\[
\kappa_2=2(\log2)^2,
\tag{27}
\]

exactly as in `NB-119`. These computations are regression checks only; `(12)`--`(26)` are a finite algebraic proof.

## 3. The repair constant converges instead of growing

First,

\[
J_2(n)
=n^2\prod_{p\mid n}(1-p^{-2})
\ge\frac{n^2}{\zeta(2)}.
\tag{28}
\]

Therefore

\[
S_2(\infty)
:=
\sum_{n\ge2}\frac{\Lambda(n)^2}{J_2(n)}
<\infty.
\tag{29}
\]

Since `Lambda` is supported on prime powers,

\[
\begin{aligned}
S_2(\infty)
&=
\sum_p(\log p)^2
\sum_{k\ge1}\frac1{J_2(p^k)}\\
&=
\sum_p
\frac{p^2(\log p)^2}{(p^2-1)^2}.
\end{aligned}
\tag{30}
\]

It remains to show that the rank-one correction in `(9)` vanishes. A crude bound already gives

\[
S_1(M)
\le
\zeta(2)\sum_{n\le M}\frac{\Lambda(n)}n
=O((\log M)^2).
\tag{31}
\]

For the denominator, note the exact multiplicative simplification

\[
\frac{\varphi(n)^2}{J_2(n)}
=
\prod_{p\mid n}\frac{p-1}{p+1}.
\tag{32}
\]

Set

\[
h(d)
:=
\mu(d)^2
\prod_{p\mid d}\left(-\frac2{p+1}\right).
\tag{33}
\]

Then the right side of `(32)` is `sum_(d|n) h(d)`. Since

\[
\sum_{d\ge1}\frac{|h(d)|}{d}<\infty,
\tag{34}
\]

and `|h(d)|<=2^{omega(d)}/d<=tau(d)/d`, ordinary divisor summation yields

\[
\boxed{
S_0(M)
=c_*M+O((\log M)^2),
}
\tag{35}
\]

with

\[
\boxed{
c_*
=
\prod_p\left(1-\frac{2}{p(p+1)}\right)>0.
}
\tag{36}
\]

Consequently

\[
\frac{36S_1(M)^2}{1+3S_0(M)}
=O\!\left(\frac{(\log M)^4}{M}\right)
\longrightarrow0.
\tag{37}
\]

Combining `(9)`, `(29)`, `(30)`, and `(37)` proves

\[
\boxed{
\kappa_M\longrightarrow\kappa_\infty
=12S_2(\infty),
}
\tag{38}
\]

which is `(5)`. The constant is bounded away from zero already at `M=2`, and finite because of `(29)`. Numerically, for orientation only,

\[
\kappa_{10}\approx2.0105,
\quad
\kappa_{100}\approx6.8727,
\quad
\kappa_{1000}\approx9.6739,
\tag{39}
\]

converging slowly toward approximately `10.614`.

This is the first representation-level warning: even the **formal leading tail cost** of satisfying more and more Nyman equations saturates at a finite constant rather than becoming coercive.

## 4. The fixed-`M` tail law is uniform in a growing mixed regime

To turn the limiting constant into an actual growing-`M` matched control, the fixed-`M` asymptotic of `NB-119` must be made uniform.

For a bounded `q`-periodic sequence `x_n` with mean `mu`, the centered partial sums are bounded by `q`. Summation by parts with

\[
w_n=\frac1{n(n+1)}
\tag{40}
\]

therefore gives the explicit tail estimate

\[
\boxed{
\sum_{n\ge R}x_nw_n
=
\frac{\mu}{R}
+O\!\left(\frac q{R^2}\right).
}
\tag{41}
\]

For `x_n={n/i}{n/j}`, the period is `lcm(i,j)<=ij<=M^2`. Hence the tail Gram `Gamma_(M,R)` from `NB-119` satisfies entrywise

\[
\Gamma_{M,R}(i,j)
=
\frac{C_M(i,j)}R
+O\!\left(\frac{M^2}{R^2}\right),
\tag{42}
\]

and therefore

\[
\boxed{
\|R\Gamma_{M,R}-C_M\|_{op}
=O\!\left(\frac{M^3}{R}\right).
}
\tag{43}
\]

A crude inverse bound is enough. From `(16)` and `(19)`,

\[
C_M\succeq\frac1{12}D^{-1}HD^{-1}.
\tag{44}
\]

The inverse divisor-incidence matrix has entries

\[
(Z^{-1})_{n,d}
=
\mu(n/d)\mathbf1_{d\mid n},
\tag{45}
\]

so

\[
\|Z^{-1}\|^2
\le\|Z^{-1}\|_F^2
\le\sum_{n\le M}\tau(n)
\le M(1+\log M).
\tag{46}
\]

Also `J_2(d)>=3` for `d>=2`. Thus

\[
\|H^{-1}\|
\le\frac13M(1+\log M),
\tag{47}
\]

and `(44)` yields

\[
\boxed{
\|C_M^{-1}\|
\le4M^3(1+\log M).
}
\tag{48}
\]

Put

\[
B_{M,R}:=R\Gamma_{M,R}.
\tag{49}
\]

Equations `(43)` and `(48)` imply

\[
\left\|
C_M^{-1/2}(B_{M,R}-C_M)C_M^{-1/2}
\right\|
=O\!\left(\frac{M^6(1+\log M)}R\right).
\tag{50}
\]

Under `(1)` this is `o(1)`, so `Gamma_(M,R)` is invertible and `B_(M,R)^(-1)` is asymptotically equivalent to `C_M^(-1)` in quadratic form.

The finite head-correlation vector is

\[
a_{M,R}(b)=\langle e_R,g_b\rangle.
\tag{51}
\]

Applying `(41)` to `{n/b}` gives, uniformly for `b<=M`,

\[
a_{M,R}(b)
=
\frac{\log b}{b}
-
\frac{u_b}{R}
+O\!\left(\frac b{R^2}\right).
\tag{52}
\]

The perturbation in `(52)` is also negligible in the `C_M^{-1}` metric. Indeed `C_M\succeq uu^*` implies

\[
u^*C_M^{-1}u\le1,
\tag{53}
\]

while `(48)` controls the `O(b/R^2)` remainder. Since `(38)` also gives

\[
a_M^*C_M^{-1}a_M=\kappa_M=O(1),
\tag{54}
\]

we obtain

\[
\boxed{
a_{M,R}^*B_{M,R}^{-1}a_{M,R}
=\kappa_M+o(1)
=\kappa_\infty+o(1).
}
\tag{55}
\]

This is the uniform bridge that fixed-`M` `NB-119` did not provide.

## 5. A growing family of exact source equations still has a perfect matched control

Let

\[
h_{b,R}:=(I-Q_R)g_b,
\qquad 2\le b\le M,
\tag{56}
\]

and define, exactly as in `NB-119`,

\[
\lambda_{M,R}:=\Gamma_{M,R}^{-1}a_{M,R},
\qquad
y_{M,R}:=-\sum_{b=2}^{M}\lambda_{M,R}(b)h_{b,R},
\tag{57}
\]

\[
f_{M,R}:=e_R+y_{M,R}.
\tag{58}
\]

For every `2<=b<=M`,

\[
\langle f_{M,R},g_b\rangle=0,
\tag{59}
\]

while, because `y_(M,R)` is supported beyond the cutoff,

\[
Q_Rf_{M,R}=e_R.
\tag{60}
\]

Thus `(3)` is exact, not asymptotic. The tail repair is minimum norm and

\[
\|y_{M,R}\|^2
=a_{M,R}^*\Gamma_{M,R}^{-1}a_{M,R}.
\tag{61}
\]

Using `Gamma_(M,R)=B_(M,R)/R` and `(55)`,

\[
\boxed{
\|y_{M,R}\|^2
=\kappa_\infty R+o(R).
}
\tag{62}
\]

Finally, head and tail are orthogonal and

\[
\|e_R\|^2=1-\frac1R.
\tag{63}
\]

Therefore

\[
\frac{\|Q_Rf_{M,R}\|^2}{\|f_{M,R}\|^2}
=
\frac{1-1/R}{1-1/R+\kappa_\infty R+o(R)}
=
\frac{1+o(1)}{\kappa_\infty R},
\tag{64}
\]

proving `(4)`.

The control satisfies `M(R)-1 -> infinity` exact source equations. For example any power law `M=R^alpha` with fixed `alpha<1/6` lies in the proved regime after harmless logarithmic slack. The exponent `1/6` comes from combining the entrywise periodic-tail error with the rough inverse bound `(48)`; it is a proof threshold, not an asserted phase transition.

## 6. Prior-art boundary, matched-control audit, and what remains open

The ingredients in the arithmetic factorization are classical. GCD matrices and their divisor-incidence factorizations go back to Smith-type matrix theory; the identity `gcd(i,j)^2=sum_(d|gcd(i,j)) J_2(d)` is the standard Jordan-totient convolution. Recent Nyman--Beurling Gram work, including Werner Ehm's 2024 analysis of Nyman Gram kernels and the finite Gram-spectral literature already anchored in this line, confirms that arithmetic Gram structure itself is not new. No novelty is claimed for `(17)`--`(23)` separately.

A targeted audit did not locate the specific combination used here: the **tail-periodic** covariance `(7)`, its insertion into the `NB-119` minimum-norm source repair, the exact scalar reduction `(9)`, or the conclusion `(4)` that a growing family of exact Nyman annihilation equations still permits perfect visible target capture at inverse-section retention. No external theorem is load-bearing in the derivation, so `SOURCES.md` needs no new dependency.

The matched control remains deliberately non-zeta. It need not be a confluent zero-power packet of `NB-117`, and it is rebuilt for each pair `(M,R)`. It satisfies only the equations `g_b`, `b<=M(R)`, not the complete infinite Nyman family. Therefore `(4)` does **not** construct an off-critical zeta-zero rescue and says nothing about whether actual zero packets can occupy this mode.

What it does rule out is stronger than `NB-119`: merely replacing a fixed source section by a slowly growing one does not by itself create coercivity. Any successful use of growing Nyman orthogonality must enter a genuinely non-mixed regime where `M` is large enough relative to `R` that the periodic tail approximation is no longer uniform, or exploit constants/structure substantially sharper than the generic Gram repair. The other live routes from `NB-117`--`NB-119` remain untouched: the confluent zero-power form, zero-specific identities, or coherence that couples the **same actual packet** across cutoffs rather than rebuilding an arbitrary Hilbert-space tail repair.

This distinction is the main research consequence. The next source theorem cannot merely say "take more exact Nyman equations." It must quantify how fast and in what geometry those equations grow relative to the finite cell resolution, or use information that the matched controls `(57)`--`(58)` do not possess.