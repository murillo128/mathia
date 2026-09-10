# ANF-157 — bow variance is source Fejer energy minus an exact endpoint completion square function

**Status:** `EXACT-DERIVED + SOURCE-FREQUENCY-NORMAL-FORM + ENDPOINT-COMPLETION + PRIME-RAMANUJAN-BRIDGE`. `ANF-152`--`ANF-156` identify the bow target with alignment of the demodulated post-sieve innovation to a fixed moving-window low spectrum, and `ANF-156` describes the positive spectrum through a dual Fejer Toeplitz matrix plus a positive finite-rank boundary correction. There is a complementary source-side identity that does not require approximating spectral projectors. In the integer moving-window model, the bow energy is exactly the **full Fejer energy of the coefficient/source polynomial minus the square energy of the missing prefix and suffix windows**. For the actual source `r_X=vartheta-Q_R`, the coefficient polynomial is exactly a signed prime polynomial minus the finite Ramanujan polynomial of `ANF-149`. Thus a strong enough Fejer-null-frequency concentration theorem for this hybrid additive--multiplicative polynomial would imply the bow target directly, while a Fejer lower bound cannot rule the bow out unless it also defeats the endpoint completion. This gives a concrete source-frequency interface and isolates the finite-horizon boundary as a real arithmetic gate rather than a spectral bookkeeping nuisance.

## 1. The integer bow model is a cropped box convolution

Retain the integer moving-window geometry of `ANF-146`--`ANF-156`. Let

\[
A_{N,K}:\mathbb C^{N+K-1}\to\mathbb C^N,
\qquad
(A_{N,K}b)_j
=
\sum_{r=1}^{K}b_{j+r},
\quad 0\le j<N,
\tag{1}
\]

where `1<=K<=N`, and put

\[
M:=N+K-1.
\tag{2}
\]

Write

\[
V_{N,K}(b)
:=
\sum_{j=0}^{N-1}
\left|\sum_{r=1}^{K}b_{j+r}\right|^2.
\tag{3}
\]

For integer `X=N` and integer `K`, the continuous bow integral over `x in [X,2X]` is exactly of this form after the translation

\[
b_n
=
r_X(X+n)(X+n)^{-iU},
\qquad
1\le n\le N+K-1,
\tag{4}
\]

because the active set of integers is constant on every unit interval `x in [X+j,X+j+1)`. Thus

\[
V_X(U;K)=V_{N,K}(b)
\tag{5}
\]

in that integer model, with the same exact logarithmic carrier used in `ANF-149`--`ANF-153`.

This restriction is harmless at the bow scale when one only wants the source-frequency interface. For integer `K` and arbitrary real integration endpoints, at most two fractional unit cells are added to or removed from the full-row sum. Since `|r_X(n)|<<log X`, their total contribution is

\[
O(K^2\log^2 X)
=
o(XK\log X)
\tag{6}
\]

in the bow range `K=X^{1-2 epsilon+o(1)}` with fixed `epsilon>0`. Rounding a real `K` by `O(1)` changes each short sum by at most `O(log X)` in amplitude, hence changes the `L^2` norm by `O(X^{1/2}\log X)`, which is `o((XK\log X)^{1/2})`. The exact finite identity below therefore represents the original bow target up to a target-negligible endpoint/rounding perturbation.

## 2. Full convolution gives an exact Fejer completion identity

Define the coefficient polynomial and length-`K` box response

\[
B_b(\theta)
:=
\sum_{n=1}^{M}b_ne^{in\theta},
\qquad
H_K(\theta)
:=
\sum_{r=1}^{K}e^{ir\theta},
\tag{7}
\]

and normalize the box power response as the Fejer symbol

\[
F_K(\theta)
:=
\frac1K|H_K(\theta)|^2
=
\frac1K
\left|
\frac{\sin(K\theta/2)}{\sin(\theta/2)}
\right|^2.
\tag{8}
\]

Extend `b_n` by zero outside `1<=n<=M`. Then

