# NB-099 — zeta symmetries and arbitrarily sparse zero counts cannot regularize collective shear

**Status:** `EXACT-DERIVED + CANONICAL-BLASCHKE-GEOMETRY + VERTICAL-TRANSLATION-INVARIANCE + ZETA-SYMMETRY-MATCHED-CONTROL + ARBITRARILY-SPARSE-ZERO-COUNT-CONTROL + NEGATIVE-METHOD-BOUNDARY`.

`NB-098` proves that three distinct right-half-plane states can have unit canonical pivots and uniformly benign two-state subsystems while the full canonical Cholesky shear grows like `epsilon^(-1)` and the transformed Gram condition number grows like `epsilon^(-4)`. That finding leaves open whether elementary source-specific facts about the actual zeta divisor — high ordinate, the standard zero symmetries, simplicity, or global zero-density information — might already exclude the bad geometry.

They do not, at that level of information. The canonical half-line geometry is **exactly invariant under common vertical translation** of every selected zero parameter. Hence the transverse three-state family from `NB-098` can be transplanted to arbitrarily large ordinate without changing its transformed Gram at all. Moreover one can complete each transplanted triple by the usual zeta involutions and place infinitely many such clusters so sparsely that the resulting synthetic divisor still obeys the Riemann--von Mangoldt global counting law, can be chosen simple, and can satisfy any prescribed unbounded global allowance for off-critical zeros. Thus neither standard quartet symmetry nor any purely global zero-count bound that still allows infinitely many off-critical zeros can provide the separation-insensitive conditioning theorem ruled out by `NB-098`.

The conclusion is deliberately source-boundary rather than a claim about the actual zeta zeros: a successful repair must use **local** information coupling nearby ordinates and horizontal displacements, a genuinely symmetry-closed representation that changes the canonical coordinate problem, or a target-conversion argument that avoids uniform conditioning altogether.

## 1. Canonical deflation is exactly invariant under common vertical translation

Let

\[
F=(\lambda_1,\ldots,\lambda_d),
\qquad
\lambda_r=a_r+i\gamma_r,
\qquad a_r>0,
\tag{1}
\]

be an ordered finite family of pairwise distinct right-half-plane parameters. The normalized half-line state Gram used in `NB-095`--`NB-098` is

\[
G_F(r,s)
=
\frac{2\sqrt{a_ra_s}}
     {\lambda_r+\overline{\lambda_s}}.
\tag{2}
\]

Let `T_F` be the exact upper-triangular canonical-deflation matrix from `NB-095`, so

\[
C_F=T_F^*G_FT_F
\tag{3}
\]

is the canonical transformed state Gram. In particular its diagonal entries satisfy

\[
(T_F)_{kk}
=
\prod_{\ell<k}
\frac{\lambda_k+\overline{\lambda_\ell}}
     {\lambda_k-\lambda_\ell},
\tag{4}
\]

and the off-diagonal formula in `NB-098` is built from the same three kinds of quantities: `a_r`, differences `lambda_r-lambda_s`, and reflected sums `lambda_r+overline(lambda_s)`.

For any real `Gamma`, put

\[
\lambda_r^{(\Gamma)}:=\lambda_r+i\Gamma.
\tag{5}
\]

Then

\[
\Re\lambda_r^{(\Gamma)}=a_r,
\qquad
\lambda_r^{(\Gamma)}-\lambda_s^{(\Gamma)}
=\lambda_r-\lambda_s,
\tag{6}
\]

and

\[
\lambda_r^{(\Gamma)}
+\overline{\lambda_s^{(\Gamma)}}
=
\lambda_r+\overline{\lambda_s}.
\tag{7}
\]

Therefore every entry in both `(2)` and the exact triangular formulas is unchanged:

\[
\boxed{
G_{F+i\Gamma}=G_F,
\qquad
T_{F+i\Gamma}=T_F,
\qquad
C_{F+i\Gamma}=C_F.
}
\tag{8}
\]

The positive-diagonal Cholesky factor and all singular values are consequently unchanged as well. This is stronger than an asymptotic high-height statement: **absolute ordinate is a gauge variable for this canonical half-line conditioning problem**. Only relative ordinates and horizontal positions enter.

## 2. The bad three-state geometry survives at arbitrary zeta height

