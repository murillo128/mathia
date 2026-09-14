# PF-338 — finite-boundary critical translations force total half-cuff mixing to vanish

**Status:** `EXACT-DERIVED + UNIFORM-ODD-OFFSET-AGGREGATION + HALF-CUFF-SYMMETRY-OBSTRUCTION + ROUTE-SHARPENING`.

PF-337 shows that, on the PF-324 subsequence `r_n=h_{n+1}/h_n\to0`, every **fixed** odd Fourier diagonal of the normalized pant insertion

\[
K_n=Q_{L,n}^{-1/2}\Lambda_{LL,n}Q_{L,n}^{-1/2}
\]

must lose its Hilbert--Schmidt mass if the PF-336 translation gate

\[
\sup_{t\in I_n}\|[K_n,\tau_t]\|_{\mathcal S_2}=o(1)
\tag{1}
\]

is to hold. The fixed-offset restriction is unnecessary. The whole retained odd-offset sector is uniformly visible to the positive-length critical interval.

Fix PF-328 parameters

\[
0<\lambda_0<\lambda_1<1,
\qquad
I_n=[\tau_{n,\lambda_0},\tau_{n,\lambda_1}],
\qquad
\tau_{n,\lambda}=\operatorname{arcosh}(\lambda/s_n),
\]

and work on one retained physical-low cuff/face-parity component with `|\xi_{n,k}|\le\kappa+o(1)`. Along `r_n\to0`, put

\[
D_{i,n}:=\frac{\ell_n}{2}-\tau_{n,\lambda_i},
\qquad
D_i:=\log(1/\lambda_i).
\]

PF-324 gives `D_{i,n}\to D_i`, with

\[
0<D_1<D_0,
\qquad
|I_n|=D_{0,n}-D_{1,n}\to D_0-D_1>0.
\]

For a Fourier offset `m=j-k`, write `\delta_{m,n}=2\pi m/\ell_n`. If `m` is odd, then the exact PF-337 interval weight can be rewritten as

\[
\boxed{
W_n(\delta_{m,n})
=\frac4{|I_n|}
\int_{D_{1,n}}^{D_{0,n}}
\cos^2\!\left(\frac{\delta_{m,n}D}{2}\right)dD.
}
\tag{2}
\]

Because retained indices satisfy `|\delta_{m,n}|\le2\kappa+o(1)`, compactness gives a constant

\[
\boxed{
c_*=c_*(\kappa,\lambda_0,\lambda_1)>0
}
\tag{3}
\]

such that, for every sufficiently large `n` and **every retained odd offset `m`**, including offsets growing proportionally to `\ell_n`,

\[
\boxed{W_n(\delta_{m,n})\ge c_*.}
\tag{4}
\]

Therefore PF-337's averaged commutator identity strengthens to

\[
\boxed{
\frac1{|I_n|}\int_{I_n}
\|[K_n,\tau_t]\|_{\mathcal S_2}^2dt
\ge
c_*
\sum_{j-k\ \mathrm{odd}}|K_{n;jk}|^2.
}
\tag{5}
\]

Define the physical half-cuff translation

\[
H_n:=\tau_{\ell_n/2}.
\]

In the physical Fourier basis,

\[
H_ne_{n,k}=(-1)^k e_{n,k},
\]

so

\[
\boxed{
\|[K_n,H_n]\|_{\mathcal S_2}^2
=4\sum_{j-k\ \mathrm{odd}}|K_{n;jk}|^2.
}
\tag{6}
\]

Combining (5)--(6),

\[
\boxed{
\frac1{|I_n|}\int_{I_n}
\|[K_n,\tau_t]\|_{\mathcal S_2}^2dt
\ge
\frac{c_*}{4}\|[K_n,H_n]\|_{\mathcal S_2}^2.
}
\tag{7}
\]

Thus (1) has the stronger necessary consequence

\[
\boxed{\|[K_n,H_n]\|_{\mathcal S_2}=o(1).}
\tag{8}
\]

Equivalently, if `P_{n,+}` and `P_{n,-}` are the `+1` and `-1` eigenspace projections of the half-cuff translation, then self-adjointness of `K_n` gives

\[
\boxed{
\|P_{n,+}K_nP_{n,-}\|_{\mathcal S_2}=o(1).
}
\tag{9}
\]

