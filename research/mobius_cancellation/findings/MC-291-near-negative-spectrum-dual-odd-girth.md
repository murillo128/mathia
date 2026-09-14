# MC-291 — Near-negative Walsh modes inherit dual odd girth and affine/sparse rigidity

**Status:** `EXACT-DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`

## Claim

Continue the weighted Boolean-shell setup of `MC-289` and `MC-290`. Let

\[
H\cong \mathbf F_2^r,
\qquad |H|=q,
\]

let `S subset H` carry positive integer multiplicities `n_s`, and write

\[
N=\sum_{s\in S}n_s,
\qquad
E_2=\sum_{s\in S}n_s^2,
\qquad
\eta=\frac{N^2}{qE_2}.
\tag{1}
\]

For `lambda in H^*`, set

\[
A_\lambda=\sum_{s\in S}n_s(-1)^{\lambda(s)},
\qquad
x_\lambda=\frac{A_\lambda}{N}.
\tag{2}
\]

The natural one-sided defect of a strongly negative character is

\[
d_\lambda
:=
\frac{1+x_\lambda}{2}
=
\frac1N\sum_{\substack{s\in S\\\lambda(s)=0}}n_s.
\tag{3}
\]

Thus `d_lambda` is exactly the weighted shell mass on which the character fails to take its preferred value `-1`.

For `0<tau<1/3`, define the near-negative spectrum

\[
\mathcal E_\tau
:=
\{\lambda\in H^*\setminus\{0\}:d_\lambda\le\tau\}
=
\{\lambda\ne0:x_\lambda\le-1+2\tau\}.
\tag{4}
\]

Then the following three conclusions hold.

### A. Near-negative modes have a forced odd-girth gap

If `lambda_1,...,lambda_j` are distinct elements of `E_tau`, `j` is odd, and

\[
\lambda_1+\cdots+\lambda_j=0,
\tag{5}
\]

then necessarily

\[
\boxed{
\sum_{i=1}^j d_{\lambda_i}\ge1.
}
\tag{6}
\]

Hence no odd zero-sum subset of `E_tau` can have cardinality `j` with `j tau<1`. In particular, for every odd `t>=3` satisfying

\[
t\tau<1,
\tag{7}
\]

`E_tau` has no odd circuit of size at most `t`.

This is a dual analogue of the primal odd-girth condition exploited in `MC-288`: sufficiently near-constant-negative Walsh modes cannot themselves satisfy short odd linear relations.

### B. Geelen rigidity therefore applies to the near-negative spectrum itself

Let

\[
R=\dim_{\mathbf F_2}\langle\mathcal E_\tau\rangle,
\qquad
J=|\mathcal E_\tau|.
\tag{8}
\]

For any odd `t>=3` with `t tau<1`, one has the dichotomy

\[
\boxed{
0\notin\operatorname{aff}(\mathcal E_\tau)
}
\tag{9a}
\]

or

\[
\boxed{
J\le(t+2)2^{R-t-1}.
}
\tag{9b}
\]

Equivalently, unless the near-negative spectrum is contained in an affine hyperplane of its own span,

\[
\boxed{
\frac{J}{2^R}\le\frac{t+2}{2^{t+1}}.
}
\tag{10}
\]

The affine alternative `(9a)` has a concrete primal interpretation. Because every linear functional on `span(E_tau) subset H^*` extends to `H^*`, there exists a point `s_0 in H` such that

\[
\lambda(s_0)=1
\qquad(\lambda\in\mathcal E_\tau).
\tag{11}
\]

Thus a large family of highly negative modes is forced either to be exponentially sparse in its generated dual space or to share one exactly compatible `-1` sign cell.

### C. Effective occupancy directly bounds the rank of near-extremal modes

Choose any linearly independent

\[
\lambda_1,\ldots,\lambda_R\in\mathcal E_\tau.
\tag{12}
\]

If `R tau<1`, the common preferred-sign cell

\[
C=\{s\in H:\lambda_i(s)=1\text{ for all }i\}
\tag{13}
\]

has weighted shell mass at least

\[
\sum_{s\in C}n_s\ge(1-R\tau)N.
\tag{14}
\]

Since the `lambda_i` are independent, `C` has exactly `q/2^R` points. Cauchy--Schwarz on that cell gives

\[
E_2
\ge
\frac{(1-R\tau)^2N^2}{q/2^R}.
\tag{15}
\]

Therefore

\[
\boxed{
\eta\le\frac{2^{-R}}{(1-R\tau)^2}
\qquad(R\tau<1).
}
\tag{16}
\]

For example, if `R tau<=1/2`, then

\[
\boxed{
R\le\log_2\frac4\eta.
}
\tag{17}
\]

