# PC-105 — cumulative primitive-root kernel discrepancy is exactly Farey/Mertens data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-RH-EQUIVALENCE` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY`. The exact circle-Fourier and translation-invariant-kernel formulas below are derived here from the Prime-Circle primitive layers and classical Ramanujan/Möbius identities. The RH equivalence through the Mertens function, the Farey-discrepancy framework, and broad kernel/RKHS Farey criteria are classical or established prior art. No theorem-level historical novelty is claimed.

PC-007 already identifies the cumulative set of newly born Prime-Circle vertices with the Farey sequence and closes one-dimensional angular discrepancy as a novelty route. A remaining natural loophole in the current mandate is to keep the same cumulative root cloud but replace pointwise matching/discrepancy by a genuinely nonlocal positive kernel on the circle. That looks more operator-theoretic because every point interacts with every other point before scalar compression.

For the entire class of fixed translation-invariant positive kernels treated below, however, the RH-sensitive content is already present in the **first Fourier mode** of the cumulative primitive-root measure. That mode is exactly the normalized Mertens function. The full kernel energy is an explicit weighted `l^2` package of divisor transforms of the same Mertens data. Thus this nonlocal repair yields a clean intrinsic RH criterion, but not a new RH mechanism.

## 1. The cumulative primitive-root cloud

For `N>=1`, let

\[
\mathcal C_N
:=\bigsqcup_{1\le q\le N} P_q^*,
\qquad
A_N:=|\mathcal C_N|
=\sum_{q\le N}\varphi(q),
\]

and put the normalized counting measure

\[
\boxed{
\nu_N
:=\frac1{A_N}
\sum_{q\le N}\sum_{\alpha\in P_q^*}\delta_\alpha.
}
\]

The union is disjoint because a root of unity has a unique exact order. Under the angular parametrization

\[
x\longmapsto e^{2\pi i x},
\]

`P_q^*` is exactly the set of reduced fractions `a/q` of exact denominator `q`. Hence `\mathcal C_N` is the Farey sequence of order `N` with the `0/1` endpoint omitted; cutting the circle at the common anchor and duplicating that anchor as the two interval endpoints gives the conventional full Farey sequence. This is precisely the PC-007 identification, now retained as a measure rather than immediately ordered and matched.

Equivalently, the intrinsic cumulative cyclotomic polynomial

\[
Q_N(z)=\prod_{q\le N}\Phi_q(z)
\]

has `\mathcal C_N` as its simple boundary zero set.

## 2. Every Fourier mode is an exact summatory Ramanujan/Mertens transform

For an integer `k!=0`, the `k`th Fourier coefficient of `\nu_N` is

\[
\begin{aligned}
\widehat\nu_N(k)
&=\int_{\mathbb T}z^k\,d\nu_N(z)\\
&=\frac1{A_N}\sum_{q\le N}\sum_{\alpha\in P_q^*}\alpha^k\\
&=\frac1{A_N}\sum_{q\le N}c_q(k),
\end{aligned}
\]

where `c_q(k)` is the Ramanujan sum. Using the classical divisor formula

\[
c_q(k)=\sum_{d\mid(q,k)}d\,\mu(q/d)
\]

and writing `q=dm` gives the exact finite identity

\[
\boxed{
A_N\widehat\nu_N(k)
=\sum_{\substack{d\mid k\\d\le N}}
 d\,M\!\left(\left\lfloor\frac Nd\right\rfloor\right),
}
\]

where

\[
M(x)=\sum_{m\le x}\mu(m)
\]

is the Mertens function.

No limiting interchange is involved. This is a finite rearrangement of the exact primitive-root Fourier sums.

The first mode is especially rigid. Since `c_q(1)=\mu(q)`,

\[
\boxed{
\widehat\nu_N(1)=\frac{M(N)}{A_N}.
}
\]

Thus the cumulative root cloud already contains the Mertens function as its first nonconstant angular moment.

As a finite control, for `N=5`,

\[
A_5=1+1+2+2+4=10,
\qquad
M(5)=-2,
\]

so

\[
\widehat\nu_5(1)=-\frac15.
\]

Direct summation of the ten exact-order roots gives the same value.

## 3. The first Fourier mode alone is an RH-equivalent geometric rate

The classical summatory-totient asymptotic is

\[
A_N
=\frac{N^2}{2\zeta(2)}+O(N\log N)
=\frac{3}{\pi^2}N^2+O(N\log N).
\]

Also classically,

