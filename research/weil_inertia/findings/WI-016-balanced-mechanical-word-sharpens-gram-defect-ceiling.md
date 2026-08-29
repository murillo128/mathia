# WI-016 — a balanced mechanical-word countermodel sharpens the collapsed Gram-defect ceiling to 450/667

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE` for the same **collapsed support-one Montgomery--Taylor Gram-defect interface** isolated in WI-015. The new countermodel is an explicit rational mechanical word of density `450/667`; every inequality below is exact or reduced to rational arithmetic. No optimality claim is made for `450/667`, for mechanical words, or for the full support-one Weil/inertia method.

## 1. Precise claim

Retain the WI-015 master interface

\[
S\ge HN+\mathcal D(M)-o(N),
\qquad
H=H_{\rm MT}
=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2},
\tag{1}
\]

where `S` is the number of retained simple critical-line atoms, `M` is their limiting Montgomery--Taylor Gram matrix, and

\[
\mathcal D(M)=\operatorname{tr}\Psi(M),
\qquad
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

Suppose a downstream proof has already collapsed the zeta input to (1), the exact limiting MT Gram geometry of the simple atoms, and scalar ordering/span/count bookkeeping, as in WI-015. Then those data alone cannot force

\[
\boxed{
\frac SN>\frac{450}{667}
=0.674662668665667\ldots.
}
\tag{2}
\]

This strictly sharpens WI-015's explicit barrier

\[
\frac{56}{83}=0.67469879518\ldots.
\]

The improvement is small, but it is structural: the previous ad hoc period-83 word can be replaced by a balanced rational mechanical configuration whose pair counts admit a closed exact formula.

## 2. The period-667 mechanical configuration

Let

\[
m=450,
\qquad L=667,
\qquad \gcd(m,L)=1,
\]

and define the periodic binary word

\[
\boxed{
a_n=
\left\lfloor\frac{(n+1)m}{L}\right\rfloor
-
\left\lfloor\frac{nm}{L}\right\rfloor.}
\tag{3}
\]

It has period `L` and exactly `m` occupied sites per period. Thus the retained-atom density is

\[
r=\frac mL=\frac{450}{667}.
\tag{4}
\]

Because `m/L>1/2`, the gaps between occupied integer sites are all `1` or `2`; there are `233` gaps of length `1` and `217` gaps of length `2` in each period.

Rational mechanical words, balanced words, and the equivalent rotation coding are classical. In one-dimensional repulsive convex lattice gases, the same type of evenly distributed configurations appear as generalized Wigner lattices / most-homogeneous configurations; see Hubbard (1978), Jędrzejewski--Miękisz (2000), and the standard Sturmian/mechanical-word treatment in Lothaire. No novelty is claimed for this combinatorial object.

## 3. Exact pair-count formula

For every positive integer displacement `j`, let

\[
C_j:=\sum_{n=0}^{L-1}a_na_{n+j},
\tag{5}
\]

with indices taken modulo `L`. This is the number of positive-oriented occupied pairs at displacement `j` per period.

Equation (3) says that `a_n=1` exactly when

\[
nm\pmod L\in A:=\{L-m,L-m+1,\ldots,L-1\}.
\]

Multiplication by `m` permutes `\mathbb Z/L\mathbb Z`. Hence `C_j` is the overlap of the cyclic interval `A` with its translate by

\[
s_j:=jm\pmod L.
\]

Put

\[
d_j:=\min(s_j,L-s_j).
\]

Since `m>L/2`, the overlap of two cyclic intervals of length `m` is exactly

\[
\boxed{
C_j=\max\{\,2m-L,\ m-d_j\,\}.}
\tag{6}
\]

Here `2m-L=233`. For auditability, the first fifty exact counts are

\[
\begin{aligned}
(C_1,\ldots,C_{50})={}&(
233,233,434,249,233,418,265,233,402,281,\\
&233,386,297,233,370,313,233,354,329,233,\\
&338,345,233,322,361,233,306,377,233,290,\\
&393,233,274,409,233,258,425,233,242,441,\\
&233,233,443,240,233,427,256,233,411,272).
\end{aligned}
\tag{7}
\]

This removes the only combinatorial bookkeeping that was somewhat bespoke in WI-015.

## 4. The full spectral defect again collapses exactly to pair energy

At positive integers, the normalized MT overlap satisfies

\[
\boxed{
k(j)=\frac{(-1)^{j+1}}{2\pi^2j^2-1},}
\qquad
w_j:=|k(j)|^2
=\frac1{(2\pi^2j^2-1)^2}.
\tag{8}
\]

The Gershgorin argument of WI-015 is independent of which subset of integer sites is retained. Since `\pi>3`, every off-diagonal row sum is bounded by

\[
2\sum_{j\ge1}|k(j)|
<\frac2{17}\sum_{j\ge1}\frac1{j^2}
<\frac4{17}<1.
\tag{9}
\]

Therefore every finite Gram section has spectrum in

\[
\left(1-\frac4{17},1+\frac4{17}\right)\subset(0,2).
\]

The kink of `Psi` is never reached, so for this entire model

\[
\boxed{
\mathcal D(M)=\operatorname{tr}(M-I)^2.}
\tag{10}
\]

Consequently the limiting defect per retained atom is not a lower witness but the **exact full spectral defect**

\[
\boxed{
d
=\frac2m\sum_{j\ge1}C_jw_j.}
\tag{11}
\]

Thus global Fenchel optimization, arbitrarily long connection-Laplacian witnesses, or a perfect Bellman subaction cannot recover extra hidden `tr Psi` mass on this countermodel: (11) is already the exact value of the collapsed spectral quantity.

## 5. Fully rational upper bound for the defect

A tight decimal for `pi` is unnecessary; it is convenient to derive a rational lower bound self-containedly. Machin's identity gives

\[
\frac\pi4=4\arctan\frac15-\arctan\frac1{239}.
\tag{12}
\]

Using the alternating arctangent series, truncate `arctan(1/5)` after its negative `x^{11}/11` term and `arctan(1/239)` after its positive `x^9/9` term. The first truncation is a lower bound and the second an upper bound, so exact rational arithmetic gives

\[
\boxed{
\pi>\frac{314159265}{10^8}=3.14159265.}
\tag{13}
\]

Put `p_0=314159265/10^8` and

\[
W_j:=\frac1{(2p_0^2j^2-1)^2}.
\]

Then `w_j<W_j`. Evaluate the first fifty terms in (11) with the exact counts (6)--(7). For the tail, use `C_j\le m` and

\[
W_j\le\frac{W_1}{j^4},
\qquad
\sum_{j>50}\frac1{j^4}
\le
\frac1{51^4}+\int_{51}^{\infty}x^{-4}\,dx
=
\frac1{51^4}+\frac1{3\cdot51^3}.
\tag{14}
\]

Hence

\[
\begin{aligned}
d
&<\frac2{450}\sum_{j=1}^{50}C_jW_j
+2W_1\left(\frac1{51^4}+\frac1{3\cdot51^3}\right)\\
&<\boxed{\frac{320422}{10^8}=0.00320422.}
\end{aligned}
\tag{15}
\]

The last comparison is an exact rational inequality after substitution of `p_0`; no floating-point or interval-optimization output is required.

## 6. A matching rational upper bound for the MT baseline

Set `x=1/\sqrt2`. Alternating Taylor bounds give

\[
\cos x\ge
\sum_{k=0}^{7}\frac{(-1)^k x^{2k}}{(2k)!}
=\frac{85691248313}{112715366400},
\tag{16}
\]

and

\[
\frac{\sin x}{x}\le
\sum_{k=0}^{6}\frac{(-1)^k x^{2k}}{(2k+1)!}
=\frac{366139007209}{398529331200}.
\tag{17}
\]

Therefore

\[
x\cot x
=\frac{\cos x}{\sin x/x}
\ge
\frac{85691248313/112715366400}
{366139007209/398529331200},
\]

which implies by direct rational comparison

\[
\boxed{
H<\frac{672500704}{10^9}=0.672500704.}
\tag{18}
\]

The rational margin between the Taylor-derived upper bound and the right side of (18) is positive:

\[
\frac{672500704}{10^9}-H_{\rm Taylor,up}
=
\frac{25676407061}{80092907826968750000}>0.
\]

## 7. Exact self-consistency at density 450/667

Combining (15) and (18),

\[
\begin{aligned}
r(1-d)
&>
\frac{450}{667}
\left(1-\frac{320422}{10^8}\right)\\
&=
\frac{448558101}{667000000}\\
&>
\frac{672500704}{10^9}
>H.
\end{aligned}
\tag{19}
\]

The decisive middle margin is exactly

\[
\frac{448558101}{667000000}
-
\frac{672500704}{10^9}
=
\boxed{\frac{16429}{83375000000}>0.}
\tag{20}
\]

Take longer and longer sections consisting of whole periods. Boundary contributions to the absolutely summable pair energy are `o(N)`. Equations (10)--(20) therefore give

\[
HN+\mathcal D(M)<S-cN+o(N)
\]

for some fixed `c>0`. The periodic model satisfies the same collapsed stability inequality (1) with strict room at density `450/667`.

This proves (2).

## 8. Prior art and novelty audit

The balanced/mechanical configuration itself is classical.

- J. Hubbard, **Generalized Wigner lattices in one dimension and some applications to tetracyanoquinodimethane (TCNQ) salts**, *Phys. Rev. B* 17 (1978), 494, DOI `10.1103/PhysRevB.17.494`, gives the classical generalized-Wigner-lattice setting for evenly distributed periodic ground states under dominant repulsion.
- J. Jędrzejewski and J. Miękisz, **Ground States of Lattice Gases with “Almost” Convex Repulsive Interactions**, *J. Stat. Phys.* 98 (2000), 589--620, describes the strictly convex repulsive model's ground states as generalized Wigner lattices / most homogeneous configurations.
- M. Lothaire, **Algebraic Combinatorics on Words**, Chapter 2, Cambridge University Press (2002), gives the standard equivalence between balanced/Sturmian words, mechanical words, and rotation codings (with rational mechanical words periodic rather than Sturmian in the aperiodic sense).
- `trmdy/zeta-simple-zeros-673137`, `docs/campaign-2.md`, is the direct zeta-side prior art already recorded in `SOURCES.md`: it uses balanced periodic integer-gap / phase-locked witnesses to screen pair-energy and Bellman certificate families.

Accordingly, no novelty is claimed for mechanical words, balanced placement, generalized Wigner lattices, periodic-orbit screening, or the integer MT kernel. The specific contribution recorded here is the exact specialization of the rational mechanical autocorrelation (6) to the **full collapsed MT Gram defect**, together with a self-contained rational certificate that the explicit `450/667` model is admissible for (1) and strictly sharpens WI-015's `56/83` barrier.

A numerical scan can of course suggest still better rational slopes, but such optimization is deliberately not part of this finding. `450/667` is an explicit exact witness, not a claimed optimum of the mechanical family.

## 9. Boundaries and falsification tests

This is an information-loss obstruction with the same scope discipline as WI-015.

- **It is not a zeta-zero construction.** A zeta-specific spacing/correlation theorem that excludes this periodic mechanical model, or a whole quantitative neighborhood around it, would add information not present in (1) and evade the barrier.
- **It does not cap the uncollapsed exceptional block.** WI-004 retains negative-mass, multiplicity and positive-index remainder terms involving `Q'`. WI-005--WI-007 kill naive depth-only pricing, but a new simple/ex\-ceptional coupling is outside (2).
- **It does not cap multi-profile arguments.** A proof using several genuinely independent bandlimited profiles keeps information not represented by a single MT Gram matrix. In particular this finding neither verifies nor refutes the recent Devine multi-profile `0.673399` claim, which remains `NEEDS-AUDIT` in this line.
- **It does not cap support greater than one.** Wider Fourier support, higher correlation, or new prime-side arithmetic can invalidate the admissible-model class.
- **It does not prove `450/667` optimal.** A different periodic or aperiodic simple-atom model may lower the ceiling further.

A direct falsification test is exact: derive from already-established support-one zeta input an additional positive-density constraint that the mechanical model violates, without smuggling in information discarded before (1). If that cannot be done, optimizing `tr Psi(M)` itself cannot beat the model because (10)--(11) already evaluate the full defect.

## 10. Consequence for the research line

WI-015 showed that exact global Fenchel optimization of the simple Gram block has a ceiling below the obvious local/Bellman limits. WI-016 moves that ceiling down again and, more usefully, replaces the bespoke witness by a structured family with closed autocorrelation.

The live escape routes are therefore even more sharply separated:

\[
\boxed{\text{retain and exploit the uncollapsed exceptional block}}
\]

or

\[
\boxed{\text{import a zeta-specific spacing/correlation constraint}}
\]

or

\[
\boxed{\text{use genuinely additional profiles / support / arithmetic data}.}
\]

Further optimization of the same single-profile collapsed MT Gram defect can still improve constants below `450/667`, but it cannot by itself establish a theorem beyond an explicit self-consistent model that it is unable to distinguish from the available data.
