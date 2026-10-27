# PF-370 — positive-shift trace cost dominates the two-cuff escape construction

**Status:** EXACT-DERIVED + CLASSICAL-INTERVAL-DTN + ACTUAL-PANT-ENERGY-BOUND + SPECIFIC-WITNESS-TRANSFER-OBSTRUCTION.

[PF-369](PF-369-nearly-equal-cuff-lattices-hide-broad-band-residual-mass-beyond-actual-windows.md)
constructs two exact cuff traces whose difference escapes the actual corridor
window. That construction does **not** give an energetically inexpensive
escape in the positive-shift pant problem. Its common central amplitude is
large, and transverse energy together with the positive mass term charges
that amplitude even where the difference cancels.

For the entire period-separation regime of PF-369, the full-line
difference energy of its explicit pair is asymptotically negligible relative
to the minimized actual pant energy of that pair. This conclusion also holds
for its real and imaginary parts. Thus even realizing those periods on
prime cuffs would not, by itself, turn this scalar counterexample into a
counterexample to a full-line lower certificate for actual energy.

## 1. Precise comparison for the specified traces

Fix `alpha>1/log(16)`, let `L->infinity`, `n=ceil(alpha L)`, and put

\[
 L'=L+\delta>0,\qquad 0<|\delta|=o(L^2e^{-L/2}).
\tag{1}
\]

Use the exact tight-flute correspondence

\[
 h=4\operatorname{artanh}(e^{-L/2}),\quad
 h'=4\operatorname{artanh}(e^{-L'/2}),\quad
 s=(h+h')/2=(4+o(1))e^{-L/2}.
\tag{2}
\]

Consider an embedded two-cuff pant corridor with these data and the
trace-preserving coordinates of
[PF-363](PF-363-trace-preserving-corridor-charts-give-a-coupled-pant-energy-lower-bound.md).
The inward hypercycle offsets satisfy
`rho_1+rho_2<=eta_0 s` for a fixed `eta_0<1`. Its prescribed embedded window
has `T=arsinh(vartheta/sinh(s))-1`, with fixed sufficiently small
`vartheta>0`; in particular it contains every fixed central interval on a
sufficiently far tail. These are geometric assumptions, not a claim that
arbitrary prescribed `L,L'` occur among prime cuffs.

Let `E_pant[f,f']` be the infimum of
`integral (|du|_g^2+|u|^2) dvol_g` on the full cut pant with the two traces
fixed in the inherited cuff coordinates. This is the positive-shift problem
used by PF-363. No artificial Dirichlet data are imposed at corridor end cuts.

For completeness, specify PF-369's pair. Write

\[
 c_j=4^{-n}\binom{2n}{j-n},\quad n\le j\le3n,
 \qquad \sum_jc_j=1,
\]
\[
 \xi_j=2\pi j/L,\quad \xi'_j=2\pi j/L',\quad
 d_j=\xi'_j-\xi_j=-\frac{2\pi j\delta}{LL'}.
\tag{3}
\]

Let `P_n` be the Fourier partial sum with indices `-n,...,n` of the
periodic extension of `t cos^(2n)(pi t/L)` from `[-L/2,L/2]`. Set

\[
 Q(t)=e^{4\pi int/L}\cos^{2n}(\pi t/L),\qquad
 A(t)=e^{4\pi int/L}P_n(t),
\]
\[
 f'(t)=\sum_{j=n}^{3n}\frac{c_j}{id_j}e^{i\xi'_jt},\qquad
 f(t)=A(t)+\sum_{j=n}^{3n}\frac{c_j}{id_j}e^{i\xi_jt},\qquad
 g=f'-f.
\tag{4}
\]

Here the prime on `f'` labels the second cuff, not differentiation.
All frequencies are in a fixed positive band. Define

\[
 H[g]=\int_{\mathbb R}|g(t)|^2\operatorname{sech}t\,dt,
 \qquad D_s[f,f']=s^{-1}H[f'-f].
\tag{5}
\]

There are constants `c,C>0`, depending only on `alpha` and the fixed
geometric bounds, such that eventually

