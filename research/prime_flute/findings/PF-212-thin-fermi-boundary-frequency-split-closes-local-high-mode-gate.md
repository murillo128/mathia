# PF-212 — thin Fermi boundary frequency splitting closes the local high-mode gate

**Status:** `EXACT-DERIVED + CONDITIONAL-APPLICATION + POSITIVE/ROUTE-NARROWING`. PF-211 reduces the smooth-seam global-to-buffer problem to two separate tasks: a fixed physical-frequency boundary sector of rank `O(1+a_n)`, already harmless by PF-210 once it is assembled modulewise, and a complementary high-frequency Poisson factor whose uniform thin-buffer Schatten scaling was left open. On the **actual canonical PF-205 Fermi seam strip** that local high-frequency estimate can be proved directly. The universal signed Fermi metric separates tangential Fourier modes, the energy-normalized Poisson factor above a fixed physical frequency has `S_{4/3}` norm `O(L_n^{3/4})` with no inverse power of the strip width, while the Dirichlet gradient resolvent on the same `2w_n`-thin strip has `S_4` norm `O(L_n^{1/4}w_n^{3/4})`. Hence every high/Dirichlet recoupling word has strong trace norm `O(a_n d_n^{7/4})`, which is absolutely summable. The high/high boundary word is not absolutely trace-summable by that argument, but its modewise singular values obey a quadratic `j^{-2}` envelope; combined with `d_n\asymp P_n^{-1}`, `L_n=O(log P_n)`, and Chebyshev's `vartheta(X)=O(X)`, any modulewise or fixed-color two-sided block family is globally weak trace class. Terms containing a low boundary factor satisfy PF-210 directly. Thus **local high-frequency Poisson scaling and the long-thin aspect ratio are no longer the remaining PF-211 obstruction**. The unresolved smooth-seam boundary gate is now the genuinely global one: construct the simultaneous native boundary decomposition so that the exterior Schur complement can be reassembled modulewise/finitely colored, or otherwise control its cross-module mixing. This finding does not close that reassembly gate and does not touch the independent true-short-collar splice.

## Claim

Use the exact signed Fermi-area coordinates of PF-205 around one distinguished decomposition cuff:

\[
Q_{L,w}=(-w,w)\times(\mathbb R/L\mathbb Z),
\qquad
0<w\le w_0<1,
\tag{1}
\]

with

\[
g=\frac{dx^2}{1+x^2}+(1+x^2)ds^2,
\qquad
d\mu=dx\,ds.
\tag{2}
\]

Here `L` is the physical cuff length. Let

\[
H=\Delta_g+1
\tag{3}
\]

on `Q_{L,w}`. Denote by `H_D` the realization with Dirichlet condition on both boundary circles `x=\pm w`, and put

\[
G_D:=\nabla H_D^{-1}.
\tag{4}
\]

Let `K` be the two-sided Poisson operator for `Hu=0` with arbitrary Dirichlet data on the two boundary circles, let `\Lambda` be its positive Dirichlet-to-Neumann energy form, and define on the corresponding boundary energy space

\[
A:=\nabla K\Lambda^{-1/2},
\qquad
M:=K\Lambda^{-1/2}.
\tag{5}
\]

As in PF-211,

\[
A^*A+M^*M=I,
\qquad
\|A\|,\|M\|\le1.
\tag{6}
\]

For a fixed physical tangential cutoff `\kappa\ge1`, let `P_\kappa` be the projection on both boundary components onto Fourier modes

\[
\left|\frac{2\pi k}{L}\right|\le\kappa.
\tag{7}
\]

Then, uniformly for `L\ge1` and `0<w\le w_0`, the following hold.

### High Poisson factor

For `q=4/3`,

\[
\boxed{
\|M(I-P_\kappa)\|_{\mathcal S_{4/3}}
\le C L^{3/4}\kappa^{-1/4}.
}
\tag{8}
\]

More precisely, after ordering the high-frequency singular values,

\[
\boxed{
s_j\!\left(M(I-P_\kappa)\right)
\le
\frac{CL}{j+c\kappa L}
\qquad(j\ge1).
}
\tag{9}
\]

The same bounds hold for

\[
C_{\rm hi}=A D(I-P_\kappa)M^*
\tag{10}
\]

for every contraction `D` on this module's boundary energy space, in particular for the energy-normalized exterior factor of PF-211.

### Thin-strip Dirichlet gradient factor

\[
\boxed{
\|G_D\|_{\mathcal S_4}
\le C L^{1/4}w^{3/4}.
}
\tag{11}
\]

