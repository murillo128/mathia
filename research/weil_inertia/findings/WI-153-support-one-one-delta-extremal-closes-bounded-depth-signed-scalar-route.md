# WI-153 — the one-delta extremal closes the bounded-depth signed support-one scalar route

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`.

The bounded-depth universal scalar census studied in WI-145--WI-152 still permits a signed spectral profile `phi` at finite depth `B`: WI-151 gives a pointwise negative floor and WI-152 confines total negative mass to an `O(phi(0)/B)` boundary layer, but WI-152 explicitly leaves open an escape through a growing central spike `phi(0)`. For the **support-one arithmetic interface**, that escape is in fact irrelevant. The real two-point tests already force the Fourier transform `H=widehat phi` into the classical nonnegative one-delta admissible class of Carneiro--Chandee--Littmann--Milinovich (CCLM). Their sharp extremal theorem then implies that the pair-correlation cost cannot fall below the Montgomery--Taylor constant, even though `phi` itself may remain signed.

Precisely, assume `B>0`, `phi : R -> R` is continuous and even,

\[
\operatorname{supp}\phi\subset[-1,1],\qquad
\int_{\mathbb R}\phi(t)\,dt=1,
\tag{1}
\]

and put

\[
H(z)=\int_{\mathbb R}\phi(t)e^{-2\pi i zt}\,dt.
\tag{2}
\]

Assume the full bounded-depth Lamzouri-form scalar census

\[
s(\mathcal Z)
\ge
2|\mathcal Z|-\sum_{z,w\in\mathcal Z}H(z-w)
\tag{3}
\]

for every nonempty finite conjugation-invariant multiset `Z` contained in `|Im z|<=B`. Then the support-one pair-correlation functional

\[
C(\phi):=
\phi(0)+2\int_0^1 t\phi(t)\,dt
\tag{4}
\]

satisfies the sharp lower bound

\[
\boxed{
C(\phi)
\ge
C_{\rm MT}
:=
\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}
=
1.327499296320588\ldots .
}
\tag{5}
\]

Consequently any zero-count argument that factors completely through this one-scalar universal census and the ordinary support-one pair-correlation cost has ceiling

\[
\boxed{
2-C(\phi)
\le
H_{\rm MT}
:=
\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}
=
0.672500703679411\ldots .
}
\tag{6}
\]

This is a finite-depth obstruction: no limit `B -> infinity`, no estimate for `phi(0)`, and no proof that `phi>=0` are required. It therefore closes the support-one signed-scalar central-spike escape left open by WI-152. It does **not** cap the full Weil-inertia program: the already established Gram-defect improvements in this line retain matrix/local geometric information not present in the collapsed scalar functional (4), and multi-profile, higher-order, zeta-restricted, or justified support-greater-than-one interfaces remain outside the theorem.

## 1. Finite-depth two-point universality puts `H` in the CCLM admissible cone

The key input from the zero-side census is much cheaper than the phase-masked constructions of WI-149--WI-152. Take two distinct simple real points `{0,x}`. They form a conjugation-invariant multiset at every positive depth `B`. Substituting them into (3) gives the exact WI-146/WI-152 consequence

\[
\boxed{H(x)\ge0\qquad(x\in\mathbb R).}
\tag{7}
\]

Because `phi` is real and even, `H` is real and even on the real axis. The Fejer argument recorded in WI-152 applies verbatim: for

\[
w_R(x)=\left(1-\frac{|x|}{R}\right)_+,
\]

monotone convergence and the Fejer approximate identity give

\[
\boxed{
H\in L^1(\mathbb R),
\qquad
\int_{\mathbb R}H(x)\,dx=\phi(0).
}
\tag{8}
\]

Since `H in L^1`, `phi in L^1`, and `phi` is continuous, Fourier inversion gives

\[
\widehat H(t)=\phi(-t)=\phi(t).
\tag{9}
\]

Therefore

\[
\operatorname{supp}\widehat H\subset[-1,1].
\tag{10}
\]

Finally,

\[
H(0)=\int_{\mathbb R}\phi(t)\,dt=1.
\tag{11}
\]

Thus `R:=H` is exactly a **nonnegative admissible function** in the sense used by CCLM: `R in L^1(R)`, its Fourier transform is supported in `[-1,1]`, it is nonnegative on the real axis, and `R(0)>=1` (here equality holds). Notice what has and has not happened. Finite-depth universality has not forced `phi>=0`; that requires stronger configuration families as in WI-147--WI-151. It has instead forced its Fourier transform `H` into a classical sharp extremal cone, and that is already enough for the support-one arithmetic cost.

## 2. The CCLM one-delta theorem is exactly the missing sharp inequality

Carneiro, Chandee, Littmann and Milinovich define, for an admissible function `R`,

\[
M(R)
:=
\int_{\mathbb R}
R(x)
\left[
1-
\left(\frac{\sin\pi x}{\pi x}\right)^2
\right]dx.
\tag{12}
\]

Their Corollary 14 solves the one-delta problem: for every nonnegative admissible `R` with `R(0)>=1`,

\[
\boxed{
M(R)
\ge
m_{\rm MT}
:=
\frac1{\sqrt2}\cot\frac1{\sqrt2}-\frac12
=
0.327499296320588\ldots,
}
\tag{13}
\]

with an explicitly characterized unique extremizer. This is the reproducing-kernel formulation of the Montgomery--Taylor extremal calculation; CCLM themselves attribute the original one-delta result to Montgomery--Taylor and note the more general treatment in Iwaniec--Luo--Sarnak.

Apply (13) to `R=H`. The Fourier transform of

\[
\left(\frac{\sin\pi x}{\pi x}\right)^2
\]

under the convention (2) is the triangular function `(1-|t|)_+`. Hence Parseval/Fourier inversion and (9)--(10) give

\[
\begin{aligned}
\int_{\mathbb R}H(x)
\left(\frac{\sin\pi x}{\pi x}\right)^2dx
&=
\int_{-1}^{1}\phi(t)(1-|t|)\,dt\\
&=
1-2\int_0^1 t\phi(t)\,dt.
\end{aligned}
\tag{14}
\]

Using (8),

\[
\begin{aligned}
M(H)
&=
\phi(0)-
\left(1-2\int_0^1t\phi(t)\,dt\right)\\
&=
C(\phi)-1.
\end{aligned}
\tag{15}
\]

Combining (13) and (15) proves

\[
C(\phi)\ge1+m_{\rm MT}
=
\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}
=C_{\rm MT},
\tag{16}
\]

which is (5). The obstruction is therefore not an asymptotic estimate or a comparison of nearby kernels: it is an exact identification of the signed scalar optimization with a classical sharp extremal problem after the real two-point census has imposed `H>=0`.

## 3. Connection to Lamzouri's support-one proof

Youness Lamzouri's arXiv:2609.02882v1 gives a new unconditional proof of the `67.25%` simple-critical lower bound. Proposition 2.1 is the concrete finite-multiset Hilbert-space inequality from which (3) is abstracted. In Section 3, Lamzouri applies the unconditional Montgomery pair-correlation formula to real even test functions supported in `[-1,1]`; the resulting main coefficient is exactly of the form

\[
f(0)+2\int_0^1\alpha f(\alpha)\,d\alpha.
\tag{17}
\]

For his square-kernel construction he obtains

\[
C_{\rm MT}
=
\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2},
\]

and Remark 3.4 explicitly invokes CCLM Corollary 14 to state that this constant is optimal for his method. Thus the extremal constant itself and the one-delta optimization are established prior art.

The Mathia deduction here is narrower and different: WI-145--WI-152 had enlarged the search space to **signed** spectral profiles satisfying the same universal finite-multiset scalar census at only a fixed bounded off-real depth. The new bridge shows that, once support one is imposed, this enlargement buys no improvement in the pair-correlation objective. The reason is not that the signed profile is secretly nonnegative. Rather, its transform `H` is already nonnegative from real two-point tests and therefore falls directly under the CCLM extremal theorem.

## 4. Stress tests and equality boundary

### Signed `phi` is genuinely allowed

No step uses `phi(t)>=0`. The CCLM positivity hypothesis is imposed on `R=H`, and (7) supplies exactly that positivity from the universal scalar census. The theorem therefore addresses the finite-depth signed regime that WI-147 cannot reach by its unbounded-depth positivity argument.

### No hidden `B -> infinity` passage

Only real two-point configurations are used to derive (7), so every fixed `B>0` is sufficient. The bounds of WI-151 and WI-152 are not needed. In particular, the `phi(0)=Omega(B)` central-spike escape from the `L^1` estimate in WI-152 cannot improve the support-one cost: regardless of the spike height, `H` remains a feasible CCLM one-delta function and (13) applies.

### Fourier regularity is sufficient

Compact support makes `phi` integrable, while (7) plus the Fejer argument gives `H in L^1`; continuity of `phi` gives pointwise Fourier inversion. Hence `H` satisfies the actual CCLM admissibility requirements rather than only a distributional surrogate. No Paley--Wiener extrapolation beyond those hypotheses is needed for the inequality.

### Sharpness does not imply scalar-census equality

CCLM characterize the unique one-delta extremizer, and Lamzouri/Montgomery--Taylor realize the same optimal constant through the classical support-one construction. This proves sharpness of the **one-delta objective**. It does not by itself prove that the CCLM extremizer, viewed through an arbitrary inverse transform `phi`, saturates every bounded-depth finite-multiset inequality (3). The present finding needs only the lower bound (13), so no such stronger equality claim is made.

### The barrier is intentionally narrower than the current Weil-inertia record

The conclusion (6) must not be read as a ceiling on matrix inertia, Gram-defect refinements, local gap geometry, multiple kernels, or higher-order statistics. Those methods do not factor through the single number `C(phi)` after imposing the universal scalar census. In particular, the established `weil_inertia` improvements above `H_MT` do not contradict WI-153; they retain information discarded by this scalarization.

## 5. Prior-art and novelty audit

The primary classical source is Emanuel Carneiro, Vorrapan Chandee, Friedrich Littmann and Micah B. Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function*, J. Reine Angew. Math. 725 (2017), 143--182, arXiv:1406.5462. Section 3.5 identifies the one-delta problem and Corollary 14 proves (13), with equality characterization. The paper explicitly traces the original zeta application to Montgomery--Taylor and notes the Iwaniec--Luo--Sarnak treatment. Later work on variants of the one-delta/Caratheodory--Fejer--Turan problem confirms that this extremal family is classical rather than a new optimization principle.

The primary modern zero-side source is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026). Proposition 2.1 supplies the finite universal conjugation-invariant census for the concrete Hilbert-space kernel, Lemma 3.1 records the unconditional support-one pair-correlation input, and Remark 3.4 explicitly identifies CCLM Corollary 14 as the optimality theorem behind `C_MT`.

A targeted audit of the current `weil_inertia` corpus, especially WI-145--WI-152, located the ingredients separately but not this finite-depth signed-support-one closure. WI-147 obtains physical nonnegativity only under full unbounded-depth universality; WI-151--WI-152 retain signed profiles at bounded depth and leave a central-spike escape; the existing CCLM source anchor was used for classical single-window optimality. The additional deduction here is the exact bridge

\[
\text{bounded-depth universal real two-point census}
\Longrightarrow H\ge0
\Longrightarrow H\ \text{is CCLM-admissible}
\Longrightarrow C(\phi)\ge C_{\rm MT},
\]

which closes the signed support-one scalar objective without upgrading `phi` to a nonnegative function. This is the novelty boundary used for persistence, not a claim of mathematical priority.

## 6. Consequence for the research program

The support-one signed-reservoir route is now decisively closed **within the full universal one-scalar abstraction**. A profile cannot evade Montgomery--Taylor by hiding negative mass in an `O(B^{-1})` layer, by growing `phi(0)`, or by exploiting the fact that bounded depth does not force `phi>=0`: real two-point universality alone already places the transformed kernel in the sharp one-delta cone.

Therefore a genuine improvement must retain information that this reduction removes or alter the arithmetic interface. Viable exits include restricting the zero-side inequality to configurations actually realizable by zeta rather than every conjugation-invariant multiset, using matrix/multi-kernel observables whose joint constraints do not collapse to one nonnegative admissible `H`, exploiting higher/mixed correlations, or justifying support beyond one with genuinely new arithmetic input. This barrier strengthens the motivation for those routes while preventing further optimization effort on signed support-one scalar profiles under full finite-multiset universality.

## References

- Emanuel Carneiro, Vorrapan Chandee, Friedrich Littmann and Micah B. Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function*, J. Reine Angew. Math. 725 (2017), 143--182; arXiv:1406.5462, especially §3.5 and Corollary 14. https://arxiv.org/abs/1406.5462
- Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), especially Proposition 2.1, Lemma 3.1, Lemma 3.2 and Remark 3.4. https://arxiv.org/abs/2609.02882
- H. L. Montgomery and A. E. Taylor, *Distribution of the zeros of the Riemann zeta function*, Michigan Math. J. 23 (1976), 21--37. Classical origin of the one-delta extremizer used in the zeta simple-zero problem.
