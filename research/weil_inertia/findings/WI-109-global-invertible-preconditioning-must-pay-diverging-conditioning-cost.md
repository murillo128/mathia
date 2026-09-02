# WI-109 — Global invertible preconditioning must pay the diverging full-packed conditioning cost

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It closes the uniformly well-conditioned part of the two global linear escapes left open by WI-108. After arbitrary target-local processing, neither an invertible source-side transformation nor an invertible cross-target transformation, nor any combination of the two, can turn the WI-107 full-packed counterfamily into a uniformly coercive system unless the transformations themselves acquire a condition-number product at least as large as the conditioning defect they are trying to remove.

The statement is sharp. Arbitrary source whitening can of course make any full-row-rank concatenation perfectly conditioned, but its condition number is **exactly** the condition number of the concatenation. Thus global linear reparametrization does not destroy the WI-108 obstruction for free; it merely transfers the bad conditioning into the reparametrization. A genuinely new analytic use of source-side or cross-target mixing must therefore justify access to this diverging anisotropy, or use a noninvertible/rectangular selection mechanism not covered by the theorem.

Let

\[
B:H_{\rm tar}\to H_{\rm src}
\tag{1}
\]

be any finite-dimensional full-row-rank operator, and write

\[
r(B):=\frac{\sigma_{\min}(B)}{\sigma_{\max}(B)},
\qquad
\kappa_2(B)=r(B)^{-1}.
\tag{2}
\]

For arbitrary invertible operators

\[
L:H_{\rm src}\to H_{\rm src},
\qquad
R:H_{\rm tar}\to H_{\rm tar},
\tag{3}
\]

one has the exact condition-number transport inequality

\[
\boxed{
\kappa_2(LBR)
\ge
\frac{\kappa_2(B)}{\kappa_2(L)\kappa_2(R)}
}
\tag{4}
\]

or equivalently

\[
\boxed{
r(LBR)
\le
\kappa_2(L)\kappa_2(R)\,r(B).
}
\tag{5}
\]

Consequently, if the transformed system is required to have a fixed relative source gap

\[
r(LBR)\ge c>0,
\tag{6}
\]

then necessarily

\[
\boxed{
\kappa_2(L)\kappa_2(R)
\ge c\,\kappa_2(B)
=\frac{c}{r(B)}.
}
\tag{7}
\]

Apply this after the arbitrary target-local right processing already allowed by WI-108. On the simultaneous full-packed family of WI-107, put

\[
B=[\,G_1C_1\;\cdots\;G_JC_J\,],
\tag{8}
\]

where every `C_j` is an arbitrary target-local finite-dimensional linear map and suppose `B` retains full source row rank. WI-108 proves

\[
r(B)
\le
\varepsilon_{p,J}
:=
\sqrt{\frac{3(J-1)\Delta}{2p}},
\qquad
\Delta=q_J-q_1=O(J\log p).
\tag{9}
\]

Hence every pair of invertible global transformations satisfying (6) must obey

\[
\boxed{
\kappa_2(L)\kappa_2(R)
\ge
c\sqrt{\frac{2p}{3(J-1)\Delta}}.
}
\tag{10}
\]

In particular, for

\[
J=o\!\left(\sqrt{\frac{p}{\log p}}\right),
\tag{11}
\]

the right-hand side diverges, and using `Delta=O(J log p)` gives

\[
\boxed{
\kappa_2(L)\kappa_2(R)
=\Omega_c\!\left(
\frac1J\sqrt{\frac{p}{\log p}}
\right)
\longrightarrow\infty.
}
\tag{12}
\]

Thus every uniformly well-conditioned invertible global source/cross-target reparametrization leaves the relative singular gap tending to zero on the same arithmetic counterfamily. If the cost is split between source and target sides, at least one transformation must satisfy

\[
\boxed{
\max\{\kappa_2(L),\kappa_2(R)\}
\ge
\sqrt{c}\left(
\frac{2p}{3(J-1)\Delta}
\right)^{1/4}.
}
\tag{13}
\]

For fixed `J`, this is at least order `(p/log p)^(1/4)` for one side, while the product cost is at least order `sqrt(p/log p)`.

## 1. The global transport inequality is elementary and exact

For compatible full-rank factors the two-norm condition number is submultiplicative. Since `L` and `R` are invertible and `B` has full row rank,

\[
B=L^{-1}(LBR)R^{-1}.
\tag{14}
\]

