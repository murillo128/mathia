# MC-227 — Möbius BDH gives arbitrary-log first-shell energy but no fixed-power gain

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Keep the first square-defect shell of `MC-221`--`MC-226`:

\[
y=c\log X,
\qquad
P=\prod_{p\le y}p,
\qquad
T=X-P,
\]

\[
A_d(T)=
\sum_{\substack{n\le T\\(n,P)=1\\n\equiv-P\pmod{d^2}}}\mu(n),
\qquad
y<d\le2y,\ d\text{ prime},
\]

and

\[
W_y(X)=
\sum_{y<d\le2y\atop d\text{ prime}}d\,|A_d(T)|^2.
\tag{1}
\]

The classical Barban--Davenport--Halberstam theorem for the Möbius function, combined with the exact smooth-semigroup removal of the primorial cutoff from `MC-222`, gives the unconditional bound

\[
\boxed{
W_y(X)\ll_A \frac{X^2}{(\log X)^A}
\qquad\text{for every fixed }A>0.
}
\tag{2}
\]

Thus the exact first-shell energy already enjoys **arbitrarily strong fixed logarithmic savings** from classical Möbius arithmetic-progression variance. Nevertheless `(2)` remains

\[
X^{2-o(1)},
\]

whereas the shell target is

\[
W_y(X)\le X^{1+o(1)}.
\tag{3}
\]

So even Möbius-specific all-residue dispersion, at arbitrary fixed logarithmic strength, misses the target by one full power of `X`. This sharpens `MC-224`: the obstruction is not merely that a coefficient-uniform large sieve forgets Möbius arithmetic. Classical Möbius BDH does use that arithmetic and still remains power-insufficient after the primorial fibers are separated.

The exact loss in the composition occurs when the smooth-semigroup fibers are estimated independently and recombined by Minkowski. Therefore a continuation of this route must obtain a **fixed-power gain from signed coupling between those fibers, between the shell moduli, or directly from the common source relation**

\[
n+P=d^2m,
\]

rather than merely replacing one logarithmic progression estimate by a stronger fixed power of `log X`.

No fixed-power improvement for `W_y`, no new BDH theorem, and no consequence for RH is proved here.

## 1. Classical Möbius BDH input

For

\[
M(U;q,a):=
\sum_{m\le U\atop m\equiv a\pmod q}\mu(m),
\qquad (a,q)=1,
\tag{4}
\]

classical Barban--Davenport--Halberstam theory gives the following form: for every fixed `K>0`, there is a fixed `B=B(K)` such that

\[
\boxed{
\sum_{q\le U/(\log U)^B}
\sum_{a\in(\mathbb Z/q\mathbb Z)^*}
|M(U;q,a)|^2
\ll_K
\frac{U^2}{(\log U)^K}.
}
\tag{5}
\]

Klurman--Mangerel--Teräväinen, *Multiplicative functions in short arithmetic progressions*, Proceedings of the London Mathematical Society 127 (2023), 366--446, DOI `10.1112/plms.12546`, record `(5)` explicitly as their equation (11) in the prior-art discussion of Barban--Davenport--Halberstam theory. This paper is already anchored as `MC-S45` in `SOURCES.md`.

The theorem is substantially stronger for the present calculation than a generic coefficient large sieve: it is a theorem about the actual Möbius sequence and gives an arbitrary fixed power of logarithmic saving. The question is whether that strength changes the exponent budget of `(1)`.

## 2. Exact primorial removal reduces the shell to ordinary progression sums

`MC-222` records the exact identity

\[
\mu(n)\mathbf 1_{(n,P)=1}
=
(\mu*\mathbf 1_{\mathcal S_P})(n),
\]

where

\[
\mathcal S_P
=
\{r\ge1:p\mid r\Rightarrow p\le y\}.
\]

Since every shell prime `d` satisfies `d>y`, each `r\in\mathcal S_P` is invertible modulo `d^2`. Hence

\[
\boxed{
A_d(T)
=
\sum_{\substack{r\le T\\r\in\mathcal S_P}}
M\!\left(T/r;d^2,-P\overline r\right).
}
\tag{6}
\]