Fix

\[
0<a<\frac12,
\qquad c\in\mathbb R\setminus\{0\}.
\tag{9}
\]

For sufficiently small positive `epsilon`, so that also `0<a+c epsilon<1/2`, and any `Gamma>epsilon`, define

\[
\begin{aligned}
\lambda_1&=a+i(\Gamma+\epsilon),\\
\lambda_2&=a+c\epsilon+i\Gamma,\\
\lambda_3&=a+i(\Gamma-\epsilon).
\end{aligned}
\tag{10}
\]

This is exactly the `NB-098` transverse family translated by `i Gamma`. Hence `(8)` and `NB-098` give

\[
\boxed{
\kappa_2(C_F)
=\Theta_{a,c}(\epsilon^{-4})
}
\tag{11}
\]

uniformly in `Gamma`. In particular sending the cluster to arbitrarily large height provides no conditioning gain.

Now write

\[
\rho_j=\frac12+\lambda_j.
\tag{12}
\]

All three points lie in the right half of the critical strip and have positive ordinate. For each one form the usual formal zeta-symmetry quartet

\[
Q(\rho_j)
=
\{\rho_j,\overline{\rho_j},1-\rho_j,1-\overline{\rho_j}\}.
\tag{13}
\]

The union of these quartets is symmetric about both the real axis and the critical line, exactly as the nontrivial zeta zero set is. The positive-ordinate right-half member of each quartet is still the original `rho_j`, so the local right-half triple `(10)` survives unchanged. Thus the standard zeta involutions impose no algebraic relation that kills the transverse coefficient found in `NB-098`.

This statement is intentionally narrower than saying that symmetry cannot help in any representation. A new construction that deflates entire symmetry-closed blocks jointly may have different coordinates and could behave better. What `(13)` rules out is deriving a **subset-uniform bound for the existing canonical finite-set geometry** merely from the fact that actual zeros come with the standard companions. `NB-095` is formulated for an arbitrary fixed finite set of actual right-half zeros, so any uniform version of that route must still control the right-half subtriples themselves.

## 3. Even the global Riemann--von Mangoldt count can coexist with unbounded shear

The previous control can be made globally sparse. Let

\[
M(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi},
\tag{14}
\]

so the classical Riemann--von Mangoldt formula is

\[
N(T)=M(T)+O(\log T)
\tag{15}
\]

up to an immaterial bounded constant. For large `T`, `M` is strictly increasing. Choose a baseline synthetic divisor consisting of simple critical-line pairs

\[
\frac12\pm i\tau_n,
\qquad
M(\tau_n)=n
\tag{16}
\]

for all sufficiently large integers `n`, with finitely many initial points filled arbitrarily. Its positive-ordinate counting function satisfies

\[
N_0(T)=M(T)+O(1).
\tag{17}
\]

Now choose heights

\[
\Gamma_k=e^{k^2}
\tag{18}
\]

(after harmless perturbation if necessary to keep all ordinates distinct), choose `epsilon_k -> 0`, and at each `Gamma_k` adjoin the three translated points `(10)` together with their symmetry completions `(13)`. Each cluster contributes six positive-ordinate points: three on the right of the critical line and their three reflected partners on the left. Therefore, if

\[
K(T)=\#\{k:\Gamma_k\le T\},
\tag{19}
\]

then

\[
K(T)=O(\sqrt{\log T})
\tag{20}
\]

and the completed synthetic divisor satisfies

\[
\boxed{
N_{\rm syn}(T)
=M(T)+O(\sqrt{\log T})
=M(T)+O(\log T).
}
\tag{21}
\]

At the same time, the right-half canonical Gram associated with the `k`th selected triple has

\[
\kappa_2(C_{F_k})
=\Theta_{a,c}(\epsilon_k^{-4})
\longrightarrow\infty.
\tag{22}
\]

All points can be chosen pairwise distinct, so simplicity alone does not change this control.

There is a stronger abstract version. Let `D(T)` be any nondecreasing unbounded function prescribing a global allowance for right-half off-critical points. Choose the heights inductively so that

\[
D(\Gamma_k)\ge 3k,
\qquad
\log\Gamma_k\ge k^2.
\tag{23}
\]

