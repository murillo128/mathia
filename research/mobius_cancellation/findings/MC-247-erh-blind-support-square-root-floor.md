# MC-247 — ERH forces square-root-scale blind support but still does not close shell generation

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CONDITIONAL`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell-square blind-character setting of `MC-239`--`MC-246`. Let

\[
y=c\log X,
\qquad
S\subset\{r\text{ prime}:y<r\le2y\},
\]

and let a nonprincipal blind character have active shell support

\[
T(\chi)=\{r\in S:\chi_r\ne1\},
\qquad
k(\chi)=|T(\chi)|.
\]

By `MC-239`, every blind character factors through the squarefree shell radical, so after deleting principal local components its active character `\chi_T` has conductor

\[
q_\chi=\prod_{r\in T(\chi)}r.
\]

Assume the Extended Riemann Hypothesis in the form used by Bach's explicit small-subgroup-witness theorem. Then every nonprincipal blind character satisfies, for sufficiently large `y`,

\[
\boxed{
 k(\chi)
 >
 \frac{\sqrt{y/2}}{\log(2y)}.
}
\tag{1}
\]

Thus the unconditional support floor from `MC-242`, which is only of order `\log\log y`, becomes conditionally

\[
k(\chi)\gg \frac{\sqrt y}{\log y}.
\tag{2}
\]

This is a substantial strengthening, but it still does **not** imply full small-prime generation. In the active first-shell regime used by `MC-243`,

\[
|S|\asymp\frac y{\log y},
\]

so `(2)` remains smaller than the full shell size by a factor of order `\sqrt y`.

For the quadratic blind code

\[
K_y(S)=\ker_{\mathbb F_2}A
\]

of `MC-238`/`MC-243`, `(1)` gives the same lower bound for every nonzero codeword. Combining this conditional minimum distance with the Hamming sphere-packing argument already isolated in `MC-243` yields

\[
\boxed{
\operatorname{rank}_{\mathbb F_2}A
\ge
\left(\frac{1}{4\sqrt2\,\log2}-o(1)\right)\sqrt y
}
\tag{3}
\]

whenever the quadratic blind sector is nontrivial; if it is trivial, the rank is already `|S|`. Abstract coding-theory controls still permit binary linear kernels with the same minimum-distance scale and redundancy only `O(\sqrt y)`, so even this ERH-strengthened support information remains parametrically insufficient to force full rank `\asymp y/\log y`.

The durable conclusion is therefore two-sided:

\[
\boxed{
\text{generic ERH small-witness theory greatly thins blind modes,}
\quad
\text{but does not prove }H=G\text{ for the shell family.}
}
\tag{4}
\]

Any proof of the `H=G` exit in `MC-246` must exploit additional simultaneous shell structure beyond the generic ERH subgroup-witness bound, or bypass generation and prove cancellation in the source-selected rough Möbius coset directly.

No RH/GRH consequence is proved; `(1)`--`(3)` are conditional consequences of ERH.

## 1. Blindness puts every integer below `y` in one proper character kernel

For a nonprincipal blind `\chi`, `MC-239` gives the active primitive character

\[
\chi_T=\prod_{r\in T(\chi)}\chi_r
\pmod{q_\chi},
\qquad
q_\chi=\prod_{r\in T(\chi)}r.
\tag{5}
\]

Every active shell prime satisfies `r>y`. Hence every positive integer `n<y` is coprime to `q_\chi`. Moreover, all prime factors of such an `n` are at most `y`, while blindness means

\[
\chi_T(p)=1
\qquad
(p\le y\text{ prime}).
\tag{6}
\]

Complete multiplicativity therefore gives

\[
\boxed{
\chi_T(n)=1
\qquad
(1\le n<y).
}
\tag{7}
\]

Thus the proper subgroup

\[
G_\chi:=\ker\chi_T
< (\mathbb Z/q_\chi\mathbb Z)^\times
\tag{8}
\]

contains every positive integer below `y`.

This is exactly the input of Bach's subgroup-witness theorem; no new translation through prime sums, Möbius estimates, or zero-density arguments is needed.

## 2. Bach's ERH bound converts directly into a support floor

Bach's 1990 explicit theorem states, under ERH, that if a proper multiplicative subgroup of the reduced residues modulo `m` contains every positive integer below `x`, then

\[
x<2(\log m)^2.
\tag{9}
\]

Apply `(9)` to `(8)` with `m=q_\chi` and `x=y`. Equation `(7)` gives the subgroup hypothesis, hence

\[
y<2(\log q_\chi)^2.
\tag{10}
\]

If `k=k(\chi)`, all active conductor primes lie in `(y,2y]`, so

\[
q_\chi
=\prod_{r\in T(\chi)}r
\le(2y)^k
\tag{11}
\]

and therefore

\[
\log q_\chi\le k\log(2y).
\tag{12}
\]

Combining `(10)` and `(12)` yields

\[
y
<2k^2\log^2(2y),
\]

which is exactly `(1)`.

This derivation also explains why simply invoking a generic ERH generator theorem does not close the shell problem. For a full shell modulus, `\log q` is itself of order `y`; Bach's generic generator cutoff is therefore of order `y^2`, whereas the physical smooth-dilation subgroup is generated only by primes up to `y`. The support-sensitive reduction above extracts what the generic theorem *does* force: any surviving blind relation must spread over at least `\gg\sqrt y/\log y` shell coordinates.

## 3. Conditional quadratic-code rank pressure rises only to `sqrt(y)`

For the quadratic sector, a nonzero vector

\[
v\in K_y(S)=\ker_{\mathbb F_2}A
\]

corresponds to a blind quadratic character whose active shell support equals the Hamming support of `v`. Hence its minimum distance `d_y` obeys, conditionally on ERH,

\[
d_y
\ge
\left(\frac1{\sqrt2}-o(1)\right)
\frac{\sqrt y}{\log y}.
\tag{13}
\]

Let

\[
n=|S|
=\left(\frac\alpha c+o(1)\right)\frac y{\log y}
\tag{14}
\]

in the active first-shell scaling of `MC-243`, and put

\[
t_y=\left\lfloor\frac{d_y-1}{2}\right\rfloor.
\]

The exact Hamming bound from `MC-243` gives

\[
\operatorname{rank}A
\ge
\log_2\!\left(\sum_{j=0}^{t_y}\binom nj\right)
\ge
\log_2\binom n{t_y}.
\tag{15}
\]

Here `t_y=o(n)` and

\[
t_y
=\left(\frac1{2\sqrt2}-o(1)\right)
\frac{\sqrt y}{\log y},
\qquad
\log\frac n{t_y}
=\frac12\log y+O(1).
\tag{16}
\]

Using the standard small-weight binomial asymptotic

\[
\log_2\binom nt
=
\frac{t}{\log2}\left(\log\frac nt+O(1)\right)
\qquad(t=o(n))
\tag{17}
\]

gives `(3)`.

This improves the unconditional coding-pressure scale in `MC-243` from

\[
\asymp \log y\,\log\log y
\]

to

\[
\asymp\sqrt y.
\]

But the target full rank is still

\[
n\asymp\frac y{\log y},
\]

so the conditional generic rank pressure remains lower by the diverging factor `\asymp\sqrt y/\log y`.

## 4. Minimum-support information remains insufficient even under ERH

The negative coding control of `MC-243` survives at the stronger scale. Standard Gilbert--Varshamov/Varshamov existence bounds permit binary linear codes of length

\[
n\asymp\frac y{\log y}
\]

and minimum distance

\[
d\asymp\frac{\sqrt y}{\log y}
\]

with redundancy bounded by

\[
O\!\left(d\log\frac nd\right)
=O(\sqrt y).
\tag{18}
\]

Thus abstract kernels can satisfy the entire ERH-derived minimum-support floor while still having dimension

\[
n-O(\sqrt y).
\tag{19}
\]

This is not a model for the actual Legendre matrix; it is a matched information control. It proves that **minimum blind support by itself**, even at the ERH scale `(2)`, cannot force annihilator triviality or full quadratic rank. Any stronger conclusion must use arithmetic dependencies among the Legendre columns, a direct quotient-size theorem, simultaneous character information beyond least witnesses, or source-coupled signed cancellation.

## 5. Prior art and novelty audit

The external theorem is classical and no novelty is claimed for it:

Eric Bach, *Explicit bounds for primality testing and related problems*, Mathematics of Computation 55 (1990), no. 191, 355--380, DOI `10.1090/S0025-5718-1990-1023756-8` (also `10.2307/2008811`). Under ERH, Bach gives the explicit proper-subgroup witness bound used in `(9)`; standard later expositions restate it as: if a proper subgroup of `(Z/mZ)^*` contains every positive integer below `x`, then `x<2(log m)^2`.

An accessible published restatement is H. C. Williams and J. O. Shallit, *Factoring integers before computers*, in *Mathematics of Computation 1943--1993: A Half-Century of Computational Mathematics*, Proc. Sympos. Appl. Math. 48 (1994), which quotes Bach's conditional theorem in exactly this subgroup form and derives the corresponding pseudosquare lower bound.

`MC-240` already used Pollack's unconditional prime-character-nonresidue theorem to force the fixed support floor `k>=7`; `MC-242` strengthened the unconditional shell support to order `log log y` through smooth-modulus character-sum technology. The present finding does not replace either theorem. It records the materially stronger **conditional** support consequence obtained by feeding the exact shell conductor into Bach's ERH subgroup witness.

The literature audit did not identify a separate published theorem formulated as the square-root-over-log support bound `(1)` for this source-selected shell annihilator, nor as the rank consequence `(3)`. No novelty is claimed for Bach's theorem, character kernels, the conductor product, Hamming sphere packing, or Varshamov bounds. The durable Mathia delta is the specialization and the resulting quantitative diagnosis of the `H=G` exit.

## 6. Boundaries and falsification tests

- The result is conditional on ERH/GRH-strength zero information for the relevant Dirichlet `L`-functions. It must not be presented as unconditional progress on Möbius cancellation or RH.
- Bach's theorem is applied to the **active conductor** `q_\chi`, not the full shell modulus. Replacing it by the full modulus would lose the support-sensitive inequality and would not prove `(1)`.
- The fact that every `n<y` lies in `ker chi_T` uses the exact shell separation `r>y`. If the modulus family changes, this step must be rechecked.
- `(1)` is a support lower bound, not a bound on the number of blind characters, the quotient index `[G:H]`, a Fourier-decay estimate, or a signed Möbius amplitude estimate.
- `(3)` concerns only the quadratic blind code. The general character support result `(1)` does not by itself linearize the full annihilator over `F_2`.
- The coding-theory comparison in `(18)`--`(19)` is an information-theoretic control, not evidence that the actual Legendre kernel attains those dimensions.
- Even proving `H=G` would leave the separate rough-coset signed-cancellation/amplitude issue isolated by `MC-246`; this finding closes neither route.
