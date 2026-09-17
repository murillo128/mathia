# FD-174 — Integer geometric midpoint ladders have explicit finite-scale certification

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** quantitative sparse acquisition / prime-power recurrence / finite-scale target certification
- **Depends on:** FD-170, FD-172, FD-173
- **Classification:** `EXACT-DERIVED + SOURCE-RESTRICTED + QUANTITATIVE-ACQUISITION + TARGET-CERTIFICATION`

## Claim

`FD-173` proves that every fixed integer geometric ladder

\[
\mathcal H_B=\{B,B^2,B^3,\ldots\},\qquad B\in\mathbb Z,\ B\ge2,
\]

is exactly Möbius-target-rigid inside the bounded squarefree multiplicative source class, because every odd-prime power orbit eventually enters one observed annulus `(B^k/2,B^k]`. That proof is qualitative: density of an irrational rotation gives no finite source-scale certification bound.

For an integer base `B>=3`, define

\[
Q_B:=\lfloor\log_2 B\rfloor+1,
\qquad
C_B:=Q_B\bigl(1+\sqrt B\,\log B\bigr).
\tag{1}
\]

Then every odd prime `p` has a positive power `p^j` in a geometric observation annulus with the explicit bounds

\[
\boxed{
1\le j\le C_B p^{Q_B},
\qquad
1\le k\le C_B p^{Q_B}\log_B p+1,
\qquad
\frac{B^k}{2}<p^j\le B^k.
}
\tag{2}
\]

The endpoint equality in (2) occurs only in the rational-log case and is harmless. Consequently, for every source cutoff `X>=3`, the first

\[
\boxed{
K_B(X)
:=
\left\lceil C_B X^{Q_B}\log_B X\right\rceil+1
}
\tag{3}
\]

geometric midpoint samples already certify every prime coordinate up to `X`. More precisely, if `a` is multiplicative with

\[
a(1)=1,
\qquad
a(p^r)=0\quad(r\ge2),
\qquad
-1\le a(p)\le1,
\tag{4}
\]

and

\[
E_H:=P_a(H)-P_\mu(H),
\tag{5}
\]

then

\[
\sup_{1\le k\le K_B(X)}|E_{B^k}|\le\varepsilon
\tag{6}
\]

implies

\[
\boxed{
0\le1+a(p)\le2\varepsilon
\qquad(p\le X\text{ prime}).
}
\tag{7}
\]

For `epsilon<=1/2`, every squarefree `n<=X` therefore satisfies

\[
\boxed{
|a(n)-\mu(n)|\le2\varepsilon\,\omega(n).
}
\tag{8}
\]

At exact agreement, the same finite sample prefix forces `a(n)=mu(n)` for all `n<=X`.

For `B=2`, `FD-172` is much sharper: one may take

\[
K_2(X)=\lceil\log_2 X\rceil,
\tag{9}
\]

so the largest required horizon is only `O(X)`. For fixed `B>=3`, (3) is deliberately crude but completely elementary:

\[
K_B(X)=O_B\!\left(X^{Q_B}\log X\right),
\tag{10}
\]

while the largest observed horizon obeys

\[
B^{K_B(X)}
=
\exp\!\left(O_B(X^{Q_B}\log X)\right).
\tag{11}
\]

Thus `FD-173`'s infinite-horizon recurrence can be made effective without Baker theory or a quantitative equidistribution theorem. The price is a very large, and not claimed optimal, source-scale-to-horizon bound.

## 1. Reduce prime-power hitting to a one-sided rotation window

Fix `B>=3` and an odd prime `p`. Put

\[
\alpha:=\log_B p,
\qquad
L:=\log_B2.
\tag{12}
\]

A pair `(j,k)` satisfies

\[
\frac{B^k}{2}<p^j<B^k
\tag{13}
\]

exactly when

\[
0<k-j\alpha<L.
\tag{14}
\]

Equivalently, if `j alpha` is not an integer, we need

\[
\{j\alpha\}>1-L,
\tag{15}
\]

and then `k=ceil(j alpha)` works. Since `B>2`,

\[
0<L<1.
\tag{16}
\]

The qualitative proof in `FD-173` uses density of the irrational rotation `{j alpha}`. To make it effective, only a very low-denominator near-return to an integer is needed.

## 2. A bounded-denominator near-return is enough

Let

\[
Q:=Q_B=\lfloor\log_2B\rfloor+1.
\tag{17}
\]

Because `Q>log_2 B=1/L`,

\[
\frac1Q<L.
\tag{18}
\]

Assume first that `alpha` is irrational. Apply the elementary Dirichlet pigeonhole argument to the `Q+1` fractional parts

