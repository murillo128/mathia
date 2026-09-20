# PL-393 — Fixed-`N` Jessen averaging forgets the Euler–Maclaurin continuation tail

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION`

## Claim

Fix an integer `N >= 1` and `0 < sigma < 1`. Set

\[
P_N(s)=\sum_{n\le N} n^{-s},\qquad
Q_N(s)=P_N(s)+\frac{N^{1-s}}{s-1}.
\]

On the vertical line `s=sigma+it`, the second term is the elementary Euler–Maclaurin continuation correction used in `PL-392`; as `N -> infinity`, `Q_N` converges locally uniformly to `zeta` on compact subsets of `Re(s)>0` away from `s=1`.

For fixed `N`, however, the standard two-sided Jessen logarithmic mean cannot distinguish the continuation-faithful representative `Q_N` from the raw Dirichlet polynomial `P_N`:

\[
\boxed{
\lim_{T\to\infty}\frac1{2T}\int_{-T}^{T}\log|Q_N(\sigma+it)|\,dt
=
\lim_{T\to\infty}\frac1{2T}\int_{-T}^{T}\log|P_N(\sigma+it)|\,dt .
}
\]

The right-hand limit is the classical Jessen mean of the analytic almost-periodic exponential polynomial `t -> P_N(sigma+it)`, hence exists. The equality is unconditional and does not use RH.

Thus the nonlinear observable `mean_t log|.|` still erases the same fixed-`N` continuation tail that is invisible in Besicovitch `B^2` in `PL-392`. This is a fixed-`N`, infinite-height statement; it does **not** cover coupled limits `N=N(T)` or finite-height/local zero statistics.

## Derivation

Write

\[
p(t)=P_N(\sigma+it)
=\sum_{n\le N} n^{-\sigma}e^{-it\log n},
\]

and

\[
h(t)=\frac{N^{1-\sigma}e^{-it\log N}}{\sigma-1+it},
\qquad q(t)=p(t)+h(t).
\]

The function `p` is a finite holomorphic uniformly almost-periodic exponential polynomial. The correction `h` tends to zero under translation **locally uniformly in a complex strip around the real axis**: if `0<delta<1-sigma`, then for every compact `K subset {|Im z|<delta}`,

\[
\sup_{z\in K}|h(z+\tau)|\longrightarrow0
\qquad (|\tau|\to\infty).
\]

The strip restriction only avoids the pole of `h` at `t=-i(1-sigma)`.

Now take any real sequence `|tau_j| -> infinity`. Because `p` has only finitely many frequencies, compactness of its finite phase torus gives a subsequence for which

\[
p(\tau_j+z)\longrightarrow p_*(z)
\]

locally uniformly in `z`. Every such hull limit has the form

\[
p_*(z)=1+\sum_{n=2}^{N}n^{-\sigma}\omega_n e^{-iz\log n},
\qquad |\omega_n|=1,
\]

with the phase relations inherited from translation. In particular `p_*` cannot be identically zero: the frequency `0` has coefficient `1`, while all other frequencies `-log n` are distinct. Since `h(\tau_j+z)->0` locally uniformly,

\[
q(\tau_j+z)\longrightarrow p_*(z)
\]

locally uniformly along the same subsequence.

Use the standard local logarithmic stability of nonzero holomorphic limits: if `f_j -> f` locally uniformly and `f` is not identically zero, then

\[
\log|f_j|\longrightarrow\log|f|
\quad\text{in }L^1_{\mathrm{loc}}.
\]

This follows equivalently from the usual subharmonic compactness theorem or by factoring the finitely many zeros of `f` on a slightly larger compact set and applying Hurwitz/Rouché there. Applying it separately to `p(\tau_j+.)` and `q(\tau_j+.)` gives, on every fixed compact real interval `I`,

\[
\int_I
\left|
\log|q(\tau_j+x)|-\log|p(\tau_j+x)|
\right|dx
\longrightarrow0.
\]

Because every sequence `|tau_j|->infinity` has a subsequence with this conclusion, the block discrepancy itself tends to zero:

\[
D_I(\tau):=
\int_I
\left|
\log|q(\tau+x)|-\log|p(\tau+x)|
\right|dx
\longrightarrow0
\qquad(|\tau|\to\infty).
\]

Partition `[-T,T]` into translates of one fixed interval `I`. Outside a fixed central region each block has arbitrarily small discrepancy; the finitely many central blocks contribute only `O(1)` because logarithmic singularities at isolated zeros are locally integrable. Therefore

\[
\frac1{2T}\int_{-T}^{T}
\left|
\log|q(t)|-\log|p(t)|
\right|dt
\longrightarrow0.
\]

The claimed equality of Jessen means follows immediately.

## Why this is stronger than the `B^2` control

`PL-392` showed that the correction `h` is `C_0` and Besicovitch-`B^2` null, so additive quadratic orbit data sees `[Q_N]=[P_N]`. A natural escape was that `log|.|` is nonlinear and singular at zeros, so a small or mean-square-null perturbation might still leave a nonvanishing Jensen/Jessen signature.

The argument above rules out that escape at fixed `N`: holomorphic local compactness controls the logarithmic singularities strongly enough that the `C_0` tail is also null for the infinite-height mean of `log|.|`. The continuation term can recover fixed compact-strip zeta zeros in the limit `N->infinity` while contributing zero to this fixed-`N` asymptotic logarithmic observable.

## Prior-art and novelty audit

The existence and basic zero-distribution role of Jessen functions for analytic almost-periodic functions are classical; the relevant framework goes back to B. Jessen and H. Tornehave, *Mean motions and zeros of almost periodic functions*, Acta Math. 77 (1945), 137–279, DOI `10.1007/BF02392225`, and V. Borchsenius and B. Jessen, *Mean motions and values of the Riemann zeta function*, Acta Math. 80 (1948), 97–166, DOI `10.1007/BF02393647`.

A targeted audit for Jessen functions under asymptotically almost-periodic / `AP+C_0` perturbations did not locate an exact published statement of the matched-pair identity above. The stored claim is therefore **not** that a new general Jessen theorem has been discovered. The durable delta is the derived application to the exact Euler–Maclaurin pair `(P_N,Q_N)`, closing the nonlinear logarithmic-mean escape explicitly left open by `PL-392`.

## Boundary conditions and failure modes

The order of limits is essential. The proof fixes `N` and then sends `T -> infinity`. It gives no uniform estimate in `N`; therefore it does not imply

\[
\lim_{T\to\infty}
\frac1{2T}\int_{-T}^{T}
\bigl(\log|Q_{N(T)}|-\log|P_{N(T)}|\bigr)dt=0
\]

for a growing cutoff `N(T)`. Such a coupled regime may resolve the continuation tail before its contribution is diluted in height.

Likewise, the result does not erase local-uniform convergence, finite-height zero counts, divisor convergence, or target-relative/model-space observables. Those retain information that a translation-invariant infinite-height mean discards. The result also does not assert that `P_N` and `Q_N` have the same zeros or the same finite-window Jensen data; they generally do not.

A direct falsification test for this finding would be a fixed pair `(N,sigma)` with `0<sigma<1` for which both two-sided logarithmic means exist but differ. The compactness argument above excludes such a pair unless one of its two load-bearing facts fails: local-uniform `C_0` decay of the Euler–Maclaurin correction in a strip, or `L^1_loc` stability of logarithmic moduli under nonzero holomorphic limits.

## Consequence for the research line

The standard Jessen observable is not a surviving bridge from the finite prime-frequency torus to the analytically continued zeta divisor in the critical strip. At fixed cutoff, both additive `B^2` geometry and the nonlinear infinite-height mean of `log|.|` forget the same continuation correction.

A continuation-sensitive harmonic route must therefore keep information that this averaging destroys: finite-height/local divisor data, a quantitatively controlled coupled `N,T` limit, or a target-relative geometry whose observable is not invariant under adding this `C_0` continuation tail.