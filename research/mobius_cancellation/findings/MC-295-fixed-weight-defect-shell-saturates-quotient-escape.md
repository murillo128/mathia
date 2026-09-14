# MC-295 — Fixed-weight defect shells saturate the cheap-balance / high-cost quotient escape

**Status:** `EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the finite Fourier setup of `MC-291`–`MC-294`. Let

\[
H\cong\mathbf F_2^r,
\qquad
W\le H^*,
\qquad
\dim W=d,
\tag{1}
\]

and let

\[
\lambda_1,\ldots,\lambda_R\in H^*
\tag{2}
\]

be such that their span

\[
L:=\langle\lambda_1,\ldots,\lambda_R\rangle
\tag{3}
\]

has dimension `R` and

\[
L\cap W=\{0\}.
\tag{4}
\]

Thus the images of the `lambda_i` are linearly independent in `H^*/W`. Fix an integer

\[
1\le k<R/2
\tag{5}
\]

and, to keep the occupied set generating the whole `L`-coordinate factor, assume `R-k` is odd. Choose any complementary dual coordinates so that

\[
H^*=W\oplus L\oplus U.
\tag{6}
\]

Define a flat probability measure `p_k` on `H` by taking the `W`- and `U`-coordinates uniformly and independently, while restricting the `L`-coordinate vector

\[
(\lambda_1(s),\ldots,\lambda_R(s))\in\mathbf F_2^R
\tag{7}
\]

to the fixed-weight layer having exactly `k` zeros and `R-k` ones, uniformly over that layer.

Equivalently, take multiplicity `n_s=1` on

\[
S_k
:=
\left\{s\in H:
\#\{i:\lambda_i(s)=0\}=k
\right\}
\tag{8}
\]

and zero multiplicity elsewhere. Then `S_k` spans `H`, and the resulting shell observables satisfy all of the following exactly.

First, every nonzero cheap direction is **perfectly balanced**:

\[
\boxed{x_w=0\qquad(w\in W\setminus\{0\}).}
\tag{9}
\]

Indeed the full pushforward of `p_k` to the sign cube dual to `W` is uniform, so `(9)` is stronger than the Page balance available in `MC-293`--`MC-294`.

Second, each selected quotient direction is strongly negative with identical defect

\[
\boxed{
 d_{\lambda_i}=\frac{k}{R},
 \qquad
 x_{\lambda_i}=-1+\frac{2k}{R}.
}
\tag{10}
\]

Third, the participation ratio is

\[
\boxed{
\eta
=2^{-R}\binom{R}{k}.
}
\tag{11}
\]

Fourth, the complete Fourier profile on the selected span is the classical Krawtchouk profile. If `I subset {1,...,R}` has `j=|I|`, then

\[
\boxed{
 x_{\sum_{i\in I}\lambda_i}
 =(-1)^j
 \frac{K_k(j;R)}{\binom{R}{k}},
}
\tag{12}
\]

where

\[
K_k(j;R)
=
\sum_{\ell=0}^{k}
(-1)^\ell
\binom j\ell
\binom{R-j}{k-\ell}.
\tag{13}
\]

Finally, because of `(4)`, no nonempty combination of the selected near-negative modes lands in `W`:

\[
\boxed{
\sum_{i\in I}\lambda_i\in W
\quad\Longrightarrow\quad
I=\varnothing.
}
\tag{14}
\]

Thus the quotient-girth conclusion of `MC-294` is not merely consistent with a large high-cost quotient: it has an explicit finite extremal model in which the cheap sector is *more balanced than Page theory guarantees*, while all selected near-negative modes occupy genuinely independent quotient directions.

The live boundary case is especially sharp. Take

\[
k=1,
\qquad R\to\infty\text{ through even integers}.
\tag{15}
\]

Then

\[
\boxed{
\tau=\frac1R,
\qquad
\eta=R2^{-R},
\qquad
R\tau=1.
}
\tag{16}
\]

Every occupied point has exactly one defect, so the `R` defect sets partition the shell and the common preferred-sign cell is empty. This realizes exactly the threshold at which the common-cell argument of `MC-291` stops. At the same time the entropy budget of `MC-292` is asymptotically saturated up to an additive constant:

\[
\log_2\frac1\eta
-
R\bigl(1-h_2(1/R)\bigr)
=R h_2(1/R)-\log_2R
\longrightarrow\log_2 e.
\tag{17}
\]

If in addition `U=0`, so that `H^*=W\oplus L`, then

\[
\boxed{
r-d=R.}
\tag{18}
\]

Hence the high-source-complexity quotient escape left by `MC-294` can consume exactly one quotient bit per independent near-negative mode while matching the Geelen-scale participation law `eta=R2^{-R}` and the reciprocal defect scale `tau=1/R`.

This is a **finite-model obstruction**, not an arithmetic construction. It does not assert that the actual Legendre shell realizes `p_k`, nor does it assign genuine source costs to the directions in `L`. Its consequence is instead a no-go boundary: the finite Fourier, participation-ratio, defect, Page-balance-on-`W`, and quotient-girth information accumulated through `MC-291`--`MC-294` is jointly consistent at the live scale. Any theorem that closes the remaining escape must therefore use additional arithmetic information restricting the actual high-source-cost quotient or the actual shell occupancy beyond these observables.

No estimate for `M(x)` follows.

## 1. Construction and generated rank

Choose bases

\[
w_1,\ldots,w_d
\quad\text{of }W,
\qquad
\lambda_1,\ldots,\lambda_R
\quad\text{of }L,
\tag{19}
\]

and extend them by a basis of `U` to a basis of `H^*`. The associated evaluation map identifies `H` with the full binary coordinate cube dual to this basis.

In the `L` block, `S_k` projects onto the layer of vectors with Hamming weight `R-k`. A fixed-weight layer of odd weight spans `F_2^R`: differences of two layer vectors give the even-weight subspace, while any one odd-weight layer vector lies outside that subspace. The parity assumption that `R-k` is odd therefore makes the `L` projection span all of `F_2^R`.

The `W` and `U` coordinates are unrestricted in `(8)`, so their coordinate directions are also in the span. Consequently

\[
\langle S_k\rangle=H.
\tag{20}
\]

Thus the construction fits the generated-shell convention rather than hiding an unused ambient direction.

The support size is

\[
|S_k|
=2^{r-R}\binom Rk.
\tag{21}
\]

With flat multiplicities `n_s=1`, one has

\[
N=E_2=|S_k|.
\tag{22}
\]

Using the participation definition of `MC-291`--`MC-292`,

\[
\eta
=\frac{N^2}{2^rE_2}
=\frac{|S_k|}{2^r}
=2^{-R}\binom Rk,
\tag{23}
\]

which proves `(11)`.

## 2. The cheap block is exactly uniform

The defining condition `(8)` depends only on the `L` coordinates. For every allowed `L` vector, all `2^d` sign patterns in the `W` block occur with the same number of `U` completions. Therefore the pushforward of `p_k` under

\[
s\longmapsto(w_1(s),\ldots,w_d(s))
\tag{24}
\]

is exactly the uniform measure on `F_2^d`.

Every nonzero `w in W` is a nontrivial character of this uniform cube, hence character orthogonality gives

\[
x_w
=\mathbb E_{p_k}(-1)^{w(s)}
=0.
\tag{25}
\]

This is stronger than merely requiring `|x_w|<=epsilon_y` for Page-cheap nonexceptional modes. There is no exceptional cheap mode in this model at all.

The point is structural: perfect low-complexity balance does not force the high-complexity quotient to lose near-negative directions.

## 3. Fixed-weight defects give the exact Krawtchouk spectrum

Let

\[
Z(s)=\{i:\lambda_i(s)=0\}.
\tag{26}
\]

Under `p_k`, `Z` is uniform over the `k`-subsets of `{1,...,R}`. Therefore for each coordinate

\[
d_{\lambda_i}
=\Pr[i\in Z]
=\frac{k}{R},
\tag{27}
\]

and since `x_lambda=2d_lambda-1`, equation `(10)` follows.

For a subset `I` of size `j`,

\[
(-1)^{\sum_{i\in I}\lambda_i(s)}
=(-1)^{j-|I\cap Z(s)|}
=(-1)^j(-1)^{|I\cap Z(s)|}.
\tag{28}
\]

Averaging over uniform `k`-subsets gives

\[
\mathbb E(-1)^{|I\cap Z|}
=
\frac1{\binom Rk}
\sum_{\ell=0}^k
(-1)^\ell
\binom j\ell
\binom{R-j}{k-\ell},
\tag{29}
\]

which is `(12)`--`(13)`. This is precisely the classical Krawtchouk Fourier multiplier of a Hamming sphere.

Equation `(4)` now supplies the quotient statement. If a nonempty subset `I` satisfied

\[
\sum_{i\in I}\lambda_i\in W,
\tag{30}
\]

then the left side belongs to `L cap W={0}`. Independence of the `lambda_i` would then force `I` to be empty, a contradiction. This proves `(14)`.

Thus no Page-exceptional deletion is needed and the quotient configuration has no dependency of *any* length, not merely no dependency below the `MC-294` threshold.

## 4. The one-defect layer hits the live finite-structural frontier

Set `k=1` and take even `R`, so the occupied `L` vectors have odd weight `R-1` and generate the full `L` block.

Each point has one and only one zero among the selected evaluations. Hence the defect sets

\[
D_i=\{s:\lambda_i(s)=0\}
\tag{31}
\]

are a partition of `S_1`, with

\[
p(D_i)=1/R.
\tag{32}
\]

There is no point of `S_1` for which every `lambda_i(s)=1`. Therefore the union estimate in `MC-291` is sharp at

\[
\sum_i d_{\lambda_i}=R(1/R)=1.
\tag{33}
\]

At this same point, `(23)` gives

\[
\eta=R2^{-R},
\tag{34}
\]

which is exactly the participation scale isolated in `MC-292`. The entropy inequality there reads

\[
R\bigl(1-h_2(1/R)\bigr)
\le R-\log_2R.
\tag{35}
\]

The gap equals the left side of `(17)`. Since

\[
R h_2(1/R)
=
\log_2R-(R-1)\log_2(1-1/R),
\tag{36}
\]

one obtains

\[
R h_2(1/R)-\log_2R
\to\log_2e.
\tag{37}
\]

So the threshold-free entropy refinement does not create a growing spare margin in the live regime: this explicit flat shell misses equality only by `O(1)` bits.

Finally, if `H^*=W\oplus L`, the quotient dimension is exactly `R`. All `R` selected modes remain independent after quotienting, while every nonzero mode in `W` is perfectly balanced. Thus the final escape named in `MC-294` is not an artifact of loose inequalities. It is a realizable extremal configuration in the abstract finite model.

## 5. Prior art and novelty boundary

No novelty is claimed for the finite harmonic analysis. Uniform fixed-weight layers of the Boolean cube are the Hamming association scheme, and their Walsh-Fourier multipliers are Krawtchouk polynomials. This exact language was already audited for the Mathia shell in `MC-267`. Yury Polyanskiy, *Hypercontractivity of Spherical Averages in Hamming Space*, SIAM Journal on Discrete Mathematics **33** (2019), 731--754, DOI `10.1137/15M1046575`, studies the Hamming-sphere averaging operator explicitly through its Krawtchouk/Fourier eigenvalues. The affine/subspace side of Boolean Fourier structure is classical as well; B. L. Rothschild and J. H. van Lint, *Characterizing finite subspaces*, Journal of Combinatorial Theory, Series A **16** (1974), 97--110, DOI `10.1016/0097-3165(74)90075-2`, is an early structural reference.

A targeted literature search on 14 September 2026 found the fixed-weight/Krawtchouk and affine-spectrum mechanisms as standard prior art, not a new theorem. It did not identify an arithmetic result asserting that an actual Legendre shell can or cannot realize the combined cheap-uniform/high-cost fixed-weight model above. Accordingly the durable content is only the **frontier falsification**: the generic finite constraints already derived in this line admit a simultaneous extremizer at the live parameter scale, so another purely finite Fourier/entropy/coding refinement cannot close the arithmetic escape unless it uses an additional hypothesis violated by this model.

## Boundaries and falsification tests

- **This is not an arithmetic realization.** The construction is an abstract shell measure on `F_2^r`; it neither produces actual shell primes nor assigns real conductors/source costs to `L`.
- **`W` is only the certified cheap sector.** Equation `(9)` shows compatibility with a stronger form of Page balance on `W`; it does not say every character outside `W` is arithmetically expensive.
- **The parity condition is bookkeeping, not substance.** Requiring `R-k` odd ensures the occupied fixed-weight layer generates the full selected coordinate block. Other parity choices can be handled after passing to the generated span, but then the displayed rank parameters change by one.
- **Flat multiplicity is deliberate.** It makes `eta` equal support density exactly and therefore gives a clean extremizer. No claim is made that actual prime-shell multiplicities are flat.
- **The Krawtchouk profile contains additional higher-mode data.** A future arithmetic theorem is free to exploit that profile or show that the actual shell cannot approximate it. The no-go applies only to arguments whose hypotheses are exhausted by the already-recorded generic observables.
- **Page uniqueness is not contradicted.** The cheap sector has no large coefficient at all. All near-negative modes live in quotient directions outside `W`.
- **No RH-scale input appears.** The construction is finite combinatorics; no zeta continuation, zero-free region in the critical strip, GRH, or Möbius summatory estimate is assumed.

## Consequence for the research line

The finite-structural route has reached a real boundary. At the reciprocal-defect scale `tau=1/R` and participation scale `eta=R2^{-R}`, a shell can simultaneously have perfect uniformity on every certified Page-cheap direction, `R` independent almost-constant-negative modes, no quotient relations of any length, and only the minimal `R` high-complexity quotient dimensions needed to host them.

Therefore the next useful theorem cannot be another consequence of generic Walsh orthogonality, collision entropy, union bounds, or binary sphere packing applied to the same data. It must constrain something specifically arithmetic about the actual Legendre shell: the dimension or realization of the high-source-cost quotient, the source/conductor geometry of its Krawtchouk profile, or another invariant that this fixed-weight extremizer fails to satisfy.