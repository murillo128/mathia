# FD-136 — logarithmically scale-balanced prime ancestry decay still does not recover Möbius

**Status:** `EXACT-CONSTRUCTION + SQUAREFREE-ERDOS-KAC-AUXILIARY + APPROXIMATE-ANCESTRY + HARMONIC-SCALE-WEIGHTING + ALMOST-FULL-PRIME-UNIFORMITY + COMMON-SOURCE + FIXED-RANK-ANCHOR + POSITIVE-LOGARITHMIC-DENSITY-MOBIUS-DISAGREEMENT + NEGATIVE/OBSTRUCTION`.

`FD-130`--`FD-134` show that counting-measure averages of prime-ancestry defects can vanish while a squarefree-unit source remains macroscopically non-Möbius. `FD-135` then pins the opposite endpoint: a genuinely local `L^infinity` condition becomes exact ancestry and has a sharp rough-core recovery threshold. A natural intermediate repair is to keep averaging but balance multiplicative scales, so that the huge population of large parents cannot dilute defects occurring at smaller parent scales.

The critical multiplicative weight `1/n` does exactly that: every fixed-ratio interval `[T,2T]` carries comparable total weight. Nevertheless it still does not coerce Möbius. The same common source used in `FD-132`--`FD-134` defeats the logarithmically scale-balanced ancestry norm throughout the same almost-full active-prime regime, while its disagreement with Möbius has positive logarithmic density under the **same** `1/n` weighting.

For a prime `p`, horizon `H`, and fixed `1<=r<infinity`, put
\[
X:=\frac Hp,
\qquad
\mathcal E_{p,H}
:=
\{n\le X:n\text{ squarefree},\ p\nmid n\},
\tag{1}
\]
and define the harmonic primewise ancestry defect
\[
\boxed{
\mathfrak L_{p,r,H}(a)
:=
\frac{
\displaystyle\sum_{n\in\mathcal E_{p,H}}
\frac{|a_{pn}+a_n|^r}{n}
}{
\displaystyle\sum_{n\in\mathcal E_{p,H}}\frac1n
}.
}
\tag{2}
\]

Let `P=P(H)` satisfy `2<=P(H)<H`, define
\[
Y(H):=\frac{H}{P(H)},
\tag{3}
\]
and assume exactly the scale conditions from `FD-134`:
\[
Y(H)\longrightarrow\infty
\tag{4}
\]
and
\[
\boxed{
1+\log\!\left(\frac{\log H}{\log Y(H)}\right)
=o\!\left(\sqrt{\log\log Y(H)}\right).
}
\tag{5}
\]
Then for every fixed integer `K>=0` there is one squarefree-supported unit-sign source `a^(K)`, independent of `H`, `P`, and `r`, such that
\[
a^{(K)}_n=\mu(n)
\qquad(\omega(n)\le K),
\tag{6}
\]
while for every fixed finite `r>=1`,
\[
\boxed{
\sup_{\substack{p\le P(H)\\p\text{ prime}}}
\mathfrak L_{p,r,H}(a^{(K)})
\longrightarrow0.
}
\tag{7}
\]
At the same time the disagreement is not lost under logarithmic weighting. If
\[
\mathfrak C_{r,H}(a)
:=
\frac{
\displaystyle\sum_{n\le H}\frac{|a_n-\mu(n)|^r}{n}
}{
\displaystyle\sum_{n\le H}\frac1n
},
\tag{8}
\]
then
\[
\boxed{
\mathfrak C_{r,H}(a^{(K)})
\longrightarrow
\frac{2^{r-1}}{\zeta(2)}>0.
}
\tag{9}
\]
Equivalently, the logarithmic density of the coefficient-disagreement set itself is
\[
\boxed{
\frac{
\displaystyle\sum_{\substack{n\le H\\a_n^{(K)}\ne\mu(n)}}\frac1n
}{
\displaystyle\sum_{n\le H}\frac1n
}
\longrightarrow
\frac1{2\zeta(2)}=\frac3{\pi^2}.
}
\tag{10}
\]

Thus replacing counting measure by the natural multiplicative Haar-type weight `dn/n` does not repair the ancestry relaxation. There cannot be an `H`-uniform coercivity inequality that bounds the harmonic coefficient distance (8) by a fixed multiple of the worst active-prime harmonic ancestry defect (7) in this source class.

## 1. The witness is the same moving central-rank gauge

