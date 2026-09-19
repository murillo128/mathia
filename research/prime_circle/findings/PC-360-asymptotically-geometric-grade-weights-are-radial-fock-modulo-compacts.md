# PC-360 — asymptotically geometric grade weights are radial free-Fock transport modulo compacts

- **Finding ID:** `PC-360`
- **Status:** `EXACT-DERIVED` + `CLASSICAL-OPERATOR-THEORY` + `NEGATIVE/OBSTRUCTION`
- **Research line:** `prime_circle`
- **Result type:** exact borderline-completion classification / matched-control falsification
- **Scope:** tests the main scalar-weight frontier left explicitly open by PC-359: weighted infinite word completions with nonzero asymptotic fixed-lag ratios, so positive-degree creation remains bounded and noncompact while reciprocal parity may still be unbounded.
- **RH relevance:** high as a boundary result. The borderline regime avoids PC-359's compactification collapse, but its high-grade operator is only a radial rescaling of the ordinary free-Fock creation model modulo compacts. Moreover, source/control spectral-radius separation can be made arbitrarily large in a nonarithmetic two-dimensional matched control by changing only the fixed one-particle metric. Such a gap is therefore not, by itself, arithmetic or RH-facing information.

## Claim

Let `K` be a nonzero finite-dimensional complex Hilbert space with norm induced by a fixed positive Hermitian form `G`, and consider the scalar grade-weighted full word completion

\[
\mathcal H_w
=
\bigoplus_{m\ge0}
\left(K^{\otimes m},w_m G^{\otimes m}\right),
\qquad w_m>0.
\tag{1}
\]

Assume the weights are asymptotically geometric in the precise sense

\[
\boxed{
\frac{w_{m+1}}{w_m}\longrightarrow r
\qquad(m\to\infty),
\qquad 0<r<\infty.
}
\tag{2}
\]

Then for every fixed `k>=1`,

\[
\frac{w_{m+k}}{w_m}\longrightarrow r^k.
\tag{3}
\]

Let `d_k in K^{\otimes k}` and let `L_{d_k}^{(w)}` be left creation by `d_k` on `\mathcal H_w`. Under the canonical unitary reweighting from `\mathcal H_w` to the unweighted full Fock space `\mathcal F_G(K)`, one has

\[
\boxed{
U_w L_{d_k}^{(w)} U_w^{-1}
-
r^{k/2}L_{d_k}^{(0)}
\in \mathcal K(\mathcal F_G(K)),
}
\tag{4}
\]

where `L_{d_k}^{(0)}` denotes ordinary left creation and `\mathcal K` the compact operators. Consequently every finite positive-degree polynomial

\[
Q_K^{(w)}=\sum_{k=1}^{K_0}L_{d_k}^{(w)}
\tag{5}
\]

satisfies

\[
\boxed{
U_w Q_K^{(w)}U_w^{-1}
=
\sum_{k=1}^{K_0}r^{k/2}L_{d_k}^{(0)}+C,
\qquad C\text{ compact}.
}
\tag{6}
\]

Thus the Calkin-class/high-grade operator carried by any such scalar completion is exactly the ordinary free-Fock multiplier after the radial degree dilation

\[
d_k\longmapsto r^{k/2}d_k.
\tag{7}
\]

If the weights are exactly geometric, `w_m=C r^m`, the compact error vanishes identically.

For a single nonzero homogeneous `d_k`, if `dim K>=2`, then

\[
\boxed{
\sigma\!\left(L_{d_k}^{(w)}\right)
=
\sigma_{\rm e}\!\left(L_{d_k}^{(w)}\right)
=
\left\{z:|z|\le r^{k/2}\|d_k\|_{G^{\otimes k}}\right\}.
}
\tag{8}
\]

The same statement applied to the reciprocal control `d_k\mapsto J^{\otimes k}d_k` replaces the radius by

\[
r^{k/2}\|J^{\otimes k}d_k\|_{G^{\otimes k}}.
\tag{9}
\]

That possible source/control radius gap is not intrinsically arithmetic. Already on `K=C^2`, with

\[
J=\operatorname{diag}(1,-1),
\qquad
G_t=
\begin{pmatrix}1&t\\ t&1\end{pmatrix},
\qquad 0<t<1,
\tag{10}
\]

and `v=e_1-e_2`, one gets

\[
\|v\|_{G_t}^2=2(1-t),
\qquad
\|Jv\|_{G_t}^2=2(1+t).
\tag{11}
\]

For `d_k=v^{\otimes k}`, the matched control/source spectral-radius ratio is therefore

\[
\boxed{
\frac{\rho(L_{J^{\otimes k}d_k}^{(w)})}
{\rho(L_{d_k}^{(w)})}
=
\left(\frac{1+t}{1-t}\right)^{k/2},
}
\tag{12}
\]

which can be made arbitrarily large as `t\to1^-` without any arithmetic input.