The residue `-P\overline r` is reduced modulo `d^2`. Thus `(5)` applies to every individual smooth-semigroup fiber in `(6)` once its length is large enough.

Two standard estimates used already in `MC-222` will be needed below. First,

\[
|\mathcal S_P\cap[1,X]|=X^{o(1)}
\tag{7}
\]

at `y=c log X`. Second, Mertens' product theorem gives

\[
\sum_{r\in\mathcal S_P}\frac1r
=
\prod_{p\le y}(1-p^{-1})^{-1}
\ll \log y
\asymp\log\log X.
\tag{8}
\]

## 3. BDH controls every main semigroup fiber in the shell energy

Fix

\[
\eta=\frac13
\]

and first restrict `(6)` to

\[
r\le X^{1-\eta}=X^{2/3}.
\]

Then

\[
U_r:=T/r\ge X^{\eta+o(1)}.
\tag{9}
\]

For the shell,

\[
d^2\le4c^2(\log X)^2.
\tag{10}
\]

For every fixed `K`, `(9)` implies for sufficiently large `X` that

\[
4c^2(\log X)^2
\le
\frac{U_r}{(\log U_r)^{B(K)}}.
\tag{11}
\]

Therefore `(5)` applies at length `U_r` to a range containing every modulus `d^2` in the shell.

For each main fiber define its weighted shell energy

\[
E_r
:=
\sum_{y<d\le2y\atop d\text{ prime}}
 d\,
\left|M(U_r;d^2,-P\overline r)\right|^2.
\tag{12}
\]

Since `d\le2y`, and the selected residues and square moduli form only a subset of the nonnegative terms in `(5)`, we obtain

\[
E_r
\ll_K
 y\frac{U_r^2}{(\log U_r)^K}.
\tag{13}
\]

Now view the shell coordinates as vectors with norm

\[
\|v\|_W^2
:=
\sum_{y<d\le2y\atop d\text{ prime}}d|v_d|^2.
\]

Minkowski applied to `(6)` and `(13)` gives

\[
\begin{aligned}
W_{\rm main}^{1/2}
&\le
\sum_{r\le X^{2/3}\atop r\in\mathcal S_P}
E_r^{1/2}\\
&\ll_K
\sqrt y
\sum_{r\le X^{2/3}\atop r\in\mathcal S_P}
\frac{X/r}{(\log(X/r))^{K/2}}.
\end{aligned}
\tag{14}
\]

Because `log(X/r)>= (1/3)log X` in this range, `(8)` yields

\[
W_{\rm main}^{1/2}
\ll_K
\frac{X\sqrt y\,\log y}{(\log X)^{K/2}},
\]

and hence

\[
\boxed{
W_{\rm main}
\ll_K
\frac{X^2\,y(\log y)^2}{(\log X)^K}
\ll_K
\frac{X^2(\log\log X)^2}{(\log X)^{K-1}}.
}
\tag{15}
\]

Since `K` in the classical theorem is any fixed constant, `(15)` gives any prescribed fixed logarithmic saving after increasing `K` by a fixed amount.

## 4. The large-semigroup tail is below the target scale

It remains to control

\[
r>X^{2/3}.
\]

For each such `r`, use the trivial progression estimate

\[
|M(T/r;d^2,b)|
\le
\frac{T}{rd^2}+1.
\tag{16}
\]

By `(7)`, the number of admissible `r\le X` is `X^{o(1)}`. Since each tail element also satisfies `1/r\le X^{-2/3}`, summing `(16)` gives, uniformly in the shell,

\[
\left|
\sum_{r>X^{2/3}\atop r\in\mathcal S_P}
M(T/r;d^2,-P\overline r)
\right|
\le X^{1/3+o(1)}.
\tag{17}
\]

Consequently

\[
W_{\rm tail}
\ll
X^{2/3+o(1)}
\sum_{y<d\le2y\atop d\text{ prime}}d
=
X^{2/3+o(1)}.
\tag{18}
\]

Writing `A_d=A_{d,main}+A_{d,tail}` and using `|u+v|^2<=2|u|^2+2|v|^2`, equations `(15)` and `(18)` prove `(2)` after relabeling the arbitrary fixed logarithmic exponent.

