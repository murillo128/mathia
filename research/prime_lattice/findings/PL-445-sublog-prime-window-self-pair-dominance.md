# PL-445 — Sublogarithmic prime windows satisfy the dephasing floor by self-pair dominance

**Evidence/status:** `LITERATURE+EXACT-DERIVED + SCALE-BOUNDARY + GENERIC-DIAGONAL-DOMINANCE`.

**Parent findings:** `PL-421`, `PL-422`, `PL-423`, `PL-435`, `PL-439`, `PL-444`.

## Claim

Let `p` be a fixed odd prime, `q=p-1`, `X → ∞`, and `1 ≤ H=H(X) ≤ log X`. For each reduced residue `a mod p` and each real `t`, define

\[
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\pmod p}}\Lambda(n)n^{-it},
\qquad R_{a,t}(y)=P_{a,t}(y)-b_{a,t}(y),
\]

where the deterministic centers satisfy `sup_{a,y,t}|b_{a,t}(y)| ≤ BH`, for a fixed `B`. Both the raw signal `b=0` and the deterministic subtraction `b_{a,0}=H/q` are admitted. A natural twisted example is `b_{a,t}(y)=q^{-1}∫_y^{y+H}u^{-it}du`. These centers do **not** mean the exact data-dependent principal-character projection forbidden by `PL-423`.

Write the positive semidefinite Hermitian Gram and its diagonal as

\[
S_X(t)_{ab}=\int_X^{2X}R_{a,t}(y)\overline{R_{b,t}(y)}\,dy,
\qquad D_X(t)=\operatorname{Diag} S_X(t).
\]

Then, uniformly in real `t`, fixed reduced residues, and `1≤H≤log X`,

\[
\boxed{S_X(t)_{aa}=\frac{XH\log X}{q}(1+o_p(1))+O_{p,B}(XH^2),}
\tag{1}
\]
\[
\boxed{S_X(t)_{ab}=O_{p,B}(XH^2)\quad(a\ne b).}
\tag{2}
\]

For `H=o(log X)`, all diagonal entries are eventually positive, and the correlation normalization obeys

\[
\boxed{
\sup_{t\in\mathbb R}
\|D_X(t)^{-1/2}S_X(t)D_X(t)^{-1/2}-I_q\|_{\rm op}
\ll_{p,B}\frac{H}{\log X}\longrightarrow0.
}
\tag{3}
\]

For some `c_{p,B}>0`, every sufficiently large `X` and every `1≤H≤c_{p,B}log X` even satisfy the strict `PL-421` local-factor image-cone gate

\[
\boxed{S_X(t)-\frac1qD_X(t)\succ0\qquad(t\in\mathbb R).}
\tag{4}
\]

At `p=5` the least normalized eigenvalue tends to `1`, which exceeds the local deletion floor `1/4`. This supplies a **small-window countercontrol** to the `PL-422` collapse for uncentered polynomial windows `H=X^θ`, `1/6<θ≤1/2`: the two results concern genuinely disjoint scales. It does not locate a transition scale between them.

The mechanism is **prime self-pair/shot-noise dominance**, not arithmetic cancellation. It applies to the raw Gram as well as deterministic-main-term-subtracted Grams and does not prove anything about zeros of zeta.

## Exact decomposition and unconditional arithmetic estimate

For integers `n,m` define the nonnegative window-overlap weight

\[
W_X(n,m)=|[X,2X]\cap[n-H,n)\cap[m-H,m)|\le(H-|n-m|)_+.
\tag{5}
\]

Opening the raw Gram gives an exact finite identity,

\[
\int_X^{2X}P_{a,t}(y)\overline{P_{b,t}(y)}\,dy
=\sum_{\substack{n\equiv a\ (p)\\m\equiv b\ (p)}}
\Lambda(n)\Lambda(m)(n/m)^{-it}W_X(n,m).
\tag{6}
\]

Only the `a=b` entries contain the self-pairs `n=m`; their phase is identically one. The self-pair contribution is

\[
H\sum_{\substack{X<n\le2X\\n\equiv a\ (p)}}\Lambda(n)^2
+O(H(H+1)\log^2(3X)).
\tag{7}
\]

The fixed-modulus prime number theorem and partial summation, with the elementary negligible contribution of proper prime powers, imply

\[
\sum_{\substack{X<n\le2X\\n\equiv a\ (p)}}\Lambda(n)^2
=\frac{X\log X}{q}(1+o_p(1)).
\tag{8}
\]

For `1≤k≤log X`, the classical two-prime Selberg upper-bound sieve bounds the number of prime pairs separated by `k` by `O(X 𝔖({0,k})/(log X)^2)`, apart from `O(1)` exceptional pairs for an inadmissible tuple. Here `𝔖({0,k})` is bounded by a fixed multiple of

\[
w(k)=\prod_{\substack{\ell\mid k\\\ell>2}}\frac{\ell-1}{\ell-2}.
\tag{9}
\]

Inserting von-Mangoldt weights multiplies the prime-prime count by `O(log² X)`. Pairs containing a proper prime power contribute at most `O(X^{1/2}log^3 X)` per shift. Consequently,

\[
\sum_{X<n\le2X+H}\Lambda(n)\Lambda(n+k)
\ll Xw(k)+X^{1/2}\log^3 X.
\tag{10}
\]

For odd `k` the ordinary two-prime singular series vanishes; its only possible prime-prime pairs involve the prime `2`, already included in the harmless exceptional count. No Hardy--Littlewood prime-pair asymptotic is used.

