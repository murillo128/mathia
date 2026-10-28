# PF-371 — full-cuff trace cost controls coupled residuals at bounded length contrast

**Status:** EXACT-DERIVED + CLASSICAL-NONSTANDARD-COLLAR + COEFFICIENT-UNIFORM-ACTUAL-ENERGY-LOWER-BOUND + UNBOUNDED-CONTRAST-OPEN.

The failure of two-cuff scalar window concentration in
[PF-369](PF-369-nearly-equal-cuff-lattices-hide-broad-band-residual-mass-beyond-actual-windows.md)
does not prevent a full-line lower certificate for actual positive-shift
pant energy. The part missed by the embedded corridor can be charged to
variable-width collars along the **entire** two cuffs. At bounded additive
cuff-length contrast this proves the desired lower bound for arbitrary
finite-energy traces, with no bandwidth or coefficient restriction.

Unlike [PF-370](PF-370-positive-shift-trace-cost-dominates-the-two-cuff-escape-construction.md),
the argument is not specific to the divided-difference pair. Unlike
[PF-368](PF-368-fixed-single-cuff-bands-concentrate-in-actual-windows-in-density.md),
it does not assert concentration of the scalar residual. The contribution
outside the window is paid for by actual energy elsewhere in the pant.

## 1. Statement and geometric hypotheses

Let a tight one-cusp pant have cuff lengths `2a,2b`, with `a,b->infinity`.
Write

\[
 w_a=\operatorname{artanh}(\operatorname{sech}a),\quad
 w_b=\operatorname{artanh}(\operatorname{sech}b),\quad s=w_a+w_b.
\tag{1}
\]

These are the standard collar half-widths and the exact inter-cuff
distance, respectively; PF-032 gives `w_a=h/2`. Fix `0<epsilon<=1/8`.
Remove inward seam strips of normal widths satisfying the **individual**
conditions

\[
 0\le\rho_a\le\frac{\epsilon}{2\cosh a},\qquad
 0\le\rho_b\le\frac{\epsilon}{2\cosh b}.
\tag{2}
\]

This is stronger than a condition on `(rho_a+rho_b)/s` alone. The natural
PF-205 cuts meet (2) on a far tail after choosing their fixed admissible
width constant sufficiently small: their area width is `kappa d_n`,
where `d_n` is the prime/shift half-cuff length defect; thus
`rho_n=arsinh(kappa d_n)~kappa/P_n`. The relations
`h_n~g_n/P_n`, `g_n>=2`, and `cosh(a_n)=coth(h_n/2)` give
`rho_n cosh(a_n)<=kappa(1+o(1))`. No subsequent shrinkage depending on
the traces or their bandwidth is required.

Let `f,g` be the traces in the inherited axis coordinates, centered at the
common perpendicular and equally oriented. Extend them periodically to
the real line with periods `2a,2b`. Let `E_pant[f,g]` be the infimum of
`integral (|du|_g^2+|u|^2) dvol_g` over `H^1` fields on the remaining
pant with these two traces fixed on the hypercycles `r=rho_a,rho_b`. The cusp retains the usual finite-energy condition; no
Dirichlet data are imposed on artificial interior cuts. Set

\[
 H[v]=\int_{\mathbb R}|v(t)|^2\operatorname{sech}t\,dt,
 \qquad \chi=s\max\{\cosh a,\cosh b\}.
\tag{3}
\]

There is a constant `c>0`, independent of `a,b,f,g`, such that on a
sufficiently far tail

\[
 \boxed{E_{\rm pant}[f,g]\ge
 \frac{c}{1+\chi}\,\frac{H[g-f]}s.}
\tag{4}
\]

The fixed constants depend on the chosen collar fraction and the embedded
corridor constant below. In particular, for every fixed `B<infinity`,

\[
 \boxed{|a-b|\le B\quad\Longrightarrow\quad
 E_{\rm pant}[f,g]\ge c_B s^{-1}H[g-f].}
\tag{5}
\]

This covers all periodic traces admitting finite pant energy, including
arbitrary combinations on both exact Fourier lattices, real traces,
growing bands and coefficient choices depending on the geometry.

## 2. An entire-cuff collar pays a weighted trace norm

Split the pant into its two reflected ideal pentagons and each pentagon
into the ideal Lambert pieces `Q(a),Q(b)` of PF-125. In one `Q(a)`, use
Fermi coordinates about its finite cuff side. Here `0<=t<a` runs from the
common-perpendicular foot to the cusp ray, and `r` points inward. The
metric is

\[
 dr^2+\cosh^2r\,dt^2.
\]

The opposite split geodesic is exactly

\[
 r_a(t)=\operatorname{artanh}\!\left(\frac{\cosh t}{\cosh a}\right).
\tag{6}
\]