The standard singular-value product inequalities therefore give

\[
\begin{aligned}
\kappa_2(B)
&\le
\kappa_2(L^{-1})\,
\kappa_2(LBR)\,
\kappa_2(R^{-1})\\
&=
\kappa_2(L)\,
\kappa_2(LBR)\,
\kappa_2(R),
\end{aligned}
\tag{15}
\]

which is (4). No Ramanujan structure, kernel preservation, block-diagonality, or compatibility with the individual `K_j` is used here.

This last point is what makes the statement stronger than WI-108. A global target map `R` may have completely off-diagonal blocks and may mix columns from all targets before the singular-value test. Such mixing need not preserve any individual left kernel `K_j`. Equation (4) bypasses that issue: if `R` is an invertible reparametrization of the full combined target space, the original bad condition number can improve by at most the condition number paid by `R`, together with any source-side cost in `L`.

The same conclusion can be written directly in terms of singular values. Applying

\[
\sigma_{\max}(XY)\le\sigma_{\max}(X)\sigma_{\max}(Y),
\qquad
\sigma_{\min}(XY)\ge\sigma_{\min}(X)\sigma_{\min}(Y)
\tag{16}
\]

to the inverse factorization (14) yields (15). The rectangular nature of `B` causes no problem because full row rank gives a positive smallest nonzero singular value and the outer factors are square and invertible.

## 2. WI-108 therefore survives every bounded-condition global reparametrization

WI-108 permits arbitrary maps `C_j` acting independently on each target block, including nonscalar diagonal weights, changes of target basis, local whitening, and singular local compression. Its common-near-kernel argument says that either the resulting `B` in (8) is source-rank deficient already, or it satisfies (9).

Assume the latter. After **any** arithmetic-dependent invertible global source map `L` and any arithmetic-dependent invertible global cross-target map `R`, equation (5) gives

\[
r(LBR)
\le
\kappa_2(L)\kappa_2(R)
\sqrt{\frac{3(J-1)\Delta}{2p}}.
\tag{17}
\]

If, for example,

\[
\kappa_2(L)\le K_L,
\qquad
\kappa_2(R)\le K_R
\tag{18}
\]

with constants independent of the arithmetic scale, then under (11)

\[
r(LBR)
=O\!\left(
K_LK_R J\sqrt{\frac{\log p}{p}}
\right)
\longrightarrow0.
\tag{19}
\]

This closes the simplest global-preconditioner loophole left by WI-108. Merely allowing source coordinates to change, or allowing targets to mix globally, does not create quantitative transversality if those coordinate changes are required to remain uniformly stable.

The conclusion is stronger than an invariance statement under unitary transformations. Unitarians have condition number one and preserve all singular values exactly, but (17) allows arbitrary nonnormal or anisotropic invertible transformations whose condition numbers may depend on every modulus and on the observation length. Their only restriction is the amount of conditioning they themselves introduce.

## 3. Whitening shows that the conditioning price is the exact boundary

A blanket statement that source-side preprocessing can never rescue the counterfamily would be false. For every full-row-rank `B`, define the positive-definite source whitening operator

\[
L_0=(BB^*)^{-1/2}.
\tag{20}
\]

Then

\[
(L_0B)(L_0B)^*=I,
\tag{21}
\]

so every nonzero singular value of `L_0B` equals one and

\[
\kappa_2(L_0B)=1.
\tag{22}
\]

But the eigenvalues of `L_0` are the reciprocals of the singular values of `B`, hence

\[
\boxed{
\kappa_2(L_0)=\kappa_2(B).
}
\tag{23}
\]

Therefore the lower bound (7) with `c=1` is attained exactly by source whitening with `R=I`:

\[
\boxed{
\inf_{\substack{L,R\ {m invertible}\\
\kappa_2(LBR)=1}}
\kappa_2(L)\kappa_2(R)
=
\kappa_2(B).
}
\tag{24}
\]

The lower bound is (4), and (20)--(23) give equality. There is an analogous target-side realization. If

\[
B=U[\Sigma\;0]V^*
\tag{25}
\]

is a singular-value decomposition, take

\[
R_0
=V\,\operatorname{diag}(\Sigma^{-1},cI)\,V^*
\tag{26}
\]

with `c` chosen between `1/sigma_max(B)` and `1/sigma_min(B)`. Then `BR_0` has all nonzero singular values equal to one and

\[
\kappa_2(R_0)=\kappa_2(B).
\tag{27}
\]