\[
B_b(\theta)\overline{H_K(\theta)}
=
\sum_{j=1-K}^{M-1}
c_je^{ij\theta},
\qquad
c_j:=\sum_{r=1}^{K}b_{j+r}.
\tag{9}
\]

For the interior indices `0<=j<N`, one has simply

\[
c_j=(A_{N,K}b)_j.
\tag{10}
\]

The coefficients outside the observed output range are exactly the partial endpoint sums. For `1<=s<=K-1`,

\[
c_{-s}
=
\sum_{n=1}^{K-s}b_n,
\tag{11}
\]

while for `0<=s<=K-2`,

\[
c_{N+s}
=
\sum_{n=N+s+1}^{M}b_n.
\tag{12}
\]

Consequently Parseval gives the exact identity

\[
\frac1{2\pi}
\int_{-\pi}^{\pi}
|H_K(\theta)|^2|B_b(\theta)|^2\,d\theta
=
V_{N,K}(b)+E_{\partial}(b),
\tag{13}
\]

where

\[
\boxed{
E_{\partial}(b)
:=
\sum_{r=1}^{K-1}
\left|\sum_{n=1}^{r}b_n\right|^2
+
\sum_{r=1}^{K-1}
\left|\sum_{n=M-r+1}^{M}b_n\right|^2
\ge0.
}
\tag{14}
\]

Equivalently, if

\[
\mathcal F_K(b)
:=
\frac1{2\pi}
\int_{-\pi}^{\pi}
F_K(\theta)|B_b(\theta)|^2\,d\theta,
\tag{15}
\]

then

\[
\boxed{
V_{N,K}(b)
=
K\mathcal F_K(b)-E_{\partial}(b).
}
\tag{16}
\]

This is the source-side counterpart of the dual identity in `ANF-156`. There the positive dual Gram is `T_N(F_K)+E` and the finite-horizon correction is a **positive boundary tax on output modes**. Here one starts from the source coefficient polynomial, completes the cropped convolution to the full Laurent convolution, and therefore the missing output rows appear as a **subtracted positive endpoint-completion square function**. The opposite signs are not contradictory: they arise from two different exact factorizations of the same rectangular operator.

The Fejer form can also be written directly as a signed lag ledger:

\[
\boxed{
\mathcal F_K(b)
=
\sum_{n=1}^{M}|b_n|^2
+
2\operatorname{Re}
\sum_{h=1}^{K-1}
\left(1-\frac hK\right)
\sum_{n=1}^{M-h}
\overline{b_n}b_{n+h}.
}
\tag{17}
\]

Thus (16) is not merely a transform notation. It says exactly how the triangular full-line pair weights differ from the cropped moving-window overlap: the difference is the two endpoint square functions in (14).

## 3. The diagonal has a much smaller edge defect than the Fejer completion

Let

\[
d_n
:=
\#\{(j,r):0\le j<N,\ 1\le r\le K,\ j+r=n\}
\tag{18}
\]

be the moving incidence weight, so the exact diagonal is

\[
D_{N,K}(b)
=
\sum_{n=1}^{M}d_n|b_n|^2.
\tag{19}
\]

Since `d_n=K` in the coefficient bulk and ramps linearly on the two edge blocks,

\[
\boxed{
K\|b\|_2^2-D_{N,K}(b)
=
\sum_{r=1}^{K-1}
(K-r)
\left(
|b_r|^2+|b_{M-r+1}|^2
\right).
}
\tag{20}
\]

For the actual post-sieve source, `|r_X(n)|<<log X`, so (20) gives

\[
0\le
K\|b\|_2^2-D_{N,K}(b)
\ll
K^2\log^2X
=
o(XK\log X).
\tag{21}
\]

Using the diagonal normalization from `ANF-149` and `ANF-152`,

\[
D_{N,K}(b)
=
(1+o(1))XK\log X,
\tag{22}
\]

one obtains

\[
\boxed{
\|b\|_2^2
=
(1+o(1))X\log X.
}
\tag{23}
\]