Put
\[
\ell(n):=\log\log(n+e^e)
\tag{11}
\]
and on squarefree integers define
\[
b_K(n):=
\begin{cases}
+1,&\omega(n)\le K\text{ or }\omega(n)\le\ell(n),\\
-1,&\omega(n)>K\text{ and }\omega(n)>\ell(n),
\end{cases}
\qquad
a^{(K)}_n:=\mu(n)b_K(n),
\tag{12}
\]
with `a_n^(K)=0` on nonsquarefree integers.

This is exactly the common infinite source of `FD-132`--`FD-134`. For every admissible ancestry edge `n -> pn`,
\[
a^{(K)}_{pn}+a^{(K)}_n
=
\mu(n)\bigl(b_K(n)-b_K(pn)\bigr),
\tag{13}
\]
so an edge defect is either `0` or has magnitude exactly `2`.

The source agrees with Möbius at every fixed rank at most `K`. Once `ell(n)>K`, disagreement is equivalent to `n` being squarefree and
\[
\omega(n)>\ell(n).
\tag{14}
\]
The squarefree Erdős--Kac law therefore gives the natural-density statement already used in `FD-132`--`FD-134`:
\[
D_K(x)
:=
\#\{n\le x:a_n^{(K)}\ne\mu(n)\}
=
\left(\frac1{2\zeta(2)}+o(1)\right)x.
\tag{15}
\]
Partial summation immediately preserves that density under the weight `1/n`:
\[
\sum_{\substack{n\le H\\a_n^{(K)}\ne\mu(n)}}\frac1n
=
\frac{D_K(H)}H+
\int_1^H\frac{D_K(t)}{t^2}\,dt
=
\left(\frac1{2\zeta(2)}+o(1)\right)\log H.
\tag{16}
\]
Since `sum_(n<=H) 1/n = log H+O(1)`, equation (16) proves (10); multiplying by `2^r` on every disagreement proves (9).

So the logarithmic reweighting does not make the witness itself sparse. The only question is whether it makes the ancestry interface visible.

## 2. The denominator has uniformly full logarithmic mass

Fix an active prime `p<=P(H)` and again write `X=H/p`. Then `X>=Y(H)->infinity` uniformly over all active primes.

Let
\[
E_p(t)
:=
\#\{n\le t:n\text{ squarefree},\ p\nmid n\}.
\tag{17}
\]
Using the elementary squarefree count
\[
Q(t)=\frac{t}{\zeta(2)}+O(\sqrt t)
\tag{18}
\]
and subtracting all multiples of `p` gives, uniformly in every prime `p`,
\[
E_p(t)
\ge
Q(t)-\frac tp
\ge
\left(\frac1{\zeta(2)}-\frac12\right)t+O(\sqrt t).
\tag{19}
\]
The coefficient in parentheses is positive. Hence there are absolute constants `c_0>0` and `T_0` such that
\[
E_p(t)\ge c_0t
\qquad(t\ge T_0)
\tag{20}
\]
for every prime `p`.

Partial summation now gives
\[
\sum_{n\in\mathcal E_{p,H}}\frac1n
=
\frac{E_p(X)}X+
\int_1^X\frac{E_p(t)}{t^2}\,dt
\ge
c_0\log X+O(1).
\tag{21}
\]
Thus the denominator in (2) is `Omega(log X)` uniformly in the whole growing prime family. The harmonic norm genuinely keeps `Theta(log X)` multiplicative-scale mass; its vanishing below is not caused by a collapsing normalization.

## 3. A small logarithmic prefix costs only a small fraction of the norm

Fix temporarily a real `0<epsilon<1/2`. Split the parents into
\[
n\le X^\epsilon
\qquad\text{and}\qquad
X^\epsilon<n\le X.
\tag{22}
\]
No arithmetic information is needed for the first part. Since every defective edge has magnitude `2`,
\[
\sum_{\substack{n\in\mathcal E_{p,H}\\n\le X^\epsilon}}
\frac{|a^{(K)}_{pn}+a^{(K)}_n|^r}{n}
\le
2^r\sum_{n\le X^\epsilon}\frac1n
=
2^r\epsilon\log X+O_r(1).
\tag{23}
\]
By (21), this prefix contributes only `O_r(epsilon)` to (2), uniformly in `p`.

This is the key geometric difference from counting measure. The interval `[1,X^epsilon]` may contain `X^epsilon` integers, but under `1/n` it occupies only an `epsilon` fraction of the total logarithmic scale. We may therefore discard it, prove uniform anti-concentration on the remaining multiplicative scales, and send `epsilon` to zero only after the horizon tends to infinity.

## 4. Every remaining bad edge lies in a thin central strip on its own dyadic scale

