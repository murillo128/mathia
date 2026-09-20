# WI-376 — True source slots do not remove the corrected gamma bulk floor

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + SOURCE-CONDITIONED-BARRIER + DECISIVE-REPAIR-NOGO + CLASSICAL-ARITHMETIC + NON-ESTABLISHED-RH`.

## Claim

The true arithmetic source slots incident to one target cell in Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* do **not** remove the negative bulk sector of the gamma-corrected archimedean form reconstructed in WI-369. In the physical logarithmic coordinate, even after forcing a test function to vanish on every active source slot for the target cell `C_k=[k,k+1)`, the constrained form bottom still tends to the same sharp value

\[
-C_\Gamma,
\qquad
C_\Gamma=\frac\pi2+\gamma+\log(8\pi).
\]

More precisely, put

\[
A_k=\log(k+1)
\]

and let `\mathcal A_{A_k}` be the corrected archimedean form from WI-369 after the unitary physical-log rescaling to `(0,A_k)`. For every active prime power `n` with `2\le n\le k` and `\Lambda(n)>0`, the exact source interval feeding the target cell is

\[
I_{k,n}=\left[\frac{k}{n},\frac{k+1}{n}\right),
\]

so in the physical logarithmic coordinate its slot is

\[
J_{k,n}
=\left[\log k-\log n,\ \log(k+1)-\log n\right).
\]

Let

\[
S_k=\bigcup_{\substack{2\le n\le k\\ \Lambda(n)>0}}J_{k,n}
\]

and define the source-zero constrained bottom

\[
\lambda_k^{\rm src}
:=
\inf_{\substack{0\ne F\in\mathcal D(\mathcal A_{A_k})\\F=0\ \mathrm{a.e.\ on}\ S_k}}
\frac{\mathcal A_{A_k}[F]}{\|F\|_2^2}.
\]

Then

\[
\boxed{
\lim_{k\to\infty}\lambda_k^{\rm src}=-C_\Gamma.
}
\tag{1}
\]

Consequently, for all sufficiently large `k` there is a nonzero test direction that vanishes on every true source slot but has strictly negative corrected archimedean energy. Therefore the ordinary variational short of the **corrected archimedean block alone** to those source slots has zero-data value

\[
\boxed{-\infty.}
\tag{2}
\]

This is a decisive obstruction to the most direct repair of the gamma-free common-cut step audited in WI-375: one cannot simply retain the corrected gamma channel, substitute the resulting archimedean form for the gamma-free one-cell form, and perform the same source-complement infimum. A viable repair must bring a coercive inherited/global/arithmetic channel into the form **before** that elimination, or justify a different elimination object that excludes the bulk quasimodes below.

The statement is deliberately scoped. It does not say that the full rooted Weil form or Desogus's complete old-core/source network has an unbounded short, and it does not refute RH. It shows that true source conditioning by itself does not cure the corrected archimedean gamma debt.

## 1. Physical-log form of the corrected archimedean block

WI-369 proves on the normalized interval `(0,1)` that

\[
\mathcal A_A[f]+C_\Gamma\|f\|_2^2
=
\frac A2\iint h(A|u-v|)|f(u)-f(v)|^2\,du\,dv
+\int\bigl(H(Au)+H(A(1-u))\bigr)|f(u)|^2\,du
+A\iint h(A(u+v))f(u)\overline{f(v)}\,du\,dv,
\]

where

\[
h(s)=\frac{e^{-s/2}}{1-e^{-2s}},
\qquad
H(z)=\operatorname{artanh}(e^{-z/2})+\arctan(e^{-z/2}).
\]

Set `s=Au` and use the unitary rescaling

\[
f(u)=\sqrt A\,F(Au).
\]

The identity becomes exactly

\[
\boxed{
\mathcal A_A[F]+C_\Gamma\|F\|_2^2
=D_A[F]+E_A[F]+J_A[F],
}
\tag{3}
\]

on `(0,A)`, with

\[
D_A[F]
=\frac12\iint_{(0,A)^2}
h(|s-t|)|F(s)-F(t)|^2\,ds\,dt,
\tag{4}
\]

\[
E_A[F]
=\int_0^A\bigl(H(s)+H(A-s)\bigr)|F(s)|^2\,ds,
\tag{5}
\]

and

\[
J_A[F]
=\iint_{(0,A)^2}h(s+t)F(s)\overline{F(t)}\,ds\,dt.
\tag{6}
\]

All three terms are nonnegative. Hence the lower half of (1) is immediate from WI-369:

\[
\lambda_k^{\rm src}\ge -C_\Gamma.
\tag{7}
\]

The issue is whether the exact source constraints force a positive amount of the remainder in (3). They do not.

## 2. The true source slots occupy asymptotically negligible logarithmic measure

Desogus's source routing sends the interval

\[
I_{k,n}=\left[k/n,(k+1)/n\right)
\]

under multiplication by `n` exactly onto `C_k=[k,k+1)`. Passing to `s=\log t` gives `J_{k,n}` above. Every slot has the same logarithmic length

\[
\varepsilon_k
=\log\frac{k+1}{k}
=\log\left(1+\frac1k\right).
\tag{8}
\]

The slots are pairwise disjoint. Indeed it is enough to compare consecutive integer indices:

\[
\frac{k+1}{n+1}\le\frac{k}{n}
\quad\Longleftrightarrow\quad n\le k.
\tag{9}
\]

Thus increasing `n` moves the whole source interval weakly to the left without overlap.

Let `M_k` be the number of prime powers `n\le k`. Classical Chebyshev bounds for primes, plus the crude count of higher prime powers, give

\[
M_k
\le \pi(k)+O(\sqrt{k}\log k)
=O\!\left(\frac{k}{\log k}\right).
\tag{10}
\]

Therefore

\[
\boxed{
|S_k|=M_k\varepsilon_k=O\!\left(\frac1{\log k}\right)=o(1).
}
\tag{11}
\]

This is much stronger than merely saying that the source constraints have zero density in the growing log interval: their total physical-log measure actually tends to zero while `A_k\sim\log k` tends to infinity.

## 3. A perforated bulk test keeps only bounded positive remainder

Take the interior bulk interval

\[
B_k=[1,A_k-1].
\]

We construct `0\le F_k\le1`, compactly supported in `(0,A_k)`, such that `F_k=0` on `S_k`, `F_k=1` on most of `B_k`, and

\[
\|F_k\|_2^2=A_k-O(1).
\tag{12}
\]

One may first remove the `\varepsilon_k`-neighborhood of each component of `S_k\cap B_k` and then smooth the finitely many boundaries. The removed/smoothed defect has `L^1` mass `O(M_k\varepsilon_k)` and total variation `O(M_k)`. Consequently its translation modulus is bounded by

\[
O\!\left(M_k\min(r,\varepsilon_k)\right),
\tag{13}
\]

while the two outer bulk boundaries contribute `O(r)`. Since `0\le F_k\le1`, the squared translation difference is bounded by the corresponding `L^1` difference. Extending by zero to the real line therefore gives

\[
D_{A_k}[F_k]
\le
2\int_0^\infty r h(r)\,dr
+C M_k
\left(
\int_0^{\varepsilon_k}r h(r)\,dr
+\varepsilon_k\int_{\varepsilon_k}^\infty h(r)\,dr
\right)
\tag{14}
\]

for an absolute constant `C` independent of `k`.

The first moment

\[
M_1:=\int_0^\infty r h(r)\,dr
\tag{15}
\]

is finite. Moreover WI-369 gives

\[
\int_z^\infty h(r)\,dr=H(z)
=\log2+\frac\pi4-\frac12\log z+o(1)
\qquad(z\downarrow0),
\tag{16}
\]

while `r h(r)` stays bounded at zero. Hence the bracket in (14) is

\[
O\!\left(\varepsilon_k\log\frac1{\varepsilon_k}\right).
\tag{17}
\]

Using (8) and (10),

\[
M_k\varepsilon_k\log(1/\varepsilon_k)=O(1),
\]

so

\[
\boxed{D_{A_k}[F_k]=O(1).}
\tag{18}
\]

The other two positive pieces are even easier. Since `0\le F_k\le1` and `H(z)=\int_z^\infty h(r)\,dr`, Fubini gives

\[
0\le E_{A_k}[F_k]
\le 2\int_0^\infty H(s)\,ds
=2M_1,
\tag{19}
\]

and

\[
0\le J_{A_k}[F_k]
\le\iint_{(0,\infty)^2}h(s+t)\,ds\,dt
=M_1.
\tag{20}
\]

Thus the entire positive remainder in (3) is uniformly bounded:

\[
D_{A_k}[F_k]+E_{A_k}[F_k]+J_{A_k}[F_k]=O(1).
\tag{21}
\]

Combining (3), (12), and (21),

\[
\frac{\mathcal A_{A_k}[F_k]}{\|F_k\|_2^2}
=-C_\Gamma+O\!\left(\frac1{A_k}\right).
\tag{22}
\]

Together with (7), this proves (1).

The smoothing above can be carried out inside the complement of the closed source slots, so the same conclusion holds using smooth compactly supported test functions rather than relying on discontinuous indicators. Equivalently, the step-function picture is a finite-energy element of the natural screened form domain and the smooth functions are a form-core approximation.

## 4. The corrected archimedean source short is unbounded below

For sufficiently large `k`, equation (22) gives an admissible source-zero direction `F_k` with

\[
\mathcal A_{A_k}[F_k]<0.
\tag{23}
\]

An ordinary variational short at zero source data minimizes over precisely such complement directions. Therefore, for every scalar `R`,

\[
\mathcal A_{A_k}[R F_k]
=R^2\mathcal A_{A_k}[F_k]\longrightarrow-\infty
\qquad(|R|\to\infty).
\tag{24}
\]

This proves (2). The point is not merely that a finite positive reserve is lost: the archimedean-only short ceases to be a finite quadratic form once the gamma-corrected block replaces the gamma-free positive model.

Desogus's printed common-cut and rooted-Schur steps avoid this problem because they short the gamma-free one-cell form `\mathfrak b`, whose positive lower model is the input to the common-complement theorem. WI-375 showed that this is downstream of the unresolved gamma cancellation. The present finding sharpens that audit: **retaining the true gamma channel and then applying the same source short is not a neutral repair.** The exact source slots leave the sharp gamma bulk floor essentially untouched.

## 5. Consequence for the repair tree

WI-369 showed that the corrected archimedean block has sharp full-core floor `-C_\Gamma`. WI-371--WI-373 showed that this debt has a macroscopic negative-index profile rather than being a single scalar defect. WI-374 showed that fresh endpoint collars eventually become gamma-positive, while WI-375 isolated the remaining mismatch between that corrected picture and the printed gamma-free common-cut/pivot mechanism.

Equation (1) now rules out a natural escape from those results: the arithmetic source geometry for the current target does **not** itself exclude the bulk quasimodes responsible for the negative floor. The holes cut out by all true source intervals have vanishing total logarithmic measure and cost only `O(1)` in the positive screened remainder, while the negative scalar contribution is `-C_\Gamma A_k+O(1)`.

Accordingly, any repaired Gate-II style induction must do at least one of the following before taking the source-complement infimum: retain an inherited/global coercive form that acts on the slot complement, prove a source-conditioned coupling that charges these bulk directions, or replace the ordinary short by another exact elimination whose admissible complement is genuinely smaller. A parentwise reuse of the gamma-free common-cut theorem with only the corrected archimedean block substituted in is impossible.

This is a mechanism-level barrier, not a theorem about zeta zeros by itself. It does not establish that the full source/arithmetic/polar network fails to provide the missing coercivity, and it does not promote or refute the preprint's RH conclusion.

## 6. Prior art and novelty boundary

**Primary source under audit.** Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1, submitted 17 September 2026. Section 3 gives the source subcells and exact multiplication routing; Section 5 gives the Cauchy--Carleman/gamma transport; Section 6 builds the coherent common-source short and rooted induction. The arXiv record was rechecked on 20 September 2026 and remained at version 1.

**Internal exact dependencies.** WI-369 supplies the corrected physical archimedean decomposition and the sharp constant `C_\Gamma`; WI-373 identifies the same bulk debt spectrally; WI-375 shows that the printed common-cut and inherited-pivot chain still consumes the gamma-free one-cell model. No result from another Mathia research line is promoted here.

**Classical inputs.** The source-slot count uses only the classical Chebyshev upper bound `\pi(x)=O(x/\log x)` and a crude count of higher prime powers. The translation-modulus estimate for finite unions of intervals, Fubini identities for nonnegative kernels, and the scaling argument for a negative direction in a quadratic-form short are elementary analysis.

A fresh targeted audit on 20 September 2026 searched for independent technical discussion of the Desogus source short, retained regular-gamma channel, source-slot perforation, and corrections to the common-cut step. It located the primary preprint and generic mirrors/listings but no independent statement of (1) or the source-zero short obstruction (2). That absence is recorded only as an audit result; no priority claim is made.

## 7. Falsification and scope controls

The result has several direct failure tests.

First, the source geometry can be checked without operator theory: each active branch must really correspond to `I_{k,n}=[k/n,(k+1)/n)`, and after `s=\log t` all slots must have length `\varepsilon_k`. A different source map with positive logarithmic density would invalidate the perforated-bulk estimate.

Second, (14) can be audited independently from the translation representation of (4): the outer interval contributes `O(r)`, while `M_k` holes of width `O(\varepsilon_k)` contribute `O(M_k\min(r,\varepsilon_k))`. Together with the exact `H` asymptotic from WI-369 this must remain `O(1)`.

Third, the conclusion (2) is only about shorting the corrected **archimedean block alone** against the true current-target source slots. If the mathematically correct elimination includes an additional positive inherited/global term before the infimum, that term must be retained and analyzed; it is outside the no-go statement rather than contradicted by it.

Finally, the result does not identify the uncertified complement of the simple-critical-zero theorem with off-line zeros, does not assume global Weil positivity, and does not use support beyond what has been justified elsewhere in this line.

## Research consequence

The immediate Desogus-audit target is no longer just to `put the gamma term back` in the common-cut proof. The exact source constraints are too sparse in physical logarithmic measure to remove the corrected gamma bulk modes. The next viable theorem must therefore be a genuinely **source-conditioned inherited coercivity** statement: it has to show that the old-core/global part of the rooted form finances the `C_\Gamma` bulk debt on the complement before Schur elimination, or else provide an exact alternative to that elimination. That is the narrowest remaining repair gate exposed by the current chain WI-369--WI-376.