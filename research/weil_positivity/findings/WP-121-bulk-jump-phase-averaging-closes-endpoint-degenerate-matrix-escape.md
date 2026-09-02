# WP-121 — Bulk-jump phase averaging closes the endpoint-degenerate matrix escape

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + ENDPOINT-FREE + MATRIX-GRAM + PRIME-CIRCLE-BRIDGE + SHARP-THRESHOLD + MATCHED-CONTROL + PRIOR-ART-AUDITED` for fixed bounded jump-local positive matrix couplings of the canonical even/odd Gamma–Schoenberg channels.

`WP-120` proves that every bounded positive matrix weight `M(y)` with a finite nonzero short-jump limit retains the coherent prime divergence through `sigma=1`. Its explicit scope boundary leaves open a natural escape: let `M(y)` tend to zero, oscillate, or fail to converge as `y -> 0`, thereby suppressing the `dy/y` endpoint responsible for the `log log X` shell cost.

That escape does **not** work. The short-jump endpoint is needed for the sharp logarithmic asymptotic of the Riemann Gamma response, but it is not needed for the prime-shell obstruction itself.

Let

\[
u_t(y):=
\begin{pmatrix}
\cos(ty)-1\\
\sin(ty)
\end{pmatrix},
\qquad
\rho(y):=2\frac{e^{-y/2}}{1-e^{-2y}},
\qquad y>0,
\tag{1}
\]

and let `M:(0,infinity)->Mat_2(R)` be any bounded measurable field with

\[
M(y)\succeq0
\quad\text{a.e.},
\qquad
M\not=0
\quad\text{on a set of positive Lebesgue measure}.
\tag{2}
\]

No endpoint limit, continuity, or lower bound is assumed. Define the positive seminorm

\[
\mathcal E_M(g)
:=
\int_0^\infty g(y)^TM(y)g(y)\rho(y)\,dy.
\tag{3}
\]

Then for every `sigma>0` the coherent prime series

\[
\boxed{
\sum_p \frac{\log p}{p^\sigma}\,u_{\log p}
\text{ converges in }\mathcal E_M
\iff
\sigma>1.
}
\tag{4}
\]

In particular, the exact critical amplitudes `(log p)/sqrt(p)` fail for **every nontrivial fixed bounded jump-local positive matrix geometry**, even if that geometry is completely blind to arbitrarily short jumps. At `sigma=1/2`, every dyadic prime block has energy at least of order `X`; if `M` also has the nonzero endpoint response of `WP-120`, the stronger `X log log X` asymptotic from that finding applies.

The new mechanism is a positive **bulk-jump phase average**. On any compact jump interval where `M` is nontrivial, the prime number theorem gives a deterministic limiting phase profile for a multiplicative dyadic prime shell. As the common shell frequency `log X` tends to infinity, the Riemann--Lebesgue lemma kills the rotating linear and double-frequency terms. What survives is a strictly positive phase average forced by `M>=0`. Thus suppressing the Gamma endpoint cannot make the exact same-sign prime shell Cauchy.

This closes the bounded jump-local matrix escape left by `WP-120`. It does **not** exclude prime/frequency-dependent matrices, nonlocal integral intertwiners, unbounded singular forms, quotients/compressions formed before the norm, cohomological primitive sectors, or a genuinely nonseparable finite--archimedean geometry. It does not prove Weil positivity or RH.

## 1. A dyadic prime shell has a deterministic internal phase profile

Fix `sigma>0` and put

\[
A_{X,\sigma}
:=
\sum_{X<p\le2X}\frac{\log p}{p^\sigma}.
\tag{5}
\]

For a jump coordinate `y`, define the normalized internal shell phase

\[
m_{X,\sigma}(y)
:=
\frac{1}{A_{X,\sigma}}
\sum_{X<p\le2X}
\frac{\log p}{p^\sigma}
\left(\frac pX\right)^{iy}.
\tag{6}
\]

The prime number theorem in the form

\[
\vartheta(x)=\sum_{p\le x}\log p=x+o(x)
\tag{7}
\]

and Stieltjes partial summation give, uniformly for `y` in every fixed compact interval,

\[
\sum_{X<p\le2X}
\frac{\log p}{p^\sigma}
\left(\frac pX\right)^{iy}
=
X^{1-\sigma}
\left(
J_\sigma(y)+o(1)
\right),
\tag{8}
\]

where

\[
J_\sigma(y)
:=
\int_1^2 u^{-\sigma+iy}\,du.
\tag{9}
\]

At `y=0` this yields

\[
A_{X,\sigma}
=
X^{1-\sigma}
\left(J_\sigma(0)+o(1)\right)
\tag{10}
\]

for `sigma != 1`, while at `sigma=1` it gives

\[
A_{X,1}\longrightarrow\log2.
\tag{11}
\]

Consequently

\[
\boxed{
m_{X,\sigma}(y)
\longrightarrow
m_\sigma(y)
:=
\frac{J_\sigma(y)}{J_\sigma(0)}
}
\tag{12}
\]

locally uniformly in `y`.

The limiting profile is explicit. For `sigma != 1`,

\[
m_\sigma(y)
=
\frac{2^{1-\sigma+iy}-1}
{1-\sigma+iy}
\left/
\frac{2^{1-\sigma}-1}{1-\sigma}
\right.,
\tag{13}
\]

and its numerator never vanishes for real `y`, because

\[
|2^{1-\sigma+iy}|=2^{1-\sigma}\ne1.
\tag{14}
\]

At `sigma=1`,

\[
m_1(y)
=
\frac{2^{iy}-1}{iy\log2},
\tag{15}
\]

with the continuous value `m_1(0)=1`; its real zeros form only the discrete set

\[
y=\frac{2\pi k}{\log2},
\qquad k\in\mathbb Z\setminus\{0\}.
\tag{16}
\]

Hence for every `sigma>0`,

\[
\boxed{
|m_\sigma(y)|>0
\quad\text{for a.e. }y>0.
}
\tag{17}
\]

This nonvanishing is the only arithmetic shape information needed after the PNT.

## 2. The normalized shell is a rotating bulk profile

Let

\[
F_{X,\sigma}(y)
:=
\sum_{X<p\le2X}
\frac{\log p}{p^\sigma}u_{\log p}(y).
\tag{18}
\]

Writing `L:=log X`, equations (1) and (6) give the exact normalized identity

\[
\boxed{
\frac{F_{X,\sigma}(y)}{A_{X,\sigma}}
=
\begin{pmatrix}
\operatorname{Re}\!\left(e^{iLy}m_{X,\sigma}(y)\right)-1\\
\operatorname{Im}\!\left(e^{iLy}m_{X,\sigma}(y)\right)
\end{pmatrix}.
}
\tag{19}
\]

Thus a multiplicative dyadic shell is not merely a collection of nearby frequencies. After normalization it is one rapidly rotating carrier `e^{iLy}` with a bounded deterministic envelope `m_sigma(y)`.

Because `M` is nontrivial in the sense of (2), there exists a compact interval

\[
I=[a,b]\subset(0,\infty)
\tag{20}
\]

such that

\[
\int_I \rho(y)\operatorname{tr}M(y)\,dy>0.
\tag{21}
\]

On this interval the Gamma density is bounded above and below by positive finite constants. In particular, the argument below uses no behavior of either `rho` or `M` at `y=0`.

By the locally uniform convergence (12) and boundedness of `M`, replacing `m_{X,sigma}` by `m_sigma` in the restricted normalized energy changes that energy by `o(1)`. It therefore remains to average the vector

\[
v_L(y)
:=
\begin{pmatrix}
\operatorname{Re}(e^{iLy}m_\sigma(y))-1\\
\operatorname{Im}(e^{iLy}m_\sigma(y))
\end{pmatrix}.
\tag{22}
\]

## 3. Riemann--Lebesgue leaves a strictly positive phase average

Write

\[
M(y)=
\begin{pmatrix}
a(y)&c(y)\\
c(y)&b(y)
\end{pmatrix}.
\tag{23}
\]

Expanding `v_L^T M v_L` produces a constant part plus terms oscillating at frequencies `L` and `2L`. The constant part is exactly

\[
\boxed{
a(y)
+
\frac{|m_\sigma(y)|^2}{2}
\bigl(a(y)+b(y)\bigr).
}
\tag{24}
\]

All coefficients of the oscillatory terms are integrable on `I`: they are bounded combinations of `rho`, the entries of `M`, `m_sigma`, and `m_sigma^2`. The classical Riemann--Lebesgue lemma therefore gives

\[
\boxed{
\int_I v_L(y)^TM(y)v_L(y)\rho(y)\,dy
\longrightarrow
C_{\sigma,I}(M),
}
\tag{25}
\]

where

\[
C_{\sigma,I}(M)
:=
\int_I
\rho(y)
\left[
M_{11}(y)
+
\frac{|m_\sigma(y)|^2}{2}
\operatorname{tr}M(y)
\right]dy.
\tag{26}
\]

This constant is **strictly positive**. Indeed, `M(y)>=0` implies

\[
M_{11}(y)\ge0,
\qquad
\operatorname{tr}M(y)\ge0,
\tag{27}
\]

and wherever a positive-semidefinite `2 x 2` matrix is nonzero its trace is positive. Equations (17) and (21) then force

\[
\boxed{
C_{\sigma,I}(M)>0.
}
\tag{28}
\]

The off-diagonal entry `c(y)` can change finite-frequency signs but cannot contribute to the surviving phase average. More importantly, unlike `WP-120`, no short-jump limit of `M` appears anywhere in (25)--(28).

Combining (19), local uniform convergence, and positivity of the full integrand yields the endpoint-free shell lower bound

\[
\boxed{
\liminf_{X\to\infty}
\frac{\mathcal E_M(F_{X,\sigma})}
{A_{X,\sigma}^2}
\ge
C_{\sigma,I}(M)>0.
}
\tag{29}
\]

This is the decisive obstruction.

## 4. The coherent convergence threshold is still exactly sigma equals one

For `0<sigma<1`, equation (10) gives

\[
A_{X,\sigma}
\sim
J_\sigma(0)X^{1-\sigma},
\tag{30}
\]

so (29) implies

\[
\boxed{
\mathcal E_M(F_{X,\sigma})
\gg_{M,\sigma,I}
X^{2(1-\sigma)}.
}
\tag{31}
\]

At the Weil value `sigma=1/2`,

\[
J_{1/2}(0)
=
2(\sqrt2-1),
\tag{32}
\]

and therefore

\[
\boxed{
\liminf_{X\to\infty}
\frac{\mathcal E_M(F_{X,1/2})}{X}
\ge
4(\sqrt2-1)^2 C_{1/2,I}(M)>0.
}
\tag{33}
\]

At `sigma=1`, equations (11) and (29) give

\[
\boxed{
\liminf_{X\to\infty}
\mathcal E_M(F_{X,1})
\ge
(\log2)^2 C_{1,I}(M)>0.
}
\tag{34}
\]

If the prime series converged in the seminorm completion, every contiguous dyadic tail block would have seminorm tending to zero. Equations (31) and (34) therefore prove nonconvergence for every `0<sigma<=1`.

For the converse, boundedness of `M` gives `M(y)<=K I` almost everywhere for some `K`. From the canonical Gamma identity of `WP-117`,

\[
\int_0^\infty \|u_t(y)\|^2\rho(y)\,dy
=
2H_\infty(t),
\tag{35}
\]

and

\[
H_\infty(t)=\log t+O(1)
\qquad(t\to\infty).
\tag{36}
\]

Hence

\[
\|u_{\log p}\|_M
\ll_M
\sqrt{\log\log p}.
\tag{37}
\]

For `sigma>1`,

\[
\sum_p
\frac{\log p}{p^\sigma}
\|u_{\log p}\|_M
<\infty,
\tag{38}
\]

so the series converges absolutely in the seminorm. This proves (4).

The sharp threshold `sigma=1` from `WP-118`--`WP-120` is therefore not a consequence of the nonzero Gamma endpoint coefficient. The endpoint controls the **rate** of divergence, but any fixed nontrivial bounded local positive jump geometry already retains enough bulk response to prevent critical coherent summability.

## 5. Matched controls close the apparent endpoint escape

Several controls isolate what the theorem does and does not use.

First, take a bounded weight supported away from the origin, for example

\[
M(y)=\mathbf 1_{[1,2]}(y)I.
\tag{39}
\]

This geometry discards the Gamma short-jump singularity completely, so the `log t` asymptotic mechanism of `WP-120` is absent. Nevertheless (29)--(34) still rule out every `sigma<=1`. Thus merely damping or deleting short jumps cannot repair the critical prime coupling.

Second, take a rank-one odd-channel weight

\[
M(y)=w(y)
\begin{pmatrix}0&0\\0&1\end{pmatrix},
\qquad
w\ge0,
\tag{40}
\]

with any bounded nonzero measurable `w`, even one vanishing faster than every power at the origin. Then the anchor term `M_11` in (26) vanishes, but the surviving term

\[
\frac12 |m_\sigma(y)|^2\operatorname{tr}M(y)
\tag{41}
\]

is still strictly positive on a set of positive measure. Removing the even channel therefore does not evade the obstruction.

Third, arbitrary bounded oscillation of `M(y)` near zero is irrelevant: the proof chooses one fixed compact interval away from zero and never takes an endpoint limit. The only endpoint-degenerate bounded multiplication field that escapes (29) is the trivial field `M=0` almost everywhere, which supplies no positive geometry at all.

The same harmonic argument works for non-prime positive shells whenever their normalized internal logarithmic-frequency profile converges locally to a function nonzero almost everywhere. Primality enters through the PNT only to identify the exact shell mass and profile in (8)--(17). This is a matched control against reading the obstruction itself as evidence for RH.

## 6. Consequence for the Mathia global-positivity search

`WP-117` is still a genuine positive result: Prime Circle intrinsically selects the Riemann `q=2` Gamma channel, and its vertical digamma variation is an independently nonnegative Lévy--Dirichlet energy. `WP-118`--`WP-120` then show that the obvious scalar, parity-split, and endpoint-nondegenerate matrix gluings to exact critical prime amplitudes fail.

The present result closes the remaining **bounded fixed jump-local matrix** loophole. The obstruction survives even after deliberately sacrificing the short-jump part that makes the Gamma symbol asymptotic to `log t`. Therefore the direct route cannot be rescued by a softer local positive weight, an endpoint cutoff, a rapidly vanishing local matrix, or bounded endpoint oscillation.

A surviving construction must now change something more structural before positivity is taken. The genuine remaining classes include:

- a matrix/operator depending on prime frequency rather than only on jump position;
- a nonlocal integral intertwiner between jump scales;
- an unbounded or singular closed form not represented by a bounded multiplication matrix;
- a canonical quotient/compression or primitive sector formed before the Gamma norm;
- a finite--archimedean geometry whose positive form is nonseparable from the outset.

Those escapes remain subject to the research mandate: they must be intrinsic, retain the exact finite-prime and archimedean/global terms under audited normalization, and obtain nonnegativity from an independent geometric theorem rather than from RH, zero data, or a hand-picked cancelling kernel.

## 7. Prior-art and novelty audit

No novelty is claimed for the prime number theorem, Stieltjes partial summation, the Riemann--Lebesgue lemma, matrix-valued positive multiplication forms, or Schoenberg/Lévy geometry. The matrix-valued conditional-negative-definite literature already audited in `WP-120` concerns structural characterizations of matrix kernels and variograms; it does not supply this arithmetic shell theorem.

A targeted literature search by equivalent structure — matrix-valued positive weights, clustered exponential sums, logarithms of primes, Riemann--Lebesgue averaging, and dyadic prime shells — did not identify a standard result whose statement is the Gamma/prime coupling obstruction (4). The nearby literature uses the same classical harmonic or PNT ingredients for different purposes. The durable Mathia-specific content is therefore the exact composition

\[
\boxed{
\text{PNT shell profile}
\to
\text{rapid common }\log X\text{ phase}
\to
\text{positive matrix phase average on any bulk jump window}
\to
\text{nonzero dyadic tail energy through }\sigma=1.
}
\tag{42}
\]

This is a strengthening of `WP-120`, not a claim that its classical ingredients are new.

## 8. Falsification surface and exact boundaries

The finding is falsified if any of the following fails:

1. `theta(x)=x+o(x)` does not imply the locally uniform shell asymptotic (8) by partial summation;
2. the explicit limiting profile (13)--(16) vanishes on a set of positive Lebesgue measure;
3. the quadratic expansion of (22) has a constant phase average different from (24);
4. the Riemann--Lebesgue lemma does not remove the `L` and `2L` terms on a compact jump interval;
5. a nonzero positive-semidefinite matrix field can make (26) vanish despite (17) and (21);
6. convergence of the ordered prime series does not force its contiguous dyadic blocks to tend to zero;
7. the bounded-form domination (35)--(38) fails for `sigma>1`.

Items 1 and 6 are standard consequences of the PNT and the Cauchy criterion; items 2, 3, and 5 are explicit algebra; item 4 is classical Fourier analysis; item 7 is the already audited Gamma norm estimate from `WP-117`/`WP-120`.

The boundedness and fixed jump-local multiplication hypotheses are essential to the exact biconditional (4). A frequency-dependent, nonlocal, singular, quotient, or cohomological construction is not covered and must be tested separately. Same-sign critical prime amplitudes are also load-bearing: inserting frequency-dependent phases or signs can alter shell coherence, but such phases would need an intrinsic Mathia derivation and a separate exact Weil-match audit rather than being chosen to cancel (29).
