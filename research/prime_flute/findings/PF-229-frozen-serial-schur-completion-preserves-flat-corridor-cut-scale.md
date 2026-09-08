# PF-229 — frozen serial Schur completion preserves the flat-corridor `w/s` cut scale

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + OPERATOR-THEORETIC + POSITIVE/ROUTE-NARROWING`. PF-228 proves that an isolated straight two-interface corridor pays a dressed transmission factor of order `w/s` on the inverse-seam frequency band, but deliberately leaves open whether a **global** Schur inverse can destroy that gain by shorting through the rest of the flute. In the first genuinely global serial control, it cannot. Freeze one symmetric PF-228 Fourier channel and repeat the same normalized corridor cell along a bi-infinite chain. The complete prefix-to-tail block of the global inverse is rank one and has the exact singular value

\[
\boxed{
\sigma_{\rm cut}
=\frac{c}{H(H+4c)},
\qquad
H=1+2m,
}
\]

where `c` is the cell conductance and `m` its same-sign mass. The isolated two-interface transmission is

\[
\boxed{
 x_{\rm loc}=\frac{c}{h(h+2c)},
\qquad h=1+m,
}
\]

and the two are uniformly comparable:

\[
\boxed{
\frac14 x_{\rm loc}\le \sigma_{\rm cut}\le x_{\rm loc}.
}
\]

For the equal-width PF-228 corridor,

\[
m=\frac{\tanh(z/2)}{\tanh(\mu w)},
\qquad
c=\frac{\operatorname{csch}z}{\tanh(\mu w)},
\qquad
z=\mu s,
\]

so the **full global cut block** in this serial, mode-preserving control retains exactly the same inverse-seam scale and frequency envelope as the isolated cell:

\[
\sigma_{\rm cut}\lesssim \frac ws\frac{z}{\sinh z},
\qquad
\sigma_{\rm cut}\asymp \frac ws
\quad(z=O(1))
\]

under the same bounded-ratio hypotheses as PF-228. Thus serial globality and scalar Schur shorting by themselves do not erase the prime-square weighted scale exposed by PF-228. Any failure of the actual PF cut flux to inherit that gain must use structure absent from this control — most plausibly tangential mode mixing/noncommutativity in the variable pant, non-frozen coefficient effects, or the overlapping nested-cut reassembly — rather than merely the fact that `D=(I+K)^{-1}` is global.

## Claim

Freeze one PF-228 tangential frequency

\[
\mu=\sqrt{1+\xi^2},
\qquad
z=\mu s,
\qquad
t=\tanh(\mu w),
\tag{1}
\]

and take equal seam-normalizer halfwidths `w_1=w_2=w`. The normalized exterior precision of one straight corridor is

\[
K_{\rm edge}
=
\begin{pmatrix}
d&-c\\-c&d\end{pmatrix},
\qquad
d=\frac{\coth z}{t},
\qquad
c=\frac{\operatorname{csch}z}{t}.
\tag{2}
\]

Since

\[
\coth z-\operatorname{csch}z=\tanh(z/2),
\tag{3}
\]

put

\[
m:=d-c=\frac{\tanh(z/2)}{t}>0,
\qquad
h:=1+m.
\tag{4}
\]

Then

\[
I+K_{\rm edge}
=hI+c
\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\tag{5}
\]

and direct inversion gives PF-228's local off-diagonal transmission in the equivalent form

\[
\boxed{
x_{\rm loc}=\frac{c}{h(h+2c)}.}
\tag{6}
\]

Now repeat this **same edge form** between every adjacent pair of modules in `\ell^2(\mathbb Z)`. Each module belongs to two cells, so the global shifted precision is

\[
M_\infty
:=I+K_\infty
=H I+cL_{\mathbb Z},
\qquad
H:=1+2m=2h-1,
\tag{7}
\]

where

\[
(L_{\mathbb Z}u)_j=2u_j-u_{j-1}-u_{j+1}.
\tag{8}
\]

Let

\[
D_\infty=M_\infty^{-1},
\qquad
E=\mathbf 1_{\{j\le0\}},
\qquad
F=I-E.
\tag{9}
\]

Then the complete global prefix-to-tail cut block

\[
X_\infty:=F D_\infty E
\tag{10}
\]

has rank one. Its unique nonzero singular value is

\[
\boxed{
s_1(X_\infty)=\frac{c}{H(H+4c)}.}
\tag{11}
\]

Moreover, for every `m,c\ge0`,

\[
\boxed{
\frac14\frac{c}{h(h+2c)}
\le
\frac{c}{(2h-1)(2h-1+4c)}
\le
\frac{c}{h(h+2c)}.
}
\tag{12}
\]

Thus

\[
\boxed{\frac14x_{\rm loc}\le s_1(X_\infty)\le x_{\rm loc}.}
\tag{13}
\]

The statement is about the **full half-chain cut operator**, not merely the nearest-neighbor Green coefficient.

## 1. Exact Green kernel of the frozen serial completion

For `c>0`, define

\[
R:=\sqrt{H(H+4c)},
\qquad
r:=\frac{H+2c-R}{2c}.
\tag{14}
\]

Then `0<r<1` and

\[
r+r^{-1}=2+\frac Hc.
\tag{15}
\]

The standard second-order recurrence for the massive discrete Laplacian gives

\[
\boxed{
(D_\infty)_{ij}
=\frac1R r^{|i-j|}.
}
\tag{16}
\]

This can also be checked directly: away from `i=j`, (15) makes `(H I+cL)r^{|\cdot-j|}=0`, while the jump at `i=j` fixes the coefficient `R^{-1}`.

Across the cut `i\ge1`, `j\le0`, equation (16) factorizes:

\[
(D_\infty)_{ij}
=\frac1R r^i r^{-j}.
\tag{17}
\]

Hence `X_\infty` is rank one and

\[
\begin{aligned}
s_1(X_\infty)
&=\frac1R
\left(\sum_{i\ge1}r^{2i}\right)^{1/2}
\left(\sum_{j\le0}r^{-2j}\right)^{1/2}\\
&=\frac1R\frac r{1-r^2}.
\end{aligned}
\tag{18}
\]

From (15),

\[
\frac{1-r^2}{r}=r^{-1}-r=\frac Rc,
\tag{19}
\]

so (18) becomes exactly (11).

This calculation is the scalar Jacobi/Weyl version of eliminating the two half-chains by their positive boundary self-energies. It makes the spatial delocalization of the global inverse explicit: the prefix-to-tail operator is not a nearest-neighbor coefficient, but the geometric tails still combine into the finite factor in (11).

## 2. Serial completion changes the local transmission by at most a fixed factor

The isolated edge inverse in (6) follows immediately from

\[
\det(I+K_{\rm edge})=h(h+2c).
\tag{20}
\]

Using `H=2h-1`, the ratio between the global cut singular value and the isolated transmission is

\[
\frac{s_1(X_\infty)}{x_{\rm loc}}
=
\frac{h(h+2c)}{(2h-1)(2h-1+4c)}.
\tag{21}
\]

Because `h\ge1`,

\[
(2h-1)(2h-1+4c)-h(h+2c)
=(3h-1)(h-1)+(6h-4)c\ge0,
\tag{22}
\]

while

\[
4h(h+2c)-(2h-1)(2h-1+4c)
=4c+4h-1>0.
\tag{23}
\]

Equations (22)--(23) prove (12). No asymptotic regime is needed.

The lower comparison is useful conceptually. A global serial inverse can spread one boundary excitation over arbitrarily many modules, but in this positive mode-preserving completion that spatial tail does **not** turn the local `w/s` gain into a parametrically different cut singular value. It only changes it by a bounded factor.

## 3. The PF-228 inverse-seam envelope survives the global cut

PF-228 proves for the equal-width local corridor

\[
x_{\rm loc}
\le
\rho\frac z{\sinh z},
\qquad
\rho:=\frac ws,
\tag{24}
\]

and, whenever `z\le z_0` and `w/s` stays in the same bounded regime used there,

\[
x_{\rm loc}\ge c_0\rho.
\tag{25}
\]

Combining (13), (24), and (25) yields

\[
\boxed{
s_1(X_\infty)
\le
\rho\frac z{\sinh z}}
\tag{26}
\]

for every frequency, and

\[
\boxed{
s_1(X_\infty)\ge \frac{c_0}{4}\rho}
\tag{27}
\]

on the inverse-seam band.

If the tangential direction is periodized with length `\mathcal L`, Fourier modes remain orthogonal in the frozen chain. Therefore the complete cut operator has one singular channel for each tangential frequency, and PF-228's counting estimate transfers unchanged up to constants:

\[
\boxed{
N_{X_\infty}(\lambda)
\le
C\frac{\mathcal L}{s}
\left(1+\log_+\frac{C\rho}{\lambda}\right).
}
\tag{28}
\]

The order `\mathcal L/s` inverse-seam population also survives by (27). Thus the local PF-228 calibration was not an artifact of truncating the **module-index** direction to a single two-interface cell.

For the canonical frozen PF scales

\[
w_n\asymp P_n^{-1},
\qquad
s_n\asymp\frac{g_n+g_{n+1}}{P_n},
\qquad
\delta_n=\frac1{P_n}-\frac1{P_{n+1}},
\tag{29}
\]

the largest reciprocal-weighted cut singular value in this serial control still satisfies

\[
\delta_n\|X_{\infty,n}\|
\lesssim
\delta_n\frac{w_n}{s_n}
\lesssim\frac1{P_n^2}.
\tag{30}
\]

Consequently PF-228's threshold-counting proof for the orthogonal family of frozen weighted cut controls remains valid verbatim. This is still a **control-family** weak-`S_1` statement, not the actual nested PF commutator.

## 4. What is removed from the live obstruction list

PF-228 listed two distinct global dangers: the full `D=(I+K)^{-1}` can short through the rest of the flute, and the true PF-222 cut-flux series uses overlapping nested cuts rather than orthogonal control blocks. PF-229 separates them.

In a frozen, scalar, tangential-mode-preserving serial completion, the first danger is absent at the level of the **complete prefix-to-tail cut singular value**. The two infinite half-chains change the isolated-cell transmission by only a factor in `[1/4,1]`; they neither restore order-one inverse-seam amplitude nor create a new multiplicity scale.

Therefore a canonical counterexample to the PF-228 `w/s` gain cannot be explained merely by saying that the inverse is global. It must exploit at least one feature not represented here:

- the actual pant mixes tangential modes because its Fermi thickness and boundary correspondence vary with the tangential coordinate;
- neighboring PF cells are not frozen copies, so their boundary-energy operators do not share one Fourier diagonalization;
- the physical `P/H` projections and exact exterior precision need not commute with the local mode decomposition;
- even if every individual cut has the PF-228 singular-value envelope, the nested series `\sum_n\delta_nP[D,E_n]H` still requires a genuine reassembly theorem.

This does **not** prove that one of those mechanisms really destroys the gain. It identifies them as the remaining places where a destruction mechanism would have to live.

## 5. Prior art and novelty audit

No novelty is claimed for the abstract ingredients. The Green kernel of a constant-coefficient Jacobi operator, half-line Weyl/Green-function factorization, and Schur-complement elimination are classical. A standard broad reference is Gerald Teschl, *Jacobi Operators and Completely Integrable Nonlinear Lattices*, AMS Mathematical Surveys and Monographs 72 (2000), which develops Jacobi operators, Green functions, and Weyl theory. Kron/Schur elimination of passive graph networks with diagonal self-loads is likewise standard; see Florian Dörfler and Francesco Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks*, IEEE Transactions on Circuits and Systems I 60 (2013), 150--163, DOI `10.1109/TCSI.2012.2215780`.

A structure-directed search did not identify a source that contains the project-specific PF statement (13), namely the comparison between the **full half-chain cut singular value** of the frozen PF-228 normalized corridor chain and the isolated PF corridor transmission, followed by the inherited `w/s`/reciprocal-prime counting consequence. That comparison is elementary once the control is written down; the durable value is not a new Jacobi theorem but the elimination of a specific false obstruction in the prime-flute weak-trace route.

## 6. Falsification and boundary checks

1. The serial chain repeats the same **edge form**, so its node mass is `H=1+2m`; using `1+m` globally would incorrectly count only one incident pant per module.
2. Equation (11) is the singular value of the full prefix-to-tail block `F D_\infty E`, not the nearest-neighbor matrix element. The rank-one factorization (17) is what makes the distinction exact.
3. The equal-width hypothesis is deliberate. It is the clean frozen symmetric control of PF-228; canonical neighboring seam widths are asymptotically comparable, but no variable-width theorem is inferred here.
4. Translation invariance in the module index and tangential Fourier conservation are essential. PF-217 shows that nonconstant tangential boundary profiles can alter shorted low forms in the real flute, so the actual operator cannot be replaced by this scalar chain without a new comparison theorem.
5. Equation (28) is a per-cut singular-value statement. It does not make different prefix cuts orthogonal and therefore does not prove the actual PF-222 commutator weak trace class.
6. The reciprocal-prime estimate (30) uses only the persisted PF scales already used in PF-228. No average prime-gap law or statistical assumption is added.
7. The result does not address PF-204's unsmoothed native factorization, PF-183's true-short-collar splice, the separate `S_r`, `r>1`, clue, wave operators, determinants/resonances, prime/clone separation, or any RH implication.

## Consequences for the research line

PF-226/PF-227 show that the raw canonical pant has too many inverse-seam channels for a naive saturated-mass argument. PF-228 shows that an isolated straight local inverse converts those channels to the compatible `w/s` scale. PF-229 now verifies that this scale survives a **complete infinite serial Schur inverse** when the geometry is frozen and mode-preserving.

The next smooth-route theorem should therefore not spend another iteration testing generic scalar/global shorting. It should attack the first genuinely missing structure: compare the variable hyperbolic pant cut flux with a mode-preserving serial control strongly enough to retain the `w_n/s_n` gain, or identify a concrete tangential mode-mixing/noncommutative mechanism that violates such a comparison. Even after that, nested-cut weak-`S_1` reassembly remains a separate gate.