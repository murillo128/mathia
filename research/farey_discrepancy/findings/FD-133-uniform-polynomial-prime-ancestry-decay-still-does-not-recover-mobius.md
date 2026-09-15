# FD-133 — uniform polynomial-prime ancestry decay still does not recover Möbius

**Status:** `EXACT-DERIVED + SQUAREFREE-ERDOS-KAC-AUXILIARY + APPROXIMATE-ANCESTRY + GROWING-PRIME-UNIFORMITY + COMMON-SOURCE + FIXED-RANK-ANCHOR + POSITIVE-DENSITY-MOBIUS-DISAGREEMENT + NEGATIVE/OBSTRUCTION`.

`FD-132` leaves one immediate repair genuinely open: its central-rank witness has vanishing ancestry defect for every **fixed** prime, but the proof there imports squarefree Erdős--Kac only after excluding that fixed prime and therefore does not justify a growing-prime supremum such as
\[
\sup_{p\le P(H)}\mathfrak P_{p,r,H}(a)\longrightarrow0.
\]

For every fixed power cutoff `P(H)=H^alpha` with `0<alpha<1`, that repair is still insufficient. In fact, the **same common infinite source** from `FD-132` already satisfies the stronger uniform statement. The key is that no Erdős--Kac theorem uniform in `p` is needed: every bad edge for every `p<=H^alpha` can be embedded into one unconditioned fixed-width central `omega` strip at the parent scale, while the prime-exclusion denominator has a uniform elementary lower bound.

For a prime `p`, horizon `H`, and fixed `1<=r<infinity`, retain
\[
\mathcal E_{p,H}
:=
\{n\le H/p:n\text{ squarefree},\ p\nmid n\},
\qquad
\mathfrak P_{p,r,H}(a)
:=
\frac1{|\mathcal E_{p,H}|}
\sum_{n\in\mathcal E_{p,H}}|a_{pn}+a_n|^r.
\tag{1}
\]

Then for every fixed `K>=0` there is one squarefree-supported unit-sign source `a^(K)` such that
\[
a^{(K)}_n=\mu(n)\qquad(\omega(n)\le K),
\tag{2}
\]
and, **for every fixed `0<alpha<1` and every fixed finite `r>=1`**, 
\[
\boxed{
\sup_{\substack{p\le H^\alpha\\p\ {m prime}}}
\mathfrak P_{p,r,H}(a^{(K)})
\longrightarrow0
}
\qquad(H\to\infty),
\tag{3}
\]
while
\[
\boxed{
\frac1H\#\{n\le H:a^{(K)}_n\ne\mu(n)\}
\longrightarrow\frac1{2\zeta(2)}=\frac3{\pi^2}.
}
\tag{4}
\]

Thus even ancestry control that is simultaneous over a polynomially growing family of prime directions does not coerce the source toward Möbius. The remaining multiplicative route has to retain more than primewise mean control alone: for example simultaneous visibility in **rank and prime direction**, genuinely local/`L^infinity` ancestry, a growing exact anchor strong enough to freeze the moving gauge, or a direct destination-side Fourier-skeleton estimate.

## 1. The central-rank source is independent of the active prime cutoff

As in `FD-132`, put
\[
\ell(n):=\log\log(n+e^e)
\tag{5}
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
\tag{6}
\]
with `a_n^(K)=0` on nonsquarefree integers.

This is one infinite source; it does not depend on `H`, `p`, `alpha`, or `r`. Equation (2) is immediate. For an admissible edge `n -> pn`, both endpoints are squarefree and
\[
a^{(K)}_{pn}+a^{(K)}_n
=
\mu(n)\bigl(b_K(n)-b_K(pn)\bigr),
\tag{7}
\]
so every bad edge has magnitude exactly `2`.

The coefficient disagreement statement (4) is exactly the density calculation of `FD-132`: once `ell(n)>K`, disagreement is equivalent to `n` being squarefree with `omega(n)>ell(n)`. Squarefree Erdős--Kac places asymptotically one half of the squarefree integers on that side of the central threshold, while squarefree integers themselves have density `1/zeta(2)`.

The new issue is therefore only whether the bad ancestry edges remain sparse **uniformly for all primes up to `H^alpha`**.