Consequently, if `F` is a bounded scalar or fixed-fibre matrix coefficient on the strip, every high/Dirichlet quadratic recoupling word satisfies

\[
\boxed{
\|C_{\rm hi}^*M_FG_D\|_1
+
\|G_D^*M_FC_{\rm hi}\|_1
\le
C\|F\|_\infty Lw^{3/4}\kappa^{-1/4}.
}
\tag{12}
\]

For the PF-205 seam family,

\[
L_n=2a_n,
\qquad
w_n\asymp d_n,
\qquad
\|F_n\|_\infty=O(d_n),
\tag{13}
\]

so

\[
\boxed{
\sum_n
\left(
\|C_{n,\rm hi}^*M_{F_n}G_{n,D}\|_1+
\|G_{n,D}^*M_{F_n}C_{n,\rm hi}\|_1
\right)<\infty,
}
\tag{14}
\]

because the module bound is

\[
O(a_nd_n^{7/4})
=O\!\left(\frac{\log P_n}{P_n^{7/4}}\right).
\tag{15}
\]

### Double-high boundary word

For matched source/target thin strips with comparable `L,w`, let

\[
E_{\rm hh}=C_{h,\rm hi}^*M_FC_{g,\rm hi}.
\tag{16}
\]

The singular-value product inequality and (9) give

\[
\boxed{
s_{2j-1}(E_{\rm hh})
\le
\frac{C\|F\|_\infty L^2}
{(j+c\kappa L)^2}.
}
\tag{17}
\]

Now suppose the PF module words are two-sided orthogonal blocks, or are the sum of a fixed number of colors with that property, exactly as required in PF-210/PF-199. Then the complete double-high family belongs to `\mathcal S_{1,\infty}`. Indeed, with

\[
L_n\le C(1+\log P_n),
\qquad
\|F_n\|_\infty\le \frac{C}{P_n},
\tag{18}
\]

(17) implies

\[
N_{E_{n,\rm hh}}(\sigma)
\le
C L_n\sqrt{\frac{1}{P_n\sigma}},
\tag{19}
\]

and the left side is zero unless

\[
P_n\le \frac{C}{\kappa^2\sigma}.
\tag{20}
\]

Chebyshev's bound `\vartheta(X)=O(X)` gives by partial summation

\[
\sum_{p\le X}\frac{\log p}{\sqrt p}
=O(\sqrt X).
\tag{21}
\]

Therefore the orthogonal block sum obeys

\[
\boxed{
N_{E_{\rm hh}}(\sigma)
\le \frac{C_\kappa}{\sigma},
}
\tag{22}
\]

and hence is weak trace class. A fixed finite coloring preserves (22) by the Fan counting inequality used in PF-199/PF-210.

Finally, every recoupling word containing at least one **low** factor

\[
C_{\rm lo}=ADP_\kappa M^*
\tag{23}
\]

has

\[
\operatorname{rank}C_{\rm lo}
\le C(1+\kappa L),
\qquad
\|C_{\rm lo}\|\le1.
\tag{24}
\]

After insertion of the PF coefficient, the corresponding quadratic word has rank `O(1+a_n)` and norm `O(d_n)`, so PF-210 applies directly under the same modulewise/fixed-color reassembly hypothesis.

Thus, **conditional only on the still-open global placement/reassembly requirement**, the entire local two-sided boundary-recoupling expansion on the PF-205 thin Fermi seams is in `\mathcal S_{1,\infty}`; all terms except the low-containing and double-high families are in fact absolutely trace-summable.

## 1. The high Poisson estimate is an energy inequality, not a thin-domain asymptotic

The special feature of the PF seam strip is that the exact metric (2) is independent of the tangential coordinate `s`. Tangential Fourier modes therefore remain orthogonal for the interior energy, the two-boundary DtN form, and the Poisson extension.

Write

\[
\xi_k=\frac{2\pi k}{L}.
\tag{25}
\]

For a Poisson solution in the `k`th Fourier mode, its positive shifted energy is

\[
\mathcal E_k(u)
=
\int_{-w}^w
\left(
(1+x^2)|u'|^2
+\frac{\xi_k^2}{1+x^2}|u|^2
+|u|^2
\right)dx.
\tag{26}
\]

Since `w\le w_0`,

\[
\mathcal E_k(u)
\ge c(1+\xi_k^2)\|u\|_{L^2(-w,w)}^2.
\tag{27}
\]

But the boundary-energy norm of the Dirichlet datum is exactly `\mathcal E_k(u)`. Hence on each two-dimensional boundary Fourier block,

