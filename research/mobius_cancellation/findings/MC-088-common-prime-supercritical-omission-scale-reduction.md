# MC-088 — A common-prime supercritical annular omission reduces exactly to lower Mertens scales

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CANDIDATE-NEW-STRUCTURE`, `BOUNDARY/CONDITIONAL-GAIN`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-087` showed that an omitted physical-space subset of the Huxley--Watt sawtooth annulus is not a weaker carrier when its contribution can already be restored at the target scale by the generic bound `|z|<=1/2`. The first natural way to cross that support-only barrier is to omit a set that is **supercritical in cardinality** but arithmetically self-similar.

Fix an integer `L>=2` and a prime `p`, and put

\[
X=p^L,
\qquad
N=pX=p^{L+1}.
\tag{1}
\]

Let

\[
z(x)=\lfloor x\rfloor+\frac12-x,
\qquad |z(x)|\le\frac12,
\tag{2}
\]

and omit from the annulus the pairs sharing the prime `p`:

\[
E_{p,L}
:=
\{(m,n):m,n\le N,\ mn>N,\ p\mid m,\ p\mid n\}.
\tag{3}
\]

Define their signed sawtooth contribution

\[
T_{p,L}
:=
\sum_{(m,n)\in E_{p,L}}
\mu(m)\mu(n)
 z\!\left(\frac{N^2}{mn}\right).
\tag{4}
\]

Then `E_{p,L}` is far too large to be harmless by the support estimate of `MC-087`:

\[
\boxed{
\#E_{p,L}
=
X^2+O\!\left(\frac Xp\log X\right)
=
N^{2L/(L+1)+o(1)}.
}
\tag{5}
\]

For every `L>=2`, the support exponent `2L/(L+1)` is strictly larger than `1`, so this omission is supercritical at the RH square-scale resolution.

Nevertheless its **signed** contribution has an exact reduction to ordinary Möbius data at scales no larger than `X^2=N^{2L/(L+1)}`. Define

\[
S_M(p,L):=\sum_{r=0}^{L}M(p^r),
\tag{6}
\]

\[
S_H(p,L):=\sum_{r=0}^{L}p^r H(p^r),
\qquad
H(Y):=\sum_{n\le Y}\frac{\mu(n)}n,
\tag{7}
\]

and

\[
S_2(p,L):=\sum_{r=0}^{L}\sum_{s=0}^{L}M(p^{r+s}).
\tag{8}
\]

Then

\[
\boxed{
T_{p,L}
=
2(L+1)S_M(p,L)
-S_2(p,L)
-S_H(p,L)^2
+\frac12S_M(p,L)^2
-J_{p,L},
}
\tag{9}
\]

where the only leftover term is supported on a genuinely small product hyperbola and satisfies

\[
\boxed{
|J_{p,L}|
\ll
\frac Xp\log X.
}
\tag{10}
\]

Consequently, for every fixed `L>=2` and every fixed exponent

\[
\frac12<\beta<1,
\tag{11}
\]

the prior global hypothesis

\[
M(y)=O(y^\beta)
\tag{12}
\]

implies

\[
\boxed{
T_{p,L}
=O_{L,\beta}(X^{2\beta})
=O_{L,\beta}\!\left(N^{2\beta L/(L+1)}\right).
}
\tag{13}
\]

This is a **strict power reduction** relative to the old square-scale budget `N^{2 beta}`. Therefore the support threshold in `MC-087` is not an intrinsic information threshold: a supercritical omitted set can be recursively cheap when arithmetic structure reduces it to genuinely smaller scales.

But this does not by itself improve the Mertens exponent. For the retained source-coupled statistic

\[
P_N(E_{p,L})
:=
N^2H(N)^2-\frac12M(N)^2
+W_N-T_{p,L},
\tag{14}
\]

`MC-087` still gives exactly

\[
P_N(E_{p,L})
=
2M(N)-M(N^2)-I_N-T_{p,L},
\qquad I_N=O(N\log N).
\tag{15}
\]

Thus, assuming the old exponent `(12)`, an **independent** estimate

\[
P_N(E_{p,L})=O(N^{2\alpha}),
\qquad
\frac12<\alpha<\beta,
\tag{16}
\]

would yield along these scales

