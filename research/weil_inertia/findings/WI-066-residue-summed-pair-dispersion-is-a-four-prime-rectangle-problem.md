# WI-066 — residue-summed Mikawa dispersion opens exactly into a four-prime rectangle problem

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + DECISIVE-NEGATIVE`, with the Mikawa square-function/source normalization inherited from WI-061 and therefore retaining WI-061's `NEEDS-AUDIT` boundary. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate, change Mathia's current unconditional simple-critical proportion, or rule out a new residue-averaged/vector-valued prime-pair theorem. It closes a narrower but strategically important shortcut left open by WI-064--WI-065: replacing Mikawa's residue maximum by the residue-summed square norm is not merely a better pair-level bookkeeping theorem. Opening that norm exactly raises the arithmetic correlation order and exposes a four-von-Mangoldt parallelogram/rectangle correlation.

The resulting target is source-faithful and more precise. If

\[
A_h(n):=\Lambda(n)\Lambda(n+h)
\]

on the finite interval where both prime legs are present, then the raw residue square at modulus `q` is

\[
\boxed{
\sum_{a\bmod q}\Psi_q(a;h)^2
=
\sum_{\substack{r\\q\mid r}}
\sum_n
\Lambda(n)\Lambda(n+h)
\Lambda(n+r)\Lambda(n+r+h),
}
\]

with the interval restrictions on all four arguments understood. Thus a modulus-weighted vector estimate of the type needed after WI-065 becomes a divisor-weighted average of the four-form system

\[
(n,\ n+h,\ n+r,\ n+r+h).
\]

For `r=qs` this is the finite-complexity system `(n,n+h,n+qs,n+qs+h)`, so the conditioning modulus itself is a linear-form coefficient. Bienvenu's higher-dimensional Siegel--Walfisz theorem controls such a system when that coefficient is bounded by a fixed power of `log X`, but WI-059 proves that no fixed-polylogarithmic conductor slice captures asymptotically all of the `W`-local Fourier energy. Therefore the currently established finite-complexity prime-pattern theorem can close only the low-conductor part of this vector route; the lossless tail still requires genuinely new arithmetic information or a source-specific identity that avoids the full residue norm.

## 1. Exact residue-square identity

Fix a nonzero even shift `h` and let

\[
I_h:=\{n\in\mathbb Z:0<n\le x,\ 0<n+h\le x\}.
\]

Write

\[
A_h(n):=\Lambda(n)\Lambda(n+h)\,1_{I_h}(n)
\tag{1}
\]

and use the Mikawa pair count in the equivalent one-variable form

\[
\Psi_q(a;h)
:=
\sum_{\substack{n\in I_h\\n\equiv a\pmod q}}
A_h(n).
\tag{2}
\]

(The sign convention for `h` is immaterial; WI-061 reconstructs Mikawa's printed `m-n=2k` normalization and books parity/collision conventions separately.) Since `A_h` is real and nonnegative,

\[
\begin{aligned}
\sum_{a\bmod q}|\Psi_q(a;h)|^2
&=
\sum_{a\bmod q}
\sum_{\substack{n_1\in I_h\\n_1\equiv a\pmod q}}
\sum_{\substack{n_2\in I_h\\n_2\equiv a\pmod q}}
A_h(n_1)A_h(n_2)\\
&=
\sum_{\substack{n_1,n_2\in I_h\\q\mid n_2-n_1}}
A_h(n_1)A_h(n_2).
\end{aligned}
\tag{3}
\]

Put `r=n_2-n_1`. Then (3) is exactly

\[
\boxed{
\sum_{a\bmod q}|\Psi_q(a;h)|^2
=
\sum_{\substack{r\in\mathbb Z\\q\mid r}}
\sum_{\substack{n\in I_h\\n+r\in I_h}}
\Lambda(n)\Lambda(n+h)
\Lambda(n+r)\Lambda(n+r+h).
}
\tag{4}
\]

No Hardy--Littlewood conjecture, asymptotic replacement, or Fourier truncation enters (4). It is simply the exact expansion of a residue `L^2` norm.

The special values `r=0` and, depending on the sign/range convention, collisions such as `r=\pm h` are lower-dimensional diagonal/collision pieces and must be booked separately in a source-level application. Away from those values, the four displayed linear forms are distinct and (4) is a genuine four-prime correlation.

## 2. Centering by Mikawa's local main does not remove the four-prime term

Let `M_q(a;h)` be the all-residue local main used in WI-064 and

\[
\widetilde E_q(a;h):=\Psi_q(a;h)-M_q(a;h).
\tag{5}
\]

For a finite booked shift family `\mathcal H`, define the residue-summed square function

\[
V_q(\mathcal H)
:=
\sum_{h\in\mathcal H}
\sum_{a\bmod q}|\widetilde E_q(a;h)|^2.
\tag{6}
\]

Expanding (6) gives

\[
\sum_a|\widetilde E_q(a;h)|^2
=
\sum_a|\Psi_q(a;h)|^2
-2\sum_a\Psi_q(a;h)M_q(a;h)
+\sum_aM_q(a;h)^2.
\tag{7}
\]

The first term is exactly the four-prime rectangle sum (4). The other two terms are lower-order in correlation complexity. On the reduced locally admissible residue classes, Mikawa's main is independent of `a`; writing its value as `\mathcal M_q(h)`,

\[
M_q(a;h)
=
1_{(a,q)=1}1_{(a+h,q)=1}\,\mathcal M_q(h),
\tag{8}
\]

up to the separately booked non-reduced prime-power classes. Hence

\[
\sum_a\Psi_q(a;h)M_q(a;h)
=
\mathcal M_q(h)
\sum_{\substack{n\in I_h\\(n(n+h),q)=1}}
\Lambda(n)\Lambda(n+h),
\tag{9}
\]

while

\[
\sum_aM_q(a;h)^2
=
\mathcal A_q(h)\,\mathcal M_q(h)^2,
\qquad
\mathcal A_q(h)
:=\#\{a\bmod q:(a,q)=(a+h,q)=1\}.
\tag{10}
\]

Thus centering subtracts an explicit local-main square and a conditioned **pair** count, but it does not algebraically cancel the off-diagonal four-prime rectangle in (4). Any proof of a small vector norm must therefore prove cancellation/asymptotics for that four-prime object or exploit additional structure before the norm is expanded.

This also clarifies the relation with the divisor martingale of WI-064. With the Fourier normalization used there,

\[
q\sum_{a\bmod q}|\widetilde E_q(a;h)|^2
=
\sum_{c\bmod q}|\widetilde T_{q,c}(h)|^2.
\tag{11}
\]

The zero-frequency coordinate is the projected/coarse pair error; the vector theorem demanded after WI-065 must control **all** nonzero residue frequencies as well. Long-shift information for the unconditioned pair correlation therefore does not, by itself, upper-bound (11).

## 3. Modulus weighting produces an exact divisor-weighted four-prime energy

The Mikawa square-function interface reconstructed in WI-061 naturally carries a modulus weight. To see what the optimistic residue-summed replacement would require, let `\mathcal Q` be any finite modulus family and consider

\[
\mathcal V_{\mathcal Q}
:=
\sum_{q\in\mathcal Q}q\,V_q(\mathcal H).
\tag{12}
\]

Insert only the raw first term of (7), use (4), and interchange the `q` and `r` sums. Define

\[
W_{\mathcal Q}(r)
:=
\sum_{\substack{q\in\mathcal Q\\q\mid r}}q.
\tag{13}
\]

Then the raw four-prime contribution to (12) is exactly

\[
\boxed{
\sum_{h\in\mathcal H}
\sum_r W_{\mathcal Q}(r)
\sum_{\substack{n\in I_h\\n+r\in I_h}}
\Lambda(n)\Lambda(n+h)
\Lambda(n+r)\Lambda(n+r+h).
}
\tag{14}
\]

If `\mathcal Q` contains all admissible moduli up to a cutoff, `W_{\mathcal Q}(r)` is the corresponding truncated divisor-sum weight. The arithmetic problem is therefore not merely to improve `max_a` to `sum_a`; it is to control a **divisor-weighted four-prime rectangle average** after the pair-level and local-main pieces in (7)--(10) are subtracted.

Writing `r=qs` for one modulus exposes the coefficient geometry directly:

\[
\boxed{
(n,\ n+h,\ n+qs,\ n+qs+h).
}
\tag{15}
\]

For noncollision parameters this is a finite-complexity affine-linear system in `(n,h,s)`, but the coefficient `q` grows with the conditioning conductor. That growing coefficient is exactly where the existing low-conductor prime-pattern input stops being uniform enough for the lossless `W` spectrum.

## 4. Classical BDH explains why the correlation order rises

There is a classical analogue of (3)--(4). A Barban--Davenport--Halberstam variance for a general sequence is obtained by opening the square of residue-class discrepancies; after divisor switching, the result is expressed through additive correlations of the underlying sequence. Harper's 2025 treatment, already recorded in `SOURCES.md`, makes this mechanism explicit for general sequences and reviews the classical Montgomery--Hooley/Gallagher range.

For the ordinary von Mangoldt sequence, opening a second-moment progression variance leads to **two-prime** additive correlations. For the shifted-pair sequence

\[
A_h(n)=\Lambda(n)\Lambda(n+h),
\]

the same operation necessarily leads to the **four-prime** additive correlation (4). This is a correlation-order lift, not a peculiarity of the notation.

The generic theorem in Harper's paper does not black-box solve the present problem. Its asymptotic theorem is stated in a large-modulus regime (`Q>\sqrt{2x}` in the theorem surface audited here) and assumes a progression-distribution condition on the input sequence. Feeding the shifted-pair sequence `A_h` into that interface would require precisely the sort of pair-in-progressions information under discussion, while opening its variance still produces (4). Classical BDH for the ordinary prime-counting error therefore cannot simply be substituted for a residue-summed Mikawa pair-error theorem.

Likewise, the Matomäki--Radziwiłł--Tao long-shift theorem recorded in `SOURCES.md` gives strong average information for the **unconditioned** two-prime shifted correlation. It is a crucial ingredient in the Yang--Yang one-sided route, but equation (11) shows why that information alone is not the missing vector statement: it controls the coarse/zero-frequency pair error, whereas the residue `L^2` norm contains the whole nonzero-frequency spectrum.

## 5. Existing finite-complexity prime-pattern input closes only the fixed-polylog conductor slice

Bienvenu's higher-dimensional Siegel--Walfisz theorem, already used in WI-050, gives the expected singular-series asymptotic for admissible finite-complexity affine-linear systems whose linear coefficients are bounded by a fixed power of `log X`. Applied to (15), it can therefore control the generic four-prime rectangle when

\[
q\le(\log X)^B
\tag{16}
\]

for any **fixed** `B`, after the usual admissibility, convex-body, boundary, and collision bookkeeping.

That is useful but cannot make the residue-summed repair lossless. WI-059 proves that for every fixed `K` a positive proportion of the exact `W`-local Fourier `L^2` energy lies at conductor

\[
d>w^K,
\qquad
w=(\log X)^C.
\tag{17}
\]

Equivalently, no conductor cutoff bounded by one fixed power of `log X` captures `1-o(1)` of the local spectrum. Therefore the established Bienvenu input covers only an initial slice of the exact-conductor family required by WI-059--WI-065. Letting the exponent in (16) grow with `X` is **not** supplied by the printed theorem.

The resulting barrier is

\[
\boxed{
\text{lossless residue-summed pair dispersion}
\Longrightarrow
\text{four-prime rectangles at super-polylog conductors},
}
\tag{18}
\]

unless a different source-specific identity reduces the required spectrum before the full vector norm is invoked.

## 6. Consequence for the Yang welding decision tree

WI-064--WI-065 left a residue-averaged or vector-valued shifted-pair theorem as the cleanest way to avoid the `max_a`/Hilbert cost. The present calculation shows that this escape remains logically valid, but it must be reclassified: **it is a genuinely four-prime arithmetic input**, not a cheap strengthening of Mikawa's pair theorem.

The following routes remain alive and are outside the decisive-negative scope here:

1. prove a four-prime rectangle dispersion theorem uniform or averaged in `q` through the `X^{o(1)}` conductor range actually needed by the lossless `W` spectrum;
2. exploit the divisor weight `W_{\mathcal Q}(r)` in (14) by a cross-`q` cancellation theorem stronger than separate residue variances;
3. estimate the exact Yang source contraction directly, before replacing it by the full residue `L^2` norm;
4. find a source-specific identity that removes enough `W`-local spectral mass that a fixed-polylog conductor theorem becomes lossless.

By contrast, simply asking for a ``BDH version of Mikawa'' and then applying it as a black box does not lower the correlation complexity: the desired square function itself is the four-prime problem.

## 7. Prior-art and novelty audit

No novelty is claimed for opening a residue variance, divisor switching, Parseval, the Barban--Davenport--Halberstam philosophy, finite-complexity linear forms in primes, or the observation that a second moment of a two-prime weight produces a four-prime correlation. The relevant established anchors are already recorded in `research/weil_inertia/SOURCES.md`: Mikawa through the WI-061 source reconstruction, Harper for general-sequence BDH variance, Matomäki--Radziwiłł--Tao for long-shift two-prime correlations, and Bienvenu/Green--Tao for finite-complexity prime linear forms.

A targeted prior-art check around residue-summed shifted-prime-pair variance, prime-pair Barban--Davenport--Halberstam theorems, multiplet-in-progressions mean values, and general-sequence BDH did not locate an established theorem whose printed interface gives the required small-/subpolynomial-modulus **centered pair residue `L^2` norm** uniformly over the Yang shift family. Nearby multiplet and general-sequence results either assume distribution of the input sequence in progressions, work in a different modulus range, or do not provide the source-weighted rectangle estimate (14). Absence from that bounded search is **not** used as a priority claim.

The durable Mathia deduction is source-specific and narrower: the exact escape proposed after WI-065 has now been reduced to the explicit object (14), and the fixed-polylog theorem already available for (15) is provably insufficient for an asymptotically lossless `W` spectrum because of WI-059. That materially changes the next proof obligation without asserting a new four-prime theorem.

## 8. Falsification and narrowing gates

Narrow or withdraw the program consequence if any of the following occurs.

1. The all-residue main/error normalization of WI-064 fails its final parity/collision audit. Equation (4) for the raw pair count remains exact, but equations (7)--(10) and the exact source splice would need adjustment.
2. The Mikawa square-function extraction in WI-061 fails independent audit. The four-prime identity remains exact, but its role as the escape from the current Mikawa interface must be downgraded with WI-061.
3. An established theorem is located that directly controls the centered divisor-weighted rectangle (14), or equivalently the required residue-summed shifted-pair error, with the Yang moving-interval/shift normalization and a modulus range large enough to retain `1-o(1)` of the WI-059 spectrum. That would bypass the present prior-art barrier.
4. A source-level derivation shows that the Yang contraction can be bounded without the full residue square function (6), using a smaller spectral projection whose discarded `W`-local energy is provably negligible. Such a route lies outside the black-box vector-norm shortcut closed here.
5. WI-059's positive fixed-polylog conductor-energy tail fails on the actual booked full-active source shift family. That would remove the step from Bienvenu's fixed-log coefficient range to the lossless-conductor obstruction.