\[
\|M_k\|
\le \frac{C}{\sqrt{1+\xi_k^2}}.
\tag{28}
\]

No factor `w^{-1}` appears. This is the correct statement for a **two-sided** thin strip. Low symmetric boundary data can extend almost constantly across the strip, so one must not claim the stronger one-sided-Dirichlet estimate `\|M_k\|=O(w)` uniformly at low frequency. PF-210 exists precisely to pay for that finite physical-frequency sector.

Each tangential frequency contributes at most two boundary singular directions. Summing (28) over `|\xi_k|>\kappa` gives

\[
\sum_j
s_j\!\left(M(I-P_\kappa)\right)^{4/3}
\le
C\sum_{|k|>c\kappa L}
\left(1+\frac{k^2}{L^2}\right)^{-2/3}
\le C L\kappa^{-1/3},
\tag{29}
\]

which is (8). The same ordering immediately gives (9). Since `A` and the PF-211 factor `D` are contractions, bounded ideal multiplication proves the corresponding statements for (10), without any estimate on the exterior DtN map beyond positivity.

This calculation is exactly where the long/thin aspect ratio should be charged. The high Poisson factor sees the **one-dimensional boundary length** `L`, not the cell count `L/w`, and the strip width does not enter with a negative exponent.

## 2. The Dirichlet gradient carries the missing positive width power

Let `\lambda_j` be the Dirichlet eigenvalues of `\Delta_g` on `Q_{L,w}`. The quadratic form in (26), now with zero values at `x=\pm w`, is uniformly comparable to the flat rectangular form. By the min-max principle,

\[
\lambda_{m,k}
\ge
c\left(
\frac{m^2}{w^2}+\frac{k^2}{L^2}
\right),
\qquad
m\ge1,\ k\in\mathbb Z,
\tag{30}
\]

up to harmless fixed `\pi` factors.

The nonzero singular values of `G_D` are

\[
\frac{\sqrt\lambda}{1+\lambda}.
\tag{31}
\]

Therefore

\[
\|G_D\|_4^4
\le
C\sum_{m\ge1}\sum_{k\in\mathbb Z}
\left(
\frac{m^2}{w^2}+\frac{k^2}{L^2}
\right)^{-2}.
\tag{32}
\]

For fixed `m`, comparison of the `k`-sum with the corresponding integral gives

\[
\sum_{k\in\mathbb Z}
\left(
\frac{m^2}{w^2}+\frac{k^2}{L^2}
\right)^{-2}
\le
C\left(
\frac{w^4}{m^4}+
\frac{Lw^3}{m^3}
\right).
\tag{33}
\]

Summing in `m` and using `L\ge1>w` yields

\[
\|G_D\|_4^4\le CLw^3,
\tag{34}
\]

which proves (11).

Combining (8) and (11) with Schatten Hölder,

\[
\frac1{4/3}+\frac14=1,
\tag{35}
\]

proves (12). This is the anisotropic counterpart of PF-209's isotropically dilated fixed-cell estimate. The individual factors are no longer both `O(w)`: the long high-boundary factor costs `L^{3/4}`, while the two-dimensional Dirichlet factor returns `L^{1/4}w^{3/4}`. Their product is still cheap enough after the PF coefficient contributes its additional `O(w)`.

In particular, replacing the long thin strip by `O(L/w)` separate isotropic cells and summing their boundary low modes is unnecessary and would recreate PF-210's forbidden cell-scale multiplicity. The full Fermi strip should remain one module-scale boundary object at this stage.

## 3. The double-high term is weak, not strongly summable

A tempting overstatement would be to conclude from (12) that every high-frequency boundary term is absolutely trace-summable. The word `C_{h,hi}^*M_FC_{g,hi}` has no Dirichlet gradient factor from which to obtain `w^{3/4}`. Strong Schatten Hölder alone gives a bound too expensive to sum over modules.

The modewise estimate is better suited to the endpoint. From (9) and

\[
s_{j+k-1}(XY)\le s_j(X)s_k(Y),
\tag{36}
\]

one obtains (17). Thus one module has a `j^{-2}` high-mode tail with amplitude `O(d_nL_n^2)` rather than a flat rank-times-norm envelope.

At a fixed singular threshold `\sigma`, only modules whose **top high-mode singular value** exceeds the threshold can contribute. Equation (17) gives the cutoff (20), and the number of modes above threshold obeys (19). Summing at the threshold rather than summing trace norms first produces

\[
N(\sigma)
\le
C\sigma^{-1/2}
\sum_{p\le C/(\kappa^2\sigma)}
\frac{\log p}{\sqrt p}.
\tag{37}
\]