## Derivation

### 1. Canonical reweighting exposes the high-grade shift weights

Define

\[
U_w:\mathcal H_w\to\mathcal F_G(K),
\qquad
U_w|_{K^{\otimes m}}=\sqrt{w_m}\,I.
\tag{13}
\]

This is unitary because the grade-`m` norm in `\mathcal H_w` is `\sqrt{w_m}` times the ordinary `G^{\otimes m}` norm.

For `x\in K^{\otimes m}`,

\[
U_wL_{d_k}^{(w)}U_w^{-1}x
=
\sqrt{\frac{w_{m+k}}{w_m}}\,d_k\otimes x.
\tag{14}
\]

Hence the weighted creation operator is an operator-valued unilateral shift whose grade-`m` weight is

\[
a_m^{(k)}
:=
\sqrt{\frac{w_{m+k}}{w_m}}.
\tag{15}
\]

Condition (2) telescopes:

\[
\frac{w_{m+k}}{w_m}
=
\prod_{j=0}^{k-1}
\frac{w_{m+j+1}}{w_{m+j}}
\longrightarrow r^k,
\tag{16}
\]

so `a_m^{(k)}\to r^{k/2}`.

### 2. Convergent grade weights differ from constant creation only compactly

Set

\[
D_k
:=
U_wL_{d_k}^{(w)}U_w^{-1}
-r^{k/2}L_{d_k}^{(0)}.
\tag{17}
\]

On input grade `m`,

\[
\|D_k|_{K^{\otimes m}}\|
=
\left|a_m^{(k)}-r^{k/2}\right|
\|d_k\|.
\tag{18}
\]

The block norm tends to zero. Truncating `D_k` to the finitely many input grades `0,...,M` gives a finite-rank operator, because every tensor grade of a finite-dimensional `K` is finite-dimensional. The tail norm is exactly the supremum of the remaining block norms and tends to zero. Therefore `D_k` is compact, proving (4).

Finite sums preserve compactness, which proves (6). In the exactly geometric case, `a_m^{(k)}=r^{k/2}` for every `m`, so (6) holds with `C=0`.

This is the exact borderline opposite of PC-359. Ratio decay to zero compactifies positive-degree creation. A positive finite limit keeps transport noncompact, but only by retaining the standard Fock shift at a rescaled radius.

### 3. The homogeneous spectrum is the classical shift disk

Normalize first in the ordinary Fock space:

\[
V:=\frac{1}{\|d_k\|}L_{d_k}^{(0)}.
\tag{19}
\]

`V` is an isometry. It is pure because repeated application prefixes arbitrarily many copies of `d_k`, while the intersection of all ranges contains no nonzero finite-grade vector and hence is zero.

When `dim K>=2`, the defect space `\ker V^*` is infinite-dimensional: at every sufficiently high grade, the target tensor power contains directions orthogonal to the subspace prefixed by `d_k`. By the Wold decomposition, `V` is therefore a unilateral shift of infinite multiplicity. Its ordinary and essential spectra are both the closed unit disk.

Equation (4) and invariance of essential spectrum under compact perturbations yield

\[
\sigma_{\rm e}(L_{d_k}^{(w)})
=
\{z:|z|\le r^{k/2}\|d_k\|\}.
\tag{20}
\]

No spectral point can lie outside this disk. Indeed, a point outside the essential spectrum could only occur as an isolated finite-multiplicity eigenvalue, whereas `L_{d_k}^{(w)}` has no nonzero eigenvalues: it raises grade by exactly `k`, so comparing the least occupied grade in an equation `L_{d_k}^{(w)}x=\lambda x`, `\lambda\ne0`, gives an immediate contradiction. This proves (8).

For `dim K=1`, the same compact-equivalence statement (4) remains exact, but the shift multiplicity is finite and the essential spectrum is the boundary circle rather than the full disk. The Prime-Circle word construction of interest is in the nontrivial multi-letter regime, so (8) is stated with `dim K>=2`.

### 4. The matched nonarithmetic control makes the spectral gap arbitrary

The source/control construction of PC-355--PC-359 uses an algebraic involution `J` on one-particle data. Scalar grade weights do not affect the gradewise norm of its second quantization, so when `\|J\|_G>1` the reciprocal parity remains unbounded exactly as in PC-359.

The borderline weights now keep creation noncompact, so unlike PC-359 the source and control spectra can genuinely have different radii. But this difference fails the matched nonprime/nonarithmetic audit.

For (10), `G_t` is positive definite for `0<t<1`. Direct calculation gives (11). Tensor multiplicativity then gives

\[
\|v^{\otimes k}\|_{G_t^{\otimes k}}
=[2(1-t)]^{k/2},
\qquad
\|(Jv)^{\otimes k}\|_{G_t^{\otimes k}}
=[2(1+t)]^{k/2}.
\tag{21}
\]