Thus the theorem identifies a **price**, not an absolute impossibility. Pure linear algebra always permits perfect global conditioning, but the least condition-number product needed to do so is exactly the original condition number. On the WI-107/WI-108 counterfamily that price diverges at least as in (10)--(12).

This sharpness check is load-bearing for the interpretation. It shows that no stronger obstruction to arbitrary invertible preconditioning can follow from condition numbers alone. A future analytic argument may legitimately use a highly anisotropic transformation, but then the mechanism must explain why the arithmetic provides that transformation together with enough quantitative control to absorb its diverging norm/inverse-norm cost.

## 4. Boundaries and falsification controls

The result applies to invertible global reparametrizations of the existing source and combined target spaces. It deliberately does **not** rule out a genuinely noninvertible or rectangular cross-target selection. A singular square target map can still leave `BR` full row rank while discarding some target directions; a rectangular map can select a lower-dimensional mixed subspace. In the full-space condition-number convention such a singular map has infinite condition number, so (7) becomes formally vacuous rather than a quantitative obstruction on its surviving range. A partial isometry may also change the ratio by deleting directions instead of reparametrizing them. Any claim involving such a selection must therefore be analyzed as a different information-reduction mechanism, not smuggled into (4).

Likewise, the result does not assert that the synchronized CRT counterfamily occurs with positive analytic density in the zeta problem. WI-105--WI-108 and the present finding are uniform finite-window obstructions: they falsify theorems that would derive a scale-independent coercive gain from the full-packed algebraic interface alone.

The theorem also does not prevent positive-slack information away from exact full packing, additional arithmetic normalization, or a target count at or above the first scale not excluded by WI-107. Those mechanisms can alter the input operator `B` before the conditioning argument and may supply information absent from the countermodel.

Finally, no conclusion about the uncertified zeta-zero complement follows merely from (10). The finding constrains a proposed route for extracting quantitative information from simultaneous Ramanujan defect blocks; it does not identify multiple critical zeros, off-line pairs, or proof slack.

## 5. Prior art and novelty boundary

The linear-algebra content of (4) is classical. The singular-value product inequalities and two-norm condition-number submultiplicativity are standard; see R. A. Horn and C. R. Johnson, *Matrix Analysis*, Cambridge University Press, 1985, and *Topics in Matrix Analysis*, Cambridge University Press, 1991. The source-whitening construction (20) is the usual polar/SVD normalization of a full-row-rank operator.

James W. Demmel, **The Condition Number of Equivalence Transformations That Block Diagonalize Matrix Pencils**, *SIAM Journal on Numerical Analysis* 20:3 (1983), 599--610, DOI `10.1137/0720040`, is closer structural prior art. Demmel proves in a block-diagonalization setting that nearly overlapping prescribed subspaces force the equivalence transformations themselves to become ill-conditioned, with the best conditioning governed by principal-angle data. WI-106 already anchored that paper for the `csc(theta)` phenomenon. The present use is the elementary global condition-number transport specialization after WI-108, not a claim that the underlying preconditioning principle is new.

A targeted audit around left/right preconditioning, condition-number minimization, principal-angle conditioning, equivalence transformations, and block/fusion-frame reparametrization found the classical conditioning literature above. It did not locate the arithmetic specialization (10)--(12) to simultaneous finite-window Ramanujan full-packing defects; that negative search is **not** a priority claim. The durable contribution here is the exact consequence for the current Mathia obstruction chain and the sharp identification of what the remaining global-linear escape must pay.

## 6. Program consequence

WI-108 left source-side transformations and genuinely cross-target right mixing as possible ways to evade target-local kernel preservation. This finding separates the live part of those escapes from the merely coordinate-theoretic part.

If a proposed covariance or inertia improvement uses only an **invertible** global change of source or target coordinates with bounded condition number, the route is closed by (17)--(19). If it uses an invertible transformation strong enough to produce a fixed relative singular gap, then (10) quantifies the diverging anisotropy that the analytic argument must control. For perfect whitening, equation (24) shows that the full original condition number must simply reappear in the transformation itself.

The genuinely open linear escape is therefore narrower: a noninvertible/rectangular cross-target selection whose surviving subspace is justified by the arithmetic, or an analytically natural transformation with enough additional weighted norm control that its diverging condition cost can be paid. Together with positive-slack information and larger target families, those are qualitatively new inputs; a stable invertible reparametrization of the already-available full-packed data is not.