## 2. Every active prime crosses the gauge only in one fixed-width central strip

Fix once and for all `0<alpha<1`, and let
\[
p\le H^\alpha,
\qquad
X:=H/p.
\tag{8}
\]
Then
\[
X\ge H^{1-\alpha}\longrightarrow\infty
\tag{9}
\]
uniformly over all active primes.

Discard temporarily the parents `n<=sqrt(X)`. Their number is only `O(sqrt(X))`, uniformly in `p`. For `sqrt(X)<n<=X`, equation (9) makes `n` tend to infinity uniformly over the active family, so for sufficiently large `H` we have `ell(n)>K+1` and the finite anchor no longer participates in a bad edge.

Write
\[
m:=\omega(n),\qquad
L_1:=\ell(n),\qquad
L_2:=\ell(pn)-1.
\tag{10}
\]
In this large-parent range, the parent gauge is `+1` exactly when `m<=L_1`, while the child gauge is `+1` exactly when
\[
m+1\le\ell(pn),
\quad\text{i.e.}\quad
m\le L_2.
\tag{11}
\]
Hence the two signs differ only when the integer `m` lies between the two real thresholds `L_1` and `L_2`. In particular,
\[
|m-\ell(n)|
\le
1+\ell(pn)-\ell(n).
\tag{12}
\]

The threshold displacement is uniformly bounded for `p<=H^alpha`. Since `pn<=H` and `n>sqrt(X)`, monotonicity of `ell` gives
\[
0\le\ell(pn)-\ell(n)
\le
\ell(H)-\ell(\sqrt X).
\tag{13}
\]
Using `X>=H^(1-alpha)` and `ell(t)=log log t+o(1)` uniformly once `t` is bounded below by a quantity tending to infinity,
\[
\ell(H)-\ell(\sqrt X)
\le
\log\frac{2}{1-\alpha}+o(1).
\tag{14}
\]
Likewise, throughout `sqrt(X)<n<=X`,
\[
|\ell(n)-\log\log X|
\le
\log2+o(1).
\tag{15}
\]

Combining (12)--(15), there is a constant `C_alpha<infinity`, independent of `H`, `p`, and `n`, such that every sufficiently large bad parent outside the discarded square-root prefix satisfies
\[
\boxed{
|\omega(n)-\log\log X|\le C_\alpha.
}
\tag{16}
\]

This is the key strengthening over `FD-132`. There, `p` was fixed before the Erdős--Kac step. Here the entire moving family `p<=H^alpha` is first trapped in the **same kind of fixed-width unconditioned central layer at its own parent scale `X=H/p`**.

## 3. Unconditioned anti-concentration gives uniform primewise decay

For a fixed constant `C`, define
\[
A_C(X)
:=
\#\{n\le X:n\text{ squarefree},\ |ω(n)-\log\log X|\le C\}.
\tag{17}
\]
The squarefree Erdős--Kac theorem with no excluded primes gives
\[
A_C(X)=o(X)
\qquad(X\to\infty).
\tag{18}
\]
Indeed, after normalization by `sqrt(log log X)`, a fixed-width interval around the center shrinks to a point, while the limiting Gaussian distribution is continuous.

Because convergence in (18) is ordinary tail convergence,
\[
\sup_{X\ge Y}\frac{A_C(X)}X\longrightarrow0
\qquad(Y\to\infty).
\tag{19}
\]
Together with `X>=H^(1-alpha)`, equations (16)--(19) show that the number of bad parents is
\[
o(X)+O(\sqrt X)=o(X)
\tag{20}
\]
**uniformly over all primes `p<=H^alpha`**.

It remains only to ensure that the normalization in (1) cannot become small when `p` varies. Let
\[
Q(X):=\#\{n\le X:n\text{ squarefree}\}.
\]
The elementary squarefree count
\[
Q(X)=\frac{X}{\zeta(2)}+O(\sqrt X)
\tag{21}
\]
follows directly from
\[
1_{\rm squarefree}(n)=\sum_{d^2\mid n}\mu(d).
\]
At most `X/p` integers up to `X` are divisible by `p`, hence for every prime `p`
\[
|\mathcal E_{p,H}|
\ge
Q(X)-\frac Xp
\ge
\left(\frac1{\zeta(2)}-\frac12\right)X+O(\sqrt X).
\tag{22}
\]
Since `1/zeta(2)-1/2>0`, the denominator is bounded below by `cX` for one absolute `c>0`, uniformly in the prime direction once `X` is large.