To verify (6), put the cuff on the hyperboloid as
`(cosh t,sinh t,0)`. Its normal coordinates are
`(cosh r cosh t,cosh r sinh t,sinh r)`. The split geodesic at perpendicular
distance `w_a` has plane equation
`-x_0 sinh(w_a)+x_2 cosh(w_a)=0`. Thus
`tanh r=tanh(w_a) cosh t=cosh(t)/cosh(a)`.
Its asymptote is the normal cusp ray at `t=a`. The reflected Lambert
piece supplies `-a<t<=0`; the endpoints `-a,a` represent the same cuff
point. These pieces have disjoint interiors, so the normal tubes below
are embedded in the actual pant, not in a complete infinite-axis lift.

Choose the Lipschitz tube

\[
 \rho_a<r<d_a(t),\qquad
 d_a(t)=\epsilon\frac{\cosh t}{\cosh a},\quad -a\le t\le a.
\tag{7}
\]

Since `artanh x>=x` on `[0,1)`, this lies below (6), and
`d_a(t)<=epsilon`. At the cusp-ray endpoint (6) tends to infinity, so the
bounded tube remains admissible there too. The corresponding tubes for
the two different cuffs lie in their respective Lambert pieces and are
disjoint. Condition (2) also keeps each removed seam strip within its
own piece. The remaining ray length satisfies

\[
 d_a(t)-\rho_a\ge\frac{\epsilon}{2}
                         \frac{\cosh t}{\cosh a}.
\tag{8}
\]

For an interval of length `ell` whose initial value is `z` and whose
other end is free, the classical positive-shift minimum is

