# MC-205 — Cyclic mixed-shift kernels split exactly into a principal carrier and relational spectrum

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-204` shows that the full permutation quotient of a ternary source class retains only its signed sum and support count, so a genuine escape must preserve a relation between labelled sites. The first natural such class is a translation/shift-sensitive bilinear statistic coupling the Möbius sign at one site to square-free support at another.

That class does preserve genuinely new relational data, but its principal-mode bookkeeping is rigid.

Work at a complete logarithmic-primorial block

\[
X=Nq,
\qquad
q=q_y=\prod_{p\le y}p,
\qquad
y=c\log X,
\qquad 0<c<\frac12.
\tag{1}
\]

For each reduced residue class `a mod q`, enumerate the `N` source sites by

\[
x_{a,j}:=\mu(a+jq)\in\{-1,0,1\},
\qquad
z_{a,j}:=x_{a,j}^2,
\qquad 0\le j<N,
\tag{2}
\]

and write

\[
A_a=\sum_jx_{a,j},
\qquad
B_a=\sum_jz_{a,j},
\qquad
S=\sum_aA_a,
\qquad
Q=\sum_aB_a,
\tag{3}
\]

with `phi=phi(q)` and the class-level covariance from `MC-200`--`MC-201`

\[
C_{1,2}
:=
\sum_a
\left(A_a-\frac S\phi\right)
\left(B_a-\frac Q\phi\right).
\tag{4}
\]

Inside each class center the labelled fields themselves:

\[
u_{a,j}=x_{a,j}-\frac{A_a}{N},
\qquad
v_{a,j}=z_{a,j}-\frac{B_a}{N}.
\tag{5}
\]

Let `w_0` be a diagonal weight and let `w_h`, `h in Z/NZ`, `h!=0`, be arbitrary complex cyclic-shift weights. Put

\[
R_w:=\sum_{h\ne0}w_h
\tag{6}
\]

and define the mixed statistic

\[
T_w
:=
\sum_a\sum_{j=0}^{N-1}
\left(
 w_0x_{a,j}z_{a,j}
 +\sum_{h\ne0}w_hx_{a,j}z_{a,j+h}
\right),
\tag{7}
\]

where the second site index is taken modulo `N`. Define the genuinely relational centered remainder

\[
K_w
:=
\sum_a\sum_j\sum_{h\ne0}
 w_hu_{a,j}v_{a,j+h}.
\tag{8}
\]

Then the exact decomposition is

\[
\boxed{
T_w
=
\alpha_w S
+\frac{R_w}{N}C_{1,2}
+K_w,
\qquad
\alpha_w
:=
w_0+R_w\frac{Q}{\phi N}.
}
\tag{9}
\]

Hence the entire cyclic bilinear shift family has an exact principal/relational dichotomy:

- if `alpha_w=0`, the direct rough-Möbius carrier cancels and the statistic reduces to the already controlled class-support covariance plus the centred relational spectrum;
- if `alpha_w!=0`, there is the exact decoder

\[
\boxed{
S
=
\frac{T_w-(R_w/N)C_{1,2}-K_w}{\alpha_w}.
}
\tag{10}
\]

Thus choosing a shift kernel does **not** by itself make the principal coordinate leak out of controlled transverse data. What the smaller cyclic symmetry genuinely buys is the new term `K_w`: labelled sign/support correlations survive there. Any improvement over `MC-204` must therefore come from a new arithmetic theorem about that relational term, or about the numerator in `(10)` jointly, rather than from the representation change alone.

The decomposition has an equally sharp Fourier form. With

\[
\widehat u_a(k)
=\frac1N\sum_{j=0}^{N-1}u_{a,j}e^{-2\pi i k j/N},
\qquad
\widehat v_a(k)
=\frac1N\sum_{j=0}^{N-1}v_{a,j}e^{-2\pi i k j/N},
\tag{11}
\]

and

\[
W(k)=\sum_{h\ne0}w_he^{-2\pi i k h/N},
\tag{12}
\]

one has

\[
\boxed{
K_w
=
N\sum_a\sum_{k\ne0}
W(k)\widehat u_a(k)\widehat v_a(-k).
}
\tag{13}
\]

The direct class means sit in the zero site-frequency through `R_w=W(0)`; the surviving nonzero site frequencies are exactly the relational information that full permutation symmetry erased in `MC-204`.

No bound for `S`, `M(X)`, a shifted Möbius correlation, or the zeta zero set is claimed.

## 1. Exact decomposition of a cyclic shift kernel

For one class, abbreviate `x_j=x_{a,j}`, `z_j=z_{a,j}`, `A=A_a`, `B=B_a`, `u_j=u_{a,j}`, and `v_j=v_{a,j}`. Since `x_j` is ternary,

\[
x_jz_j=x_j^3=x_j,
\tag{14}
\]

so the diagonal part of `(7)` is exactly `w_0A`.

For every nonzero cyclic shift `h`, substitute

\[
x_j=\frac AN+u_j,
\qquad
z_{j+h}=\frac BN+v_{j+h}.
\]

Because cyclic translation preserves a zero sum,

\[
\sum_ju_j=0,
\qquad
\sum_jv_{j+h}=0,
\]

and therefore

\[
\sum_jx_jz_{j+h}
=
\frac{AB}{N}
+\sum_ju_jv_{j+h}.
\tag{15}
\]

Weighting `(15)` and summing over `h!=0` gives

\[
T_w
=w_0S
+\frac{R_w}{N}\sum_aA_aB_a
+K_w.
\tag{16}
\]

The class-level centering identity used already in `MC-200` is

\[
\sum_aA_aB_a
=
\frac{SQ}{\phi}+C_{1,2}.
\tag{17}
\]

Substituting `(17)` into `(16)` proves `(9)` and hence `(10)`.

The point is not that `K_w` is harmless. In general it is not. Equation `(9)` identifies it as the **only new labelled-site channel** added by this bilinear cyclic representation once the old class-level carrier is separated exactly.

## 2. Fourier diagonalization isolates the relational channel

Insert the inverse discrete Fourier expansions of `u_a` and `v_a` into `(8)`. Summing over `j` imposes opposite frequencies, while the shift sum contributes the multiplier `W(k)`. This gives

\[
K_w
=N\sum_a\sum_k
W(k)\widehat u_a(k)\widehat v_a(-k).
\tag{18}
\]

The `k=0` term vanishes because both centred fields have zero mean, proving `(13)`.

This is standard finite cyclic harmonic analysis. Circulant/convolution operators are diagonalized by the discrete Fourier transform; see, for example, R. M. Gray, *Toeplitz and Circulant Matrices: A Review*, Foundations and Trends in Communications and Information Theory 2 (2006), 155--239, DOI `10.1561/0100000006`. No novelty is claimed for circulant diagonalization or `(18)` as an abstract Fourier identity.

What matters for the present line is the placement of the arithmetic target. The coefficient `alpha_w` depends only on the diagonal weight, the total off-diagonal weight, and the unsigned support density `Q/(phi N)`. All finer shift geometry enters through `K_w`.

## 3. Three calibrations show exactly what survives

### Uniform all-shift weighting returns to the symmetric quotient

Take

\[
w_0=0,
\qquad
w_h=1\quad(h\ne0).
\tag{19}
\]

Then `(7)` sums every ordered distinct pair in every source class, so

\[
T_w=E_{1,2}
\tag{20}
\]

from `MC-200`. Here `R_w=N-1` and

\[
W(k)=-1\qquad(k\ne0).
\tag{21}
\]

The apparently relational spectrum therefore recombines uniformly. Using `x_j^3=x_j`,

\[
K_w
=-\sum_a\sum_ju_{a,j}v_{a,j}
=-S+\frac1N\sum_aA_aB_a.
\tag{22}
\]

Substitution into `(9)` gives exactly

\[
E_{1,2}
=
\left(\frac Q\phi-1\right)S+C_{1,2}.
\tag{23}
\]

Thus `MC-200` is recovered as a calibration case. **Uniformly summing all labelled shifts restores the full pair symmetry and collapses the new relational coordinates back to `(A_a,B_a)`.** Merely introducing shift labels and then averaging them uniformly does not escape `MC-204`.

### A genuinely nonuniform shift retains new information

For a single nonzero cyclic shift `h`, take `w_h=1` and every other weight zero. Then

\[
T_h
=
\frac{Q}{\phi N}S
+\frac1N C_{1,2}
+K_h,
\tag{24}
\]

where

\[
K_h
=\sum_a\sum_ju_{a,j}v_{a,j+h}.
\tag{25}
\]

Unlike `(19)`, this statistic is not determined by `(A_a,B_a)`: two class words with the same symbol counts can have different lag-`h` correlations. This is a real representation escape, not another symmetric moment.

But `(24)` also makes the burden exact. A useful theorem must control `K_h`, `T_h`, or their combination at a power scale strong enough to improve the decoder. The fact that a fixed-shift correlation is relational does not itself supply such a theorem. The logarithmically averaged fixed-shift correlation machinery recorded in `MC-S28` remains far weaker than the required ordinary fixed-power estimate.

### Mean-zero shift filters isolate relation but remove the direct carrier

If `w_0=0` and

\[
R_w=\sum_{h\ne0}w_h=0,
\tag{26}
\]

then `(9)` becomes simply

\[
\boxed{T_w=K_w.}
\tag{27}
\]

Such a filter can be excellent for detecting positional structure because its multiplier suppresses the zero site-frequency. But the same operation removes the explicit class-mean carrier. Any later recovery of `S` from `(27)` would need a genuinely Möbius-specific relation between the centred relational spectrum and the principal sum; it is not supplied by shift invariance or Fourier analysis.

This is an architectural statement, not an impossibility theorem for actual Möbius. The ternary relation `z=x^2` can impose additional identities among centred modes, and arithmetic multiplicativity can impose still more. A theorem exploiting either would be new source information and lies outside the present decomposition.

## 4. Exact cancellation and conditioning mirror the affine-centering barrier

Equation `(9)` also classifies attempts to tune the diagonal against the off-diagonal shifts. The unique diagonal weight that cancels the explicit principal carrier is

\[
\boxed{
w_0^*
=-R_w\frac{Q}{\phi N}.
}
\tag{28}
\]

It depends only on unsigned support data and block geometry. At this value,

\[
T_w
=\frac{R_w}{N}C_{1,2}+K_w,
\tag{29}
\]

and `(10)` disappears. Thus a cyclic relational analogue of exact support centering succeeds in isolating the transverse/relational object, but it does so by deleting the direct principal coefficient.

For approximate cancellation, suppose

\[
|\alpha_w|
=|R_w|X^{-\delta+o(1)}
\qquad(\delta\ge0)
\tag{30}
\]

with `R_w!=0`. `MC-201` gives, after choosing the logarithmic-primorial exponent `c` sufficiently small relative to a target `epsilon`,

\[
\frac{|C_{1,2}|}{N}
\ll X^{1/2+c+o(1)}.
\tag{31}
\]

Therefore the already-controlled class-covariance term in decoder `(10)` costs

\[
\frac{|R_w|}{|\alpha_w|}
\frac{|C_{1,2}|}{N}
\ll
X^{1/2+c+\delta+o(1)}.
\tag{32}
\]

Suppressing the explicit carrier by a fixed power `X^{-delta}` spends that same power in inverse conditioning before the new relational term `K_w` has even been estimated. Exact cancellation corresponds to the singular endpoint.

This does **not** rule out subpower tuning or a joint theorem in which `T_w-(R_w/N)C_{1,2}-K_w` is controlled by additional arithmetic structure. It says that the weighting operation itself creates no power gain.

## 5. The ordinary ordered shift differs only by a quantified boundary layer

The cyclic model is exact for the all-pair aggregate `(20)`, because every ordered distinct pair has a unique nonzero cyclic displacement. Individual number-theoretic shifted correlations, however, normally use the linear interval rather than wrap-around.

Let weights now be indexed by ordinary integer shifts with `0<|h|<=H<N/2`, and define

\[
T_w^{\rm lin}
:=
\sum_a\sum_{0\le j,j+h<N}
 w_hx_{a,j}z_{a,j+h},
\tag{33}
\]

with the analogous cyclic statistic `T_w^{cyc}` obtained by reducing `j+h` modulo `N`. For each fixed `h`, exactly `|h|` pairs per class are added by cyclic wrap-around. Hence

\[
\boxed{
|T_w^{\rm lin}-T_w^{cyc}|
\le
\phi\sum_{0<|h|\le H}|h|\,|w_h|.
}
\tag{34}
\]

This gives a concrete boundary ledger. For a single shift `h` of unit weight, the artificial cyclic correction is at most `phi|h|<=q|h|`. Thus whenever the physical displacement `q|h|` is already at or below the desired square-root-scale error budget, cyclicization does not hide a polynomially larger contribution.

Conversely, a proposal that relies on a wide or badly conditioned shift kernel must pay the first-moment factor in `(34)`. Boundary sensitivity is a legitimate way to break cyclic symmetry, but it is not free.

## 6. Prior art and novelty audit

The abstract ingredients are classical: centering of a bilinear form, cyclic convolution, discrete Fourier diagonalization, and the distinction between Toeplitz/linear and circulant/cyclic shift operators. Gray's review cited above is a standard reference for the Toeplitz/circulant side. No novelty is claimed for these mechanisms.

On the arithmetic side, `MC-S28` already anchors logarithmically averaged fixed-shift correlations of multiplicative functions, while `MC-200` audits why existing fixed-shift/logarithmic information does not provide the polynomially quantitative growing-shift estimate needed by its decoder. `MC-204` establishes the complementary representation fact that full source-site permutation invariance destroys shift information entirely.

A targeted literature check for cyclic/circulant diagonalization and mixed Möbius--square-free shift language found standard harmonic-analysis machinery and the existing multiplicative-correlation framework, not an external theorem giving the fixed-power control required for `K_w`. No literature-absence claim is used as evidence here. The durable contribution is the line-specific classification `(9)`: it identifies exactly what a shift-sensitive bilinear representation adds beyond the `(A_a,B_a)` quotient and exactly how its principal coefficient is conditioned.

## Boundaries and falsification tests

- Equations `(9)`--`(18)` concern bilinear sign/support kernels invariant under cyclic translation of the site coordinate. They do not classify arbitrary nonlinear relational statistics, divisor-labelled kernels, multi-scale relations, or operators that break cyclic symmetry in a source-forced way.
- The exact algebra holds for arbitrary ternary source arrays at a complete block and uses no Möbius cancellation, analytic continuation, or zero-free region. Only the target-scale estimate `(31)` imports the support regularity already proved in `MC-201`.
- `K_w` is **not** asserted to be independent of `S` on actual Möbius data. It is the centred relational remainder after the explicit class-mean carrier is separated. Extra ternary or arithmetic identities may couple it back to `S`; proving a useful such relation would be substantive new mathematics.
- The uniform calibration `(19)` is deliberately degenerate: it re-symmetrizes all shifts and therefore must collapse by `MC-204`. It should not be used to argue that every nonuniform shift statistic collapses.
- The linear/cyclic comparison `(34)` assumes a bandwidth below `N/2` so each ordinary shift has an unambiguous cyclic representative without aliasing opposite shifts. Larger supports require a separate boundary accounting.
- A small `alpha_w` is not itself a contradiction. Equation `(32)` only records the conditioning cost of using the already available separate estimate for `C_{1,2}`; a genuinely joint estimate may behave differently.

The core identity is finitely falsifiable: choose any finite ternary arrays and cyclic weights, evaluate `(7)` directly, and compare with `(9)`. The Fourier form is falsified if the direct centred shift sum `(8)` disagrees with `(13)`. The boundary estimate is falsified if a linear/cyclic pair differs by more than the weighted number of wrap-around entries in `(34)`.

## Consequence for the active frontier

`MC-204` left fixed shifts, ordered correlations, and site Fourier modes as genuine representation escapes. The present result separates the live part of that escape from another symmetry illusion.

**Uniform shift aggregation is dead as a new representation mechanism:** it simply returns to the permutation-invariant `MC-200` carrier. **Nonuniform shift weighting is genuinely different**, because it retains the centred cross-spectrum `K_w`; however its explicit principal coefficient is still only `alpha_w`, and canceling or suppressing that coefficient does not create a free decoder.

The next viable theorem in this branch should therefore target a specific nonuniform, source-forced shift kernel and prove an arithmetic estimate for its centred sign/support cross-spectrum, or prove a joint identity that couples that cross-spectrum to `S` with a net fixed-power gain. Generic shift averaging, Fourier re-expression, or exact principal centering alone is now classified and should not be recycled as progress.