\[
\boxed{
M(N^2)
=
O\!\left(N^{2\gamma}\right),
\qquad
\gamma=
\max\!\left\{\alpha,\frac{L}{L+1}\beta\right\}
<\beta.
}
\tag{17}
\]

Equation (17) is a genuine conditional contraction ledger. The common-prime omission supplies the missing **complement reduction**, but not the missing estimate for the retained carrier. A successful continuation must therefore prove a sub-`beta` bound for the retained signed statistic from information weaker than the target Mertens bound, and then still satisfy the scale-coverage requirements of `MC-027`.

## 1. The omitted support is supercritical

Write `m=pa`, `n=pb`. Since `m,n<=N=pX`, one has `a,b<=X`, and the annulus condition becomes

\[
p^2ab>pX
\quad\Longleftrightarrow\quad
ab>\frac Xp.
\tag{18}
\]

Therefore

\[
\#E_{p,L}
=
X^2-
\#\{(a,b):a,b\le X,\ ab\le X/p\}.
\tag{19}
\]

The cutoff `ab<=X/p` already implies `a,b<=X`, and the classical divisor-hyperbola count gives

\[
\#\{(a,b):ab\le Y\}
=
O(Y\log Y).
\tag{20}
\]

Substituting `Y=X/p` proves (5).

At the RH epsilon boundary, the support-only criterion in `MC-087` would require roughly `#E=O(N^{1+epsilon})`. Here

\[
\frac{2L}{L+1}-1
=
\frac{L-1}{L+1}>0,
\tag{21}
\]

so for every fixed `L>=2` and every sufficiently small positive `epsilon`, the omission violates that criterion by a fixed power. Any successful estimate must therefore use signed arithmetic structure rather than cardinality.

## 2. Removing one Euler prime gives an exact geometric stack of Möbius coefficients

Only square-free `m` and `n` contribute to (4). Define the `p`-sifted Möbius function

\[
\nu_p(a)
:=
\mu(a)\mathbf 1_{p\nmid a}.
\tag{22}
\]

For `m=pa` with `p\nmid a`, one has `mu(pa)=-mu(a)`, so the two minus signs cancel. Equation (18) gives

\[
T_{p,L}
=
\sum_{\substack{a,b\le X\\ab>X/p}}
\nu_p(a)\nu_p(b)
 z\!\left(\frac{X^2}{ab}\right).
\tag{23}
\]

Now define the complete `p`-sifted quadratic form

\[
Q_{p,L}
:=
\sum_{a,b\le X}
\nu_p(a)\nu_p(b)
 z\!\left(\frac{X^2}{ab}\right)
\tag{24}
\]

and the low-product piece

\[
J_{p,L}
:=
\sum_{\substack{a,b\le X\\ab\le X/p}}
\nu_p(a)\nu_p(b)
 z\!\left(\frac{X^2}{ab}\right).
\tag{25}
\]

Then exactly

\[
T_{p,L}=Q_{p,L}-J_{p,L}.
\tag{26}
\]

Boundedness of `z` and (20) immediately give (10).

The key arithmetic identity is the finite Euler-factor deletion

\[
\boxed{
\nu_p(n)
=
\sum_{\substack{i\ge0\\p^i\mid n}}
\mu\!\left(\frac{n}{p^i}\right).
}
\tag{27}
\]

Indeed, if `p` does not divide `n`, only `i=0` occurs. If `p` divides `n`, the only potentially nonzero consecutive terms in the sum cancel, because `mu(pm)=-mu(m)` when `p` does not divide `m`; higher square powers contribute zero in the appropriate adjacent pair. In Dirichlet-series language this is the elementary removal of one Euler factor

\[
\sum_{n\ge1}\frac{\nu_p(n)}{n^s}
=
\frac{1}{(1-p^{-s})\zeta(s)}
\qquad(\Re s>1),
\tag{28}
\]

but no analytic continuation is used below.

Because `X=p^L`, substituting (27) into (24) has no floor mismatch. With

\[
A_i:=\frac{X}{p^i}=p^{L-i}
\qquad(0\le i\le L),
\tag{29}
\]

one obtains the exact finite decomposition

\[
\boxed{
Q_{p,L}
=
\sum_{i=0}^{L}\sum_{j=0}^{L}
Z(A_i,A_j),
}
\tag{30}
\]

where