The common radial factor `r^{k/2}` cancels, proving (12). The ratio diverges as `t\to1^-` although this two-dimensional model contains no primes, roots of unity, cyclotomic shells, zeta function, or critical line.

Thus meeting the two necessary gates identified by PC-359 -- unbounded reciprocal parity and noncompact high-grade transport -- is still not sufficient. A source/control spectral separation can be created entirely by the arbitrary choice of one-particle Hilbert metric.

## Prior-art and novelty audit

The functional-analytic mechanism is classical. Scalar weighted creations are weighted shifts after the unitary reweighting (13); a convergent shift-weight sequence differs compactly from the corresponding constant shift; and the left regular/free-Fock creation operators are the standard free-semigroup model. Allen L. Shields' 1974 survey **Weighted shift operators and analytic function theory** is a classical weighted-shift reference (AMS Mathematical Surveys 13, pp. 49--128, DOI `10.1090/surv/013/02`). Kenneth R. Davidson and David R. Pitts' **Invariant Subspaces and Hyper-Reflexivity for Free Semigroup Algebras**, *Proceedings of the London Mathematical Society* 78 (1999), 401--430, DOI `10.1112/S002461159900180X`, gives the standard left-regular free-semigroup/Fock operator setting. Gelu Popescu's *Operator theory on noncommutative domains*, *Memoirs of the AMS* 205, no. 964 (2010), develops the broader weighted universal-creation framework.

No novelty is claimed for weighted-shift compact perturbations, Wold decomposition, free-Fock creation operators, or their spectra. The Prime-Circle-specific delta is the classification of the exact PC-359 borderline scalar completion: once the fixed-lag ratio tends to a positive finite constant, the surviving noncompact transport is only radial standard-Fock transport modulo compacts, while the most immediate reciprocal-control spectral discriminator fails a deliberately arithmetic-free matched control by an arbitrarily large factor.

The novelty audit therefore classifies the operator theory as classical and the present result as a research-line obstruction/boundary, not as a new spectral theorem or RH mechanism.

## Consequence for the Prime-Circle program

PC-359 showed that making reciprocal parity unbounded is insufficient if the same completion compactifies all positive-degree transport. PC-360 now covers the natural scalar borderline in the opposite direction: keeping a nonzero asymptotic transport scale avoids compactification, but does not create a new asymptotic operator geometry. Modulo compacts it is the ordinary free-Fock left multiplier with the single scalar radial substitution (7).

Moreover, the first obvious spectral quantity that can distinguish source from reciprocal control in this regime -- homogeneous spectral radius -- is not intrinsically arithmetic. It can be amplified without bound by a nonarithmetic choice of fixed one-particle metric. Therefore a future RH-facing construction cannot count a source/control radius gap produced only by `G` and `J` as progress.

The surviving frontier is narrower but nonempty. This finding does **not** rule out:

- a genuinely infinite mixed-degree multiplier when its high-degree tail is not controlled by a finite polynomial approximation or by norm-summable compact errors;
- non-scalar grade couplings rather than one weight `w_m` per tensor grade;
- unbounded/closed operators whose domains themselves encode arithmetic information;
- same-grade, backward, or two-sided interactions;
- a source-forced observable whose distinction survives matched nonarithmetic metric controls.

For an infinite series `Q=\sum_{k\ge1}L_{d_k}^{(w)}`, the same compact-equivalence conclusion follows under the additional sufficient condition that both the radially dilated series `\sum r^{k/2}L_{d_k}^{(0)}` converges in operator norm and the compact-error series from (17) is norm summable. Without such control, PC-360 makes no claim about the full infinite mixed-degree signature multiplier.

## Falsification / audit test

The exact operator statement can be refuted only by violating one of its load-bearing steps. Under (2), a counterexample would need one of the following:

1. a fixed `k` for which `w_{m+k}/w_m` does not tend to `r^k`;
2. a homogeneous creation block whose conjugated coefficients tend to `r^{k/2}` but whose difference from constant creation is not compact;
3. for `dim K>=2`, a nonzero homogeneous weighted creation with spectrum outside the disk in (8) despite having no nonzero eigenvalues there;
4. a claim that the source/control radius gap is intrinsically arithmetic that survives the explicit nonarithmetic family (10)--(12).

The first three contradict elementary finite-product limits and standard Hilbert-space operator theory. The fourth is the practical research falsification control: any future spectral discriminator built from this scalar completion must exhibit arithmetic content that cannot be reproduced by changing only the nonarithmetic one-particle metric.

## Formalization handoff

No automatic Lean handoff is warranted. The result is exact, but formalizing weighted Hilbert direct sums, compact perturbations, Calkin/essential spectrum, and infinite-multiplicity Wold theory would require substantial analytic infrastructure. At present the research value lies in the boundary it imposes on completion design rather than in a finite theorem interface whose formal proof is likely to expose a new structural asymmetry.