Then the number of selected right-half points below `T` is at most `D(T)` while the perturbation of the total zero count remains `O(sqrt(log T))`. The `epsilon_k` may still tend to zero arbitrarily fast. Hence **any purely global zero-count bound with an unbounded budget is noncoercive for uniform canonical conditioning**: arbitrarily ill-conditioned local triples can be made sparse enough to fit underneath it.

This includes, at the level of mechanism, ordinary zero-density information that only limits how many off-critical zeros occur globally. Such estimates can become relevant only if they are strengthened into a local exclusion or combined with another ingredient that prevents three offending zeros from clustering in the transverse geometry `(10)`.

## 4. What source-specific input is actually left

`NB-098` showed that generic right-half-plane geometry does not control collective shear. The present matched controls remove three immediate ways of rescuing that argument: high ordinate, standard zeta symmetry, and global sparsity of off-critical zeros. The surviving problem is local.

A conditioning theorem along the current representation would need a zeta-specific statement that forbids or quantitatively suppresses transverse clusters at the scale on which their horizontal offsets and ordinate gaps interact. Schematically, one needs information coupling the tuple

\[
(\beta_r-\tfrac12,\gamma_r)
\tag{24}
\]

across several nearby zeros, not merely a count of how many such tuples occur below height `T`. Alternatively one can change the representation — for example, a genuinely symmetry-closed confluent block system — or bypass uniform state conditioning in the final target conversion.

This also sharpens the role of zero-density estimates in the line. A stronger exponent in a global count is not by itself the missing theorem as long as the permitted number of off-critical zeros still tends to infinity. To attack the collective-shear obstruction it must yield **local spacing/transversality information** or be coupled to a mechanism that does.

## 5. Prior-art and novelty boundary

The symmetry used in `(13)` and the Riemann--von Mangoldt count `(15)` are classical zeta facts; no novelty is claimed for either. NIST DLMF §25.10 records the symmetry of nontrivial zeta zeros about the real axis and the critical line, and Titchmarsh--Heath-Brown, *The Theory of the Riemann Zeta-function*, Chapter 9, is a standard source for the global zero-counting formula. The latter book is already anchored in `SOURCES.md` for this line.

The closest contemporary Nyman-specific boundary found in the prior-art audit remains T. A. Ziad, *A Gram-Spectral Autopsy of the BNBD Inversion Problem* (2026), which isolates a finite Blaschke skeleton from an arithmetic Gram defect but does not analyze the canonical deflation shear of `NB-096`--`NB-098`, common-vertical-translation invariance of that shear, or sparse zeta-symmetric matched controls for its conditioning.

The line-local contribution here is therefore not a new theorem about zeta zero distribution. It is the exact negative implication: **the canonical collective-shear obstruction survives every constraint encoded solely by absolute height, standard quartet symmetry, simplicity, and an arbitrarily restrictive but still unbounded global off-critical count.**

## 6. Boundary conditions and falsification tests

This finding does **not** assert that the actual zeros of zeta realize `(10)`. The synthetic divisor is not required to arise from an Euler product, the zeta explicit formula, or an entire function with all of xi's analytic structure. Those omitted source constraints are precisely where a successful local exclusion could live.

It also does not rule out a symmetry-closed change of coordinates. The argument uses the canonical finite-set deflation of `NB-095`--`NB-098`; a block representation that includes conjugate or reflected companions before forming the conditioning problem must be audited separately.

The decisive way to overturn the negative boundary for the actual-zeta route is therefore to prove a local theorem unavailable to the synthetic control: for example, a quantitative restriction on several nearby off-critical zeros that makes the `NB-098` transverse coefficient uniformly bounded, or a block-deflation identity whose conditioning remains bounded even when the selected right-half subtriple has `(11)`. A purely global improvement of `N(sigma,T)` that still permits an unbounded sparse subsequence cannot do so by itself.

## Consequence

The generic-Blaschke conditioning program is now narrowed one step further. After `NB-096` removed raw Cauchy volume collapse, `NB-097` removed bad pivots and pairwise crowding, and `NB-098` exposed genuine three-state collective shear, this finding shows that the first coarse zeta-specific constraints do not repair that shear. The next useful input must be **local zero geometry, a different symmetry-aware state representation, or target conversion without uniform conditioning**; high height and global zero-density bookkeeping are dead ends on their own.