For `n>X^epsilon`, equation (4) implies `n->infinity` uniformly, so for large `H` we have `ell(n)>K+1`. Write `m=omega(n)`. As in `FD-134`, a sign change across `n -> pn` can occur only if the integer `m` lies between the parent and child thresholds. Hence
\[
|m-\ell(n)|
\le
1+\ell(pn)-\ell(n).
\tag{24}
\]
Because `pn<=H` and `n>X^epsilon`,
\[
0\le\ell(pn)-\ell(n)
\le
\ell(H)-\ell(X^\epsilon).
\tag{25}
\]
Using `X>=Y(H)`, for fixed `epsilon` this gives
\[
\ell(H)-\ell(X^\epsilon)
\le
\log\!\left(\frac{\log H}{\log Y(H)}\right)
+O_\epsilon(1).
\tag{26}
\]
Define
\[
V_{H,\epsilon}
:=
C_\epsilon
+C\log\!\left(\frac{\log H}{\log Y(H)}\right)
\tag{27}
\]
with an absolute `C` and a sufficiently large constant `C_epsilon`. Condition (5) implies
\[
\frac{V_{H,\epsilon}}
{\sqrt{\log\log Y(H)}}
\longrightarrow0
\qquad(H\to\infty)
\tag{28}
\]
for every fixed `epsilon`.

Now partition `(X^epsilon,X]` into dyadic shells
\[
\frac T2<n\le T.
\tag{29}
\]
For every such shell, `T>=X^epsilon>=Y^epsilon` up to an irrelevant factor `2`. Uniformly for `T/2<n<=T`,
\[
\ell(n)=\log\log T+o(1).
\tag{30}
\]
Consequently every bad parent in the shell lies in
\[
\boxed{
|\omega(n)-\log\log T|
\le V_{H,\epsilon}+o(1).
}
\tag{31}
\]
Moreover
\[
\log\log T
\ge
\log\log(Y^\epsilon/2)
=
\log\log Y+O_\epsilon(1),
\tag{32}
\]
so (28) also gives
\[
\sup_{T\ge Y^\epsilon/2}
\frac{V_{H,\epsilon}+o(1)}{\sqrt{\log\log T}}
\longrightarrow0.
\tag{33}
\]

## 5. Ordinary squarefree Erdős--Kac already controls every logarithmic shell

No weighted Erdős--Kac theorem is needed. Let
\[
Z_T(n)
:=
\frac{\omega(n)-\log\log T}{\sqrt{\log\log T}}
\tag{34}
\]
on squarefree integers `n<=T`. The squarefree Erdős--Kac theorem says that for every fixed real threshold, the distribution of `Z_T` converges to the standard Gaussian distribution.

Fix `eta>0`. By (33), for all sufficiently large `H`, every event in (31) is contained in
\[
|Z_T(n)|\le\eta
\tag{35}
\]
for every shell top `T>=Y^epsilon/2`. Since the ordinary Erdős--Kac convergence is eventually valid for **all** sufficiently large `T`, and the smallest allowed `T` tends to infinity, we obtain a quantity
\[
\delta_{H,\epsilon}\longrightarrow0
\tag{36}
\]
such that uniformly for every relevant shell,
\[
\#\{n\le T:n\text{ squarefree and satisfying }(31)\}
\le
\delta_{H,\epsilon}T.
\tag{37}
\]
The usual fixed-`eta` Gaussian mass is sent to zero after the horizon threshold is chosen; equivalently, (37) is the same shrinking-central-window argument used in `FD-134`, now applied separately at every dyadic parent scale.

Inside a shell `(T/2,T]`, each reciprocal weight is at most `2/T`. Hence the total reciprocal weight of bad parents in that shell is at most
\[
\frac2T\,\delta_{H,\epsilon}T
=2\delta_{H,\epsilon}.
\tag{38}
\]
There are at most `O(log X)` dyadic shells between `X^epsilon` and `X`. Therefore
\[
\sum_{\substack{n\in\mathcal E_{p,H}\\X^\epsilon<n\le X}}
\frac{|a^{(K)}_{pn}+a^{(K)}_n|^r}{n}
\le
C_r\delta_{H,\epsilon}\log X.
\tag{39}
\]
Combining (23), (39), and the denominator bound (21) gives
\[
\sup_{p\le P(H)}
\mathfrak L_{p,r,H}(a^{(K)})
\le
C_r'\bigl(\epsilon+\delta_{H,\epsilon}\bigr)+o(1).
\tag{40}
\]
First let `H->infinity` with `epsilon` fixed, so `delta_(H,epsilon)->0`; then let `epsilon->0`. This proves (7).