\[
 \boxed{E_{\rm pant}[f,f']\ge c\,sL^2/\delta^2,\qquad
 H[g]\le C L^2e^{-L/2}.}
\tag{6}
\]

Consequently

\[
 \boxed{\frac{D_s[f,f']}{E_{\rm pant}[f,f']}
 \le C\frac{\delta^2}{s^2}e^{-L/2}
 =O(\delta^2e^{L/2})
 =o(L^4e^{-L/2})\longrightarrow0.}
\tag{7}
\]

Both numerator and denominator scale quadratically under a common
rescaling of the traces. This is an energy-normalized statement, not an
absolute coefficient cap.

For PF-369's exact composite labels `6m+3`,
`delta=(8+o(1))e^(-L/2)` and `delta/s->2`. In that realized control, (7)
is `O(e^(-L/2))`.

## 2. The transverse-plus-mass trace inequality

PF-363 compares actual energy on its embedded trace-preserving chart to

\[
 q^0_{s,T}[v]=\int_{-T}^{T}\int_0^1
 \left\{\frac{|v_X|^2}{s\cosh t}
       +s\cosh t\bigl(|v_t|^2+|v|^2\bigr)\right\}dXdt
\tag{8}
\]

by a lower constant bounded away from zero uniformly as `s->0` under the
offset hypothesis. Restriction to this chart is valid for every full-pant
extension. In particular, it remains valid after taking its energy infimum.

At each fixed `t`, discard only the nonnegative tangential derivative
term. Put `w=s cosh t`. For endpoints `a,b` the remaining one-dimensional
minimum is exactly

\[
 \inf_{v(0)=a,\,v(1)=b}\int_0^1
       \{w^{-1}|v_X|^2+w|v|^2\}\,dX
 =\coth w(|a|^2+|b|^2)
   -2\operatorname{csch}w\,\Re(\overline a b).
\tag{9}
\]

Indeed the minimizer is
`a sinh(w(1-X))/sinh(w)+b sinh(wX)/sinh(w)`; integration by parts uses
`v_XX=w^2 v`. The matrix in (9) has eigenvalues `tanh(w/2)` and
`coth(w/2)`. Therefore, for some uniform `c_*>0`,

\[
 \boxed{E_{\rm pant}[f,f']\ge
 c_*\int_{-T}^{T}\tanh(s\cosh t/2)
                 (|f(t)|^2+|f'(t)|^2)\,dt.}
\tag{10}
\]

This bound holds for arbitrary traces for which the energy is finite;
it has no band or period-separation hypothesis. Its weight is of order `s`
on a fixed central interval. The positive shift is essential: dropping
the mass term from (9) leaves only `|b-a|^2/w` and no common-amplitude
penalty. The formula is a classical interval Dirichlet-to-Neumann identity,
not a new general trace theorem.

## 3. The escaping pair has a large central component cost

All `d_j` have the same nonzero sign. Let

\[
 B=\sum_{j=n}^{3n}\frac{c_j}{|d_j|}.
 \qquad
 \frac{LL'}{6\pi n|\delta|}\le B
 \le\frac{LL'}{2\pi n|\delta|}.
\tag{11}
\]

Thus `B` is comparable to `L/|delta|`. Up to a common unit complex
factor, `f'` is a positive linear combination of its exponentials. Choose
a fixed `t_0>0` sufficiently small that `xi'_j t_0<=pi/4` for every
index on the tail. For example `t_0=1/(48(alpha+1))` works once
`L/2<=L'<=2L` and `n<=(alpha+1)L`. On `[-t_0,t_0]`,

\[
 |f'(t)|\ge B/\sqrt2,\qquad
 \int_{-t_0}^{t_0}|f'(t)|^2dt\ge t_0B^2.
\tag{12}
\]

For `s<=1`, `tanh(s cosh t/2)>=tanh(s/2)>=s/4`.
Applying (10) on this fixed central interval proves
`E_pant>=c_*s t_0 B^2/4` and hence the first part of (6).
No estimate on the cancellation partner `f` is needed for this lower bound.

Realification does not avoid the cost. Since `c_j/(id_j)` have a common
purely imaginary phase, one component of `f'` is the positive cosine
sum in (12). The other is, up to sign, a positive sine sum. On
`[t_0/2,t_0]`, all its sine factors are bounded below by a positive
constant depending only on `alpha`: eventually `xi'_j>=pi alpha`
and `xi'_j t_0<=pi/4`. Each component separately therefore has central
squared mass at least `c_alpha B^2`. Equation (10) supplies the same
order of lower bound for both real pant problems.

## 4. An upper bound for the full residual norm

The Fourier-tail calculation in PF-369 gives

\[
 E_{L,n}=\frac{L}{2\pi n4^n},\quad
 R(t)=tQ(t)-A(t),\quad
 |R(t)|\le E_{L,n}\quad (|t|\le L/2).
\tag{13}
\]

On the central period, `|t cos^(2n)(pi t/L)|<=L/2`, so periodicity of
`A` gives the global bound `|A(t)|<=L/2+E_(L,n)`. Also `|Q(t)|<=1`.
It follows that

\[
 H[R]\le \pi E_{L,n}^2
 +4e^{-L/2}\{(L+E_{L,n})^2+2(L+E_{L,n})+2\}.
\tag{14}
\]

Here the second term is exactly the elementary upper integral obtained
from `|R(t)|<=|t|+L/2+E_(L,n)` and `sech(t)<=2e^(-|t|)` outside the
central period. This deliberately coarse estimate is sufficient.

The divided-difference remainder, valid for every real `t`, is

\[
 |g(t)-R(t)|\le C_d t^2,\qquad
 C_d=\frac{3\pi n|\delta|}{LL'}.
\tag{15}
\]

Since `integral_R t^4 sech(t)dt<=96`, (14) and (15) imply the explicit
finite bound

\[
 H[g]\le 2\pi E_{L,n}^2
 +8e^{-L/2}\{(L+E_{L,n})^2+2(L+E_{L,n})+2\}
 +192C_d^2.
\tag{16}
\]

Now `alpha log(16)>1`, so the first term is smaller than the second
asymptotically. By (1), `C_d^2=O_alpha(delta^2/L^2)=o(L^2e^(-L))`.
Thus (16) proves the second part of (6). The same upper bound holds for
each real component of `g`. Combined with Section 3 this proves (7)
componentwise as well. At least one of these components retains PF-369's
scalar escape, so the energy conclusion includes a real escaping witness.

## 5. Consequence and exact boundary

The scalar escape of PF-369 remains valid: most of `H[g]` is outside the
actual window. But after normalizing this particular pair to unit actual
pant energy, even its **full-line** difference energy tends to zero.
The mass outside the window cannot be promoted to a substantial missed
part of the actual energy for this pair. Adding nonnegative seam or
other pant energies while keeping these two traces fixed only strengthens
that conclusion.

This closes the proposed transfer of the explicit divided-difference
witness, including conditionally on any prime subsequence realizing (1).
It does not classify arbitrary two-cuff traces or establish a uniform
inequality `E_pant>=c s^(-1)H[f'-f]` for every fixed band. Global transition
minimization can choose different traces, and none of its optimizing
fields are identified here. The scalar concentration obstruction and the
actual completed-angle problem remain different questions.

The result uses the shift `+1`, a uniformly admissible offset fraction,
and the inherited trace chart. It is not an unshifted or on-spectrum
scattering estimate. At `delta=0` the pair (4) is undefined. No optimal
energy growth rate, prime-gap theorem, new spectral invariant, compactness,
Schatten, scattering, zeta or RH conclusion follows. Nonprime geometries
with the same corridor data satisfy the same estimate.

## 6. Prior art and validation

Olaf Post, *Boundary pairs associated with quadratic forms*,
Mathematische Nachrichten 289 (2016), 1052–1099,
[DOI](https://doi.org/10.1002/mana.201500048),
[primary manuscript](https://arxiv.org/pdf/1210.4707), Section 6.1,
equation (6.2), gives the interval DtN matrix and its positive-shift
`tanh/coth` eigenvalues. Equation (9) is this classical identity and is
also derived directly above. PF-231/PF-317 already use related interval
functional calculus; PF-363 supplies the actual trace-preserving geometric
comparison. The new consequence is the cost of PF-369's specified pair
in that actual energy, not the interval identity.

The divided-difference mechanism is classical; Avdonin–Ivanov,
[*Exponential Riesz bases of subspaces and divided differences*](https://arxiv.org/abs/math/0103160),
is the nearby prior art already recorded in S42. It does not price these
traces in a shrinking pant. The literature comparison distinguishes that
mechanism, the classical trace bound, and the derived quantitative veto
of this particular scalar-to-energy transfer. No novelty claim is based
on wording or an unsuccessful search.

Supplementary standard-library Decimal checks evaluate the residual Gram
form `G_jk=pi sech(pi(xi_j-xi_k)/2)` at both 150 and 200 digits for
`L=20,40,80,120`, `alpha=1/2`, and
`delta=8 exp(-L/2)` or `delta=-L exp(-L/2)`. All eight positive norms
agree to relative error below `1e-30` and satisfy the explicit bound (16)
and amplitude bounds (11). Five interval-width checks verify the
`coth(w) +/- csch(w)` eigenvalues. An initial 100-digit evaluation lost
the required relative accuracy at `L=120`; the higher-precision repetition
addresses that cancellation. These checks audit finite signs,
normalizations and cancellation; they do not solve a pant PDE, certify
an asymptotic by interval arithmetic, or supply independent review.
Scratch remains outside Git; the displayed inequalities prove the claim.

A standalone Lean transcription of the classical interval identity would
not test the remaining arbitrary-trace or global-minimizer question.
No compute or formalization handoff is proposed for that peripheral step.