Since

\[
w(k)=\sum_{\substack{d\mid k\\d\ {\mathrm{odd\ squarefree}}}}
\prod_{\ell\mid d}\frac1{\ell-2},
\]

we have the uniform average

\[
\sum_{1\le k\le H}w(k)
\le H\prod_{\ell>2}\left(1+\frac1{\ell(\ell-2)}\right)
\ll H.
\tag{11}
\]

This is also a special case of the singular-series/totient-factor controls in Lichtman--Teräväinen (2022), Lemmas 2.3–2.5, checked against the primary published text. Summing (10) with the window weight `(H-k)_+` proves that **every distinct-integer contribution** in each entry of (6) has absolute value `O(XH²)`, independently of `t`.

Finally Fubini and the fixed-modulus PNT give

\[
\int_X^{2X}|P_{a,t}(y)|dy
\le\int_X^{2X}P_{a,0}(y)dy\ll_p XH.
\tag{12}
\]

The mixed raw/center contributions are therefore `O_{p,B}(XH²)`; the center/center term also has this bound. Combining (7)–(12) establishes (1)–(2). For `H=o(log X)`, the diagonal asymptotic is uniformly comparable to `XHlog X/q`, so the fixed-size off-diagonal perturbation proves (3). Taking a sufficiently small fixed `c_{p,B}` makes its operator norm less than `1-1/q`, giving the strict inequality (4).

## Consequence for the two signed mod-5 orientation probes

For the `PL-439` real residue sources at `t=0`, use compatible real deterministic centers and the same residue ordering. Let `J(w)=∫_X^{2X}(w^TR(y))²dy`. The signed differences

\[
\Delta_s=J(1,-1,1,1)-J(1,1,1,-1),
\]
\[
\Delta_f=J(1,1,-1,-1)-J(1,-1,-1,1)
\]

cancel their full diagonal self-energy exactly, even when the four residue variances differ. Since only the off-diagonal terms survive and each is `O_B(XH²)`,

\[
\boxed{|\Delta_s|+|\Delta_f|\ll_B XH^2.}
\tag{13}
\]

Individual sign-probe energies have self-pair leading term `XHlog X`. Thus the orientation differences are negligible relative to that term when `H=o(log X)`, but **this is not a signed-prime cancellation theorem at the polynomial covariance scale** required by `PL-435` and `PL-439`. It is another manifestation of a much larger diagonal floor.

## Removing the self-pairs: an exact negative control

The diagonal floor itself cannot be promoted to a positive **distinct-prime residual** simply by subtraction. For integer `X`, `H=1`, `t=0`, and the fixed deterministic center `b_a=1/q`, almost every interval `(y,y+1]` holds exactly one integer. Define

\[
A_a=\sum_{\substack{X<n\le2X\\n\equiv a\ (p)}}\Lambda(n)^2,
\qquad
M_a=\sum_{\substack{X<n\le2X\\n\equiv a\ (p)}}\Lambda(n).
\]

The exact Gram is

\[
S_X(0)_{ab}
=\delta_{ab}A_a-\frac{M_a+M_b}{q}+\frac{X}{q^2}.
\tag{14}
\]

Remove *only* its self-pair diagonal:

\[
Q_X=S_X(0)-\operatorname{Diag}(A_a).
\]

By the fixed-modulus PNT, `M_a=X/q+o_p(X)`, whence

\[
\boxed{
Q_X=-\frac{X}{q^2}\mathbf 1\mathbf 1^*+o_p(X),
\qquad \mathbf1^*Q_X\mathbf1=-X+o_p(X)<0.
}
\tag{15}
\]

Thus the self-pair-deleted matrix is not positive semidefinite. We do **not** claim that it has eigenvalues of both signs; the negative quadratic form suffices. This does not conflict with (4), because `Q_X` is not a covariance, and (4) applies only to the full Gram. Deleting the easy positive mass re-exposes a signed arithmetic problem.

## Prior art, audit, and limits

The fixed-modulus PNT, Selberg upper-bound sieve, averaging `n/φ(n)` factors, short-window diagonal dominance, and finite-dimensional eigenvalue estimates are classical, not discoveries. Primary source: Jared Duker Lichtman and Joni Teräväinen, “On the Hardy–Littlewood–Chowla conjecture on average,” *Forum of Mathematics, Sigma* **10** (2022), e57, DOI `10.1017/fms.2022.54`, Lemmas 2.3, 2.4 and 2.5. The article was published 27 July 2022. Gallagher (1976, `SOURCES.md` item 65) studies the `H~log X` prime Poisson regime under Hardy–Littlewood assumptions; **no such assumptions are imported here**.

The derived contribution is limited: combining unconditional prime-pair upper bounds with `PL-421`'s exact inverse-dephasing criterion gives a positive image-cone verdict on genuinely sublogarithmic windows, contrasting with the `PL-422` polynomial-window negative result. The limiting identity correlation is generic for sparse point sources; it cannot identify rational-prime spectral data among matched sparse controls. Uniformity in `t` comes only from absolute-value bounds, not any zero-side theorem or transport through analytic continuation.

The result does **not** control the source-subtracted `PL-418` form, prove the prime-pair covariance-scale estimate at polynomial `H`, imply the oriented Schur-ellipse condition there, or establish an RH/GRH consequence. Any purported RH route using only microscopic positive Gram matrices fails the line-specific arithmetic-fidelity control: their positivity is entirely accounted for by self-pairs.