This is strictly stronger than testing `m=1`: all odd Fourier offsets, including offsets corresponding to order-one physical frequency separation, are aggregated into one basis-free half-cuff cross block.

There is also a direct energy-form falsification. Since `H_n^2=I`,

\[
K_n-H_nK_nH_n=[K_n,H_n]H_n,
\]

hence

\[
\boxed{
\|K_n-H_nK_nH_n\|_{\mathcal S_2}
=\|[K_n,H_n]\|_{\mathcal S_2}.
}
\tag{10}
\]

Consequently (1) forces asymptotic half-cuff invariance of the normalized pant quadratic form on the retained low space:

\[
\boxed{
\sup_{\|f\|=1}
\left|
\langle f,K_nf\rangle
-
\langle H_nf,K_nH_nf\rangle
\right|
=o(1).
}
\tag{11}
\]

Any unit low-band datum whose normalized pant energy differs by an order-one amount from that of its antipodal half-cuff translate therefore refutes the PF-336 translation route. This replaces a potentially expensive Fourier-matrix calculation by a geometric comparison of two boundary-energy responses.

## Claim

On the PF-324 subsequence `r_n\to0`, fix `\kappa>0` and PF-328 parameters `0<\lambda_0<\lambda_1<1`. Compress `K_n` to any fixed physical-low cuff/face-parity component preserved by the translations, with retained Fourier frequencies in `[-\kappa,\kappa]` up to the endpoint mesh error. Then there exists `c_*>0`, depending only on `\kappa,\lambda_0,\lambda_1`, such that for all sufficiently large `n` equations (4)--(7) hold. In particular the PF-336 gate (1) implies (8)--(11).

Conversely, any sequence of unit retained-low vectors `f_n` for which

\[
\limsup_{n\to\infty}
\left|
\langle f_n,K_nf_n\rangle
-
\langle H_nf_n,K_nH_nf_n\rangle
\right|>0
\tag{12}
\]

along this subsequence gives a positive lower limsup for the averaged PF-328 translation commutator and therefore falsifies (1).

## 1. Uniform positivity for all retained odd offsets

PF-337 gives, for every Fourier difference `\delta`,

\[
W_n(\delta)
=\frac1{|I_n|}\int_{I_n}
4\sin^2\!\left(\frac{\delta t}{2}\right)dt.
\tag{13}
\]

For `\delta=\delta_{m,n}=2\pi m/\ell_n`, substitute

\[
t=\frac{\ell_n}{2}-D.
\]

If `m` is odd,

\[
\sin^2\!\left(
\frac{\delta_{m,n}}2
\left(\frac{\ell_n}{2}-D\right)
\right)
=
\sin^2\!\left(
\frac{\pi m}{2}-\frac{\delta_{m,n}D}{2}
\right)
=
\cos^2\!\left(\frac{\delta_{m,n}D}{2}\right),
\]

which proves (2).

Now define, on the limiting interval,

\[
F(q):=
\frac4{D_0-D_1}
\int_{D_1}^{D_0}\cos^2(qD)dD,
\qquad |q|\le\kappa.
\tag{14}
\]

`F` is continuous. It is also strictly positive at every `q`: a nonzero analytic function `\cos(qD)` cannot vanish almost everywhere on a nondegenerate interval, while `F(0)=4`. Hence

\[
\min_{|q|\le\kappa}F(q)>0.
\tag{15}
\]

The endpoint convergence `D_{i,n}\to D_i` is fixed and the integrand is uniformly continuous for bounded `q`; therefore the corresponding finite-`n` averages converge uniformly on `|q|\le\kappa+o(1)`. Taking `q=\delta_{m,n}/2` proves (3)--(4) simultaneously for all retained odd offsets, even when `m=m_n\to\infty`.

This is the step missing from PF-337's fixed-`m` limit. The positive-length interval prevents an odd offset from hiding at a special translation phase once the whole retained physical band is considered.

## 2. The odd-offset sector is exactly half-cuff mixing

In the same Fourier basis,

\[
H_ne_{n,k}
=e^{-i\xi_{n,k}\ell_n/2}e_{n,k}
=(-1)^ke_{n,k}.
\]

Therefore

\[
([K_n,H_n])_{jk}
=K_{n;jk}\bigl((-1)^k-(-1)^j\bigr).
\]

The multiplier vanishes for equal Fourier-index parity and has modulus `2` for opposite parity. Squaring and summing proves (6).

