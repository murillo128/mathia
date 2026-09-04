# AF-116 — Tolerance covering complexity separates fixed scale count from mean bit cost

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `ONE-SHOT-QUANTIZATION`, `MULTISCALE-BUDGET-SEPARATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-115 classified whether a probability resource profile can be retained by a **fixed finite number** of moving centers. Failure at every fixed `k` was correctly identified as failure of every fixed finite scale list, but that statement leaves a second complexity question open:

> Does unbounded scale cardinality force an unbounded information cost for the repairing mark?

No. Cardinality, tolerance-dependent covering complexity, worst-case description length, and average description length are genuinely different fidelity budgets.

Let `(X,d)` be a metric space and let `(\mu_i)` be a net of Borel probability measures on `X`. For `R\ge0` and `0<\varepsilon<1`, define the **partial covering number**

\[
N_i(R,\varepsilon)
:=
\min\left\{
|C|:
C\subset X\text{ finite},\quad
\mu_i\!\left(\bigcup_{a\in C}\overline B(a,R)\right)>1-\varepsilon
\right\},
\tag{1}
\]

with value `+\infty` when no finite `C` exists.

### 1. `N_i(R,\varepsilon)` is exactly the one-shot fixed-alphabet repair cost

A deterministic mark with alphabet `{1,\ldots,M}` and decoder points `a_1,\ldots,a_M\in X` reconstructs a sample `x` to `a_{m(x)}`. Its excess-radius error is

\[
\mu_i\{x:d(x,a_{m(x)})>R\}.
\tag{2}
\]

There exists such an encoder/decoder with error strictly below `\varepsilon` if and only if

\[
\boxed{N_i(R,\varepsilon)\le M.}
\tag{3}
\]

Hence the least worst-case fixed-length binary mark for this one-shot repair uses

\[
\boxed{
\left\lceil\log_2 N_i(R,\varepsilon)\right\rceil
}
\tag{4}
\]

bits whenever `N_i(R,\varepsilon)<\infty`.

This is an operational identity, not an analogy: a successful decoder supplies a radius-`R` ball cover of every correctly reconstructed point, and a partial ball cover supplies an encoder by assigning each covered point to one covering center.

### 2. AF-115's fixed-`k` gate is a uniform-cardinality condition over all error tolerances

Recall AF-115's optimal uncovered mass

\[
c_{i,k}(R)
=
\inf_{a_1,\ldots,a_k}
\mu_i\!\left(
X\setminus\bigcup_{r=1}^k\overline B(a_r,R)
\right).
\tag{5}
\]

Its `k`-center tightness condition is equivalent to

\[
\boxed{
\forall\varepsilon>0\ \exists R<\infty\ \exists i_0:
\quad
N_i(R,\varepsilon)\le k
\quad(i\ge i_0).
}
\tag{6}
\]

Indeed, if AF-115 gives `c_{i,k}(R)\le\varepsilon/2`, the defining infimum can be approximated by `k` centers with uncovered mass `<\varepsilon`; conversely a cover with uncovered mass `<\varepsilon` gives `c_{i,k}(R)<\varepsilon`.

Define the asymptotic tolerance complexity

\[
K(\varepsilon)
:=
\inf\left\{
k\ge1:
\exists R<\infty\ \exists i_0\ 
N_i(R,\varepsilon)\le k\text{ for all }i\ge i_0
\right\}.
\tag{7}
\]

Then AF-115's fixed finite multiscale repairability is exactly boundedness of `K(\varepsilon)` by one common finite `k` for **every** `\varepsilon>0`.

A strictly weaker regime is

\[
\boxed{
K(\varepsilon)<\infty
\quad\text{for every fixed }\varepsilon>0,
}
\tag{8}
\]

while

\[
K(\varepsilon)\longrightarrow\infty
\qquad(\varepsilon\downarrow0).
\tag{9}
\]

Thus “no fixed finite scale list is faithful” does not imply that every positive error tolerance requires unboundedly many scales.

### 3. An exact spectral family has unbounded all-error scale count but logarithmic tolerance complexity

Consider positive finite-rank trace-class operators. For each integer `n\ge2`, put spectral levels

\[
\lambda_{n,\ell}=2^{-n\ell},
\qquad 1\le\ell\le n,
\tag{10}
\]

with multiplicities

\[
m_{n,\ell}=2^{(n-1)\ell}.
\tag{11}
\]

The trace mass carried by level `\ell` is exactly

\[
m_{n,\ell}\lambda_{n,\ell}=2^{-\ell},
\tag{12}
\]

and therefore

\[
M_n:=\operatorname{Tr}(A_n)
=\sum_{\ell=1}^n2^{-\ell}
=1-2^{-n}.
\tag{13}
\]

The normalized logarithmic trace-mass profile is

\[
\rho_n
=
\sum_{\ell=1}^n
w_{n,\ell}\,
\delta_{-n\ell\log2},
\qquad
w_{n,\ell}
=
\frac{2^{-\ell}}{1-2^{-n}}.
\tag{14}
\]

Adjacent support points are separated by `n\log2`. Fix `R<\infty` and `k`. Once

\[
n\log2>2R,
\tag{15}
\]

one radius-`R` ball can contain at most one support point. The optimal `k` centers therefore cover the `k` heaviest levels. For `n>k`,

\[
\boxed{
c_{n,k}(R)
=
\frac{2^{-k}-2^{-n}}{1-2^{-n}}
\longrightarrow2^{-k}.}
\tag{16}
\]

Consequently every fixed `k` fails AF-115: choose any `\varepsilon<2^{-k}` and no fixed radius can make the uncovered mass eventually smaller than `\varepsilon`.

However, for each fixed tolerance the required number of scales is finite. In fact (16) gives the exact asymptotic complexity profile

\[
\boxed{
K(\varepsilon)
=
\left\lceil\log_2\frac1\varepsilon\right\rceil,
\qquad 0<\varepsilon<1.
}
\tag{17}
\]

At tolerance `\varepsilon`, keeping only the first `K(\varepsilon)` logarithmic levels loses less than `\varepsilon` trace mass for all sufficiently large `n`. Thus this family defeats every **uniform finite-cardinality** lift while remaining finitely repairable at every fixed positive tolerance.

### 4. Exact scale labeling can still have bounded mean description length

The separation is stronger than (17). At stage `n`, exact identification of all `n` spectral levels requires `n` distinct labels. A fixed-length exact mark therefore needs

\[
\left\lceil\log_2 n\right\rceil
\tag{18}
\]

worst-case bits, which diverges.

Now label level `\ell` by the prefix-free unary word

\[
1^{\ell-1}0,
\tag{19}
\]

whose length is `\ell`. Under the trace-mass law (14), its expected length is

\[
\begin{aligned}
L_n
&=
\sum_{\ell=1}^n
\ell\,w_{n,\ell}\\
&=
\frac{\sum_{\ell=1}^n \ell 2^{-\ell}}{1-2^{-n}}\\
&=
2-\frac{n}{2^n-1}
<2.
\end{aligned}
\tag{20}
\]

Therefore

\[
\boxed{
\text{exact scale-label cardinality }n\to\infty,
\qquad
\text{worst-case fixed length }\to\infty,
\qquad
\sup_n L_n<2\text{ bits}.}
\tag{21}
\]

The limiting level law is `w_\ell=2^{-\ell}`, whose Shannon entropy is exactly

\[
H(w)
=
\sum_{\ell\ge1}2^{-\ell}\ell
=2\text{ bits}.
\tag{22}
\]

So the phenomenon is not a coding trick: the rare distant scales carry enough rapidly decaying mass that a countable scale mark has finite average information even though no finite alphabet can carry every scale exactly.

## Derivation

For (3), suppose an encoder `m` and reproduction points `(a_r)` achieve error `<\varepsilon`. Every correctly reconstructed `x` lies in `\overline B(a_{m(x)},R)`, so

\[
\mu_i\!\left(\bigcup_{r=1}^M\overline B(a_r,R)\right)>1-\varepsilon,
\tag{23}
\]

and `N_i(R,\varepsilon)\le M`.

Conversely, let `C={a_1,\ldots,a_M}` satisfy the partial-cover condition. Assign every covered point to one ball containing it and assign uncovered points arbitrarily. The resulting deterministic decoder has excess-radius error at most the uncovered mass, hence `<\varepsilon`. This proves (3), and (4) is the elementary cardinality cost of a fixed-length binary alphabet.

For the spectral family, (12) follows directly from

\[
2^{(n-1)\ell}2^{-n\ell}=2^{-\ell}.
\tag{24}
\]

When (15) holds, the balls are unable to merge two support levels. Since the weights decrease strictly in `\ell`, the maximum mass captured by `k` balls is the sum of the first `k` weights. The residual geometric tail gives (16).

If `2^{-k}\le\varepsilon`, then the finite-`n` residual in (16) is actually `<2^{-k}\le\varepsilon`; hence `k` centers work eventually. If `2^{-k}>\varepsilon`, (16) shows that `k` centers fail eventually for every fixed radius. This proves (17).

Finally,

\[
\sum_{\ell=1}^n\ell2^{-\ell}
=2-(n+2)2^{-n},
\tag{25}
\]

and division by `1-2^{-n}` yields (20).

## Exact controls and failure modes

### Average information and worst-case marking are different categories

Equation (21) does not contradict AF-115. AF-115 asks whether one **fixed finite set of centers** can retain arbitrarily close to all mass. The unary repair permits an unbounded countable label set and charges labels by their probability-weighted length. Rare scales may therefore receive arbitrarily long descriptions at small average cost.

A mechanism requiring bounded worst-case side information cannot use this escape. A mechanism whose natural resource is an average coding/information budget may be able to.

### The covering centers remain unrestricted

As in AF-114--AF-115, `N_i(R,\varepsilon)` allows centers to be chosen after inspecting the whole profile. It measures geometric/information-theoretic repairability, not canonicity. A Mathia application must separately prove that the scale labels and decoding centers arise intrinsically from the source construction rather than being fitted to the observed spectrum.

### Finite mean cost does not recover lost provenance

The code in (19) identifies only the logarithmic spectral level. It does not recover eigenvectors, multiplicity provenance, phase, orientation, arithmetic labels, or any discriminator erased within one level. This is a complexity statement about the specific multiscale defect, not a complete reconstruction theorem.

### The resource law matters as much as the support geometry

Replacing the geometric weights `2^{-\ell}` by a heavier tail can leave the same infinitely separated support while making expected label length diverge. Conversely, adding infinitely many vanishing satellites need not materially increase either `K(\varepsilon)` at fixed `\varepsilon` or average information cost.

Therefore support cardinality, number of visible scales, and condition number are not valid substitutes for a resource-weighted complexity audit.

### Radius and rate must be declared together

The quantity `N_i(R,\varepsilon)` is a one-shot rate-distortion object: increasing `R` permits coarser geometric reconstruction, while increasing `\varepsilon` permits discarding more resource mass. Quoting only a number of retained labels without the allowed radius and uncovered mass does not specify a fidelity budget.

### Arithmetic fidelity remains a separate gate

Nothing here identifies a rational-prime discriminator. A prime-derived operator and a matched Beurling/generalized-prime control could have identical tolerance-complexity profiles and identical scale-label entropy. An arithmetic application must compare the same source-admissible mark and budget against matched controls before the retained multiscale structure counts as prime-specific evidence.

## Prior art and novelty assessment

The operational mathematics is classical. **No theorem-level novelty is claimed.**

- Claude E. Shannon, **“A Mathematical Theory of Communication,”** *Bell System Technical Journal* 27, 379–423 and 623–656 (1948), DOI `10.1002/j.1538-7305.1948.tb01338.x` and `10.1002/j.1538-7305.1948.tb00917.x`. Role: foundational entropy and variable-length source-coding framework; establishes the classical distinction between source alphabet size and probability-weighted description cost.
- Claude E. Shannon, **“Coding Theorems for a Discrete Source With a Fidelity Criterion,”** *IRE National Convention Record* 7(4), 142–163 (1959). Role: foundational rate-distortion formulation, placing fidelity-constrained source representation under an explicit information budget.
- Robert M. Gray and David L. Neuhoff, **“Quantization,”** *IEEE Transactions on Information Theory* 44(6), 2325–2383 (1998), DOI `10.1109/18.720541`. Role: authoritative survey of fixed-rate, variable-rate/entropy-constrained quantization and the rate-distortion viewpoint; the partial-cover interpretation of a finite reproduction alphabet belongs to this classical quantization landscape.

AF-116 derives the exact partial-cover identity, its relation to AF-115, and the dyadic multiscale trace-class control directly. The new value for Arithmetic Fidelity is not a new coding theorem. It is a **budget-separation audit**: failure of every fixed finite scale list says only that the required repair cardinality is unbounded as the tolerated lost mass tends to zero. It does not establish divergence of tolerance-wise complexity or average information cost.

## Consequences for Arithmetic Fidelity

AF-113--AF-115 progressively removed three ambiguities: a canonical scale can follow negligible mass; failure of one chosen scale need not mean failure of every scalar scale; and genuine one-scale failure can be classified by a finite hierarchy of scale counts. AF-116 removes the next ambiguity in that hierarchy.

Before declaring a compression irreparable because every fixed finite `k` fails, the intended lift budget must be named. At minimum, distinguish:

- a uniformly bounded finite mark alphabet;
- a finite alphabet whose size may grow as the tolerated lost mass `\varepsilon` shrinks;
- bounded worst-case description length;
- bounded expected description length or entropy;
- an intrinsically admissible/canonical marking rule.

These budgets are not interchangeable. The dyadic spectral family has infinite asymptotic exact scale cardinality and fails every fixed-`k` AF-115 gate, but has `K(\varepsilon)=\lceil\log_2(1/\varepsilon)\rceil` and an exact countable scale label with mean cost below two bits.

For later RH-facing applications, an argument that a trace/determinant/spectral compression “needs infinitely many scales” is therefore incomplete unless it also proves that the **source-admissible resource distribution** makes the relevant coding/marking budget diverge. Otherwise an unbounded set of rare scale corrections may still be cheap in the mathematical category actually available to the construction.