Every bad edge contributes `2^r`, so (20) and (22) yield
\[
\sup_{p\le H^\alpha}\mathfrak P_{p,r,H}(a^{(K)})
\le
\frac{2^r\,o(X)}{cX}
\longrightarrow0,
\tag{23}
\]
where the `o(1)` is uniform because every relevant `X` lies beyond `H^(1-alpha)`. This proves (3).

No squarefree Erdős--Kac estimate uniform in a moving excluded prime is used. Prime exclusion appears only in the denominator, where the crude subtraction `Q(X)-X/p` is already enough.

## 4. What the polynomial active family does and does not buy

`FD-132` established only the quantifier pattern “for every fixed prime `p`, defect tends to zero.” Equation (3) is substantially stronger: at horizon `H` the condition simultaneously monitors every prime up to `H^alpha`, a family containing polynomially many prime coordinates. The same source stays macroscopically wrong in coefficient density while passing all of those mean ancestry tests at once.

This does not contradict `FD-129`. Exact ancestry on a complete growing prime prefix is a pointwise edge law and eventually reconstructs every fixed coefficient. Here every bad edge still has full size `2`; only its **relative frequency inside each active prime direction** tends to zero. Replacing a mean by an edgewise `L^infinity` condition detects the witness immediately.

The result also does not combine the two scale coordinates that the current frontier has separated. The central-rank gauge was designed so that bad edges concentrate near a moving rank boundary. A condition taking a simultaneous supremum over both a growing prime family **and** multiplicative-rank slices is not controlled by this argument and remains a materially stronger hypothesis. Likewise, a growing exact low-rank anchor `K=K(H)`, a nonsummable scale-sensitive norm that magnifies the central layer, or a direct Fourier-skeleton coercivity estimate may still evade the construction.

Finally, (3) is proved only for each fixed `alpha<1`. The argument uses the fixed bound (14). It does not claim uniformity when `alpha=alpha(H)->1`, where the possible threshold displacement grows and quantitative anti-concentration at an expanding central width would have to be tracked separately.

As in `FD-130`--`FD-132`, this is a **stability obstruction**, not a new Fourier-skeleton saturating source. No square-root partial-sum envelope, Franel improvement, or RH implication is obtained.

## 5. Adversarial and prior-art audit

The main failure modes were checked directly. The finite-rank anchor cannot create hidden bad edges in the uniform range because `n>sqrt(X)>=H^((1-alpha)/2)` eventually forces `ell(n)>K+1`. The child remains squarefree because `p` does not divide the squarefree parent. The denominator estimate is uniform even when `p` is comparable with or larger than `X`; it uses only `p>=2`. The central-strip constant depends on fixed `alpha`, which is why no `alpha(H)->1` statement is smuggled into the theorem.

The only non-elementary input is the same squarefree Erdős--Kac law already anchored for `FD-132`: Huixi Li, Biao Wang, Chunlin Wang and Shaoyun Yi, *Some ergodic theorems over squarefree numbers and squarefull numbers*, Acta Arithmetica **221** (2025), 117--140, DOI `10.4064/aa240909-18-6`, arXiv `2405.18157`. Here only the **unconditioned** squarefree Gaussian limit is needed, so this result is strictly less demanding than a theorem uniform in an excluded prime.

A targeted prior-art audit also checked the neighboring low-influence/majority literature for Boolean product spaces and slices. The general phenomenon that a balanced threshold can have small individual coordinate influences is classical, so no novelty is claimed for that abstract mechanism. No source was found that supplies the arithmetic statement (3) for the Möbius prime-ancestry graph or its Farey-discrepancy role directly. The durable mathematical delta is the exact uniform-in-`p<=H^alpha` transplantation, obtained without a uniform excluded-prime distribution theorem, and the resulting elimination of polynomial active-prime mean control as a coefficient-recovery mechanism.