Keeping only the odd-offset terms in PF-337's positive averaged identity and applying (4) gives (5), hence (7). If (1) holds, the left side of (7) is `o(1)`, proving (8).

Let

\[
P_{n,\pm}=\frac12(I\pm H_n).
\]

For self-adjoint `K_n`, the two cross blocks are adjoints and

\[
\sum_{j-k\ \mathrm{odd}}|K_{n;jk}|^2
=2\|P_{n,+}K_nP_{n,-}\|_{\mathcal S_2}^2.
\]

This gives (9).

## 3. A basis-free pant-energy test

Because `H_n` is a self-adjoint unitary,

\[
[K_n,H_n]H_n=K_n-H_nK_nH_n,
\]

and right multiplication by `H_n` preserves the Hilbert--Schmidt norm. This proves (10).

For any unit vector `f`,

\[
\begin{aligned}
\left|
\langle f,K_nf\rangle-
\langle H_nf,K_nH_nf\rangle
\right|
&=
|\langle f,(K_n-H_nK_nH_n)f\rangle|\\
&\le
\|K_n-H_nK_nH_n\|\\
&\le
\|K_n-H_nK_nH_n\|_{\mathcal S_2}.
\end{aligned}
\tag{16}
\]

Equation (8) therefore gives (11). Conversely, an order-one energy contrast as in (12) lower-bounds the Hilbert--Schmidt half-cuff defect, and (7) then lower-bounds the averaged critical-translation defect.

This is useful because `\langle f,K_nf\rangle` is exactly the seam-energy-normalized one-cusp-pant/core response on the chosen low component. A negative test no longer requires resolving individual Fourier matrix entries: it is enough to exhibit one retained-low boundary profile whose normalized pant energy is not asymptotically invariant under the physical half-cuff shift.

## 4. Prior art and novelty audit

The Hilbert--Schmidt commutator identity, the Fourier diagonalization of translations, and the decomposition by an involution are elementary operator/Fourier facts. General literature on Hilbert--Schmidt almost-commuting matrices exists, but no such theorem is imported here and no standalone novelty is claimed for these ingredients.

A targeted literature search for half-period/translation Hilbert--Schmidt commutator criteria and Dirichlet-to-Neumann Fourier tests did not locate an external statement matching the present specialization. The project-specific step is the combination of PF-324's arithmetic finite-boundary endpoint limits, PF-328's positive-length critical interval, and PF-337's positive Fourier weight identity to obtain **uniform positivity simultaneously over every retained odd offset**. The proof is self-contained from those persisted inputs, so `SOURCES.md` needs no new entry.

## 5. Boundaries and falsification

1. **Necessary, not sufficient.** Half-cuff invariance is forced by the PF-336 translation route on the `r_n\to0` subsequence; proving it does not prove the full translation gate.
2. **Even-offset mass remains.** Equation (7) aggregates the entire odd-offset sector. Even offsets and other fixed physical-frequency couplings can still violate PF-337's condition (7).
3. **No pant asymmetry lower bound is asserted.** The one-cusp pant need not be half-cuff symmetric geometrically, but this finding does not infer a quantitative DtN defect from that observation. Such a lower bound is the next PDE test.
4. **Low-band statement.** The constant `c_*` uses the fixed physical cutoff `\kappa`. No claim is made uniformly over arbitrarily high physical frequencies.
5. **Finite-boundary subsequence.** The half-cuff reduction uses `r_n\to0`. PF-337's fixed-physical-separation test remains the general necessary condition away from that arithmetic regime.
6. **Componentwise test.** The argument applies to each translation-invariant cuff/face-parity component. Failure in one such compression is enough to falsify the full gate.
7. **No completed-angle or RH conclusion.** This is a sharper obstruction test for one local direct-angle route only.

## Consequence for the research line

The obstruction branch of the accepted direct-angle clue should no longer start by computing only the nearest Fourier diagonal. On the `r_n\to0` subsequence, the stronger first target is the basis-free half-cuff defect

\[
K_n-H_nK_nH_n
\]

or, equivalently, the cross block `P_{n,+}K_nP_{n,-}`. An order-one normalized pant-energy contrast between any retained-low profile and its half-cuff translate kills the PF-336 translation route immediately. If this aggregate test tends to zero, only then is it useful to resolve the surviving even-offset/fixed-physical-separation mass and the separate reference-packet concentration gate.