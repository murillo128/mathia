# MC-330 — Signed bias postprocessing cannot amplify the quartic horizon

**Status:** `EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the fixed-common-modulus endpoint notation of `MC-329`. Let

\[
\beta=(\beta_\chi)_{\chi\in\Xi}\in\mathbf C^m,
\qquad
E(\beta):=\|\beta\|_2^2,
\]

where

\[
\beta_\chi=\frac1{A_y}\sum_{p\in\mathcal A_y}\chi(p).
\]

For the reciprocal endpoint family, write its exact bias vector as `x`; `MC-329` proves

\[
\boxed{
\|x\|_2^2=\frac{2^R}{R}-1.
}
\tag{1}
\]

It also supplies, for every fixed `\delta>0` and every cubefree common modulus `q\le y^{4-\delta}`, an energy bound of the shape

\[
\boxed{
\|\beta\|_2^2
\le U_\delta(y,m)
:=C_\delta\left(1+m y^{-c_\delta}\log y\right).
}
\tag{2}
\]

The natural next escape after `MC-328`–`MC-329` is to retain signs and cross-character information instead of using only positive mode weights or total squared bias. There is, however, an exact limitation:

> **No signed linear or quadratic postprocessing of the already-formed bias vector can improve the endpoint signal relative to the analytic information in `(2)`.**

More precisely, for every complex `m\times m` matrix `K`, define the joint quadratic statistic

\[
Q_K(\beta):=\beta^*K\beta.
\]

Then

\[
\boxed{
|Q_K(\beta)|
\le \|K\|_{\mathrm{op}}\,\|\beta\|_2^2.
}
\tag{3}
\]

Consequently `(2)` gives

\[
|Q_K(\beta)|
\le
\|K\|_{\mathrm{op}}U_\delta(y,m),
\tag{4}
\]

while at the exact endpoint

\[
\boxed{
\sup_{K\ne0}
\frac{|Q_K(x)|}{\|K\|_{\mathrm{op}}}
=
\|x\|_2^2
=
\frac{2^R}{R}-1.
}
\tag{5}
\]

The supremum is already attained by `K=I`, i.e. by the total bias energy used in `MC-329`. It is also attained by the rank-one matched projector

\[
K_x:=\frac{xx^*}{\|x\|_2^2}.
\tag{6}
\]

Thus allowing arbitrary signs, off-diagonal couplings, low rank, or an endpoint-matched quadratic kernel **after** the prime-character transform has been reduced to `(2)` cannot enlarge the normalized endpoint signal beyond the energy argument already used in `MC-329`. In particular it cannot move the fixed-power modulus horizon beyond exponent four.

The same ceiling already holds one degree earlier. For any signed linear combination

\[
L_c(\beta):=c^*\beta,
\]

Cauchy--Schwarz gives

\[
|L_c(\beta)|^2
\le \|c\|_2^2\,\|\beta\|_2^2,
\tag{7}
\]

and

\[
\boxed{
\sup_{c\ne0}
\frac{|L_c(x)|^2}{\|c\|_2^2}
=
\|x\|_2^2.
}
\tag{8}
\]

Equality is attained exactly when `c` is proportional to `x`. Hence even the optimally phase-aligned signed combination is merely a Cauchy-saturated repackaging of the same energy.

This does **not** rule out every joint or signed method. It identifies the precise escape condition: a successful method must control a structured postprocessed transform **before** discarding its structure into the scalar energy bound `(2)`. Equivalently, it must prove a source-natural estimate for a specific operator `B` of the form

\[
\|BT\|_{\mathrm{op}}
\ll
\|B\|_{\mathrm{op}}\,\|T\|_{\mathrm{op}}
\tag{9}
\]

with a genuine strict gain in the relevant arithmetic regime, while the endpoint vector retains a comparably large `\|Bx\|`. Here `T` is the prime-to-character transform. Such a statement would be a new analytic correlation theorem, not postprocessing of Schlage-Puchta's existing energy estimate.

No estimate for `M(x)` follows.

## 1. Arbitrary quadratic kernels are bounded by the same energy

For any vectors `u,v` and any matrix `K`, the operator norm gives

\[
|u^*Kv|
\le
\|K\|_{\mathrm{op}}\,\|u\|_2\,\|v\|_2.
\tag{10}
\]

Taking `u=v=\beta` proves `(3)`. This argument does not require `K` to be positive semidefinite, Hermitian, diagonal, or entrywise nonnegative. Therefore changing from positive mode weights to a signed off-diagonal quadratic kernel does not by itself evade the `MC-329` analytic bill.

At the endpoint, `(10)` gives

\[
\frac{|x^*Kx|}{\|K\|_{\mathrm{op}}}
\le
\|x\|_2^2.
\tag{11}
\]

Taking `K=I` gives equality, proving `(5)`. Taking the projector `(6)` gives equality again because

\[
x^*K_xx=\|x\|_2^2,
\qquad
\|K_x\|_{\mathrm{op}}=1.
\tag{12}
\]

The rank of the kernel therefore does not supply hidden leverage: a rank-one kernel can preserve the entire endpoint signal, but only at exactly the same operator-normalized scale as the full energy.

Now insert the subquartic analytic bound `(2)`. Every quadratic argument whose upper bound is obtained by the chain

\[
|Q_K(\beta)|
\le \|K\|_{\mathrm{op}}\|\beta\|_2^2
\le \|K\|_{\mathrm{op}}U_\delta(y,m)
\tag{13}
\]

can contradict the endpoint only if

\[
\frac{|Q_K(x)|}{\|K\|_{\mathrm{op}}}
>
U_\delta(y,m).
\tag{14}
\]

But `(5)` shows that the left side is at most the exact energy `(1)`. Therefore the strongest possible contradiction obtainable from `(13)` is precisely the one already obtained from `K=I` in `MC-329`. A different quadratic kernel may equal that strength or lose strength; it cannot exceed it.

## 2. Signed linear aggregation is already Cauchy-saturated

Equation `(7)` is Cauchy--Schwarz. At the endpoint,

\[
\frac{|c^*x|^2}{\|c\|_2^2}
\le\|x\|_2^2,
\tag{15}
\]

and equality holds for `c=\lambda x`, `\lambda\ne0`. Thus choosing the signs and phases of the coefficients to match the exact endpoint is not an additional source of signal: it simply saturates the Hilbert-space inequality that turns a coherent scalar sum back into total energy.

This closes a particularly tempting loophole in the interpretation of `MC-329`. Its phrase "signed or joint invariant" cannot mean merely

- form one signed linear combination of the character biases and square it;
- insert an arbitrary Hermitian kernel between two copies of the same bias vector;
- project the bias vector onto an endpoint-selected low-rank subspace; or
- diagonalize/reweight the bias vector and then invoke `(2)` as the only analytic input.

All of these are downstream contractions of the same `\ell^2` information and obey `(5)` or `(8)`.

## 3. The endpoint-matched signed combination is an exact Walsh projector

The endpoint formula itself makes the saturation transparent. On the full cube `\mathbf F_2^R`, let

\[
\chi_s(a):=(-1)^{a\cdot s},
\qquad
\mathbf 1=(1,\ldots,1).
\]

The exact endpoint coefficient is

\[
x(a)
=(-1)^{|a|}\left(1-\frac{2|a|}{R}\right)
=\frac1R\sum_{j=1}^R\chi_{\mathbf1+e_j}(a).
\tag{16}
\]

Therefore its unnormalized Walsh transform is exactly

\[
\boxed{
\widehat x(s)
:=\sum_{a\in\mathbf F_2^R}x(a)\chi_s(a)
=
\begin{cases}
2^R/R,&s\in\{\mathbf1+e_1,\ldots,\mathbf1+e_R\},\\
0,&\text{otherwise}.
\end{cases}
}
\tag{17}
\]

So the optimal signed coefficient vector `c=x` is not discovering a hidden phase relation. It is the exact Fourier projector onto the `R` endpoint Walsh atoms already encoded by the construction. Removing the principal mode `a=0` only introduces the known rank-one constant correction because `x(0)=1`; it does not create a new information channel.

This complements `MC-328`. There, nonnegative endpoint-polynomial weights of Fourier degree `o(R)` could not resolve the forced central source band. Here even an arbitrarily high-degree, perfectly endpoint-matched **signed** linear/quadratic postprocessor cannot gain once the analytic theorem has already compressed the character family to total `\ell^2` energy.

## 4. What a genuine signed/joint escape must prove

Let `T` denote the normalized prime-to-character transform for the chosen common-modulus family, so the observed bias vector is `\beta=T\mathbf1_{\mathcal A_y}`. Schlage-Puchta's theorem, after the normalizations audited in `MC-329`, is an operator-energy statement at the vector used here.

If a postprocessor `B` is applied only after this estimate, then

\[
\|B\beta\|_2
\le
\|B\|_{\mathrm{op}}\|\beta\|_2,
\tag{18}
\]

and the preceding no-go applies. The only possible leverage is to exploit arithmetic interaction between `B` and `T` *before* the generic composition bound, proving that `BT` is substantially smaller on all admissible prime-supported inputs while `Bx` remains large on the exact endpoint.

That requirement separates two mathematically different claims:

1. **postprocessing claim:** choose a clever signed kernel after obtaining the existing bias vector; `(3)`–`(8)` show this has no normalized gain;
2. **new analytic claim:** prove a sharper norm/correlation estimate for a structured transform `BT`; this is not contained in `MC-329` and remains a legitimate research direction.

A higher-order statistic is also not ruled out by this finding unless its estimate factors through the same `\ell^2` energy. The result is deliberately a no-go for **downstream linear/quadratic amplification**, not a claim that all nonlinear or arithmetic joint information is impossible.

## 5. Prior art and novelty boundary

The inequalities `(3)`, `(7)`, and `(18)` are elementary Hilbert-space operator-norm and Cauchy--Schwarz inequalities. The viewpoint that a large-sieve inequality is an operator/duality bound is classical; see H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika **20** (1973), 119–134, DOI `10.1112/S0025579300004708`. No novelty is claimed for any of this functional analysis or large-sieve duality.

The prime-supported energy estimate is exactly the classical input already audited in `MC-329`: Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143–149, DOI `10.4064/aa106-2-4`, Theorem 3. A fresh literature check on 16 September 2026 confirmed the paper's large-sieve-type prime-supported setting and the standard Montgomery--Vaughan large-sieve background; no stronger external theorem is being asserted here.

The Walsh identity `(16)` is the exact endpoint specialization of the Boolean-Fourier calculation already used in `MC-328`; Walsh orthogonality and the Hamming-cube Fourier basis are classical. No novelty is claimed for `(16)`–`(17)`.

The durable line-specific delta is the **boundary statement**: the signed/joint escape left open after `MC-328`–`MC-329` must occur before the family is compressed to total squared bias. Once the Schlage-Puchta information has been reduced to `(2)`, arbitrary signed linear or quadratic kernels have an exact operator-normalized ceiling attained by the original energy itself. This turns "use signs/cross terms" from a broad suggestion into a precise proof obligation: find a structured `B` for which the arithmetic transform `BT` admits a genuinely stronger estimate than generic composition, or leave the quartic horizon unchanged.

## Boundaries

- This finding does not improve the Schlage-Puchta theorem or the Burgess exponent.
- It does not rule out direct bilinear, multilinear, higher-moment, or nonlinear estimates that exploit arithmetic before taking total bias energy.
- It does not rule out a change of endpoint/source representation.
- The operator `B` in `(9)` must be source-natural and fixed independently of the unknown prime data for any future analytic theorem to be explanatory; choosing `B` after observing the data would only repackage the endpoint.
- No claim about the Riemann hypothesis or a new bound for the Mertens function is made.