\[
0,\alpha,2\alpha,\ldots,Q\alpha.
\]

Two lie in the same one of `Q` equal subintervals of the unit circle, so for some `1<=q<=Q`,

\[
0<\delta:=\|q\alpha\|<\frac1Q<L.
\tag{19}
\]

Choose the nearest integer `m` so that

\[
q\alpha-m=\pm\delta.
\tag{20}
\]

If the sign is negative, then

\[
\{q\alpha\}=1-\delta>1-L,
\tag{21}
\]

so `j=q` already hits the required one-sided window.

If the sign is positive, let

\[
n:=\left\lfloor\frac{1-L}{\delta}\right\rfloor+1.
\tag{22}
\]

Then

\[
1-L<n\delta\le1-L+\delta<1.
\tag{23}
\]

Hence no wrap occurs and

\[
\{nq\alpha\}=n\delta>1-L.
\tag{24}
\]

Thus `j=nq` hits the same window. In either case,

\[
j\le Q\left(1+\frac1\delta\right).
\tag{25}
\]

The remaining task is to keep `delta` from being arbitrarily tiny. This is where the **integer** nature of the geometric base becomes load-bearing.

## 3. Integer separation gives a polynomial first-hit exponent

From (20),

\[
\delta\log B
=
\left|\log(p^q)-\log(B^m)\right|.
\tag{26}
\]

Because `alpha` is irrational, `p^q` and `B^m` are distinct positive integers. Therefore

\[
|p^q-B^m|\ge1.
\tag{27}
\]

For positive `x,y`,

\[
|\log x-\log y|
\ge
\frac{|x-y|}{\max(x,y)}.
\tag{28}
\]

Also `delta<1/Q<=1/2`, and therefore

\[
\frac{B^m}{p^q}=B^{m-q\alpha}
\in[B^{-1/2},B^{1/2}].
\tag{29}
\]

Combining (26)--(29),

\[
\delta\log B
\ge
\frac1{\sqrt B\,p^q},
\]

hence

\[
\boxed{
\delta
\ge
\frac1{\sqrt B\,\log B\,p^q}
\ge
\frac1{\sqrt B\,\log B\,p^Q}.
}
\tag{30}
\]

Insert (30) into (25):

\[
j
\le
Q\left(1+\sqrt B\,\log B\,p^Q\right)
\le
C_Bp^Q.
\tag{31}
\]

Once (15) holds, set

\[
k:=\lceil j\alpha\rceil.
\tag{32}
\]

Then

\[
0<k-j\alpha<L,
\]

so (13) holds, and

\[
k
\le
j\log_Bp+1
\le
C_Bp^Q\log_Bp+1.
\tag{33}
\]

This proves (2) in the irrational-log case.

## 4. The rational-log case is easier

Suppose now that `alpha=log_B p` is rational. Write `alpha=r/s` with positive integers `r,s`. Then

\[
p^s=B^r.
\tag{34}
\]

Unique factorization implies that `B` itself is a power of `p`: say `B=p^d`. In particular, the first observed horizon already contains a prime-power witness at its closed right endpoint,

\[
p^d=B\in(B/2,B].
\tag{35}
\]

So the rational case is detected at `k=1` and is automatically covered by the much looser bounds in (2).

This split is useful conceptually. Irrational rotation supplies recurrence; discrete integer separation makes that recurrence effective at a polynomial exponent cost. No lower bound for a general linear form in logarithms is required because Dirichlet first reduces the denominator to the fixed range `q<=Q_B`.

## 5. Uniform certification through source scale X

Fix `X>=3`. For each odd prime `p<=X`, sections 2--4 produce a witness with

\[
k
\le
C_Bp^{Q_B}\log_Bp+1
\le
C_BX^{Q_B}\log_BX+1
\le
K_B(X).
\tag{36}
\]

The prime `2` needs no annulus hit: by the midpoint identity used in `FD-172`--`FD-173`, any observed horizon `H>=2` already controls its defect.

Now apply the quantitative witness inequality from `FD-173`. If `p^j` lies in the observed annulus `(B^k/2,B^k]`, then

\[
0\le1+a(p)\le -2E_{B^k}.
\tag{37}
\]

Admissibility gives `E_H<=0`, so (6) implies (7). For `epsilon<=1/2`, write on squarefree `n`

\[
a(n)=\mu(n)\prod_{p\mid n}(1-\delta_p),
\qquad
\delta_p:=1+a(p)\in[0,2\varepsilon].
\tag{38}
\]

Then

\[
1-\prod_{p\mid n}(1-\delta_p)
\le
\sum_{p\mid n}\delta_p
\le
2\varepsilon\omega(n),
\tag{39}
\]

which proves (8).