So a collision-rich shell with a non-negligible participation ratio cannot support a high-rank family of almost constant-negative generated characters. This strengthens the interpretation of `MC-290`: exceptional modes are constrained not only individually by their bias, but collectively by linear compatibility and the shell's effective occupancy.

No estimate for `M(x)` follows. The result is a finite Fourier/affine interface that any future arithmetic exceptional-character theorem must satisfy.

## 1. Odd dependencies are incompatible with simultaneous negative bias

Let

\[
p(s):=\frac{n_s}{N}
\tag{18}
\]

be the shell probability measure. Suppose `(5)` holds with `j` odd. For every `s in H`,

\[
\sum_{i=1}^j\lambda_i(s)=0\pmod2.
\tag{19}
\]

Hence the number of indices for which `lambda_i(s)=1` is even. Because the total number `j` is odd, it is impossible that all `lambda_i(s)=1`; at least one of them must satisfy `lambda_i(s)=0`. Pointwise,

\[
1
\le
\sum_{i=1}^j 1_{\{\lambda_i(s)=0\}}.
\tag{20}
\]

Averaging `(20)` against `p` gives exactly

\[
1
\le
\sum_{i=1}^j
\sum_s p(s)1_{\{\lambda_i(s)=0\}}
=
\sum_{i=1}^j d_{\lambda_i},
\tag{21}
\]

which proves `(6)`. If every `lambda_i` belongs to `E_tau`, then the right side is at most `j tau`; therefore an odd dependency with `j tau<1` is impossible.

The threshold is sharp for this information alone. At `sum_i d_{lambda_i}=1`, the defect sets may partition the support, so a bare union argument cannot rule out the odd relation.

## 2. The dual large-bias set obeys the same finite-geometric rigidity as the primal support

Fix odd `t>=3` with `t tau<1`. By Section 1, the simple binary matroid represented by `E_tau` has no odd circuit of length at most `t`.

Apply exactly the Geelen theorem already audited in `MC-288`, with `k=t+2`. If `R>=t+1` and

\[
J>(t+2)2^{R-t-1},
\tag{22}
\]

then `E_tau` is a restriction of the rank-`R` affine geometry, which is `(9a)`.

The small-rank case causes no gap. If `R<=t` and `E_tau` were non-affine, binary-matroid theory would supply an odd circuit of size at most `R+1`; since its size is odd, it is at most `t`, contradicting Section 1. Thus the affine alternative already holds whenever the rank is below Geelen's range.

This proves `(9)` and `(10)` for all ranks.

To obtain `(11)`, let `V=span(E_tau) subset H^*`. Affineness means that some nonzero element of `V^*` takes the value `1` on every element of `E_tau`. The evaluation map `H -> V^*`, `s -> (lambda -> lambda(s))`, is surjective, so that functional is evaluation at some `s_0 in H`. Hence every near-negative mode has its preferred sign at the same exact cell `s_0`.

This does **not** say that the shell puts substantial mass at `s_0`. It is a compatibility statement about the exceptional spectrum, not a coverage theorem.

## 3. Independent near-negative modes force mass into one affine cell

Take independent `lambda_1,...,lambda_R` from `(12)`. Their individual defect sets are

\[
D_i=\{s:\lambda_i(s)=0\},
\qquad p(D_i)=d_{\lambda_i}\le\tau.
\tag{23}
\]

The complement of the common preferred cell `(13)` is `union_i D_i`. Therefore the weighted union bound gives

\[
p(C)
\ge
1-\sum_{i=1}^Rp(D_i)
\ge
1-R\tau,
\tag{24}
\]

which is `(14)`.

Independence makes the map

\[
s\longmapsto(\lambda_1(s),\ldots,\lambda_R(s))
\tag{25}
\]

surjective onto `F_2^R`, so every fiber has cardinality `q/2^R`. Applying Cauchy--Schwarz to the shell weights restricted to `C` proves `(15)` and hence `(16)`.

This is stronger than a raw support-count statement because `eta` records multiplicity concentration. A shell may occupy many distinct cells while still having tiny effective occupancy; `(16)` correctly weakens in that regime.

Conversely, whenever an independent family saturates the ideal affine model with all its weight uniformly distributed over `C`, one has `tau=0` and `eta=2^{-R}`, so the exponential rank scale in `(16)` is sharp.

## 4. Relation to the `MC-288`--`MC-290` frontier

`MC-288` applies odd-girth rigidity to the **primal occupied shell cells**. `MC-289` then turns the absence of short odd relations into exact odd Fourier moments, and `MC-290` shows that a small analytically uncontrolled character family must absorb the resulting negative odd moment and contain at least one nearly constant-negative mode.

