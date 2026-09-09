# WP-223 — State-Hamiltonian diagonal selection cannot make the Bost–Connes Weil defect positive without annihilating it

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-GRAM + STATE-HAMILTONIAN + ENERGY-DIAGONAL-SOURCE-ALGEBRA + ZERO-DIAGONAL-DEFECT + SPECTRAL-COMPRESSION-NO-GO + DIAGONAL-CONGRUENCE-NO-GO + DECISIVE-NARROWING + PRIOR-ART-CLASSICAL-TOOLS + NOT-A-WEIL-BRIDGE`.

`WP-222` shows that finite coinvariant model spaces can program either strict sign for the same critical Bost–Connes one-prime Weil defect. That makes **source selection of the quotient** a load-bearing obligation. The most immediate source selector supplied by the Bost–Connes dynamics is the state-energy grading itself: spectral projections, bounded Borel functions, or positive weights of the Hamiltonian.

For that entire diagonal source algebra there is an exact obstruction. On every finite prime set `F`, the critical finite-place defect `W_F` has zero diagonal in the canonical exponent basis. Every nonzero matrix element joins two exponent vectors that differ along exactly one prime axis. Consequently any Hamiltonian-diagonal compression or positive diagonal congruence has the following dichotomy:

\[
\boxed{
D W_F D=0
\quad\text{or}\quad
D W_F D\text{ is indefinite}.
}
\]

In particular, if `Q=1_B(H_F)` is **any** spectral projection of the finite-prime Bost–Connes Hamiltonian, then

\[
\boxed{
QW_FQ\succeq0
\Longrightarrow
QW_FQ=0.
}
\]

On a single prime ray the statement is sharper: every spectral subspace of dimension at least two gives an indefinite compression, while dimensions zero and one give the zero operator. Thus no energy window, Hamiltonian Borel selector, Gibbs/Boltzmann reweighting, or other positive diagonal operation can supply a nonzero positive orientation of the source-forced Weil defect. It may preserve the defect and its two signs, or erase it, but cannot turn it into positive geometric content.

This does **not** rule out a source-forced non-diagonal quotient, an active mixed-prime operator-valued coupling, an archimedean interaction formed before compression, or the semilocal/quantized-calculus mechanisms of Connes–Consani. It rules out a precise canonical response to `WP-222`: deriving the missing positive quotient merely from the same Bost–Connes energy observable.

## 1. Exact finite-prime matrix of the critical defect

Fix a nonempty finite prime set

\[
F=\{p_1,\ldots,p_d\}
\]

and use the exponent basis

\[
e_{\alpha},
\qquad
\alpha=(\alpha_p)_{p\in F}\in\mathbb N_0^F.
\]

The source Hamiltonian grading is

\[
H_F e_\alpha
=
\left(\sum_{p\in F}\alpha_p\log p\right)e_\alpha
=
\log\!\left(\prod_{p\in F}p^{\alpha_p}\right)e_\alpha.
\tag{1}
\]

Unique factorization makes this spectrum simple on the finite-prime sector.

`WP-216` derives the critical conditional Bost–Connes Gram. On the `p` coordinate its kernel is

\[
G_p(a,b)=r_p^{|a-b|},
\qquad
r_p=p^{-1/2},
\tag{2}
\]

and `WP-220` identifies the finite-prime Weil defect as

\[
W_F
=
\sum_{p\in F}(\log p)(I-G_p),
\tag{3}
\]

where each `G_p` acts in its own coordinate and as the identity on the others.

Equation (3) immediately gives

\[
\langle e_\alpha,W_Fe_\alpha\rangle=0
\qquad
\text{for every }\alpha.
\tag{4}
\]

For distinct `\alpha,\beta`, the matrix element is nonzero exactly when the two exponent vectors differ in one coordinate only. If that coordinate is `p`, then

\[
\boxed{
\langle e_\alpha,W_Fe_\beta\rangle
=
-(\log p)\,
p^{-|\alpha_p-\beta_p|/2}.
}
\tag{5}
\]

If `\alpha` and `\beta` differ in two or more prime coordinates, the matrix element is zero.

Thus the finite critical defect is a self-adjoint **hollow** weighted graph operator on the exponent lattice: every diagonal entry is zero, and every surviving edge has a nonzero real weight.

## 2. Every Hamiltonian spectral compression is zero or indefinite

Let

\[
Q=\mathbf 1_B(H_F)
\tag{6}
\]

be an arbitrary spectral projection, with `B` any Borel subset of the energy spectrum. Because (1) has simple pure point spectrum, `Q` is precisely the coordinate projection onto some subset

\[
A\subseteq\mathbb N_0^F.
\tag{7}
\]

Suppose `A` contains two vectors `\alpha,\beta` that differ along exactly one prime coordinate `p`. The two-dimensional principal compression of `QW_FQ` to their span is

\[
\begin{pmatrix}
0 & -c\\
-c & 0
\end{pmatrix},
\qquad
c=(\log p)p^{-|\alpha_p-\beta_p|/2}>0.
\tag{8}
\]

Its eigenvalues are `+c` and `-c`. Equivalently,

\[
\langle e_\alpha+e_\beta,W_F(e_\alpha+e_\beta)\rangle=-2c<0
\tag{9}
\]

while

\[
\langle e_\alpha-e_\beta,W_F(e_\alpha-e_\beta)\rangle=2c>0.
\tag{10}
\]

Hence the whole compression is indefinite.

If `A` contains no such pair, (5) says that **every** matrix element of `QW_FQ` vanishes. Therefore

\[
\boxed{
QW_FQ
=
0
\quad\text{or}\quad
QW_FQ\text{ is indefinite}.
}
\tag{11}
\]

This proves, in particular,

\[
\boxed{
QW_FQ\succeq0
\iff
QW_FQ=0.
}
\tag{12}
\]

No limiting or spectral-theoretic subtlety is involved: whenever the compression retains any finite-place interaction at all, two retained basis states already provide exact opposite-sign witnesses.

### One-prime corollary

For `F={p}`, any two distinct exponent indices differ only in the `p` coordinate. Therefore every spectral projection with rank at least two is indefinite:

\[
\operatorname{rank}Q\ge2
\Longrightarrow
QW_pQ\text{ indefinite}.
\tag{13}
\]

Ranks zero and one give `QW_pQ=0`. Thus there is no nontrivial positive one-prime energy window.

## 3. Positive Hamiltonian weights cannot repair the sign either

The obstruction is not limited to hard spectral cuts. Let

\[
D=f(H_F)
\tag{14}
\]

for any bounded real Borel function `f`; in particular `D` may be positive. Write

\[
D e_\alpha=d_\alpha e_\alpha.
\tag{15}
\]

Then the congruence

\[
A_D:=DW_FD
\tag{16}
\]

still has zero diagonal,

\[
\langle e_\alpha,A_De_\alpha\rangle=0,
\tag{17}
\]

and on every retained prime-axis pair,

\[
\langle e_\alpha,A_De_\beta\rangle
=
-d_\alpha d_\beta
(\log p)p^{-|\alpha_p-\beta_p|/2}.
\tag{18}
\]

If the right-hand side is nonzero, the corresponding `2 x 2` principal matrix again has eigenvalues of opposite signs. If every such product vanishes, all matrix entries vanish and `A_D=0`. Hence

\[
\boxed{
DW_FD=0
\quad\text{or}\quad
DW_FD\text{ is indefinite}.
}
\tag{19}
\]

A basis-free positivity lemma gives the same conclusion. If a positive operator `A` satisfies

\[
\langle e_\alpha,Ae_\alpha\rangle=0
\quad\text{for every }\alpha,
\tag{20}
\]

then positivity gives the Cauchy–Schwarz estimate

\[
|\langle e_\alpha,Ae_\beta\rangle|^2
\le
\langle e_\alpha,Ae_\alpha\rangle
\langle e_\beta,Ae_\beta\rangle
=0,
\tag{21}
\]

so `A=0`. Thus a nonzero zero-diagonal self-adjoint defect cannot become positive through a diagonal congruence.

The canonical thermal weights illustrate the point. For

\[
D_\gamma=e^{-\gamma H_F/2},
\qquad
\gamma\ge0,
\tag{22}
\]

every coefficient `d_\alpha` is strictly positive. Therefore every prime-axis edge survives, and

\[
D_\gamma W_FD_\gamma
\tag{23}
\]

is indefinite for every nonempty `F`. At the critical half-density `\gamma=1`, the source scale that produced the Bost–Connes critical Gram does not repair the orientation when reapplied as a diagonal energy weight.

Equation (22) is used here only as a bounded source-canonical grading weight. At the Bost–Connes critical point this statement does not identify `e^{-H_F}` with a trace-class Gibbs density for the full critical KMS representation.

## 4. The entire state-energy diagonal algebra is sign-inert

Because `H_F` has simple pure point spectrum, the von Neumann algebra it generates is the full bounded diagonal algebra in the exponent basis:

\[
W^*(H_F)
=
\left\{
\sum_\alpha d_\alpha
|e_\alpha\rangle\langle e_\alpha|
:
(d_\alpha)\in\ell^\infty
\right\}.
\tag{24}
\]

This is the same programmability phenomenon that `WP-215` exposed from the opposite direction. On the discrete state spectrum, Borel functional calculus can select arbitrary integer labels or prescribe arbitrary bounded diagonal weights.

But `WP-215` concerned **inserting a desired diagonal coefficient sequence** through `F(H)`. The present theorem concerns the already source-forced **off-diagonal** Weil defect from `WP-216`. Even granting the entire programmable diagonal algebra cannot create its missing positive orientation:

\[
\boxed{
D\in W^*(H_F)
\quad\Longrightarrow\quad
DW_FD\succeq0
\ \Rightarrow\
DW_FD=0.
}
\tag{25}
\]

Likewise every energy-diagonal conditional expectation or complete dephasing erases the defect. If `\mathbb E_H` denotes the diagonal expectation in the basis of (1), then (4) gives

\[
\boxed{
\mathbb E_H(W_F)=0.
}
\tag{26}
\]

So the two obvious uses of the state-energy algebra fail in complementary ways. Keeping its off-diagonal interactions retains indefiniteness; forgetting them to obtain a diagonal positive object destroys the finite Weil payload.

## 5. Relation to the quotient escape of WP-222

`WP-222` proves that the broader coinvariant/model-space category is sign-programmable: repeated-root finite-Blaschke quotients can make the one-prime defect positive or negative depending on where their zero is placed. That result leaves open the possibility that the **source itself** chooses one quotient independently of the target sign.

The state Hamiltonian is an obvious candidate source selector because it is canonical and already carries the logarithmic arithmetic scale. Equations (11)--(25) close that candidate class. A quotient or compression defined only through the spectral algebra of the same energy grading cannot emulate the positive Blaschke localization of `WP-222` unless it annihilates the defect.

This distinction also prevents a false inference from `WP-215`. The fact that `F(H)` can encode prime powers or critical Mangoldt amplitudes does not mean that Hamiltonian spectral selection can make the intrinsic Bost–Connes defect positive. The former works because target values are written onto the diagonal; the latter fails because the target interaction is hollow and positivity cannot preserve a nonzero hollow matrix.

The surviving source-selection problem therefore requires **noncommuting information** relative to `H_F`, or an operation that changes `W_F` before the positivity test.

## 6. Matched controls and aggressive falsification

The argument is completely insensitive to primality. Replace each prime coordinate by arbitrary parameters

\[
c_j>0,
\qquad
0<r_j<1,
\tag{27}
\]

and define on `\mathbb N_0^d`

\[
W
=
\sum_{j=1}^d
c_j\bigl(I-G_{r_j}^{(j)}\bigr),
\qquad
G_{r_j}(a,b)=r_j^{|a-b|}.
\tag{28}
\]

The matrix is again zero on the diagonal and supported on one-coordinate edges. Every diagonal projection or diagonal congruence is therefore either zero or indefinite exactly as above.

This generalized-product survival is appropriate for a negative classification theorem: the obstruction comes from the interaction between zero diagonal and energy-diagonal selection, not from an RH-equivalent arithmetic identity.

Several possible overclaims are excluded.

First, adding a positive diagonal counterterm `V(H_F)` is **not** covered by (19). That changes the operator rather than selecting or reweighting the source defect. Such a repair must separately justify its coefficient, global cost, and archimedean/polar provenance; the compact and scalar-compensation obstructions of `WP-216` and `WP-218` remain relevant.

Second, a non-diagonal quotient or shorting operation need not lie in `W^*(H_F)`. `WP-222` explicitly demonstrates that non-diagonal coinvariant geometry can change the sign. The present result says only that state-energy spectral calculus cannot canonically choose a nonzero positive member of that family by itself.

Third, the theorem is finite-prime. It is nevertheless an obstruction to any purported global positivity mechanism whose restriction to a finite source-energy sector is exactly a Hamiltonian-diagonal compression of `W_F`. A genuinely global finite--archimedean form may change those finite restrictions and is therefore outside the hypothesis.

## 7. Prior-art and novelty audit

The source Hamiltonian and its logarithmic grading belong to the original Bost–Connes system: Jean-Benoît Bost and Alain Connes, **“Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory,”** *Selecta Mathematica (N.S.)* **1** (1995), 411–457, DOI `10.1007/BF01589495`. `SOURCES.md` already records this as the canonical Bost–Connes anchor.

The operator-theoretic lemma behind (20)--(21) is elementary and classical: for a positive operator, the sesquilinear form satisfies Cauchy–Schwarz, so a zero diagonal in an orthonormal basis forces the whole operator to vanish. Zero-diagonal operators also occur extensively in the paving/Kadison–Singer literature. No novelty is claimed for that lemma, diagonal compressions, Borel functional calculus, or Hamiltonian spectral projections.

The close noncommutative-geometric prior art also makes the boundary important. Connes–Consani Weil-positivity constructions use nontrivial phase-space/semilocal compression and quantized differential structure; they are not state-Hamiltonian diagonal cuts of the finite Bost–Connes Toeplitz defect. A targeted audit of Bost–Connes Hamiltonian, zero-diagonal compression, and Weil-positivity literature found no source asserting the specific consequence (11)--(25), but the mathematical ingredients are classical.

The durable Mathia delta is therefore narrow: once `WP-216` has identified the exact source-forced critical Bost–Connes defect and `WP-222` has made quotient selection the live issue, **the full source algebra generated solely by the state-energy grading is provably incapable of selecting or reweighting that defect into a nonzero positive form**.

## 8. Research disposition

This passes the substantive-finding gate as a decisive narrowing of the accepted Bost–Connes completion clue.

The excluded implication is

\[
\boxed{
\begin{gathered}
\text{critical Bost--Connes finite Weil defect}\\
+\ \text{spectral selection/reweighting from }W^*(H_F)
\end{gathered}
\not\Rightarrow
\text{nonzero positive Weil form}.
}
\tag{29}
\]

Indeed the result is stronger: within that category positivity forces annihilation of the finite defect.

The accepted global completion clue remains unresolved. A surviving Bost–Connes route must use structure not diagonal in the source energy basis: a noncommuting source relation, an active mixed-prime/operator-valued coupling, a source-forced non-diagonal quotient, or a finite--archimedean/semilocal operation formed before the sign test. It must then still recover the completed finite, Gamma, and polar coefficients and prove positivity independently rather than importing RH or zero data.