The analogous conclusion does **not** follow for `E_partial`. A deterministic prefix-sum operator on `K` coefficients has norm of order `K`, so source mass confined to the `O(K)` boundary sites can in principle create endpoint-completion energy much larger than its diagonal mass. In particular, the crude coefficient bound only gives a bound of order `K^3 log^2 X` for (14), which need not be `o(XK log X)` anywhere in the present range `0<epsilon<1/4`.

This distinction is essential. Coefficient-edge mass is negligible in the bow diagonal, but coherent **partial sums** of that edge mass need not be negligible in the completed Fejer energy.

## 4. The actual source polynomial is explicitly prime minus finite Ramanujan

Specialize (7) to the source-normal form of `ANF-149`,

\[
r_X(m)=\vartheta(m)-Q_R(m),
\qquad
Q_R(m)
=
\sum_{q\mid P(R)}
\frac{\mu(q)}{\varphi(q)}c_q(m).
\tag{24}
\]

In the exact integer model let

\[
I_{X,K}:=\{X+1,\ldots,2X+K-1\},
\tag{25}
\]

and define the hybrid additive--multiplicative source polynomial

\[
\mathcal B_{X,U}(\theta)
:=
\sum_{m\in I_{X,K}}
r_X(m)m^{-iU}e^{im\theta}.
\tag{26}
\]

It has the exact signed decomposition

\[
\boxed{
\mathcal B_{X,U}(\theta)
=
\Theta_{X,U}(\theta)
-
\sum_{q\mid P(R)}
\frac{\mu(q)}{\varphi(q)}
\mathcal C_{q,X,U}(\theta),
}
\tag{27}
\]

where

\[
\Theta_{X,U}(\theta)
:=
\sum_{m\in I_{X,K}}
\vartheta(m)m^{-iU}e^{im\theta},
\tag{28}
\]

and

\[
\mathcal C_{q,X,U}(\theta)
:=
\sum_{m\in I_{X,K}}
c_q(m)m^{-iU}e^{im\theta}.
\tag{29}
\]

No prime-pair asymptotic, periodic averaging, or Taylor replacement of `m^{-iU}` enters (27). It is only the exact finite Ramanujan identity already established in `ANF-149`.

Substituting (26) into (15)--(16) gives a concrete source-frequency form of the bow gate:

\[
\boxed{
V_X(U;K)
=
\frac{K}{2\pi}
\int_{-\pi}^{\pi}
F_K(\theta)
|\mathcal B_{X,U}(\theta)|^2\,d\theta
-
E_{\partial,X}(U)
+
o(XK\log X),
}
\tag{30}
\]

where `E_partial,X(U)` is the two endpoint square function obtained by inserting the exact coefficients `r_X(m)m^{-iU}` into (14). The `o` term is absent in the exact integer model.

Equation (30) keeps the same source information that `ANF-149` showed must not be destroyed. Expanding the modulus in (27) produces the prime--prime, prime--Ramanujan, Ramanujan--prime, and Ramanujan--Ramanujan terms with their signs intact, now organized by the explicit Fejer multiplier rather than by an abstract low-spectrum projector.

## 5. A clean sufficient source theorem and the exact obstruction to a converse

Because `E_partial>=0`, equation (16) immediately gives

\[
0\le V_{N,K}(b)\le K\mathcal F_K(b).
\tag{31}
\]

Therefore the following source theorem would be sufficient for the bow:

\[
\boxed{
\mathcal F_K(b)=o(X\log X)
\quad\Longrightarrow\quad
V_X(U;K)=o(XK\log X).
}
\tag{32}
\]

In terms of (27), this asks for the Fejer-weighted hybrid prime--Ramanujan Fourier energy

\[
\frac1{2\pi}
\int_{-\pi}^{\pi}
F_K(\theta)
\left|
\Theta_{X,U}(\theta)
-
\sum_{q\mid P(R)}
\frac{\mu(q)}{\varphi(q)}
\mathcal C_{q,X,U}(\theta)
\right|^2d\theta
=
o(X\log X)
\tag{33}
\]

