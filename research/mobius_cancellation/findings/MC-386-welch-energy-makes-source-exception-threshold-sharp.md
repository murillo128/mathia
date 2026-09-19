# MC-386 — Cayley frame energy makes the source-exception threshold sharp

**Status:** `EXACT-DERIVED` · `CLASSICAL-MECHANISM` · `FRONTIER-ADVANCE` · `SHARP-OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact source-frame setting of `MC-374` and `MC-385`. Let

\[
W\le \mathbf F_2^R,
\qquad d=\dim W,
\qquad H=|W|=2^d,
\]

and let the normalized prime-shell source rows be indexed by `I in W`. Their Gram matrix has the Cayley form

\[
G_{I,J}=g(I+J),
\qquad g(0)=1,
\qquad G\succeq0,
\qquad \operatorname{rank}G\le R.
\tag{1}
\]

Then the source-difference correlations obey the exact energy floor

\[
\boxed{
\sum_{K\in W}|g(K)|^2\ge \frac HR,
\qquad
\sum_{0\ne K\in W}|g(K)|^2\ge \frac HR-1.
}
\tag{2}
\]

Consequently, suppose an analytic input controls every nonzero difference outside an exceptional set `B subset W\{0}` of size `E` by

\[
|g(K)|\le\varepsilon
\qquad(K\notin B),
\tag{3}
\]

while no better than the trivial `|g(K)|<=1` is known on `B`. Then necessarily

\[
\boxed{
\frac HR-1
\le
E+(H-1-E)\varepsilon^2,
}
\tag{4}
\]

and, whenever `epsilon<1`,

\[
\boxed{
E\ge
\frac{H/R-1-(H-1)\varepsilon^2}{1-\varepsilon^2}
}
\tag{5}
\]

when the numerator is positive.

This materially relaxes the nonexceptional correlation threshold in `MC-385`. There the row-sum/operator-norm estimate showed that the sufficient contradiction regime was

\[
E=o(H/R),\qquad \varepsilon=o(1/R).
\]

The frame-energy inequality proves that it is already enough to have

\[
\boxed{
E=o(H/R),\qquad \varepsilon=o(R^{-1/2}).
}
\tag{6}
\]

More quantitatively, if `H/R -> infinity` and

\[
\varepsilon^2\le \frac{1-\delta}{R}
\]

for fixed `delta in (0,1)`, then

\[
E\ge (\delta+o(1))\frac HR.
\tag{7}
\]

Thus a source-family theorem does **not** need inverse-rank cancellation on every good difference. Square-root-in-rank cancellation on the nonexceptional differences is the natural frame scale.

The exceptional-cardinality requirement, however, cannot be improved by abstract frame/Cayley arguments. If `R` is a power of two with `R<=H`, there is a positive-semidefinite Cayley Gram matrix of rank exactly `R` for which

\[
|g(K)|=
\begin{cases}
1,&K\in S^\perp,\\
0,&K\notin S^\perp,
\end{cases}
\tag{8}
\]

for a dual subgroup `S` of size `R`. It has exactly

\[
E=\frac HR-1
\tag{9}
\]

nonzero exceptional differences and zero correlation everywhere else, while attaining equality in `(2)`. For arbitrary `R`, taking the largest power of two `r<=R` gives the same construction with rank `r` and fewer than `2H/R` nonzero off-diagonal differences. Hence the `H/R` exceptional scale is sharp, up to an absolute factor for general `R`, under only the structural hypotheses in `(1)`.

The live collective target after `MC-385` is therefore more precise. A useful theorem may either control the **total squared source-difference correlation energy** below `H/R-1`, produce `E=o(H/R)` exceptions together with only `o(R^{-1/2})` correlation on the rest, or exploit arithmetic restrictions that make the abstract annihilator-subgroup extremizer impossible for the actual source characters. Merely improving ambient exceptional-modulus counts without controlling their intersection with the source difference frame remains insufficient.

No estimate for `M(x)` follows.

## 1. The frame potential forces `(2)`

Let the eigenvalues of `G` be `lambda_1,...,lambda_r`, where

\[
r=\operatorname{rank}G\le R.
\]

Because every source row is normalized,

\[
\operatorname{tr}G=H.
\tag{10}
\]

Cauchy--Schwarz on the nonzero eigenvalues gives

\[
\operatorname{tr}(G^2)
=\sum_{j=1}^r\lambda_j^2
\ge
\frac{(\sum_j\lambda_j)^2}{r}
\ge
\frac{H^2}{R}.
\tag{11}
\]

This is the standard frame-potential/Welch lower bound in the present normalization.

The Cayley structure converts `(11)` into a statement about **difference modes**, not merely arbitrary row pairs. Every `K in W` occurs as `I+J` for exactly `H` ordered pairs `(I,J)`, so

\[
\operatorname{tr}(G^2)
=\sum_{I,J\in W}|G_{I,J}|^2
=H\sum_{K\in W}|g(K)|^2.
\tag{12}
\]

Combining `(11)` and `(12)` proves the first inequality in `(2)`. Since `g(0)=1`, subtracting the diagonal contribution proves the second.

Equivalently, the average squared nontrivial source-difference correlation satisfies

\[
\frac1{H-1}\sum_{K\ne0}|g(K)|^2
\ge
\frac{H-R}{R(H-1)},
\tag{13}
\]

so at least one nonzero difference obeys the familiar Welch coherence scale

\[
\max_{K\ne0}|g(K)|
\ge
\sqrt{\frac{H-R}{R(H-1)}}.
\tag{14}
\]

For `H>>R`, the unavoidable correlation scale is therefore `R^{-1/2}`, not `R^{-1}`.

## 2. Exceptional modes obey the energy budget `(4)`

For source-character rows, every Gram entry is an average of unit-modulus character values, hence

\[
|g(K)|\le1.
\tag{15}
\]

Split the off-zero energy in `(2)` into `B` and its complement. Equations `(3)` and `(15)` give

\[
\sum_{K\ne0}|g(K)|^2
\le
E+(H-1-E)\varepsilon^2.
\tag{16}
\]

Together with `(2)`, this is `(4)`, and rearrangement gives `(5)`.

Two regimes are worth separating. If `E=0`, `(5)` reduces to `(13)` and no uniform theorem can force all difference correlations below approximately `R^{-1/2}`. If `epsilon=o(R^{-1/2})` and `H/R -> infinity`, `(5)` instead forces

\[
E\ge(1-o(1))H/R.
\tag{17}
\]

Thus the endpoint can evade strong nonexceptional cancellation only by placing a genuinely macroscopic number of **source-frame differences**, on the frame scale, into the exceptional set.

This does not repair the ambient-count mismatch in `MC-385`: a theorem saying that at most `P^theta` ambient conductors are exceptional still says nothing useful if the structured source image can concentrate inside them. What changes is the terminal-saving requirement on the nonexceptional modes. It is now the weaker and sharp frame scale `o(R^{-1/2})`.

## 3. The `H/R` exceptional scale is attained exactly

The sharpness control is purely finite harmonic analysis and deliberately ignores source arithmetic.

Assume first that `R=2^r` and choose a subgroup

\[
S\le \widehat W,
\qquad |S|=R.
\]

Define Fourier-side eigenvalues by

\[
\widehat g(\xi)=
\begin{cases}
H/R,&\xi\in S,\\
0,&\xi\notin S.
\end{cases}
\tag{18}
\]

All eigenvalues are nonnegative, so the associated Cayley matrix is positive semidefinite, and its rank is `R`. Fourier inversion and character orthogonality give

\[
g(K)=\frac1R\sum_{\xi\in S}\xi(K)
=1_{S^\perp}(K).
\tag{19}
\]

Therefore `g(0)=1`, the physical support has size `H/R`, and

\[
\sum_K|g(K)|^2=H/R.
\tag{20}
\]

This simultaneously saturates the frame-potential bound and the finite-group support uncertainty product

\[
|\operatorname{supp}g|\,|\operatorname{supp}\widehat g|=H.
\tag{21}
\]

After removing `K=0`, exactly `H/R-1` differences have correlation one and every other difference has correlation zero. Hence `(17)` cannot be strengthened to `E=o(H/R)` by any argument using only positivity, Cayley symmetry, unit diagonal and rank at most `R`.

If `R` is not a power of two, take `r_0=2^{\lfloor\log_2R\rfloor}`. Then `r_0<=R<2r_0`, so the same construction has admissible rank `r_0` and off-zero support

\[
H/r_0-1<2H/R-1.
\tag{22}
\]

The scale `H/R` is therefore uniformly sharp up to a factor smaller than two.

The construction is a **matched frame control**, not an arithmetic endpoint. It does not show that primitive quadratic source characters can realize the annihilator pattern. Precisely that gap is now the only place where a stronger exceptional-geometry conclusion can enter.

## 4. What this changes in the current source frontier

`MC-385` left signed/operator cancellation among a larger bad set as one possible escape from its absolute row-sum estimate. Equation `(2)` shows that signs cannot cancel the total Hilbert--Schmidt energy: every exact endpoint frame carries at least `H/R-1` off-diagonal difference energy. This yields a cleaner collective theorem surface than an operator-norm estimate one difference at a time.

There are now three mathematically distinct ways forward:

1. prove a source-family mean-square estimate
   `sum_(K ne 0)|g(K)|^2 < H/R-1` under a trial source-cost hypothesis;
2. prove nonexceptional pointwise cancellation at the natural `R^{-1/2}` scale while showing that fewer than `H/R` source differences are exceptional;
3. allow approximately `H/R` bad differences but use arithmetic information to rule out the subgroup/annihilator-type concentration that makes that number sufficient abstractly.

The first two are analytic estimates. The third is an exceptional-geometry problem on the actual source-conductor map. None follows from ordinary ambient exceptional-modulus counting.

This is a genuine narrowing relative to `MC-385`: the good-mode saving target is easier by a square root in rank, while the bad-mode cardinality threshold is certified sharp and therefore cannot be improved without extra arithmetic structure.

## 5. Prior art and novelty boundary

The frame inequality used in `(11)`--`(14)` is classical. L. R. Welch, *Lower bounds on the maximum cross correlation of signals*, IEEE Transactions on Information Theory **20** (1974), no. 3, 397--399, DOI `10.1109/TIT.1974.1055219`, gives the classical coherence bounds; modern frame language expresses the same trace/rank mechanism through the frame potential. John J. Benedetto and Matthew Fickus, *Finite normalized tight frames*, Advances in Computational Mathematics **18** (2003), 357--385, DOI `10.1023/A:1021323312367`, develops the frame-potential viewpoint and its tight-frame minimizers.

The support-product interpretation in `(21)` is also classical uncertainty-principle territory. David L. Donoho and Philip B. Stark, *Uncertainty Principles and Signal Recovery*, SIAM Journal on Applied Mathematics **49** (1989), no. 3, 906--931, DOI `10.1137/0149053`, treats discrete support/concentration uncertainty, and the full-support product principle extends to finite abelian groups. The subgroup identity `(19)` is ordinary character orthogonality.

No novelty is claimed for Welch/frame-potential inequalities, finite-group uncertainty, subgroup annihilators, or tight frames. The line-specific durable result is their pullback to the exact endpoint source-difference Cayley frame: `(4)`--`(7)` replace the `MC-385` inverse-rank good-mode requirement by the sharp square-root-in-rank scale while proving that the `H/R` source-exception count itself is an unavoidable and sharp structural threshold.

## Boundaries

- The sharpness construction is an abstract PSD Cayley frame. It is not claimed to arise from the actual lower-prime quadratic source characters.
- The result does not improve the current proven source-cost exponent. It changes the theorem shape needed to improve it.
- `E` counts exceptional **difference modes in the source frame**, not ambient moduli; several modes may share arithmetic features, and ambient counting does not automatically bound `E`.
- The energy floor does not forbid operator cancellation inside a bad set of size at least about `H/R`; it shows exactly how much squared correlation that set must be capable of carrying.
- Approximate structural stability of near-extremizers is not proved here.
- No statement about RH, zeros of `zeta`, or the true order of `M(x)` is made.
