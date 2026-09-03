# WP-122 — Singular jump-local positive measures still diverge at critical prime coupling

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + SINGULAR-MEASURE + ENDPOINT-FREE + MATRIX-GRAM + PRIME-CIRCLE-BRIDGE + MATCHED-CONTROL + PRIOR-ART-AUDITED` for fixed jump-local positive matrix-valued Radon geometries on the canonical even/odd Gamma–Schoenberg channels.

`WP-121` closes every nontrivial bounded measurable matrix multiplier `M(y) >= 0` on the Gamma jump coordinate. Its proof uses Riemann--Lebesgue decay against an absolutely continuous bulk interval, so its explicit boundary still leaves a plausible escape: replace `M(y) rho(y) dy` by a positive **singular** jump measure, perhaps atomic or singular-continuous, for which ordinary Fourier--Stieltjes coefficients need not decay.

That escape also fails at the exact critical normalization. In fact no absolute continuity, endpoint limit, density bound, or Rajchman/Fourier-decay assumption is needed. Let

\[
u_t(y)
:=
\begin{pmatrix}
\cos(ty)-1\\
\sin(ty)
\end{pmatrix},
\qquad y>0,
\tag{1}
\]

be the canonical two-channel Gamma--Schoenberg increment from `WP-120`--`WP-121`, and let `Sigma` be any nonzero locally finite positive-semidefinite `2 x 2` matrix-valued Radon measure on `(0,infinity)`. The associated extended positive form is

\[
\mathcal E_\Sigma(g)
:=
\int_{(0,\infty)} g(y)^T\,d\Sigma(y)\,g(y)\ge0.
\tag{2}
\]

Then the ordered prime series

\[
\boxed{
\sum_p \frac{\log p}{p^\sigma}u_{\log p}
}
\tag{3}
\]

cannot converge in the `E_Sigma` seminorm for any `0<sigma<=1`. In particular the exact Weil amplitudes `(log p)/sqrt(p)` fail for **every nontrivial fixed jump-local positive Radon geometry**, including pure atoms, singular-continuous measures, and unbounded absolutely continuous weights whenever they define a locally finite matrix measure.

The proof replaces spatial Riemann--Lebesgue decay by a Cesaro average over the logarithmic location of the prime shell. Even if the jump measure has atoms and its Fourier transform never decays pointwise, averaging the rapidly rotating common shell carrier `e^{i(log X)y}` over `log X` kills every nonzero jump frequency. Positivity leaves a strictly positive phase average on any compact piece carrying nonzero matrix mass.

This closes the singular zero-order local-measure escape left by `WP-121`. It does **not** exclude nonlocal kernels coupling distinct jump scales, derivative/Sobolev-type local forms not representable by a matrix measure, prime-frequency-dependent forms, quotients or primitive sectors formed before the norm, or genuinely nonseparable finite--archimedean geometry. It does not prove Weil positivity or RH.

## 1. Every positive matrix measure has a bounded normalized density against its trace

Let

\[
\tau:=\operatorname{tr}\Sigma.
\tag{4}
\]

Because `Sigma` is positive semidefinite and locally finite, `tau` is a positive Radon measure and every matrix entry of `Sigma` is absolutely continuous with respect to `tau`. Hence there is a measurable symmetric positive-semidefinite matrix field `W(y)` such that

\[
d\Sigma(y)=W(y)\,d\tau(y),
\qquad
W(y)\succeq0,
\qquad
\operatorname{tr}W(y)=1
\quad\tau\text{-a.e.}
\tag{5}
\]

on the support of `tau`. In particular `||W(y)||<=1` almost everywhere. This reduction is purely measure-theoretic; it does **not** make `tau` absolutely continuous with respect to Lebesgue or Gamma measure.

Since `Sigma` is nonzero, inner regularity gives a compact

\[
K\Subset(0,\infty)
\tag{6}
\]

with

\[
0<\tau(K)<\infty.
\tag{7}
\]

Write the restricted energy

\[
\mathcal E_{\Sigma,K}(g)
:=
\int_K g(y)^TW(y)g(y)\,d\tau(y).
\tag{8}
\]

Positivity gives

\[
0\le \mathcal E_{\Sigma,K}(g)\le \mathcal E_\Sigma(g)
\tag{9}
\]

in the extended sense. Therefore it suffices to show that prime tail blocks fail the Cauchy criterion already in the compact restricted seminorm.

## 2. Multiplicative prime shells have the same deterministic profile for every fixed width

Fix a shell ratio `q>1` and define

\[
A_{X,\sigma,q}
:=
\sum_{X<p\le qX}\frac{\log p}{p^\sigma},
\tag{10}
\]

and

\[
m_{X,\sigma,q}(y)
:=
\frac{1}{A_{X,\sigma,q}}
\sum_{X<p\le qX}
\frac{\log p}{p^\sigma}
\left(\frac pX\right)^{iy}.
\tag{11}
\]

The same PNT plus Stieltjes-partial-summation calculation as in `WP-121`, now on `[X,qX]`, gives locally uniformly in real `y`

\[
\sum_{X<p\le qX}
\frac{\log p}{p^\sigma}
\left(\frac pX\right)^{iy}
=
X^{1-\sigma}
\left(J_{\sigma,q}(y)+o(1)\right),
\tag{12}
\]

where

\[
J_{\sigma,q}(y)
:=
\int_1^q u^{-\sigma+iy}\,du.
\tag{13}
\]

Consequently

\[
\boxed{
m_{X,\sigma,q}(y)\longrightarrow
m_{\sigma,q}(y):=
\frac{J_{\sigma,q}(y)}{J_{\sigma,q}(0)}}
\tag{14}
\]

uniformly on `K`.

For `0<sigma<1`,

\[
J_{\sigma,q}(y)
=
\frac{q^{1-\sigma+iy}-1}{1-\sigma+iy},
\tag{15}
\]

and the numerator never vanishes on the real axis because

\[
|q^{1-\sigma+iy}|=q^{1-\sigma}>1.
\tag{16}
\]

Hence

\[
\boxed{|m_{\sigma,q}(y)|>0\quad\text{for every real }y}
\qquad(0<\sigma<1).
\tag{17}
\]

At `sigma=1`,

\[
m_{1,q}(y)
=
\frac{q^{iy}-1}{iy\log q},
\qquad m_{1,q}(0)=1,
\tag{18}
\]

whose nonzero real zeros are

\[
Z_q
=
\left\{\frac{2\pi k}{\log q}:k\in\mathbb Z\setminus\{0\}\right\}.
\tag{19}
\]

For a singular measure those discrete zeros matter: `tau` could be atomic on `Z_q`. This is exactly where the fixed-dyadic proof of `WP-121` cannot simply be copied.

## 3. At sigma equals one a generic shell ratio removes the atomic zero-set escape

The shell width is only a Cauchy-test device, so it need not be fixed to `q=2`. For every fixed `y>0`, the set of `q in (1,2)` satisfying

\[
y\log q\in2\pi\mathbb Z
\tag{20}
\]

is finite or countable and therefore has Lebesgue measure zero. Tonelli applied to the finite measure `tau|_K` gives

\[
\int_1^2 \tau(K\cap Z_q)\,dq
=
\int_K
\left|\{q\in(1,2):y\in Z_q\}\right|\,d\tau(y)
=0,
\tag{21}
\]

where the inner bars denote one-dimensional Lebesgue measure. Therefore for almost every `q in (1,2)`,

\[
\boxed{\tau(K\cap Z_q)=0.}
\tag{22}
\]

Choose one such `q`. Then

\[
|m_{1,q}(y)|>0
\quad\tau\text{-a.e. on }K.
\tag{23}
\]

Thus atoms do not create a true `sigma=1` escape; they only require avoiding a countable resonance between the chosen shell width and the jump support.

## 4. Cesaro averaging in shell location works for arbitrary singular measures

Define the shell vector

\[
F_{X,\sigma,q}(y)
:=
\sum_{X<p\le qX}
\frac{\log p}{p^\sigma}u_{\log p}(y).
\tag{24}
\]

Writing `L=log X`, equations (1) and (11) give the exact identity

\[
\frac{F_{X,\sigma,q}(y)}{A_{X,\sigma,q}}
=
\begin{pmatrix}
\operatorname{Re}\!\left(e^{iLy}m_{X,\sigma,q}(y)\right)-1\\
\operatorname{Im}\!\left(e^{iLy}m_{X,\sigma,q}(y)\right)
\end{pmatrix}.
\tag{25}
\]

Uniform convergence (14), `||W||<=1`, and finiteness of `tau(K)` allow `m_X` to be replaced by `m=m_{sigma,q}` in the normalized restricted energy with an error tending uniformly to zero as `L->infinity`.

Put

\[
v_L(y)
:=
\begin{pmatrix}
\operatorname{Re}(e^{iLy}m(y))-1\\
\operatorname{Im}(e^{iLy}m(y))
\end{pmatrix}.
\tag{26}
\]

For

\[
W(y)=
\begin{pmatrix}a(y)&c(y)\\c(y)&b(y)\end{pmatrix},
\tag{27}
\]

the phase-independent part of `v_L^T W v_L` is

\[
\boxed{
a(y)+\frac{|m(y)|^2}{2}\operatorname{tr}W(y)}
=
\boxed{
a(y)+\frac{|m(y)|^2}{2}}.
\tag{28}
\]

The remaining terms are bounded multiples of `e^{iLy}` and `e^{2iLy}`. We do **not** ask their integrals against `tau` to tend to zero pointwise in `L`. Instead average `L` itself. For every fixed `y>0`,

\[
\frac1T\int_T^{2T}e^{iLy}\,dL\longrightarrow0,
\qquad
\frac1T\int_T^{2T}e^{2iLy}\,dL\longrightarrow0.
\tag{29}
\]

All coefficients are bounded on the compact `K`, so Tonelli and dominated convergence give

\[
\boxed{
\frac1T\int_T^{2T}
\frac{\mathcal E_{\Sigma,K}(F_{e^L,\sigma,q})}
{A_{e^L,\sigma,q}^2}
\,dL
\longrightarrow
C_{\sigma,q,K}(\Sigma),
}
\tag{30}
\]

where

\[
C_{\sigma,q,K}(\Sigma)
:=
\int_K
\left[
W_{11}(y)+\frac{|m_{\sigma,q}(y)|^2}{2}
\right]d\tau(y).
\tag{31}
\]

For `0<sigma<1`, equation (17) and `tau(K)>0` imply

\[
\boxed{C_{\sigma,q,K}(\Sigma)>0}
\tag{32}
\]

for every `q>1`. At `sigma=1`, the generic choice (22)--(23) gives the same strict inequality.

This is the decisive singular-measure replacement for the Riemann--Lebesgue step of `WP-121`. No Fourier transform of `tau` is assumed to decay.

## 5. Positive average shell energy forces nonconvergence through sigma equals one

Equation (30) implies that for arbitrarily large `L` there are shell locations with

\[
\frac{\mathcal E_{\Sigma,K}(F_{e^L,\sigma,q})}
{A_{e^L,\sigma,q}^2}
\ge \frac12 C_{\sigma,q,K}(\Sigma)>0.
\tag{33}
\]

For `0<sigma<1`, the PNT asymptotic gives

\[
A_{X,\sigma,q}
\sim
J_{\sigma,q}(0)X^{1-\sigma},
\tag{34}
\]

so along those shell locations

\[
\boxed{
\mathcal E_{\Sigma,K}(F_{X,\sigma,q})
\gg X^{2(1-\sigma)}.
}
\tag{35}
\]

At the exact Weil value `sigma=1/2`,

\[
J_{1/2,q}(0)=2(\sqrt q-1),
\tag{36}
\]

and therefore there is a sequence `X_j->infinity` with

\[
\boxed{
\mathcal E_{\Sigma,K}(F_{X_j,1/2,q})
\ge
2(\sqrt q-1)^2
C_{1/2,q,K}(\Sigma)X_j(1+o(1)).
}
\tag{37}
\]

At `sigma=1`,

\[
A_{X,1,q}\longrightarrow\log q>0,
\tag{38}
\]

so (33) yields a sequence with shell energy bounded away from zero.

If the ordered prime series (3) converged in the global seminorm completion, every contiguous multiplicative shell tail `(X,qX]` would have global seminorm tending to zero. By (9), its restricted `K`-seminorm would also tend to zero. Equations (35)--(38) contradict that Cauchy requirement for every `0<sigma<=1`.

Unlike bounded `WP-121`, no converse for `sigma>1` is asserted here: an arbitrary locally finite singular measure can assign arbitrarily large energy to high-frequency increments away from the tested compact set. The durable statement is the critical no-go, not a universal off-critical domain theorem.

## 6. Atomic and singular-continuous controls show what changed from WP-121

Take a pure odd-channel atom

\[
d\Sigma(y)
=
\begin{pmatrix}0&0\\0&1\end{pmatrix}
\delta_{y_0}(dy),
\qquad y_0>0.
\tag{39}
\]

Its Fourier--Stieltjes transform has no decay at all, so the spatial Riemann--Lebesgue proof of `WP-121` is unavailable. Nevertheless at `sigma=1/2`, equation (31) becomes

\[
C_{1/2,q,\{y_0\}}(\Sigma)
=
\frac12|m_{1/2,q}(y_0)|^2>0,
\tag{40}
\]

and the critical shell obstruction survives. Thus even the most concentrated positive singular jump geometry does not provide the needed cancellation.

The same argument applies without change when `tau` is a Cantor-type singular-continuous Radon measure. No Rajchman hypothesis is needed: carrier-phase averaging occurs in `L=log X`, not in the jump variable.

Conversely, equation (19) is a real edge case at `sigma=1`: for a **fixed** shell width a pure odd atom can sit exactly at a zero of `m_{1,q}`. Section 3 is therefore essential rather than cosmetic. Varying the shell width removes the resonance while leaving the Cauchy test and prime ordering unchanged.

Finally, every unbounded absolutely continuous field `M(y)>=0` for which

\[
d\Sigma(y)=M(y)\rho(y)dy
\tag{41}
\]

is locally finite falls into the present theorem. Hence boundedness of the multiplier in `WP-121` was not a genuine critical escape; it was only needed there for the sharp global `sigma>1` converse and a one-shot Riemann--Lebesgue proof.

## 7. Consequence for the Mathia global-positivity search

The positive archimedean object of `WP-117` remains genuine: Prime Circle intrinsically selects the Riemann `q=2` Gamma channel, whose normalized vertical digamma variation has an RH-independent Lévy--Dirichlet sign theorem. `WP-118`--`WP-121` progressively exclude scalar, parity-separated, bounded matrix, and endpoint-degenerate bounded local gluings to exact critical prime amplitudes.

The present result removes the next natural escape. Replacing the Gamma density by a singular positive local response, concentrating on selected jump scales, introducing atoms, or using an unbounded locally integrable matrix weight cannot make the coherent critical prime series Cauchy. The obstruction needs only one nonzero compact piece of positive jump-local mass.

The remaining viable classes are therefore genuinely more structural:

- nonlocal integral kernels coupling distinct jump coordinates before the norm;
- derivative or other higher-order closed forms not represented by a zero-order matrix measure;
- positive operators depending on prime/frequency as well as jump position;
- canonical quotient/compression or cohomological primitive sectors formed before scalarization;
- finite--archimedean geometry whose positive form is nonseparable from the outset.

Any such route must still reproduce the exact finite-prime coefficients and Gamma/polar structure without fitted cancellation and must obtain its sign before the arithmetic consequence is identified.

## 8. Prior-art and novelty audit

No novelty is claimed for positive matrix-valued Radon measures, the Radon--Nikodym reduction against the trace measure, the prime number theorem, partial summation, Tonelli/dominated convergence, or Cesaro averaging of exponentials. Matrix-valued measure theory routinely writes a positive matrix measure as a bounded positive density against its scalar trace measure; this is a standard structural fact, not a Mathia discovery.

A targeted search by equivalent structure — Fourier--Stieltjes/Cesaro averaging for singular measures, positive matrix-valued measures, prime dyadic or multiplicative shells, logarithmic prime frequencies, and Schoenberg jump geometries — found classical Fourier--Stieltjes/Wiener and matrix-measure literature but no standard theorem identifying the exact obstruction above. In particular, the argument does not rely on the stronger Rajchman property `hat tau(L)->0`, which fails for atoms. The durable Mathia-specific composition is

\[
\boxed{
\text{PNT multiplicative-shell profile}
\to
\text{common }\log X\text{ carrier}
\to
\text{Cesaro phase average against arbitrary positive jump measure}
\to
\text{nonzero critical prime-tail energy}.
}
\tag{42}
\]

This is a narrow strengthening of the `WP-121` obstruction class, not a claim that its classical ingredients are historically new.

## 9. Falsification surface and exact boundaries

The finding is falsified if any of the following fails:

1. a locally finite positive `2 x 2` matrix measure cannot be represented as `W d tau` with `tau=tr Sigma`, `W>=0`, and `tr W=1` almost everywhere;
2. PNT plus partial summation does not give the locally uniform shell limit (12)--(14) on an arbitrary fixed compact `K`;
3. `J_{sigma,q}` has a real zero for some `0<sigma<1`;
4. the Tonelli argument (21) does not permit a shell ratio `q` with `tau(K cap Z_q)=0` at `sigma=1`;
5. the phase average of (26) differs from (28);
6. Cesaro averaging in `L` cannot be interchanged with the finite restricted matrix measure in (30);
7. positive average normalized energy does not force a subsequence satisfying (33);
8. convergence of the ordered prime series does not force every contiguous multiplicative shell tail to vanish in every dominated restricted seminorm.

Items 1, 4, and 6 are standard positive-measure/Tonelli consequences; item 2 is the same PNT partial-summation input already audited in `WP-121`; items 3 and 5 are explicit algebra; items 7 and 8 are elementary averaging and Cauchy-criterion implications.

The theorem is intentionally limited to **fixed zero-order jump-local positive measures**. A kernel `K(y,y')`, a differential form, a prime-dependent family `Sigma_p`, or a quotient applied before evaluating `u_t` is outside its hypotheses and remains a legitimate research target rather than a loophole silently claimed closed.