\[
 \inf_{v(0)=z}\int_0^\ell(|v'|^2+|v|^2)\,dr
       =\tanh(\ell)|z|^2.
\tag{9}
\]

The minimizer is `z cosh(ell-r)/cosh(ell)`, with natural Neumann data at
the free end. Drop the nonnegative tangential energy in (7); its normal
and mass terms have density `cosh r>=1`. Equations (8),(9), and
`tanh(ell)>=ell tanh(epsilon)/epsilon` for `0<=ell<=epsilon` give

\[
 \boxed{E_{\rm pant}[f,g]\ge c_\epsilon
       \bigl(A_a[f]+A_b[g]\bigr),\qquad
 A_a[f]=\frac1{\cosh a}\int_{-a}^a|f(t)|^2\cosh t\,dt,
 \quad c_\epsilon=\frac{\tanh\epsilon}{2}.}
\tag{10}
\]

This is restriction of every admissible extension followed by its energy
infimum. It requires no competitor extended from the tube to the pant.
The tube's variable upper edge and its corners cause no extra terms:
only normal slices and the nonnegative omitted tangential term are used.
Smooth approximation and the Sobolev trace theorem on these bounded
Lipschitz tubes extend the calculation to finite-energy fields.

## 3. Periodization charges the missing scalar tails

Use PF-363's fixed sufficiently small `vartheta>0` and its prescribed
embedded window

\[
 T=\operatorname{arsinh}(\vartheta/\sinh s)-1.
\tag{11}
\]

On a far tail `0<T<min(a,b)` and `s cosh T->vartheta/e`.
For example `s>=w_a`, `sinh(w_a)=1/sinh a`, and `vartheta<1` imply
`arsinh(vartheta/sinh s)<a`, and similarly for `b`.

For a `2a`-periodic `f`, fold its full-line tail onto `[-a,a]`:

\[
 H_{>T}[f]=\int_{-a}^a|f(t)|^2 R_{a,T}(t)\,dt,
\]
\[
 R_{a,T}(t)=\mathbf1_{\{|t|>T\}}\operatorname{sech}t
                +\sum_{k\ne0}\operatorname{sech}(t+2ak).
\tag{12}
\]

The exponential bound on `sech` and a geometric series give

\[
 \sum_{k\ne0}\operatorname{sech}(t+2ak)
 \le\frac{4e^{-2a}\cosh t}{1-e^{-2a}}.
\]

Also `sech t<=cosh t/cosh^2 T` when `|t|>T`. Consequently

\[
 \frac{R_{a,T}(t)}s\le K_a\frac{\cosh t}{\cosh a},\qquad
 K_a=\frac{\cosh a}{s\cosh^2T}
       +\frac{4\cosh a\,e^{-2a}}{s(1-e^{-2a})}.
\tag{13}
\]

The first summand is at most `C_vartheta s cosh a`. For `a>=1`, the
second is at most `2`, because `s>=w_a>=sech a` and
`4cosh^2(a)e^(-2a)/(1-e^(-2a))<=2`. Thus

\[
 \boxed{s^{-1}H_{>T}[f]\le
 C_\vartheta(1+s\cosh a)A_a[f],}
\tag{14}
\]

with the identical bound for `g,b`. This argument uses periodicity only;
no Fourier concentration or inverse-Gram conditioning enters it.

## 4. Combining the two actual-energy restrictions

Condition (2) implies `rho_a+rho_b<=epsilon s/2`. Hence the uniform
trace-preserving corridor comparison of PF-363 applies and supplies

\[
 E_{\rm pant}[f,g]\ge\frac{c_0}s H_{\le T}[g-f]
\tag{15}
\]

with `c_0>0` fixed on the tail. The two inherited trace coordinates here
are precisely those used in (6)–(14).

Use `|g-f|^2<=2|f|^2+2|g|^2` only **outside** this window. Then

\[
 \frac{H[g-f]}s
 \le \frac{E_{\rm pant}}{c_0}
   +2C_\vartheta(1+\chi)(A_a[f]+A_b[g])
 \le\left(\frac1{c_0}
    +\frac{2C_\vartheta(1+\chi)}{c_\epsilon}\right)E_{\rm pant}.
\tag{16}
\]

This proves (4). The collar tubes can overlap the corridor: (16)
combines two separate lower bounds on the same energy with their stated
constants, and does not add overlapping integrals as disjoint energies.

For large `a,b`, `w_a~1/cosh a` uniformly, so

\[
 \chi\asymp1+e^{|a-b|}
 \asymp1+\max\{h/h',h'/h\}.
\tag{17}
\]

This proves (5) and exposes the loss when the neighboring lengths have
unbounded contrast. The bound is not claimed sharp in that regime.

## 5. Consequence and remaining boundary

Every fixed bounded-length-contrast family of actual prime pants obeys
(5); no existence, density or all-tail assertion about such a family is
needed. PF-369's nearly coincident periods, including its composite
realization, fall within this geometric regime. Their scalar residual
can still escape the window, but **no choice of finite-energy traces**
on these pants can make `s^(-1)H[g-f]/E_pant` unbounded. PF-370's stronger
vanishing ratio for its specified pair is compatible with this uniform
bound for all pairs.

The proof also gives (4) on pants with arbitrary length contrast. It does
not remove the factor (17), and therefore does not settle the uniform
comparison over the entire prime tail, where adjacent gap ratios need
not remain bounded. In particular, a failure of a uniform comparison
under (2) must leave every bounded-contrast regime. The offset condition
cannot be replaced silently by PF-363's total-offset condition.

Summing (4) over disjoint pants is a valid lower certificate with these
contrast factors. It does not give a matching upper trial at a shorted
residual scale, identify global transition minimizers, or determine the
completed normalized angle. There is no compactness, Schatten,
scattering, zeta-zero or RH conclusion. The geometry and energy argument
apply equally to nonprime tight pants. Removing the positive mass term
invalidates (9),(10); no unshifted result is asserted.

## 6. Prior art and validation

Basmajian–Hakobyan–Šarić, *The type problem for Riemann surfaces via
Fenchel–Nielsen parameters*, Proc. London Math. Soc. 125 (2022), 568–625,
[primary manuscript](https://arxiv.org/pdf/2011.03166), Section 5.2,
equations (26),(30) and the proof of Theorem 5.6, describe nonstandard
half-collars and their variable profile. The disjoint construction for
two cuffs using the third end is discussed before Lemma 6.4. These are
the classical geometric objects behind (6),(7), not new collars.
McMullen, *Complex Dynamics and Renormalization*, Section 2.9,
[pp. 23–24](https://people.math.harvard.edu/~ctm/papers/home/text/papers/real/book.pdf),
derives the ideal-quadrilateral collar identity and the tight-pants seam
sum used in (1). PF-125 records the exact local Lambert realization.

Post, *Boundary pairs associated with quadratic forms*,
[Section 6.1, equation (6.2)](https://arxiv.org/pdf/1210.4707), supplies
the classical interval DtN context. Minimizing its positive-shift form
over the second endpoint gives (9), also proved explicitly above.
Neither its interval theory nor the collar-modulus theorem is imported
as a pant-energy comparison. The derived addition is (10) together with
the periodized missing-tail bound (13) and PF-363's coupled corridor
restriction. This is a classical-geometry application, with no claim of
a new general trace theorem or of novelty from search absence.

A standard-library numerical check (seed `371`) tested 20 period pairs
`a in {8,12,20,40}`, `b-a in {-4,-1,0,1,4}`, using
`epsilon=1/8`, `vartheta=1/10` and the largest offsets in (2).
Four further pairs `(a,b)=(8,40),(40,8),(12,80),(80,12)` tested large
contrast. At 14,496 deterministic/random cuff points it checked the
split-plane containment, remaining interval floor and its `tanh` trace
charge, window bounds, and folded-tail inequality (13) with 12 positive
and 12 negative translates. All passed; the largest ratio of that finite
tail sum to its upper bound was approximately `0.9999999988`. The omitted positive terms are controlled analytically by the
displayed geometric series. These are floating-point checks of finite
formulas, not a pant PDE solve, interval certificate or independent
review. The proof above establishes the result; scratch is outside Git.
