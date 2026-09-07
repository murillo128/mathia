# XF-104 — Chebyshev mass control pushes transition nonidentifiability to a fixed q-scale fraction

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` + `ARITHMETIC-BAND` + `FIXED-MARGIN` + `TRANSITION-NONIDENTIFIABILITY`. XF-103 showed that a growing prime-power band remains transition-nonidentifying while the normalized raw moment mass tends to zero, using the crude pointwise estimate `Lambda(n) <= log n`. Two losses in that argument are unnecessary. First, an elementary Chebyshev estimate gives

\[
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\ll \sqrt X,
\tag{1}
\]

removing the extra logarithm in the arithmetic mass. Second, XF-085 does not require the normalized `ell^1` mass to be `o(1)`; it only requires a fixed interior margin. Combining these two observations moves the matched-control obstruction all the way to a **fixed positive fraction of the natural `q` arithmetic scale**. More precisely, with `a=N Delta` and the XF-103 scaling `a^2 asymp q`, there is a fixed constant `C_0` such that the distribution-safe endpoint state may include the complete prime-power contribution through

\[
\boxed{
 n\le e^{-2C_0+o(1)}a^2 \asymp c_* q,
 \qquad c_*>0,
}
\tag{2}
\]

while its entire visible periodic power-sum history remains compatible with **every prescribed fixed transition time** `0<tau<=1/2`. Thus merely reaching the `q` arithmetic scale, in the sense of a fixed positive fraction of it, does not repair the Vieta-prefix nonidentifiability found in XF-101--XF-103.

## 1. The weighted prime-power mass is `O(sqrt X)` without PNT or RH

Write

\[
\vartheta(X):=\sum_{p\le X}\log p,
\qquad
\Psi(X):=\sum_{n\le X}\Lambda(n).
\tag{3}
\]

The classical Chebyshev argument is short enough to keep the needed input internal. Every prime `p` with `r<p<=2r` divides the central binomial coefficient, hence

\[
\vartheta(2r)-\vartheta(r)
\le \log {2r\choose r}
\le 2r\log 2.
\tag{4}
\]

Dyadic summation and monotonicity give `vartheta(X) <= C X` for an absolute constant `C`. Since each prime power is counted once in each exponent,

\[
\Psi(X)
=\sum_{k\ge1}\vartheta(X^{1/k})
\le C X + C\sqrt X\log_2 X
\ll X,
\tag{5}
\]

with the finitely many small `X` absorbed into the constant. Partial summation now yields

\[
\begin{aligned}
A(X)
&:=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\\
&=\frac{\Psi(X)}{\sqrt X}
+\frac12\int_1^X \Psi(u)u^{-3/2}\,du
\ll \sqrt X.
\end{aligned}
\tag{6}
\]

No prime number theorem, zero-free region, or hypothesis on zeta zeros enters `(6)`. The estimate itself is classical; the line-specific content below is what happens when it is inserted into the XF-102/103 finite-moment interface.

## 2. The explicit-formula endpoint stays in a fixed equal-weight cone at `L=log a-C_0`

Keep the XF-103 notation

\[
N=2q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
a:=N\Delta\asymp q^{1/2},
\tag{7}
\]

and the same fixed nonnegative bump `psi`, supported in `[-1,1]`. For a physical cutoff `L` put `K=floor(L/Delta)` and prescribe the distribution-safe endpoint moments

\[
Q_m^\psi
=
B(m\Delta)
-
\frac1{2\Delta}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\psi\!\left(\frac{m\Delta-\lambda_n}{\Delta}\right),
\qquad
\lambda_n=\frac12\log n,
\tag{8}
\]

for `1<=m<=K`. Each prime-power atom contributes to at most three mesh points. Equation `(6)` therefore improves the arithmetic estimate in XF-103 to

\[
\sum_{m\le K}
\left|
\frac1{2\Delta}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\psi\!\left(\frac{m\Delta-\lambda_n}{\Delta}\right)
\right|
\ll_\psi
\Delta^{-1}e^{L+\Delta}.
\tag{9}
\]

The elementary background estimate already used in XF-103 gives

\[
\sum_{m\le K}|B(m\Delta)|
\ll
\Delta^{-1}\bigl(e^L+L+\log(K+1)+1\bigr).
\tag{10}
\]

Consequently, for

\[
S(0):=\frac1N\sum_{m\le K}|Q_m^\psi|,
\tag{11}
\]

one has

\[
\boxed{
S(0)
\ll_\psi
\frac{e^L+L+\log(K+1)+1}{a}.
}
\tag{12}
\]

Now choose

\[
\boxed{L=\log a-C_0}
\tag{13}
\]

with a sufficiently large **fixed** constant `C_0`. Since `a->infinity`, `log(K+1)=O(log q)=o(a)`, and therefore

\[
S(0)\le C_\psi e^{-C_0}+o(1).
\tag{14}
\]

Choose `C_0` once and for all so that the right side is at most `1/16` for all sufficiently large scales. At the same time

\[
\frac KN
=\frac{L}{a}+o(1)
\longrightarrow0.
\tag{15}
\]

Hence XF-085 applies with a fixed positive margin: the endpoint target `(8)` has an exact degree-`N`, equal-weight, unit-circle realization even though its normalized raw `ell^1` mass need no longer tend to zero.

## 3. The fixed margin is forward-invariant under the triangular periodic heat

Let `u_m=P_m/N` be the normalized power sums of the exact periodic carrier produced above and set, as in XF-102/103,

\[
S(t):=\sum_{m\le K}|u_m(t)|,
\qquad
D(t):=\sum_{m\le K}\xi_m|u_m(t)|,
\qquad
\xi_m=m\Delta.
\tag{16}
\]

The exact XF-087 triangular equations imply the Dini inequality

\[
D^+S
\le
\bigl[-(a-L)+2aS\bigr]D.
\tag{17}
\]

For `(13)`, `L/a->0`. On the barrier `S<=1/8`, the coefficient in `(17)` is eventually at most `-a/2`. Since `(14)` starts strictly inside that barrier, a first-exit argument gives

\[
\boxed{
S(t)\le S(0)\le\frac1{16},
\qquad 0\le t\le\frac12,
}
\tag{18}
\]

for all sufficiently large scales. Thus the endpoint construction does not merely fit the fixed-margin cone once: the whole visible periodic trajectory retains enough raw-moment margin to reapply XF-085 at any fixed target time.

Fix `0<\tau<=1/2`, set

\[
R:=K+1,
\qquad
n:=N-2R.
\tag{19}
\]

By `(15)`, `n\sim N` and `n/K->infinity`. Moreover `(18)` gives

\[
2\sum_{m\le K}|P_m(\tau)|
=2NS(\tau)
\le \frac N8
\le \frac n2
\tag{20}
\]

for all sufficiently large scales. XF-085 with `kappa=1/2` therefore realizes the same first-`K` moments at time `tau` using exactly the remaining `n` nodes.

## 4. A collision crystal still hides every prescribed positive transition time

Let `A_tau(w)` be the degree-`n` unit-circle polynomial supplied by `(20)` and choose a phase `phi` avoiding its finite root set. As in XF-101--XF-103, multiply by

\[
C_\phi(w):=(w^R-e^{i\phi})^2.
\tag{21}
\]

The crystal has degree `2R`, has `R` exact double roots, and its raw power sums vanish for every `1<=m<R`. Since `R=K+1`, the degree-`N` product

\[
F_\tau(w):=A_\tau(w)C_\phi(w)
\tag{22}
\]

has exactly the same first `K` power sums as the canonical prime-enriched periodic carrier at `t=\tau`. The autonomous triangular system XF-087 then gives equality of the complete first-`K` power-sum trajectories for every `0<=t<=1/2`. The same collision normal form and forward real-zero preservation used in XF-101 show that the periodic transition threshold of `F_tau` is exactly

\[
\boxed{\Lambda_{\rm per}(F_\tau)=\tau.}
\tag{23}
\]

Thus the entire visible time history remains transition-nonidentifying for every fixed positive `tau`, now without requiring the normalized arithmetic moment mass to vanish.

## 5. The band contains a fixed positive fraction of the natural `q` arithmetic scale

The bump in `(8)` contains the complete contribution of every prime power whose frequency is at least one mesh width below the cutoff. Hence every `n` satisfying

\[
\lambda_n\le L-\Delta
\tag{24}
\]

is included without upper-edge truncation. By `(13)`, this is

\[
n\le
\exp(2L-2\Delta)
=
 e^{-2C_0-2\Delta}a^2.
\tag{25}
\]

Because `a^2\asymp q` and `Delta->0`, there is a fixed constant `c_*>0`, depending only on the chosen interior margin and the fixed bump, such that for all sufficiently large scales the visible endpoint state contains the entire prime-power contribution through

\[
\boxed{n\le c_*q.}
\tag{26}
\]

This is a genuine scale change from XF-103, whose concrete safe band stopped at `q/(log q)^4`. The improvement has two independent causes: `(6)` removes the artificial `log X` loss from the arithmetic mass, and `(14)` recognizes that exact equal-weight realization plus heat invariance need only a fixed small margin, not `S=o(1)`.

## 6. Stress tests, prior art, and evidence boundary

The constant in `(26)` is deliberately not optimized. The argument only needs `C_0` large enough to stay uniformly inside the XF-085 cone. It therefore does **not** show that the full interval `n<=q`, or an arbitrary fixed fraction close to one, is admissible. At `L=log a+O(1)` the normalized background and arithmetic masses are both order one; whether larger constants remain realizable is a separate boundary problem. What is closed here is the qualitative rescue attempt that says the obstruction must disappear as soon as the state reaches prime-power scale: it already survives on a nonvanishing fraction of that scale.

The smoothing in `(8)` may combine atoms separated by less than one mesh width. Equation `(26)` means that their **complete explicit-formula contribution** is present in the prescribed state, not that every prime power is individually decoded from one coordinate. Any rescue that relies specifically on resolving individual near-colliding arithmetic frequencies is therefore outside the present state space.

Most importantly, this finding does not construct an `o(1)` guarded shadow of the actual Xi trajectory at `L\asymp\log a`. XF-097's continuum-to-periodic shadow was proved in a much lower prime-free band, and XF-102/103 deliberately changed to a finite periodic/interface-level nonidentifiability question after that bridge failed. The exact statement here is correspondingly a matched falsifier for any theorem whose Xi input is compressed to the prefix `(8)` and then evolved by the autonomous periodic power-sum heat. It does **not** imply that Xi itself can have arbitrary `Lambda`.

A targeted prior-art search across de Bruijn--Newman heat flow, explicit-formula prime sums, equal-weight trigonometric quadrature, and prescribed power sums found the estimate `(6)` as standard Chebyshev-level number theory, but no result combining a fixed-margin explicit-formula prefix with an invisible high-symmetry collision block to make every positive transition time compatible with the same low-mode history. No novelty is claimed for Chebyshev's estimate, partial summation, roots-of-unity cancellation, XF-085's quadrature input, or real-zero preservation. The durable line-specific result is the scale-matched combination `(12)`--`(26)`. Because the only new number-theoretic estimate is derived directly and no external theorem becomes load-bearing, `SOURCES.md` requires no update.

The live frontier is therefore sharper than after XF-103. A future Xi-specific interface cannot rely merely on entering the `q` arithmetic scale. It must either consume enough q-scale information to leave every fixed interior moment cone, impose a genuinely non-prefix/global arithmetic constraint, resolve arithmetic structure destroyed by the mesh smoothing, or abandon the autonomous triangular Vieta state whose high modes can host collision crystals invisibly.