# WI-154 — pointwise-PSD matrix one-delta bounds collapse to the scalar extremizer

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`.

WI-153 closes the support-one **scalar** Lamzouri-form route by observing that the real two-point census forces the real-gap kernel into the nonnegative one-delta class solved sharply by Carneiro--Chandee--Littmann--Milinovich (CCLM). WI-144 had already closed coherent positive-Hilbert and PSD-spectral/Frobenius multi-window lifts, but deliberately left more general matrix-valued observables open.

There is a further exact closure between those results. Let

\[
R:\mathbb R\to\operatorname{Herm}_d
\]

be continuous, even, entrywise integrable, and **pointwise positive semidefinite**,

\[
R(x)\succeq0\qquad(x\in\mathbb R),
\tag{1}
\]

with entrywise Fourier transform supported in `[-1,1]`. Define the matrix one-delta functional

\[
\mathcal M(R):=
\int_{\mathbb R}R(x)
\left[1-
\left(\frac{\sin\pi x}{\pi x}\right)^2
\right]dx.
\tag{2}
\]

Then the sharp scalar Montgomery--Taylor/CCLM constant automatically amplifies to Loewner order:

\[
\boxed{
\mathcal M(R)\succeq
m_{\rm MT}R(0),
\qquad
m_{\rm MT}:=
\frac1{\sqrt2}\cot\frac1{\sqrt2}-\frac12.
}
\tag{3}
\]

Equivalently, if `Phi=widehat R`, then

\[
\boxed{
\Phi(0)+\int_{-1}^{1}|t|\Phi(t)\,dt
\succeq
C_{\rm MT}R(0),
\qquad C_{\rm MT}=1+m_{\rm MT}.
}
\tag{4}
\]

The Fourier-side matrix `Phi(t)` is allowed to be pointwise indefinite. Thus (3)--(4) are not consequences of the positive spectral-density/Frobenius cone treated in WI-144. They say that **positivity of the matrix kernel on real gaps alone is already enough** to prevent a support-one matrix lift from lowering the one-delta cost when the final objective is consumed in Loewner order or by a positive linear functional.

Moreover the equality case is rigid. Let `R_MT` denote the unique normalized scalar CCLM one-delta extremizer, with `R_MT(0)=1`. Equality in (3),

\[
\mathcal M(R)=m_{\rm MT}R(0),
\tag{5}
\]

holds if and only if

\[
\boxed{R(x)=R_{\rm MT}(x)R(0)\qquad(x\in\mathbb R).}
\tag{6}
\]

Hence a matrix-valued support-one kernel can be sharp only by carrying a **fixed PSD channel factor times the scalar extremizer**. Noncommuting or genuinely varying channel geometry cannot survive at equality within the pointwise-PSD real-gap cone.

No new zeta-zero proportion is claimed. The result is a structural barrier for a natural matrix escape left after WI-144 and WI-153. It does not show that every matrix-valued zero-side certificate is pointwise PSD on real gaps, and it does not cover sign-indefinite matrix statistics, nonlinear joint-profile constraints, zeta-restricted configuration classes, higher correlations, or support beyond one.

## 1. Scalar compression gives the Loewner inequality exactly

Fix `v in C^d` and define

\[
r_v(x):=v^*R(x)v.
\tag{7}
\]

By (1), `r_v` is a continuous even nonnegative scalar function. Entrywise integrability of `R` gives `r_v in L^1(R)`, and the support hypothesis gives

\[
\operatorname{supp}\widehat r_v\subset[-1,1].
\tag{8}
\]

Put

\[
a_v:=r_v(0)=v^*R(0)v\ge0.
\tag{9}
\]

If `a_v>0`, then `r_v/a_v` is exactly an admissible normalized one-delta function in the sense used in CCLM Corollary 14. Their sharp theorem therefore gives

\[
\int_{\mathbb R}\frac{r_v(x)}{a_v}
\left[1-
\left(\frac{\sin\pi x}{\pi x}\right)^2
\right]dx
\ge m_{\rm MT}.
\tag{10}
\]

Multiplying by `a_v`,

\[
v^*\mathcal M(R)v
\ge m_{\rm MT}v^*R(0)v.
\tag{11}
\]

If `a_v=0`, the same inequality is immediate because the weight in (2) and `r_v` are both nonnegative. Thus (11) holds for every `v`, which is exactly the Loewner inequality (3).

This proof uses no operator-valued extremal theorem. It is the scalar CCLM theorem applied to every quadratic compression. In particular, arbitrary noncommutativity among the values `R(x)` cannot improve the constant as long as each `R(x)` is PSD.

Every positive linear functional `omega` therefore inherits

\[
\omega(\mathcal M(R))
\ge m_{\rm MT}\,\omega(R(0)).
\tag{12}
\]

If the matrix kernel is normalized by `R(0)=I`, every normalized positive state pays at least `m_MT`; after adding back the diagonal contribution, the corresponding support-one cost is at least `C_MT`, exactly as in WI-153. A non-positive scalarization is outside this consequence.

## 2. Fourier-side form

With Fourier convention

\[
\Phi(t)=\widehat R(t)
=\int_{\mathbb R}R(x)e^{-2\pi ixt}\,dx,
\tag{13}
\]

support in `[-1,1]` and Fourier inversion give

\[
R(0)=\int_{-1}^{1}\Phi(t)\,dt.
\tag{14}
\]

The Fourier transform of `(sin pi x/(pi x))^2` is `(1-|t|)_+`. Hence entrywise Fourier inversion/Parseval gives

\[
\begin{aligned}
\mathcal M(R)
&=\Phi(0)
-\int_{-1}^{1}(1-|t|)\Phi(t)\,dt\\
&=\Phi(0)-R(0)
+\int_{-1}^{1}|t|\Phi(t)\,dt.
\end{aligned}
\tag{15}
\]

Substituting (15) into (3) proves (4). The important boundary is visible here: nothing in the proof requires `Phi(t)\succeq0`. A pointwise-PSD real-gap matrix may have a signed/indefinite matrix Fourier profile, yet positive-state one-delta optimization still cannot beat `C_MT`.

This is strictly different from WI-144's Frobenius obstruction. WI-144 starts from a PSD **spectral** density and proves that particular quadratic scalarizations have nonnegative Fourier transform. Here the spectral matrix may be indefinite; what blocks improvement is instead the fact that every real-gap quadratic compression is already a scalar CCLM-admissible function.

## 3. Equality rigidity

Assume equality (5). Let

\[
D:=\mathcal M(R)-m_{\rm MT}R(0).
\]

Section 1 proves `D\succeq0`, so (5) means every scalar compression saturates its lower bound.

If `a_v>0`, equality in (10) and uniqueness of the normalized CCLM extremizer imply

\[
r_v(x)=a_vR_{\rm MT}(x)
\qquad(x\in\mathbb R).
\tag{16}
\]

If `a_v=0`, then equality gives

\[
0=v^*\mathcal M(R)v
=\int r_v(x)w(x)\,dx,
\qquad
w(x)=1-\left(\frac{\sin\pi x}{\pi x}\right)^2.
\tag{17}
\]

Here `r_v>=0`, while `w(x)>0` for every `x!=0`. Continuity therefore forces `r_v(x)=0` for all real `x`, so (16) also holds in the zero-normalization case.

Consequently, for every vector `v` and every real `x`,

\[
v^*R(x)v
=R_{\rm MT}(x)v^*R(0)v.
\tag{18}
\]

Polarization of Hermitian quadratic forms gives (6). Conversely, every kernel of the form (6) with `R(0)\succeq0` is admissible whenever the scalar extremizer is, and saturates (3). Thus (6) is the complete matrix equality class.

A faithful positive scalarization, such as the ordinary trace, can also detect this rigidity: since `D\succeq0`, `Tr D=0` implies `D=0` and hence (6). A non-faithful state may saturate on only the subspace it sees, so no stronger statement is asserted for arbitrary positive functionals.

## 4. Stress tests and exact boundary

The pointwise PSD hypothesis is load-bearing. A Hermitian matrix statistic may be sign-indefinite for some real gaps while still entering a valid global zero-side inequality through cancellations, block inertia, or another nonlinear constraint. Then some compression `r_v` is not CCLM-admissible and the argument above does not apply.

Likewise, the theorem only controls a one-delta **linear** matrix cost. Retaining several matrix observables jointly, imposing nonlinear incidence constraints before scalarization, or using an indefinite coefficient to combine channels can keep information that every positive state discards. Such a mechanism would be genuinely outside the scalar-compression closure rather than another matrix parametrization of the same cone.

The support-one assumption is also essential to the exact constant quoted here. Wider Fourier support changes the extremal problem and, in the zeta application, requires arithmetic input beyond the unconditional support-one pair-correlation interface already audited in this line.

Finally, (3) is not a ceiling on the established Gram-defect improvements above `H_MT`. Those improvements retain local Gram geometry and nonlinear spectral defect before collapsing to a one-delta pair cost. WI-154 only rules out gaining by replacing the scalar admissible real-gap kernel with a pointwise-PSD matrix kernel and then consuming that matrix through Loewner order or a positive scalar functional.

## 5. Prior art and novelty audit

The sharp scalar input is classical. Emanuel Carneiro, Vorrapan Chandee, Friedrich Littmann and Micah B. Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function*, J. Reine Angew. Math. 725 (2017), 143--182, arXiv:1406.5462, §3.5 and Corollary 14, solve the relevant one-delta problem and characterize the normalized extremizer; they trace the original zeta extremal calculation to Montgomery--Taylor and the broader treatment to Iwaniec--Luo--Sarnak. WI-153 already anchors this theorem and identifies its exact support-one cost with Lamzouri's `C_MT`.

Matrix/operator-valued positive-definite Fourier theory and scalar-compression arguments are classical functional analysis. The present proof does not claim a new operator-valued extremal theory: once (1) is assumed, (3) is an immediate but exact amplification of the scalar sharp theorem through all quadratic forms.

A targeted audit of the current `weil_inertia` frontier shows a genuine scope distinction. WI-144 closes common positive-Hilbert features and PSD-spectral/Frobenius lifts but explicitly leaves sign-indefinite matrix scalarizations and more general matrix observables open. WI-153 closes the bounded-depth signed **scalar** support-one objective and explicitly lists matrix/multi-kernel observables as a surviving route. The present deduction closes the natural intermediate subclass in which the matrix real-gap kernel itself remains pointwise PSD, even when its Fourier-side matrix is indefinite.

Targeted literature searches around matrix-valued one-delta/Caratheodory--Fejer--Turan extremals and matrix-valued positive-definite extremal problems located general matrix/positive-definite Fourier theory and scalar/multivariate Turan variants, but no source needed for or materially stronger than the compression argument above. This is a novelty boundary for the Mathia corpus, not a priority claim.

## Research consequence

After WI-153 it is not enough to say that a future support-one improvement is "matrix-valued." If its real-gap kernel is pointwise PSD and the arithmetic objective is evaluated by positive states, each channel direction separately lies in the same sharp CCLM cone and the Montgomery--Taylor cost survives unchanged. Equality is even more restrictive: all channels become a fixed PSD factor multiplying the scalar extremizer.

Therefore a genuinely new matrix route must retain structure that violates at least one load-bearing hypothesis of WI-154: a sign-indefinite real-gap matrix statistic backed by a valid zero-side inequality, a nonlinear joint constraint that cannot be tested direction-by-direction, a zeta-specific restriction smaller than universal admissibility, higher-order correlations, or arithmetic access beyond support one. This sharpens the surviving matrix direction without changing the current certified simple-critical proportion.