The order of these limits is load-bearing. Nothing here claims an Erdős--Kac error term uniform as `epsilon->0`, nor is one needed.

## 6. The same almost-full prime breadth remains available

The active-prime condition is exactly the one in `FD-134`. Writing
\[
P(H)=H^{1-\delta(H)},
\qquad
Y(H)=H^{\delta(H)},
\tag{41}
\]
condition (5) becomes
\[
\delta(H)\log H\longrightarrow\infty
\tag{42}
\]
and
\[
\log\frac1{\delta(H)}
=o\!\left(
\sqrt{\log\bigl(\delta(H)\log H\bigr)}
\right).
\tag{43}
\]
Thus the harmonic obstruction is not confined to a fixed polynomial prime family. For example, the same source passes the logarithmically weighted ancestry test simultaneously for every prime
\[
p\le H^{1-\exp(- (\log\log H)^{1/3})}
\tag{44}
\]
while (9)--(10) keep a fixed positive amount of coefficient error under logarithmic weighting.

This matters because `1/n` is the critical scale-balancing choice: every dyadic shell contributes `Theta(1)` denominator mass. The failure of (7) is therefore not the old mechanism in which the final shell simply overwhelms all earlier defects. Instead the moving central-rank interface is sparse **inside essentially every multiplicative shell**, and the harmonic norm adds many individually sparse shells.

## 7. What this closes and what remains open

`FD-135` shows that hard local control removes dilution entirely but immediately collapses to exact rough-core reconstruction in the squarefree-unit class. The present result shows that one particularly natural attempt to stop dilution without going all the way to `L^infinity` still fails: balancing physical parent scales logarithmically does not give enough resolution in multiplicative **rank**.

The next intermediate norm must therefore localize more than scale alone. Possibilities not ruled out here include rank-conditioned harmonic ancestry, simultaneous short-window control in both `log n` and `omega(n)`, a norm assigning nonvanishing mass to every `o(sqrt(log log n))` rank interface, genuinely local quantiles rather than means, or a destination-side Fourier-skeleton coercivity argument that bypasses coefficient recovery.

The obstruction remains limited to the ancestry-to-source step. It does not construct a source satisfying the physical Mertens partial-sum envelope, does not saturate the repeated-square Fourier skeleton, and does not by itself improve or contradict the Franel/RH boundary.

## 8. Adversarial and prior-art audit

Several possible loopholes were checked. The denominator in (2) is uniformly `Omega(log X)` even for `p=2`, so the conclusion is not an artifact of a sparse admissible-parent set. The small-parent discard in (23) is controlled in the **same harmonic measure** as the theorem, not by counting density. On the large-parent region, the proof does not infer harmonic anti-concentration from a single global `o(X)` count; it decomposes into dyadic shells and applies the squarefree Erdős--Kac anti-concentration at each shell's own scale. This avoids the false inference that an `o(X)` exceptional set must have `o(log X)` reciprocal mass.

The witness is one infinite source independent of `H`, `P`, `p`, and `r`; only `K` is fixed in advance. The active-prime supremum is taken after `P(H)` grows. Equation (5) is retained exactly; the proof does not claim that `Y(H)->infinity` alone is sufficient. The coefficient-side obstruction is also measured logarithmically, so the result cannot be dismissed as comparing two incompatible notions of largeness.

The only non-elementary input is the same squarefree Erdős--Kac law already anchored in `SOURCES.md` for `FD-132`--`FD-134`: Huixi Li, Biao Wang, Chunlin Wang and Shaoyun Yi, *Some ergodic theorems over squarefree numbers and squarefull numbers*, Acta Arithmetica **221** (2025), 117--140, DOI `10.4064/aa240909-18-6`, arXiv `2405.18157`. The passage from counting anti-concentration to reciprocal-weight anti-concentration is proved above by dyadic decomposition and partial summation.

A targeted prior-art search finds a broader literature on weighted Erdős--Kac theorems, including Kai (Steve) Fan, *Weighted Erdős--Kac theorems via computing moments*, Acta Arithmetica **217** (2025), 99--158, DOI `10.4064/aa231014-9-8`. No weighted limit theorem from that literature is load-bearing here, and no direct result was found that supplies the line-specific combination (7)--(10). No novelty is claimed for weighted Gaussian laws themselves. The durable delta is the matched-control statement that the natural `1/n` scale balancing still leaves the approximate ancestry relaxation noncoercive, even against a coefficient error that remains positive in the same logarithmic measure. Consequently `SOURCES.md` does not change.