at the distinguished `U asymp X^2`. This is an explicit correlation theorem, not a statement about unnamed eigenvectors. It also makes the relevant cancellation architecture visible: bounding the pieces in (27) separately before squaring would again destroy the common local-factor cancellation isolated in `ANF-149`.

There is a corresponding frequency-localization consequence. For every threshold `tau>0`,

\[
\int_{\{F_K>\tau\}}
|\mathcal B_{X,U}(\theta)|^2\,d\theta
\le
\frac{2\pi}{\tau}\mathcal F_K(b).
\tag{34}
\]

Thus (32) forces source Fourier mass away from regions where the Fejer gain stays above the chosen threshold. At the sharp levels studied in `ANF-154`--`ANF-155`, the relevant Fejer sublevel sets are the box-null tubes whose `N`-grid samples generated the explicit detuned trial directions. Equation (34) is only a sufficient source-side route to the true low projector, not an identification of the two projectors.

The converse is where the finite horizon matters. From (16),

\[
V_X(U;K)=o(XK\log X)
\tag{35}
\]

is equivalent, in the exact integer model, to

\[
\boxed{
\mathcal F_K(b)
-
\frac{E_{\partial}(b)}{K}
=
o(X\log X).
}
\tag{36}
\]

Bow cancellation can therefore occur with a large full Fejer energy if the same energy is carried by the omitted prefix/suffix convolution rows. A lower bound for (33) alone cannot disprove the bow. A negative source theorem must instead establish a positive gap

\[
K\mathcal F_K(b)-E_{\partial}(b)
\ge
\delta XK\log X
\tag{37}
\]

for some fixed `delta>0`, or control the endpoint completion strongly enough that a Fejer bulk lower bound survives it.

This is not a technical edge case. Exact `K`-periodic zero-mean kernel vectors from `ANF-153` satisfy `V=0`, while the full convolution in (13) is generally nonzero entirely because of the missing endpoint rows. They are explicit witnesses that deleting `E_partial` would turn an exact zero-energy source direction into a false positive-energy statement.

## 6. Prior-art boundary, stress tests, and frontier consequence

The harmonic-analysis ingredients in (7)--(17) are classical finite convolution and Parseval theory: the rectangular length-`K` filter has power response `K F_K`, and completing a cropped convolution adds the missing prefix and suffix outputs. `ANF-146`--`ANF-156` already record the classical boxcar/Dirichlet/Fejer boundary. The arithmetic ingredient in (24)--(29) is the exact `Lambda^sharp`/finite-Ramanujan identity already established in `ANF-149` from the Matomaki--Radziwill--Shao--Tao--Teravainen approximant. No additional literature theorem is load-bearing here, so `SOURCES.md` need not change.

The main audits are exact. Equation (13) can be checked coefficient-by-coefficient in the Laurent product `B_b overline{H_K}`; the only coefficients omitted by `A_{N,K}` are exactly those listed in (11)--(12). Equation (20) follows by counting the same window incidences and is why the diagonal edge defect is only `O(K^2 log^2 X)`. The much larger possible size of (14) prevents silently replacing the cropped bow operator by the full Toeplitz/Fejer convolution. Finally, (27) imports no Hardy--Littlewood statement: it is a finite identity for the deterministic source.

For `analytic_frontier`, this is the requested source-frequency bridge after `ANF-156`. The low-spectrum problem can now be attacked without first proving projector convergence. A positive route is to show directly that the hybrid prime--Ramanujan polynomial has `o(X log X)` Fejer energy at the distinguished twist. A negative route must show that any source mass forced into positive Fejer gain cannot be exported into the two endpoint completion square functions. In either direction the remaining theorem is explicitly arithmetic: it concerns the additive-frequency distribution and endpoint partial sums of

\[
(\vartheta(n)-Q_R(n))n^{-iU},
\tag{38}
\]

not further geometry-only eigenvalue counting.

The next useful refinement is therefore to control `E_partial,X(U)` or to replace the hard crop by a source-compatible taper whose commutator cost is below the bow diagonal. Either would turn the sufficient Fejer criterion (32) into a closer approximation to the necessary low-projector condition of `ANF-152`.
