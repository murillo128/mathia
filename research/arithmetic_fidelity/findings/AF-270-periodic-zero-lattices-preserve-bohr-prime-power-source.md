# AF-270 — Periodic zero lattices preserve Bohr recurrence and prime-power source support

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SOURCE`, `ALMOST-PERIODICITY`, `INFINITE-ZERO-TRANSPORT`, `REFLECTION-SYMMETRY`, `PRIME-POWER-SPECTRUM`, `SHARPNESS`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-268 and AF-269 show that finite zero surgery, and more generally every nontrivial paired zero rearrangement of finite total displacement, exits the exact Bohr-almost-periodic source category on a right-half-plane vertical line. That obstruction is sharp in a strong arithmetic sense: an infinite count-preserving zero transport can remain exactly periodic, reflection-symmetric, and supported on a single rational-prime-power Dirichlet frequency ray.

Fix a rational prime `p`, put

\[
\lambda:=\log p,
\qquad
L:=\frac{2\pi}{\lambda},
\tag{1}
\]

and for a real parameter `a in (0,1)` define

\[
E_a(s):=1-p^{a-s},
\qquad
H_a(s):=E_a(s)E_a(1-s).
\tag{2}
\]

Then `H_a` is an entire exponential polynomial of order one satisfying

\[
H_a(1-s)=H_a(s),
\qquad
\overline{H_a(\overline s)}=H_a(s).
\tag{3}
\]

Its zero divisor is

\[
\boxed{
Z(H_a)
=
\{a+i nL:n\in\mathbb Z\}
\sqcup
\{1-a+i nL:n\in\mathbb Z\},
}
\tag{4}
\]

with multiplicity. At `a=1/2` these two lattices coincide, so every zero on

\[
\Re s=\frac12
\tag{5}
\]

has multiplicity two. For `a\ne1/2`, the same two zeros at each ordinate split horizontally to the symmetric off-critical pair `Re s=a` and `Re s=1-a`.

Therefore the ordinate-counting function is **exactly unchanged**:

\[
\boxed{
N_a(T)
:=
\#\{\rho\in Z(H_a):0<\Im\rho\le T\}
=
N_{1/2}(T)
}
\tag{6}
\]

for every `T`, counting multiplicity. The transport from `H_{1/2}` to `H_a` nevertheless has infinite total displacement. Every transported zero moves a horizontal distance at least

\[
d:=\left|a-\frac12\right|>0,
\tag{7}
\]

and there are infinitely many zeros, so every bijective matching of the two divisors has infinite `l^1` transport cost.

Despite that off-critical transport, on every half-plane

\[
\Re s>\max(a,1-a)
\tag{8}
\]

the logarithmic derivative has the absolutely convergent ordinary Dirichlet expansion

\[
\boxed{
\frac{H_a'}{H_a}(s)
=
\lambda
+
\lambda\sum_{k\ge1}
\bigl(p^{ka}+p^{k(1-a)}\bigr)p^{-ks}.
}
\tag{9}
\]

Thus on every fixed line in `(8)` the vertical trace is exactly periodic with period `L`, hence Bohr uniformly almost periodic. Its nonconstant Bohr spectrum lies entirely on the single rational prime-power ray

\[
\{k\log p:k\ge1\},
\tag{10}
\]

up to the sign convention for vertical Fourier frequencies.

Even the **difference** between the off-critical and critical-line controls stays inside the same source class. Subtracting the case `a=1/2` gives

\[
\boxed{
\frac{H_a'}{H_a}(s)
-
\frac{H_{1/2}'}{H_{1/2}}(s)
=
\lambda\sum_{k\ge1}c_k(a)p^{-ks},
}
\tag{11}
\]

where

\[
\begin{aligned}
c_k(a)
&=p^{ka}+p^{k(1-a)}-2p^{k/2}\\
&=2p^{k/2}
\left[
\cosh\!\left(k\lambda\left(a-\frac12\right)\right)-1
\right]
>0
\end{aligned}
\tag{12}
\]

for every `k>=1` when `a\ne1/2`.

Hence the transition

\[
\text{double critical vertical lattice}
\longrightarrow
\text{symmetric off-critical vertical lattices}
\tag{13}
\]

preserves all of the following simultaneously:

- order-one entire-function category;
- Riemann-type reflection and real-conjugation symmetries;
- exact zero count by ordinate, with multiplicity;
- exact Bohr recurrence of the right-half-plane logarithmic-derivative trace;
- an absolutely convergent ordinary Dirichlet source;
- the exact prime-power frequency support `p^k`;
- one-sided coefficient sign in the source difference `(11)`.

What changes is the **coefficient law** on that retained prime-power ray. Consequently, recurrence and rational-prime frequency provenance are not by themselves faithful to critical-line location. Any stronger zeta-source gate must constrain the actual local coefficient/Euler-factor law, or another structure at least as discriminating, rather than merely requiring almost periodicity or the correct frequency alphabet.

## Exact derivation

### 1. Reflection-symmetric exponential polynomial and its zero divisor

Expanding `(2)` gives

\[
H_a(s)
=
1-p^ap^{-s}-p^{a-1}p^s+p^{2a-1}.
\tag{14}
\]

This is a nonconstant finite exponential sum with exponents `-lambda`, `0`, and `lambda`, so it is entire of exponential type and order one. Interchanging `s` and `1-s` swaps the two factors in `(2)`, which proves the first identity in `(3)`. Real `a` and `p` give the conjugation identity.

The equation `E_a(s)=0` is

\[
p^{a-s}=1,
\tag{15}
\]

hence

\[
s=a+i nL,
\qquad n\in\mathbb Z,
\tag{16}
\]

after reindexing the sign of `n`. Applying the same calculation to `E_a(1-s)` gives

\[
s=1-a+i nL.
\tag{17}
\]

Equations `(16)` and `(17)` prove `(4)`. At `a=1/2` the two factors have the same zero set and every zero is double. When `a\ne1/2` the two real parts are distinct, while the ordinates remain exactly the same. This proves `(6)`.

For any matching from the double lattice at `Re s=1/2` to the split divisor in `(4)`, every image point has real part either `a` or `1-a`. Its Euclidean distance from any source point on `Re s=1/2` is therefore at least `d` from `(7)`, independent of how ordinates are permuted. Summing over infinitely many points gives infinite total displacement. Thus this family lies exactly outside the finite-transport class ruled out by AF-269.

### 2. The off-critical divisor has an exact periodic Dirichlet source

Write

\[
x=p^{a-s}.
\tag{18}
\]

For `Re s>a`, `|x|<1`, and

\[
\frac{E_a'}{E_a}(s)
=
\lambda\frac{x}{1-x}
=
\lambda\sum_{k\ge1}p^{ka}p^{-ks}.
\tag{19}
\]

For the reflected factor put

\[
y=p^{a-1+s}.
\tag{20}
\]

If `Re s>1-a`, then `|y|>1`, so

\[
\begin{aligned}
\frac{d}{ds}\log E_a(1-s)
&=-\lambda\frac{y}{1-y}\\
&=\lambda\frac{1}{1-y^{-1}}\\
&=\lambda
+\lambda\sum_{k\ge1}p^{k(1-a)}p^{-ks}.
\end{aligned}
\tag{21}
\]

Adding `(19)` and `(21)` proves `(9)`. On every closed vertical line strictly inside `(8)`, both geometric series converge absolutely and uniformly in `t`.

Every nonconstant term is of the form

\[
p^{-k(\sigma+it)}
=p^{-k\sigma}e^{-itk\lambda}.
\tag{22}
\]

Since `lambda L=2pi`, translation by `L` leaves every term unchanged. The complete trace is therefore periodic, not merely almost periodic, and its frequencies are exactly the prime-power frequencies `(10)`.

### 3. The critical-to-off-critical transport preserves the source alphabet

At `a=1/2`, equation `(9)` becomes

\[
\frac{H_{1/2}'}{H_{1/2}}(s)
=
\lambda
+2\lambda\sum_{k\ge1}p^{k/2}p^{-ks}.
\tag{23}
\]

Subtracting `(23)` from `(9)` gives `(11)`. Formula `(12)` follows by factoring `p^{k/2}` and using

\[
p^{k(a-1/2)}+p^{-k(a-1/2)}
=2\cosh\!\left(k\lambda\left(a-\frac12\right)\right).
\tag{24}
\]

Strict positivity follows for `a\ne1/2` because `cosh u>1` for `u\ne0`.

This is stronger than merely exhibiting an almost-periodic infinite surgery. The critical and off-critical divisors have the same vertical counting data and their logarithmic derivatives use the same **single rational-prime-power frequency ray**. No generalized or irrational frequency has been introduced. The surgery is encoded entirely by changing the coefficient profile carried on that already-retained ray.

### 4. The obstruction can be grafted onto a completed-zeta control

Let `G` be any order-one entire function with

\[
G(1-s)=G(s),
\qquad
\overline{G(\overline s)}=G(s).
\tag{25}
\]

Then

\[
F_a(s):=G(s)H_a(s)
\tag{26}
\]

has the same order and symmetries. The pair `F_a,F_{1/2}` shares the complete zero divisor of `G`; the only difference is the exact count-preserving lattice transport `(13)`. Moreover

\[
\frac{F_a'}{F_a}(s)
-
\frac{F_{1/2}'}{F_{1/2}}(s)
=
\frac{H_a'}{H_a}(s)
-
\frac{H_{1/2}'}{H_{1/2}}(s),
\tag{27}
\]

so the source defect remains exactly `(11)`.

Taking `G=xi` shows that this periodic control can be grafted onto the Riemann completed-function setting without changing the fixed completion term used in AF-266--AF-269. On `Re s>1`, equation `(27)` adds no frequency outside the existing rational prime-power alphabet of the Euler logarithmic derivative. This does **not** make `F_a` another zeta function and does not preserve the von-Mangoldt coefficient law; rather, it isolates that coefficient law as information not captured by recurrence, reflection symmetry, zero counting, or the frequency set alone.

## What this changes in the Arithmetic Fidelity audit

AF-269 left one necessary escape for a nontrivial source-compatible zero rearrangement: every admissible pairing must have infinite total displacement, unless the source law changes through a genuinely global recurrent component. The family `(2)` realizes exactly that escape.

The resulting boundary is now sharp:

\[
\begin{aligned}
\text{finite-total zero transport}
&\Longrightarrow
\text{transient }C_0\text{ defect}\\
&\Longrightarrow
\text{not Bohr recurrent},\\[2mm]
\text{periodic infinite zero transport}
&\Longrightarrow
\text{periodic Dirichlet defect}\\
&\Longrightarrow
\text{exact Bohr recurrence survives}.
\end{aligned}
\tag{28}
\]

More importantly, the surviving recurrent defect is not merely an arbitrary discrete-source artifact. It occupies an actual rational-prime-power frequency ray. Thus replacing the generic `AP(R)` gate by the stronger statement “the source has rational prime-power Bohr frequencies” still does not identify critical-line geometry.

The missing resource is finer: the arithmetic source must control **which coefficients are attached to those frequencies** and how those coefficients are coupled across primes, prime powers, normalization, and global completion. In the genuine Riemann channel those coefficients are the von-Mangoldt law. Equation `(11)` demonstrates that the frequency alphabet can stay fixed while an infinite reflection-symmetric divisor moves off the critical line.

This does not prove that the full von-Mangoldt coefficient law admits any such surgery. On the contrary, exact equality of the full right-half-plane logarithmic derivative would determine the meromorphic function up to a zero-free exponential factor and therefore rigidify its divisor under the normalization already studied in AF-017--AF-019. The new result identifies the boundary between those two extremes: **source category and source support are too coarse; exact source weights are potentially rigid enough.**

## Prior art and novelty assessment

The general mechanism belongs to classical almost-periodic and exponential-polynomial theory. Børge Jessen and Hans Tornehave, **“Mean motions and zeros of almost periodic functions,”** *Acta Mathematica* 77 (1945), 137--279, DOI `10.1007/BF02392225`, is foundational prior art for zeros of analytic almost-periodic functions. S. Yu. Favorov, **“Almost periodic divisors, holomorphic functions, and holomorphic mappings,”** *Bulletin des Sciences Mathématiques* 127(10), 859--883 (2003), DOI `10.1016/j.bulsci.2003.06.001`, develops divisor criteria in the Bohr-compactification setting.

Ingo Schoolmann, **“On Bohr's theorem for general Dirichlet series,”** *Mathematische Nachrichten* 293(8), 1591--1612 (2020), DOI `10.1002/mana.201800542`, gives modern vertical-line almost-periodicity results for general Dirichlet series. Most directly, S. Yu. Favorov, **“Application of methods of quasicrystals theory to entire functions of exponential growth,”** *Analysis Mathematica* 51, 1313--1325 (2025), DOI `10.1007/s10476-025-00106-4`, relates pure-point Fourier data of zero measures for entire almost-periodic functions of exponential growth to Dirichlet-series coefficients of their logarithmic derivatives. That literature makes clear that recurrent divisor/source correspondences for exponential polynomials are established mathematics.

Accordingly, no novelty is claimed for the functions `(2)`, their periodic zero lattices, geometric-series expansions, or the general correspondence between periodic/almost-periodic divisors and discrete logarithmic-derivative spectra.

The Arithmetic Fidelity contribution is the **specific matched-control sharpness theorem for the AF-268--AF-269 obstruction**: a double critical-line lattice can be transported to a reflection-symmetric off-critical pair with exactly the same ordinate count while retaining an ordinary Dirichlet logarithmic derivative on precisely the same rational prime-power frequency ray. This identifies coefficient provenance, rather than recurrence or frequency support alone, as the next information layer that a zeta-specific fidelity gate must retain.

## Boundaries and failure modes

- `H_a` is a diagnostic exponential-polynomial control, not a zeta function. It does not preserve the exact von-Mangoldt coefficients, Euler product normalization, trivial-zero structure, or all other zeta-specific data.
- The exact counting statement `(6)` is counting by ordinate with multiplicity. Disk counts depend on the changed real parts and are not asserted to agree pointwise.
- The construction changes infinitely many zeros by a fixed positive horizontal amount, so it does not challenge AF-269; it realizes precisely the infinite-transport regime that AF-269 leaves open.
- The source series `(9)` is asserted only in the right half-plane `(8)`, where it converges absolutely. No almost-periodic continuation through the zero strip is claimed.
- The prime-power support statement is about the logarithmic derivative. It does not say that the entire function itself has an Euler product over rational primes or that its coefficients equal the von-Mangoldt law.
- Reflection symmetry and real conjugation alone are therefore still too weak. The construction is designed to expose that weakness, not to suggest that the actual Riemann `xi` admits such an independent factor while preserving all of its arithmetic data.
- Positivity in `(12)` is convention-dependent under an overall sign of the logarithmic derivative. The invariant statement is that every coefficient has the same nonzero sign; no positivity theorem for the Weil form or for zeta is implied.

## Evidence classification

`EXACT-DERIVED` for the divisor formula, exact ordinate-count preservation, infinite transport cost, Dirichlet expansion, periodicity, prime-power frequency support, and coefficient-sign formula `(12)`. `LITERATURE+DERIVED` for placement inside classical almost-periodic divisor/exponential-polynomial theory. The result is a sharp Arithmetic Fidelity counterexample to recurrence/support-level source rigidity, with **no broad novelty claim** for its classical analytic ingredients.