To keep the arithmetic input explicit, write

\[
S(X)=\sum_{p\le X}\frac{\log p}{\sqrt p}.
\tag{38}
\]

Stieltjes partial summation with `\vartheta(t)=\sum_{p\le t}\log p` gives

\[
S(X)
=
\frac{\vartheta(X)}{\sqrt X}
+\frac12\int_2^X\frac{\vartheta(t)}{t^{3/2}}\,dt
+O(1).
\tag{39}
\]

PF-210 already proves elementarily that `\vartheta(t)\le Ct`. Hence

\[
S(X)\le C\sqrt X,
\tag{40}
\]

and (37) becomes (22).

This endpoint is genuinely weaker than strong trace class. The crude per-module trace envelope is of order `d_nL_n`, whose prime sum need not converge. The weak ideal survives because prime density and the quadratic high-mode decay must be counted **before** summing modules. This is the same structural lesson as PF-210, but with boundary frequency replacing finite low-mode rank.

## 4. Low modes reduce exactly to PF-210

The projection `P_\kappa` has two boundary components and only a fixed physical frequency window. Elementary Fourier counting gives

\[
\operatorname{rank}P_\kappa
\le C(1+\kappa L).
\tag{41}
\]

PF-211 already proves that the normalized boundary correction `ADP_\kappa M^*` has operator norm at most one regardless of the exterior DtN response. Any quadratic word containing this factor has rank at most `C(1+\kappa L)` and, after inserting `F_n`, operator norm `O(d_n)`. For fixed `\kappa`, this is exactly PF-210's

\[
\operatorname{rank}=O(1+a_n),
\qquad
\|\cdot\|=O(d_n)
\tag{42}
\]

hypothesis.

The cutoff must remain at a **fixed physical frequency**. Taking `\kappa_n\asymp w_n^{-1}` would move the entire cell-scale population `O(L_n/w_n)` into the low sector and destroy the PF-210 count. Conversely, sending `\kappa` slowly to zero would make the constants in (8), (17), and (22) diverge. No varying cutoff is needed for the present endpoint.

## 5. What is actually closed, and what is still open

PF-211 left three ingredients entangled in the phrase "high-frequency complement": local Poisson singular-value decay, the long/thin module aspect ratio, and global exterior/reassembly geometry. The first two can now be separated from the third.

On the canonical PF-205 strip, the local decomposition is:

\[
\boxed{
\begin{array}{ll}
\text{low-containing boundary words} & \text{PF-210 weak }S_1,\\
\text{high/Dirichlet words} & \text{summable strong }S_1,\\
\text{double-high boundary words} & \text{prime-density weak }S_1.
\end{array}}
\tag{43}
\]

The only extra hypothesis in this table is the same one PF-210 already exposes: the physical corrections must be represented as two-sided module blocks, or as a fixed finite coloring of such blocks. The local estimates do **not** create that support structure.

This matters because the energy-normalized exterior factor `D` in PF-211 is allowed to mix boundary data. If one cuts all seam modules simultaneously, positivity alone does not prove that `D` is module diagonal, finite range, or even sufficiently off-diagonally decaying. Equation (8) controls singular values after a high projection because contractions cannot enlarge them, but the `d_n` coefficient weights and the prime-density threshold argument are module-dependent. An arbitrary global `D` can move boundary mass between those weights, so one may not silently apply (22) without a genuine reassembly theorem.

The smooth-seam exterior frontier is therefore reduced to the following precise question:

\[
\boxed{
\text{Can the simultaneous native PF boundary Schur complement be localized/reassembled}
\text{ with finite-color two-sided module control, or an equivalent weighted ideal estimate?}
}
\tag{44}
\]

A positive answer would close the decomposition-cuff boundary sector at weak trace order. A negative answer must exhibit genuine cross-module DtN mixing that defeats the prime-weighted endpoint; it can no longer be blamed on a local high-frequency Poisson constant or on the `L_n/w_n` aspect ratio by itself.

PF-203/PF-204's unsmoothed cotangent-transport route remains logically independent and may still avoid this boundary decomposition altogether. PF-183's true-short-collar exact-area splice remains independent as well.

## 6. Prior-art and novelty audit