The present result closes the next finite-structural loop: if arithmetic input ever produces **several** nearly constant-negative generated characters, they cannot behave as unrelated exceptions. Their preferred signs themselves impose a dual odd-girth condition; at high density they must become an affine family, and at high rank they force the primal shell measure into a correspondingly thin affine cell.

At a Geelen-scale primal participation ratio

\[
\eta\asymp t2^{-t},
\tag{26}
\]

any near-negative family with rank `R`, `R tau<=1/2`, satisfies from `(17)`

\[
R\le t-\log_2 t+O(1).
\tag{27}
\]

Thus a family of extremely negative modes cannot independently fill all `t` effective directions left by the primal odd-girth construction. The logarithmic codimension gap is only a finite-structural constraint, not an arithmetic cancellation theorem, but it is a sharper target than treating exceptional characters as an arbitrary list.

## 5. Prior art and novelty audit

Both mechanisms used here are established mathematical languages.

First, Chang's lemma and its descendants control the dimension of a large Fourier spectrum in terms of the entropy/density of the underlying measure or Boolean function. James R. Lee, *Covering the Large Spectrum and Generalized Riesz Products*, SIAM Journal on Discrete Mathematics 31 (2017), DOI `10.1137/15M1048604`, explicitly formulates Chang-type dimension bounds for large spectra of probability distributions on finite abelian groups. Sourav Chakraborty, Nikhil S. Mande, Rajat Mittal, Tulasimohan Molli, Manaswi Paraashar and Swagato Sanyal, *Tight Chang's-Lemma-Type Bounds for Boolean Functions*, FSTTCS 2021, DOI `10.4230/LIPIcs.FSTTCS.2021.10`, study Fourier-rank bounds in terms of the mass of a Boolean sign class. Their formulation is particularly close in spirit to `(16)`: large Fourier coefficients constrain Fourier rank when one sign class is small.

Second, Gaia Carenini and Leonardo Franchi, *A strengthening of Chang's lemma*, arXiv:`2605.07916` (2026), strengthen the classical large-spectrum conclusion by adding cosetwise correlation control. This recent result further confirms that localization of a large spectrum onto cosets is active prior art. The exact hypotheses and conclusions there differ from `(6)`--`(16)`, so it is used only as a novelty boundary, not as an input.

The affine/sparse implication `(9)` uses Jim Geelen's *A geometric version of the Andrásfai--Erdős--Sós Theorem*, Advances in Applied Mathematics 59 (2014), 1--7, DOI `10.1016/j.aam.2014.02.002`, already audited in `MC-288`.

Accordingly, **no novelty is claimed** for large-spectrum rank control, Chang's lemma, affine concentration of large Fourier modes, or Geelen odd-girth rigidity. The durable line-specific contribution is the exact one-sided composition relevant to the current shell: near-`-1` generated quadratic modes automatically inherit an odd-girth constraint `(6)`, which can be fed into the same Geelen machinery as the primal support, while the shell participation ratio yields the explicit elementary rank bound `(16)`.

## Boundaries and falsification tests

- The sign matters. A large absolute Fourier coefficient near `+1` does not enter `(4)` without changing the preferred parity; arbitrary sign choices around a dependency require the corresponding consistency condition.
- The relation `(6)` is for an **odd** zero-sum family. Even linear dependencies are compatible with all preferred signs being `-1` and are not excluded.
- `tau` controls weighted defect mass, not the number of exceptional shell cells. One heavy bad cell can exhaust the entire defect budget.
- The affine alternative `(9a)` does not imply that the common cell `s_0` is occupied, much less heavily occupied. Weighted concentration requires the independent-basis union bound `(14)`.
- The rank bound `(16)` is informative only when `R tau<1`; once the summed defect budget reaches one, independent preferred halfspaces can cover away their common intersection and the argument becomes vacuous.
- `eta` is the participation ratio from `MC-289`, not raw support density. Replacing it by `|S|/q` without controlling multiplicities can reverse the intended inference.
- The Geelen bound is a general finite-geometric theorem and is sharp in its category. Any stronger conclusion for actual generated quadratic characters requires arithmetic information beyond one-sided bias.
- No RH, GRH, zeta zero-free region, reciprocal-zeta continuation, or Möbius summatory estimate is used.

## Consequence for the research line

The exceptional-character escape isolated by `MC-290` has acquired internal structure. A small set of bad modes is no longer just a cardinality parameter `J`: once several modes become strongly negative, their linear relations and rank are constrained by the same parity geometry that constrained the primal shell. The next arithmetic question can therefore distinguish **how many** exceptional characters exist from **how many independent exceptional directions** they carry, and can target high-rank exceptional families without demanding uniform control of every generated character.