At `epsilon=0`, every prime `p<=X` is exactly Möbius. Every `n<=X` has only prime factors at most `X`, so multiplicativity and squarefree support give exact coefficient agreement throughout the full prefix `n<=X`.

The certification cost in **number of geometric samples** is therefore polynomial in `X` for each fixed integer base `B`, even though the largest sampled horizon is exponentially larger than that index.

## 6. Why this matters

`FD-173` separated exact infinite-horizon rigidity from efficient finite-scale certification but left the latter qualitative. The present bound closes the first existence question: fixed integer geometric ladders do not merely detect every prime eventually; there is an explicit finite prefix that certifies every source coordinate through any prescribed finite scale.

The mechanism is stronger than merely invoking equidistribution. The relevant recurrence window has fixed length `log_B2`. Dirichlet compresses the problem to one near-return with denominator at most `Q_B=O(log B)`, after which the fact that `p^q` and `B^m` are distinct integers prevents that near-return from being too small. This yields an elementary polynomial bound on the required prime-power exponent.

The result is not an efficiency claim. For `B>2`, the bound

\[
B^{K_B(X)}=\exp(O_B(X^{Q_B}\log X))
\]

is enormous and likely far from optimal. Its value is structural: it turns the orbit-hitting criterion into a genuinely quantitative finite-scale theorem without importing deep Diophantine approximation.

## 7. Representation audit

The generic layer is a one-sided irrational-rotation hitting problem plus the elementary separation of two distinct integers. Any sensing architecture in which a persistent defect is repeated along powers and observations cover logarithmic windows could inherit the same recurrence argument.

The Farey/Möbius-specific layer enters before this recurrence step. `FD-170` identifies the midpoint transform, and `FD-172`--`FD-173` use squarefree multiplicativity and `a(p)>=-1` to turn a prime defect into nonnegative mass repeated at every `p^j`. Without that repeated positive orbit, the logarithmic hitting theorem would certify nothing about the original source.

The integer-base hypothesis is also genuinely load-bearing for the quantitative bound. It turns a small `|q log_B p-m|` into a comparison of the distinct integers `p^q` and `B^m`. A nonintegral geometric ratio does not provide the elementary separation (27); quantitative certification there depends on the Diophantine type of the logarithmic ratio.

This remains a source-identification theorem, not a Franel--Landau estimate. It does not create cancellation, improve the RH-critical discrepancy norm, or bridge coefficient coercivity to destination coercivity.

## 8. Prior-art / source check

A focused search around one-sided Diophantine approximation, irrational-rotation hitting times, geometric progressions modulo one, prime powers, and sparse Farey/Möbius sensing found substantial general literature on one-sided inhomogeneous approximation and rotation hitting problems, but no source-specific finite-scale midpoint certification statement of the form above.

No external theorem is load-bearing here. The approximation step is the elementary finite pigeonhole proof of Dirichlet approximation; the quantitative lower bound uses only unique factorization, integrality of `p^q` and `B^m`, and the elementary logarithm inequality (28). Therefore `SOURCES.md` requires no new dependency.

The claim should not be read as a novelty statement about quantitative irrational rotations in general. The additional Mathia-specific content is the combination of a fixed-width logarithmic annulus, a bounded-denominator approximation, integer separation, and the prime-power defect repetition supplied by `FD-173`.

## 9. Boundaries and next decisive tests

The exponent `Q_B=floor(log_2 B)+1` and constant `C_B` are proof-driven rather than sharp. A better quantitative orbit theorem could reduce the certification prefix dramatically, and arithmetic information about `log_B p` may improve individual primes. No matching lower bound is claimed.

The proof also does not weaken the source assumptions from `FD-173`. Squarefree multiplicativity and primewise nonnegativity remain responsible for converting midpoint error into monotone defect mass. The unrestricted formal-source null directions of `FD-171` are untouched.

Two distinct questions remain after this result. First, determine the true worst-case first-hit growth for integer geometric ladders and whether the crude polynomial sample-index exponent can be reduced. Second, determine whether comparable finite-scale certification survives under weaker source architecture, especially squarefree/ternary but nonmultiplicative sources. Pairwise sparse inversion is still separate from Möbius-target certification.

## Related findings

- `FD-170` — consecutive midpoint horizons invert unrestricted sources through odd-indicator convolution.
- `FD-171` — unrestricted sparse midpoint sensing has exact permanent null directions.
- `FD-172` — dyadic horizons rigidify bounded squarefree multiplicative sources with a prime-defect stability modulus.
- `FD-173` — prime-power annulus hitting exactly characterizes sparse midpoint target-rigidity and proves qualitative rigidity of every fixed integer geometric ladder.