\[
Z(A,B)
:=
\sum_{a\le A}\sum_{b\le B}
\mu(a)\mu(b)
 z\!\left(\frac{AB}{ab}\right).
\tag{31}
\]

Thus deleting one prime from both Möbius coordinates does not create an opaque new kernel. It resolves into a finite geometric stack of the **same source sawtooth form at unequal, decreasing cutoffs**.

## 3. Huxley--Watt arbitrary cutoffs evaluate every layer exactly

For positive integers `A,B`, specialize the degree-two Huxley--Watt identity to `g=1` and terminal cutoff `K=AB`. Since

\[
AB<(A+1)(B+1),
\]

the source identity gives

\[
M(AB)
=
M(A)+M(B)
-
\sum_{a\le A}\sum_{b\le B}
\mu(a)\mu(b)
\left\lfloor\frac{AB}{ab}\right\rfloor.
\tag{32}
\]

Using

\[
\lfloor x\rfloor
=x-\frac12+z(x),
\tag{33}
\]

we obtain the exact asymmetric sawtooth identity

\[
\boxed{
Z(A,B)
=
M(A)+M(B)-M(AB)
-ABH(A)H(B)
+\frac12M(A)M(B).
}
\tag{34}
\]

This is the unequal-cutoff analogue of the square identity already used in `MC-020` and `MC-084`. It is derived directly from the arbitrary-cutoff source theorem recorded in `MC-S24`; no new source theorem is being asserted.

Insert (34) into (30). Since the list `(A_i)` is exactly the list `(p^r)_{0<=r<=L}` in reverse order,

\[
\sum_i M(A_i)=S_M(p,L),
\qquad
\sum_i A_iH(A_i)=S_H(p,L),
\tag{35}
\]

and

\[
\sum_{i,j}M(A_iA_j)=S_2(p,L).
\tag{36}
\]

The remaining quadratic terms factor, giving

\[
Q_{p,L}
=
2(L+1)S_M
-S_2
-S_H^2
+\frac12S_M^2.
\tag{37}
\]

Combining (26), (10), and (37) proves the exact identity (9).

This is precisely the pre-collapse information that `MC-029` left open. `MC-029` shows that arbitrary unequal Huxley--Watt cutoffs reconstruct Möbius after **full source recombination and total-product collapse**. Here the unequal cutoffs arise instead from an arithmetic projection before that collapse, and their geometric stack terminates at the smaller horizon `X^2`.

## 4. A prior Mertens exponent makes the supercritical complement strictly cheaper

Assume (12) with `1/2<beta<1`. Then the same hypothesis implies the standard weighted consequence

\[
H(y)=O(y^{\beta-1}).
\tag{38}
\]

For completeness, the power saving `M(y)=O(y^beta)=o(y)` implies convergence of `sum mu(n)/n` to zero; partial summation of the tail then gives (38). Equivalently, the Dirichlet series already converges throughout `Re(s)>beta`, so its boundary value at `s=1` is `1/zeta(1)=0` in the usual limiting sense. This is a consequence of the assumed Mertens exponent, not an additional zero-free input.

The geometric scale list now gives

\[
S_M(p,L)
=O_{L,\beta}(X^\beta),
\tag{39}
\]

\[
S_H(p,L)
=O_{L,\beta}(X^\beta),
\tag{40}
\]

and

\[
S_2(p,L)
=O_{L,\beta}(X^{2\beta}).
\tag{41}
\]

Indeed, each is a finite geometric stack with largest scale respectively `X`, `X`, and `X^2`. Equations (9)--(10) therefore give

\[
T_{p,L}
=O_{L,\beta}(X^{2\beta})
+O\!\left(\frac Xp\log X\right).
\tag{42}
\]

Since `X=p^L`, `L>=2`, and `beta>1/2`,

\[
\frac Xp\log X
=p^{L-1+o(1)}
=o(p^{2\beta L})
=o(X^{2\beta}),
\tag{43}
\]

which proves (13).

The gain is not a constant. Relative to the original square horizon `N^2`, the complement uses exponent

\[
\beta\frac{L}{L+1}
\tag{44}
\]

rather than `beta`. The reduction comes from arithmetic self-similarity under removal of a shared prime, not from a generic norm estimate.

## 5. Conditional contraction and the remaining missing theorem