\[
\boxed{
\mathrm{RH}
\iff
M(N)=O_\varepsilon(N^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
}
\]

Combining these with the exact first-mode identity yields

\[
\boxed{
\mathrm{RH}
\iff
|\widehat\nu_N(1)|
=O_\varepsilon(N^{-3/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
}
\]

This is a completely intrinsic circle statement: it uses only the unlabelled cumulative primitive-root cloud and the lowest nonconstant character of the circle. It is nevertheless not new arithmetic. It is exactly the classical Mertens criterion written in Prime-Circle Fourier coordinates.

This also explains a standard Farey identity. If the omitted `0/1` endpoint is restored, its exponential contributes one additional copy of `1`, giving

\[
\sum_{x\in F_N}e^{2\pi i x}=1+M(N),
\]

or equivalently `M(N)=-1+sum_{x in F_N} exp(2 pi i x)` under the conventional two-endpoint Farey normalization.

## 4. Fixed translation-invariant nonlocal kernels are weighted Mertens packages

Let `K` be a continuous translation-invariant positive-semidefinite kernel on the circle, with absolutely convergent Fourier expansion

\[
K(z,w)
=\sum_{k\in\mathbb Z}a_k(z\overline w)^k,
\qquad
a_k\ge0,
\qquad
\sum_k a_k<\infty.
\]

Let `m_T` be Haar probability measure on the circle. The squared kernel mean discrepancy between the cumulative root cloud and Haar is exactly

\[
\mathcal E_K(N)
:=\left\|\nu_N-m_T\right\|_{\mathcal H_K^*}^2
=\sum_{k\ne0}a_k|\widehat\nu_N(k)|^2.
\]

Substituting the exact Ramanujan/Mertens formula gives

\[
\boxed{
\mathcal E_K(N)
=\frac1{A_N^2}
\sum_{k\ne0}a_k
\left|
\sum_{\substack{d\mid |k|\\d\le N}}
 d\,M\!\left(\left\lfloor\frac Nd\right\rfloor\right)
\right|^2.
}
\]

So an apparently genuinely nonlocal pairwise statistic on the circle contains no hidden angular spectrum beyond the summatory Ramanujan coefficients. Every mode is a finite divisor transform of Mertens values at the scaled cutoffs `N/d`.

The same identity follows directly from the usual kernel-energy formula

\[
\iint K\,d(\nu_N-m_T)\,d(\nu_N-m_T),
\]

so this is not an artifact of choosing coordinates after the fact; Fourier diagonalization is forced by translation invariance of the kernel.

## 5. A broad circle-kernel class has an RH-equivalent rate, but only because it contains the Mertens mode

Define

\[
\sigma_{1/2}(k)=\sum_{d\mid k}d^{1/2}.
\]

Assume in addition that

\[
\boxed{
a_1>0,
\qquad
\sum_{k\ne0}a_k\,\sigma_{1/2}(|k|)^2<\infty.
}
\]

Then

\[
\boxed{
\mathrm{RH}
\iff
\mathcal E_K(N)^{1/2}
=O_\varepsilon(N^{-3/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
}
\]

The proof makes the classicalization transparent.

If RH holds, then for every `epsilon>0`,

\[
\left|M\!\left(\left\lfloor\frac Nd\right\rfloor\right)\right|
\ll_\varepsilon
(N/d)^{1/2+\varepsilon}.
\]

Hence for every nonzero `k`,

\[
\begin{aligned}
\left|
\sum_{\substack{d\mid |k|\\d\le N}}
 d\,M\!\left(\left\lfloor\frac Nd\right\rfloor\right)
\right|
&\ll_\varepsilon
N^{1/2+\varepsilon}
\sum_{d\mid |k|}d^{1/2-\varepsilon}\\
&\le
N^{1/2+\varepsilon}\sigma_{1/2}(|k|).
\end{aligned}
\]

The stated summability condition and `A_N\asymp N^2` therefore give

\[
\mathcal E_K(N)^{1/2}
\ll_\varepsilon N^{-3/2+\varepsilon}.
\]

Conversely, positivity of the Fourier weights gives the one-mode lower bound

\[
\mathcal E_K(N)^{1/2}
\ge
\sqrt{a_1}\,|\widehat\nu_N(1)|
=
\sqrt{a_1}\,\frac{|M(N)|}{A_N}.
\]

Thus the assumed kernel rate forces

\[
M(N)=O_\varepsilon(N^{1/2+\varepsilon}),
\]

which is RH.

For example, the periodic Sobolev/Bessel kernels with weights

\[
a_k\asymp(1+k^2)^{-s}
\]

satisfy the displayed sufficient summability condition for every `s>1` (using the standard bound `sigma_{1/2}(k)\ll_\delta k^{1/2+\delta}`). These are genuine nonlocal positive kernels, but their RH criterion is still only the Mertens criterion seen through a positive quadratic norm.

## 6. Prior-art and novelty audit

This branch is surrounded by strong classical and modern prior art.

1. **PC-007 / Franel--Landau.** PC-007 already records that the cumulative new vertices are exactly Farey points and that their ordered angular `L^2` discrepancy has the classical Franel RH criterion. Franel's original paper is J. Franel, *Les suites de Farey et le problème des nombres premiers*, Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen (1924), 198--201; Landau's companion paper is *Bemerkungen zu der vorstehenden Abhandlung von Herrn Franel*, ibid., 202--206.
2. **Harmonic/functional Farey criteria.** P. Codecà and A. Perelli, *On the uniform distribution (mod 1) of the Farey fractions and `l^p` spaces*, Mathematische Annalen 279 (1987/88), 413--422, DOI `10.1007/BF01456278`, explicitly study Farey uniform distribution and RH-linked estimates by functional and harmonic analysis.
3. **Modern kernel/RKHS formulation.** T. Karvonen and A. Zhigljavsky, *Maximum mean discrepancies of Farey sequences*, Acta Mathematica Hungarica 177 (2025), 351--362, DOI `10.1007/s10474-025-01577-5`, prove that for a large class of positive-semidefinite kernels on `[0,1]` the Farey MMD rate

\[
\mathrm{MMD}(F_N)=O_\varepsilon(N^{-3/2+\varepsilon})
\]

is equivalent to RH; their class includes Matérn kernels of order at least `1/2` and released integrated-Brownian kernels. Their theorem is not literally the periodic circle Fourier formula above, but it decisively establishes that turning Farey discrepancy into a nonlocal RKHS/kernel norm is already an existing RH-criterion framework.
4. **Mertens/Farey exponential sum.** The identity expressing `M(N)` as the first exponential sum of the Farey points is classical and is used in standard treatments of the Franel--Landau theorem. In Prime-Circle notation it becomes immediate from `c_q(1)=mu(q)`.

A directed search for Farey kernel discrepancy, periodic/Sobolev discrepancy, Fourier formulations, and Mertens exponential sums found extensive neighboring theory rather than evidence that the circle-kernel packaging should be treated as a new RH mechanism. The exact formula in Sections 2--5 is useful as a line-local information audit, not as a historical novelty claim.

## 7. Research consequence

This closes a natural loophole left by the wording of PC-007. Replacing ordered chordal/Farey discrepancy by a **fixed translation-invariant nonlocal positive kernel on the cumulative unlabelled root cloud** does not recover information that the Farey union discarded.

In the exact class above,

\[
\boxed{
\text{cumulative primitive roots}
\longrightarrow
\text{translation-invariant kernel energy}
\longrightarrow
\text{RH rate}
}
\]

is only

\[
\boxed{
\text{Farey/Ramanujan sums}
\longrightarrow
\text{Mertens divisor transforms}
\longrightarrow
\text{classical Mertens/Franel RH criterion}.
}
\]

The important boundary is therefore **label retention**. Once all exact-order shells `q<=N` are merged into one unlabelled point measure, even a genuinely nonlocal translation-invariant kernel sees only classical Farey/Mertens discrepancy. A future cumulative Prime-Circle mechanism must retain something that this pushforward forgets — for example the birth conductor as an active coordinate, nonseparable inter-level interactions, or an operator whose cross-level coupling is itself forced by the geometry rather than chosen as a fixed kernel after aggregation.

This finding does not rule out such labelled/cross-level operators, the finite mixed-shell Hardy trace-class sector of PC-080--PC-104, or the global nonlinear uniformization/monodromy branch. It only closes the fixed-kernel repair of the **unlabelled cumulative root cloud**.

## 8. Falsification surface

1. For each fixed `k`, direct summation of the roots in `P_q^*` must give `c_q(k)`, and summing `q<=N` must agree exactly with `sum_{d|k,d<=N} d M(floor(N/d))`.
2. At `k=1`, the cumulative root sum must equal `M(N)` for every `N`; any discrepancy would invalidate the RH-equivalence reduction.
3. The kernel identity requires translation invariance and nonnegative Fourier coefficients. A non-translation-invariant or geometry-dependent cross-level kernel is outside the theorem and must not be declared closed by it.
4. The RH-to-kernel upper bound in Section 5 uses the explicit summability condition `sum a_k sigma_{1/2}(k)^2<infinity`; kernels outside that class require a separate estimate.
5. The converse needs only `a_1>0`. A kernel deliberately annihilating the first mode may still carry RH-sensitive higher-mode information, but that would need a separate criterion and does not restore novelty to the broad MMD/Farey framework already present in the literature.
6. The finding concerns the **unlabelled cumulative measure**. Any construction retaining exact-order labels before aggregation is outside this no-go.
