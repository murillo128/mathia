# NB-010 — parity cancellation front-loads truncated semigroup energy

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + RESIDUAL-SPECIFIC-COERCIVITY + EARLY-DEPTH-ENERGY-LOWER-BOUND + PARITY-SHARP-CONTROL`. `NB-009` proves that the single projection normal equation against `g_2` forces one normalized tail-average witness by index `O(d_N^{-2})`, but its subsequent use of the pointwise witness through `NB-007` yields the strongest lower bound only after the semigroup cutoff is taken much larger than that witness scale. The same parity identity contains a stronger **front-loaded aggregate** statement: at the inverse-distance cutoff itself, the truncated harmonic semigroup defect already carries order `d_N^4/log(1/d_N)` energy.

Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
r_N=e-P_{V_N}e,
\qquad
d_N=\|r_N\|,
\qquad a_N=d_N^2,
\]

and retain Bagchi's semigroup defects

\[
D_mh=(A_m^*-m^{-1/2}I)h,
\qquad
\mathcal E_K(h)=\sum_{m=2}^{K}\|D_mh\|^2.
\tag{1}
\]

Write

\[
c_n(h)=n\int_0^{1/n}h(x)\,dx,
\qquad
\delta_n=c_n(r_N)-a_N.
\tag{2}
\]

For every even `K>=4`, one has the exact finite lower bound

\[
\boxed{
\mathcal E_K(r_N)
\ge
\frac{
\left[
 a_N\left(\log2-\frac1K\right)
 -\frac{d_N}{\sqrt K}
\right]_+^2
}{H_K-1}.
}
\tag{3}
\]

Thus the parity normal equation controls not only the largest tail-average mismatch but the complete harmonic square mass of all mismatches before the cutoff.

Put, as in `NB-009`,

\[
s_*:=\log2-\frac14>0
\]

and let `K_N` be the least even integer satisfying

\[
K_N\ge\frac4{a_Ns_*^2}.
\tag{4}
\]

Then

\[
\boxed{
K_N\le\frac6{s_*^2d_N^2},
\qquad
\mathcal E_{K_N}(r_N)
\ge
\frac{s_*^2}{4(H_{K_N}-1)}d_N^4
\ge
\frac{s_*^2d_N^4}
{4\log\!\left(6/(s_*^2d_N^2)\right)}.
}
\tag{5}
\]

Using Burnol's unconditional zero-sensitive distance floor, there are constants `C_1,C_2,C_3>0` such that for all sufficiently large `N`,

\[
\boxed{
K_N\le C_1\log N,
\qquad
\mathcal E_{K_N}(r_N)
\ge
\frac{C_2}
{(\log N)^2\log(C_3\log N)}.
}
\tag{6}
\]

This is weaker at very deep scale than the `NB-009` amplification obtained by taking a polynomial semigroup cutoff, but it is much stronger **at the first forced scale**. At `K\asymp d_N^{-2}`, `NB-009` alone gives one coordinate of size `\asymp d_N^6`; equation (5) forces aggregate defect energy of order `d_N^4/log(1/d_N)`. The energy therefore cannot remain concentrated in a single tiny witness until a much later cutoff.

## 1. The semigroup defect directly controls the harmonic square mass of tail averages

`NB-007` gives, for every `h` in the canonical Bagchi space,

\[
\|D_mh\|^2
\ge
\frac{|c_m(h)-c_1(h)|^2}{m}.
\tag{7}
\]

For the best residual,

\[
c_1(r_N)=\langle r_N,e\rangle=\|r_N\|^2=a_N,
\tag{8}
\]

so summing (7) over `2<=m<=K` yields

\[
\boxed{
\mathcal E_K(r_N)
\ge
T_K:=\sum_{m=2}^{K}\frac{|\delta_m|^2}{m}.
}
\tag{9}
\]

Unlike the maximum gauge `Gamma_K` of `NB-009`, `T_K` is already matched to the quadratic semigroup observable. It is therefore natural to return to the same source normal equation and estimate its entire early cancellation in this norm rather than first extracting one coordinate.

## 2. The `g_2` normal equation is an alternating functional of the complete early mismatch vector

Use the harmonic intervals

\[
I_n=\left(\frac1{n+1},\frac1n\right]
\]

and write `r_{N,n}` for the value of `r_N` on `I_n`. Since

\[
g_2|_{I_n}=\frac12\mathbf1_{n\ \mathrm{odd}},
\]

projection orthogonality gives the exact parity law from `NB-009`,

\[
\sum_{n\ \mathrm{odd}}
\frac{r_{N,n}}{n(n+1)}=0.
\tag{10}
\]

The tail averages reconstruct the shell values exactly:

\[
r_{N,n}-a_N
=(n+1)\delta_n-n\delta_{n+1},
\tag{11}
\]

hence

\[
\frac{r_{N,n}-a_N}{n(n+1)}
=\frac{\delta_n}{n}-\frac{\delta_{n+1}}{n+1}.
\tag{12}
\]

Let `M=K-1`, so `M` is odd. Summing (12) over the odd indices `1,3,...,M` uses every integer index from `1` through `K` exactly once, with alternating sign. Since `\delta_1=0`,

\[
\boxed{
\sum_{\substack{n\le M\\n\ \mathrm{odd}}}
\frac{r_{N,n}-a_N}{n(n+1)}
=
\sum_{j=2}^{K}(-1)^{j+1}\frac{\delta_j}{j}.
}
\tag{13}
\]

Cauchy--Schwarz in the harmonic mismatch norm gives

\[
\left|
\sum_{j=2}^{K}(-1)^{j+1}\frac{\delta_j}{j}
\right|^2
\le
\left(\sum_{j=2}^{K}\frac{|\delta_j|^2}{j}\right)
\left(\sum_{j=2}^{K}\frac1j\right)
=T_K(H_K-1).
\tag{14}
\]

This is the aggregation step missing from the pointwise witness argument.

## 3. The remote Hilbert tail cannot absorb the fixed odd-shell target mass

The total odd-shell measure is

\[
\sum_{n\ \mathrm{odd}}\frac1{n(n+1)}=\log2.
\tag{15}
\]

The contribution through `M=K-1` therefore satisfies

\[
S_M:=
\sum_{\substack{n\le M\\n\ \mathrm{odd}}}
\frac1{n(n+1)}
\ge\log2-\frac1K.
\tag{16}
\]

The omitted residual tail is controlled only by its true Hilbert norm:

\[
\left|
\sum_{\substack{n>M\\n\ \mathrm{odd}}}
\frac{r_{N,n}}{n(n+1)}
\right|
\le
\|r_N\|
\left(
\sum_{n>M}\frac1{n(n+1)}
\right)^{1/2}
\le\frac{d_N}{\sqrt K}.
\tag{17}
\]

Insert `r_{N,n}=a_N+(r_{N,n}-a_N)` into (10), use (16)--(17), and isolate the early deviation. Equations (13)--(14) give

\[
\sqrt{T_K(H_K-1)}
\ge
\left[
 a_N\left(\log2-\frac1K\right)
 -\frac{d_N}{\sqrt K}
\right]_+.
\tag{18}
\]

Combining (18) with (9) proves (3). No finite-dimensional matrix inversion, Gram condition number, Mellin support restriction, or additional projection equation enters.

## 4. The inverse-distance cutoff yields the `d_N^4/log(1/d_N)` law

For `K_N` from (4), `K_N>=4`, hence

\[
\log2-\frac1{K_N}\ge s_*.
\tag{19}
\]

Also

\[
\frac{d_N}{\sqrt{K_N}}
\le\frac{a_Ns_*}{2}.
\tag{20}
\]

Therefore (3) gives

\[
\mathcal E_{K_N}(r_N)
\ge
\frac{a_N^2s_*^2}{4(H_{K_N}-1)}
=
\frac{s_*^2d_N^4}{4(H_{K_N}-1)}.
\tag{21}
\]

Minimality among even integers gives the same bound as in `NB-009`,

\[
K_N<\frac4{a_Ns_*^2}+2
\le\frac6{a_Ns_*^2},
\tag{22}
\]

and the elementary estimate `H_K-1<=log K` proves the final inequality in (5).

The asymptotic scale is now transparent. The parity equation forces a target mass of order `a_N=d_N^2`; the remote tail becomes too small at `K\asymp d_N^{-2}`. The least harmonic-square energy required to create the remaining early cancellation is the square of that mass divided by the harmonic length `log K`. This produces `d_N^4/log(1/d_N)` rather than the `d_N^6` pointwise modulus.

## 5. Burnol turns the front-loaded bound into a logarithmic-section statement

Burnol's lower bound, already anchored in `SOURCES.md`, and the inclusion of the discrete section in the continuous Nyman space give, as in `NB-009`, a constant `c_B>0` such that

\[
d_N^2\ge\frac{c_B}{\log N}
\tag{23}
\]

for all sufficiently large `N`. Equation (22) then gives `K_N=O(log N)`.

For the energy bound, the function

\[
x\longmapsto
\frac{x^2}{\log(C/x)},
\qquad C=\frac6{s_*^2},
\]

is increasing on `0<x<=1`. Substituting the floor (23) into (5) therefore yields, for suitable fixed constants,

\[
\mathcal E_{K_N}(r_N)
\gg
\frac1{(\log N)^2\log(C_3\log N)},
\tag{24}
\]

which is (6).

This is an unconditional **transport** of the known distance floor into the first polylogarithmic semigroup window. It does not improve Burnol's bound and does not imply RH. Its gain over `NB-009` is localization of aggregate source defect, not a stronger distance exponent.

## 6. The logarithmic loss is sharp for the parity functional alone

The denominator `H_K-1` in (3) is not an artifact of a loose estimate. Consider only the finite mismatch vector `\delta_2,...,\delta_K` and the parity functional in (13). For a prescribed value

\[
L=\sum_{j=2}^{K}(-1)^{j+1}\frac{\delta_j}{j},
\]

minimizing

\[
\sum_{j=2}^{K}\frac{|\delta_j|^2}{j}
\]

is an elementary Hilbert-space problem. Equality in (14) is attained by

\[
\delta_j=t(-1)^{j+1},
\qquad
 t=\frac{L}{H_K-1},
\tag{25}
\]

and the minimum is exactly

\[
\boxed{
\frac{|L|^2}{H_K-1}.
}
\tag{26}
\]

This is a **method-level sharpness control**, not an admissible best-residual construction: the vector (25) is not asserted to satisfy the remaining normal equations, the residual identity `\|r_N\|^2=c_1(r_N)`, or the full Nyman source geometry. It does show that no argument using only the scalar `g_2` cancellation and the coordinate lower bounds (7) can remove the logarithmic loss in (3). A stronger early-energy theorem must use additional projection equations or a stronger semigroup relation.

## 7. Prior art, falsification controls, and research consequence

The load-bearing external inputs remain the existing source anchors. Bhaskar Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis* (2006), supplies the canonical harmonic-interval and dilation-semigroup model. Jean-François Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function* (2002), supplies only the final zero-sensitive distance floor used in (23)--(24).

A targeted prior-art check covered Bagchi's semigroup formulation, Báez-Duarte finite sections, Burnol's quantitative bound, Werner Ehm's 2024 Gram-matrix analysis, and recent multiscale Nyman Gram work. Those sources study the criterion, Gram decompositions, approximation bounds, or smoothed multiscale geometry; no source located in that check supplied the parity-residual aggregate inequality (3) or the inverse-distance front-loaded semigroup energy law (5). Search absence is not used as proof of novelty, and no new literature theorem is imported here, so `SOURCES.md` does not need an additional dependency.

Several boundaries are essential. Equation (3) is a theorem only for the **best residual** because it uses `r_N perpendicular g_2`; arbitrary target-orthogonal vectors remain subject to the alias and late-shell obstructions of `NB-006`--`NB-007`. Equation (6) imports Burnol's known distance scale and is not an independent approximation-rate improvement. The lower bound controls the source defect only; without a residual-specific upper estimate or another inequality coupling `\mathcal E_K(r_N)` back to `d_N`, it does not squeeze the distance. Finally, the sharpness example (25) is a control on the proof interface, not a physical Nyman residual.

The durable frontier is therefore narrower than after `NB-009`. The first polylogarithmic window already contains a quantitatively nontrivial amount of target-character defect energy; one does **not** need to wait for polynomial semigroup depth merely to accumulate source-visible mass. The remaining useful question is whether additional low-order normal equations can remove the parity-only logarithmic loss, or whether the actual finite-section representation gives an upper bound on this same early truncated defect sharp enough to constrain `d_N` beyond the existing Burnol floor.