Substitute (13) into the exact retained identity (15). Under the prior exponent `beta`, the term `M(N)` is `O(N^beta)`. The interior is `O(N log N)`. If an independent estimate (16) is available with `alpha>1/2`, then all terms are absorbed by

\[
N^{2\max\{\alpha,\beta L/(L+1)\}},
\]

because `2 alpha>1` absorbs `N log N` and, for `L>=2`, `2 beta L/(L+1)>beta` absorbs the lower-scale `M(N)` term. This proves (17).

Both entries in the maximum are strictly below `beta` when `alpha<beta`. Thus the common-prime split passes a test that the support-small families `MC-085`--`MC-087` could not pass: **the omitted complement can be controlled at a strictly better exponent from the old hypothesis itself.**

What remains entirely open is the retained estimate (16). The retained set contains almost all annular pairs; deleting the common-`p` block does not supply a theorem saying that its signed source-coupled contribution is smaller. Assuming (16) would therefore be a real new arithmetic input, not a consequence established here.

Nor does (17) solve the global scale problem. It is stated on the prime-power geometry `N=p^(L+1)` chosen to make the Euler-factor stack exact without floor errors. A usable bootstrap must either extend the decomposition uniformly to overlapping general scales or provide a valid interpolation/coverage argument, exactly as required by `MC-027`.

## 6. Falsification controls and matched-model boundary

The mechanism is deliberately narrow and can be killed by direct checks.

First, (27) must hold coefficientwise for every `n`. Second, substituting it into the finite quadratic form must give (30) with no unaccounted floor or endpoint term; the prime-power scale choice is what makes the numerator and the two independent cutoffs match exactly. Third, (34) must agree with the arbitrary-cutoff Huxley--Watt identity at every finite `A,B`. Fourth, the low-product difference between (23) and (24) must be only the hyperbola `ab<=X/p`, so that (10) follows without Möbius cancellation.

The reduction is not Möbius-randomness evidence. It is driven by a deterministic finite Euler-factor deletion and the exact Huxley--Watt scale identity. A matched square-free-supported multiplicative function without the corresponding Dirichlet-inverse relation need not satisfy (27) or (34). Conversely, any comparator with the same local Euler-factor deletion algebra and the same source identity would inherit this reduction, so the present mechanism is not yet a discriminator unique to rational Möbius cancellation.

The route is killed as a bootstrap if every independently provable bound for `P_N(E_{p,L})` remains at exponent `beta` or worse, if the required estimate is equivalent to an inverse-zeta zero-free bound, or if extending the prime-power calculation to a covering family loses the strict exponent margin in (17).

## 7. Prior art and novelty boundary

The finite identity with arbitrary independent cutoffs is prior art from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20--34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`, recorded as `MC-S24`. `MC-029` already audits its coefficient recovery after total-product collapse.

The Euler-factor identity (27), the Dirichlet-series form (28), divisor-hyperbola counting, and partial summation are elementary classical mechanisms. A targeted literature search around `p`-sifted Möbius sums, finite Euler-factor deletion, and the Huxley--Watt identity did not expose the exact annular combination (9), but absence from that search is not evidence of novelty. No standalone number-theoretic novelty is claimed.

The durable contribution is a frontier-specific resolution of the escape explicitly left by `MC-087`: **supercritical support can indeed become recursively cheap through signed arithmetic structure.** The common-prime block supplies an exact example and a quantitative contraction ledger, while simultaneously isolating the next missing theorem as a genuinely improved estimate for the complementary retained statistic.

## Consequence for the research line

`MC-087` forced any physical-space survivor beyond support-small omission. The present result crosses that boundary for the first time in an exact source-linked family: a common-prime block contains `N^(2L/(L+1)+o(1))` annular coordinates, yet under a prior Mertens exponent its entire signed contribution collapses to the smaller horizon `N^(2L/(L+1))` and is power-cheaper.

This does **not** resolve `CLUE-parity-sensitive-annular-transfer`, but it narrows it materially. The remaining target is no longer merely "find arithmetic cancellation in a supercritical omitted complement." One such complement is now explicit. The decisive question is whether the **retained** source-coupled statistic created by this arithmetic split has an independent sub-old-exponent estimate, and whether that estimate can be made uniform enough to close the `MC-027` iteration and scale-coverage ledger.