The analytic ingredients used above are classical: Fourier separation on a rotational/Fermi cylinder, the min-max principle, ideal stability under contractions, Schatten Hölder and product singular-value inequalities, and the boundary-energy Poisson normalization already isolated in PF-211. General Krein/DtN and boundary-resolvent Schatten theory is represented by Gerd Grubb, *The mixed boundary value problem, Krein resolvent formulas and spectral asymptotic estimates*, J. Math. Anal. Appl. 382 (2011), 339--363, DOI `10.1016/j.jmaa.2011.04.055`, arXiv:1104.0785, and by Jussi Behrndt, Matthias Langer, Vladimir Lotoreichik, *Trace formulae and singular values of resolvent power differences of self-adjoint elliptic operators*, J. London Math. Soc. 88 (2013), 319--337, DOI `10.1112/jlms/jdt012`, arXiv:1301.5780. PF-209 already audits the relevant boundary order, while PF-211 audits the interior/exterior DtN sum and energy-normalized Schur complement.

A structure-directed literature search for Poisson/Schatten estimates on thin cylinders and Krein-resolvent thin-strip reassembly found the expected general boundary-resolvent theory and thin-domain spectral literature, but no theorem was used as a substitute for the explicit estimates (27)--(40). Search absence is not treated as evidence of novelty.

No novelty is claimed for any abstract operator theorem in this finding. The project-specific deduction is the **exact endpoint bookkeeping on the canonical PF Fermi seam geometry**: fixed physical-frequency splitting avoids cell-scale low multiplicity; the long-thin Dirichlet factor contributes `w^{3/4}`; the PF coefficient contributes another `w`; and the remaining double-high `j^{-2}` tail is converted to global weak trace order by prime-density threshold counting. This removes one explicit analytic gate from PF-211 without pretending that the global exterior Schur complement has already been localized.

## 7. Falsification and boundary checks

A later adversary can audit PF-212 by:

1. checking the exact Fermi metric and volume form (2) against PF-205;
2. verifying the two-boundary Poisson energy identity and refusing the false low-frequency estimate `M=O(w)` for symmetric boundary data;
3. deriving (27)--(29) Fourier block by Fourier block, including the two boundary components;
4. proving the min-max comparison (30) for the Dirichlet strip and reproducing the double sum (32)--(34);
5. checking the Schatten exponents `4/3` and `4` in (35) and the PF substitution `L_n=2a_n`, `w_n\asymp d_n`, `\|F_n\|_\infty=O(d_n)`;
6. deriving (17) from the product singular-value inequality rather than from an unjustified trace-norm product;
7. reproducing the weighted Chebyshev partial summation (39)--(40) and the threshold cutoff (20);
8. keeping the high/high conclusion at weak `S_1`; do not silently strengthen it to trace class;
9. verifying that any claimed global application really has two-sided module orthogonality or a fixed finite coloring, rather than merely disjoint coefficient supports;
10. treating a globally mixing exterior contraction `D` as unresolved unless a separate weighted/off-diagonal reassembly estimate is proved;
11. keeping the true-short-collar PF-183 splice and the PF-204 piecewise cotangent-transport route outside this finding;
12. making no wave-operator, determinant, resonance, prime/clone separation, or RH inference from this endpoint control.

The finding would need narrowing if the canonical PF seam support cannot be taken as the two-sided Fermi strip of PF-205, if the source/target strip parameters cease to be uniformly comparable, or if a future global decomposition necessarily destroys the module-weight placement assumed in the weak-counting application. None of those possibilities changes the local estimates (8)--(17); they would affect only the conditional global handoff.

## Consequences for the research line

The optional smooth decomposition-cuff route now has a cleaner frontier. PF-207 closes the scale-correct local Dirichlet principal block, PF-208 closes scale-matched cutoff commutators, PF-209 closes fixed-profile boundary order, PF-210 supplies prime-density low-mode counting, PF-211 removes exterior amplification after energy normalization, and PF-212 closes the **canonical thin-strip high-frequency/aspect-ratio estimate** conditional on honest module reassembly.

Accordingly, further work on this branch should not spend another cycle proving a local high-frequency Poisson Schatten estimate on the same Fermi strip. It should attack (44): either derive finite-color/two-sided support for a simultaneous native boundary decomposition, prove quantitative off-diagonal decay of the normalized exterior Schur complement strong enough to substitute for it, or return to PF-204's unsmoothed native-resolvent/cotangent-transport architecture if that avoids the global boundary mixing more naturally.

Even if the decomposition-cuff sector is eventually closed at `S_{1,\infty}`, the accepted weak-trace clue remains unresolved until the independent true-short-collar endpoint splice is also controlled and the complete first relative resolvent is assembled. All present endpoint estimates are shared by the exact prime flute and its matched all-composite shift control, so they narrow what a useful arithmetic mechanism would have to retain rather than supplying such a mechanism themselves.