## 5. The result strengthens the present obstruction rather than closing it

The target `(3)` needs a full power improvement over `(2)`. For every fixed `A`,

\[
\frac{X^2}{(\log X)^A}
=
X^{2-o(1)},
\]

so taking a larger fixed logarithmic exponent never changes the leading power of `X`.

This separates three levels of information already present in the line:

- `MC-224` shows that a coefficient-uniform additive/square-modulus large-sieve norm remains at `X^{2-o(1)}` and therefore loses too much arithmetic information;
- the present finding inserts genuine Möbius-specific BDH cancellation and improves that envelope by every fixed logarithmic power, but the exponent remains `2`;
- `MC-222` shows that GRH-quality square-root progression cancellation reaches `X^{1+o(1)}` and closes the shell.

Thus the gap is not plausibly repaired by another fixed logarithmic strengthening of generic progression dispersion. A new input must alter the **power-scale geometry** of the estimate.

The derivation also identifies where the remaining information can hide. Equation `(5)` is applied separately for each `r` and `(14)` takes absolute norm before summing the smooth fibers. Any cancellation between the vectors

\[
\left(
M(T/r;d^2,-P\overline r)
\right)_{d}
\]

is discarded. But those vectors are not arbitrary: all residues arise from the same primorial source through the exact lift `n+P=d^2m`. A source-coupled theorem that controls the sum in `(6)` directly can therefore evade this obstruction; a stronger theorem that still treats each fiber independently cannot do so merely by gaining `log^{-A}X`.

## 6. Prior-art and novelty assessment

The Möbius Barban--Davenport--Halberstam estimate `(5)` is classical prior art. `MC-S45` provides a modern primary-paper statement and points to the classical literature. The semigroup identity `(6)`, the smooth-number count `(7)`, and the role of the first-shell energy are already established in `MC-222` and its dependencies.

The repository contribution is the **composition and rate audit at the exact active shell**: classical Möbius BDH can be transported through the logarithmic-primorial semigroup strongly enough to give arbitrary fixed logarithmic savings for `W_y` itself, but that still leaves the power exponent unchanged. A targeted literature search found the classical/all-modulus Möbius variance theory and stronger modern multiplicative-function progression results, but no theorem that supplies the source-coupled fixed-power gain required after `(14)`. No novelty is claimed for BDH or for the elementary norm manipulations.

## 7. Boundaries and falsification tests

- Equation `(2)` is an upper bound obtained from classical BDH plus the exact semigroup decomposition. It is not claimed to be sharp for the actual first-shell energy.
- The use of Minkowski in `(14)` is deliberately lossy. Cancellation between different `r`-fibers could be decisive and is not ruled out.
- The arbitrary logarithmic exponent is fixed before `X` tends to infinity. One may not choose `K=K(X)` growing with `X`; the constants and the modulus-range exponent `B(K)` in `(5)` depend on `K`.
- The derivation uses only reduced residues, which is legitimate because `d>y`, `(P,d)=1`, and every `r\in\mathcal S_P` is coprime to `d`.
- The tail estimate uses the established `X^{o(1)}` count of `y`-smooth integers at `y=c log X`. It does not hide a zero-free-region or RH input.
- A direct BDH theorem for the **rough, source-selected sum** `A_d` with a fixed-power saving, or a bilinear/multilinear theorem preserving cross-fiber signs, would contain information absent from `(5)` and is not obstructed here.
- A future bootstrap needs to show a strict fixed-power gain after all semigroup, exceptional-set, and shell weights are included. Merely improving the exponent of `log X` in `(2)` does not change the RH-facing budget.

## Consequence for the live frontier

The classical progression-variance route is no longer an unpriced possibility for the first square-defect shell. It reaches

\[
W_y(X)\ll_A X^2(\log X)^{-A}
\]

for every fixed `A`, but this remains one full power above the required diagonal scale. The live theorem surface should therefore be stated more narrowly: **obtain fixed-power cancellation before or across the smooth-semigroup recombination in `(6)`**, ideally by exploiting the common source lift `n+P=d^2m` rather than estimating the progression fibers independently.