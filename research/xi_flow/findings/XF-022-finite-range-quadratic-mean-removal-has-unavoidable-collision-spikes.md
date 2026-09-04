# XF-022 — finite-range quadratic mean removal has unavoidable collision-positive spikes

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `STRUCTURAL/BOUNDARY`. XF-018--XF-021 left one particularly natural escape from the compact centered-entropy obstruction: localize the collision-safe uncentered square, then remove the neutral mean by summing or combining many overlapping block variances so that individual boundary terms might cancel.

That escape fails at the universal quadratic level. Let `L` be any nonzero finite-range symmetric translation-invariant quadratic kernel on gap space that annihilates constants. Then there is a positive local gap configuration with one collapsing gap `epsilon -> 0` for which the exact Xi gap diffusion produces

\[
\boxed{Q_L'(t)=\frac{2}{\epsilon}(A L g)_1+O(1)\longrightarrow +\infty,}
\]

where `A` is the nearest-neighbor discrete Laplacian. The key algebraic fact is that `AL` cannot have the one-sided off-diagonal sign needed to make every such collision harmless: because both `A` and `L` annihilate constants, the convolution kernel of `AL` has zero second moment, while a nontrivial finite-range Laplacian/M-matrix sign pattern would force that second moment to be strictly negative.

Consequently **no nontrivial finite-range translation-invariant quadratic mean-removal functional is collision-safe from above using only the universal positive-conductance gap dynamics**. This includes the uniform sum of all translates of any fixed-length block variance. Overlap can move the dangerous boundary, but it cannot remove the source-free collision obstruction.

This does not rule out genuinely global/nondecaying mean removal, a scale-dependent construction that uses additional Xi-specific information to exclude the adversarial geometry, or nonlinear/projective span terms of the XF-018 cross-ratio type. It does sharpen the current frontier: the remaining mean-removal mechanism cannot be just a finite-range quadratic averaging of local variances.

## 1. Quadratic mean-removal class

Fix `h>0`. Let

\[
L=(L_d)_{d\in\mathbb Z}
\]

be a real finite-range convolution kernel satisfying

\[
L_{-d}=L_d,
\qquad
\sum_{d\in\mathbb Z}L_d=0.
\tag{1}
\]

The second condition is exactly constant-mode removal. For a gap configuration of the form

\[
g_i=h+u_i,
\]

with `u` finitely supported, define

\[
\boxed{
Q_L(g)
:=\frac12\sum_i u_i(L*u)_i.
}
\tag{2}
\]

Because `L*1=0`, this is equivalently the quadratic form with gradient

\[
p_i:=\frac{\partial Q_L}{\partial g_i}=(L*g)_i=(L*u)_i.
\tag{3}
\]

No positivity assumption on `L` is needed for the obstruction below. In the intended applications `L` is positive semidefinite, so `Q_L` is a genuine centered quadratic energy; the theorem is stronger because even indefinite finite-range kernels cannot avoid the universal collision test merely by changing coefficients.

On a real-simple Xi slice, XF-014 gives

\[
g_i'=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad
c_{ik}=c_{ki}>0.
\tag{4}
\]

Since `p` is finitely supported when `u` is, differentiation is a finite linear combination of the absolutely convergent pointwise gap equations from XF-014.

## 2. A collapsing gap probes `AL`, not `L`

Put the collapsing gap at index `1`:

\[
g_1=\epsilon\downarrow0,
\tag{5}
\]

while every other gap is held fixed and positive. Write

\[
g_0=a>0,
\qquad
g_2=b>0.
\tag{6}
\]

Only the two adjacent conductances containing `g_1` are singular:

\[
c_{0,1}=\frac1{a\epsilon},
\qquad
c_{1,2}=\frac1{\epsilon b}.
\tag{7}
\]

Every other conductance stays bounded as `epsilon -> 0` because every corresponding denominator contains a fixed positive intervening span.

The contribution of the pair `(0,1)` to `Q_L'` is

\[
2c_{0,1}(g_1-g_0)(p_0-p_1)
=\frac{2}{\epsilon}(p_1-p_0)+O(1),
\tag{8}
\]

and the pair `(1,2)` contributes

\[
2c_{1,2}(g_2-g_1)(p_1-p_2)
=\frac{2}{\epsilon}(p_1-p_2)+O(1).
\tag{9}
\]

Therefore

\[
\boxed{
Q_L'
=\frac{2}{\epsilon}
(2p_1-p_0-p_2)+O(1).
}
\tag{10}
\]

Let `A` denote the nearest-neighbor discrete Laplacian

\[
(Av)_i:=2v_i-v_{i-1}-v_{i+1}.
\tag{11}
\]

Because `p=L*g`, equation (10) becomes the exact leading collision law

\[
\boxed{
Q_L'
=\frac{2}{\epsilon}(ALg)_1+O(1).
}
\tag{12}
\]

This is the structural reason overlap does not trivially cure XF-021. A centered quadratic already contains one discrete derivative through constant-mode removal; the collapsing-gap dynamics contributes another nearest-neighbor Laplacian. The collision sign is therefore governed by a higher-order kernel `AL`.

## 3. The finite-range sign obstruction

Let

\[
M:=AL
\tag{13}
\]

and write its finite-range symmetric convolution kernel as `(m_d)`. Since both `A` and `L` annihilate constants,

\[
\sum_d m_d=0.
\tag{14}
\]

Symmetry also gives vanishing first moments. More importantly, the second moment of `M` is exactly zero. If `a_d` is the kernel of `A`, namely

\[
a_0=2,
\qquad
a_{\pm1}=-1,
\tag{15}
\]

then `m=a*L`, and the convolution moment identity gives

\[
\begin{aligned}
\sum_n n^2m_n
={}&
\left(\sum_n n^2a_n\right)\left(\sum_dL_d\right)
+2\left(\sum_nna_n\right)\left(\sum_ddL_d\right)\\
&+\left(\sum_na_n\right)\left(\sum_dd^2L_d\right)
=0.
\end{aligned}
\tag{16}
\]

Suppose, contrary to what we need to prove, that every off-diagonal coefficient had the collision-safe sign

\[
m_d\le0
\qquad(d\ne0).
\tag{17}
\]

Then

\[
\sum_n n^2m_n
=\sum_{n\ne0}n^2m_n\le0.
\tag{18}
\]

Because the left side is exactly zero by (16), every term in (18) must vanish:

\[
m_n=0
\qquad(n\ne0).
\tag{19}
\]

The row-sum condition (14) then forces `m_0=0`, hence

\[
M=AL=0.
\tag{20}
\]

But `A` and `L` are finite Laurent-polynomial convolution operators. The Laurent-polynomial ring has no zero divisors and `A` is nonzero, so (20) implies

\[
L=0,
\tag{21}
\]

contradicting the hypothesis.

Thus every nonzero finite-range symmetric constant-annihilating quadratic kernel satisfies

\[
\boxed{
\exists d\ne0:\quad m_d>0.
}
\tag{22}
\]

This is the decisive sign change.

## 4. Positive local gaps turn that sign change into a `+1/epsilon` spike

Because `M` also annihilates constants,

\[
(Mg)_1
=\sum_d m_d(g_{1-d}-h).
\tag{23}
\]

Choose one `d_* != 0` with `m_{d_*}>0`. Keep every gap equal to `h` except

\[
g_1=\epsilon,
\qquad
g_{1-d_*}=H,
\tag{24}
\]

with `H>h` fixed but sufficiently large. If the selected index happens to be `0` or `2`, this simply means taking the adjacent noncollapsing gap large; the asymptotic (12) remains unchanged because its leading coefficient is independent of the finite values `a,b>0`.

Equation (23) becomes

\[
(Mg)_1
=m_{d_*}(H-h)+m_0(\epsilon-h),
\tag{25}
\]

possibly plus finitely many zero terms from gaps left at `h`. Since `m_{d_*}>0`, choose `H` so that the right side has a positive limit as `epsilon -> 0`. Then (12) yields

\[
\boxed{
Q_L'
=\frac{2c_*}{\epsilon}+O(1)
\longrightarrow+\infty
}
\tag{26}
\]

for some `c_*>0`.

Therefore there is no inequality of the form

\[
Q_L'\le O(1)
\tag{27}
\]

uniform over positive ordered gap configurations using only the universal gap-diffusion structure. In particular, no finite-range quadratic constant-mode remover can be promoted to a source-free collision-safe Lyapunov by tuning its coefficients.

The witness is local. A long finite real-rooted polynomial can realize the prescribed finite positive gap pattern at an interior real-simple slice simply by choosing its roots accordingly. Its exact backward-heat root ODE has the same two adjacent `1/epsilon` singular interactions around the collapsing gap; all contributions from the remaining roots and finite endpoints stay `O(1)` as `epsilon -> 0`. Thus the leading positive spike is reproduced by the line's matched polynomial controls and is not an artifact of an impossible local ordering.

## 5. Uniform overlapping block variances are a direct corollary

For a block of `N>=2` consecutive gaps define

\[
V_j^{(N)}
:=\frac12\sum_{r=0}^{N-1}
\left(g_{j+r}-\bar g_j\right)^2,
\qquad
\bar g_j:=\frac1N\sum_{r=0}^{N-1}g_{j+r}.
\tag{28}
\]

The standard variance identity gives

\[
V_j^{(N)}
=\frac1{2N}
\sum_{0\le r<s<N}
(g_{j+r}-g_{j+s})^2.
\tag{29}
\]

Summing uniformly over all translates and counting how many length-`N` blocks contain a pair at separation `d` gives

\[
\boxed{
\sum_jV_j^{(N)}
=\frac1{2N}
\sum_{d=1}^{N-1}(N-d)
\sum_i(g_{i+d}-g_i)^2.
}
\tag{30}
\]

For a compact perturbation of a constant background the sums are finite. Equation (30) is exactly a nonzero finite-range symmetric translation-invariant quadratic form annihilating constants, so Sections 2--4 apply.

Thus the most literal overlapping-block proposal left by XF-020--XF-021 fails as a universal mechanism:

\[
\boxed{
\text{uniform overlap of fixed-length block variances}
\not\Rightarrow
\text{collision-safe upper Lyapunov}.}
\tag{31}
\]

Overlap makes a collapsing gap interior to many blocks, and those interior pieces do contribute negative dissipation. But after all translates are summed, the remaining singular coefficient is the higher-order kernel `AL`; its finite-range side lobes cannot keep a one-sided sign while still annihilating constants.

## 6. Smallest explicit witness

For `N=2`,

\[
\sum_jV_j^{(2)}
=\frac14\sum_j(g_{j+1}-g_j)^2.
\tag{32}
\]

Take a constant background `h=1` and modify only

\[
g_{-1}=M,
\qquad
g_0=1,
\qquad
g_1=\epsilon,
\qquad
g_2=1,
\qquad
g_3=1.
\tag{33}
\]

A direct differentiation using the two singular adjacent conductances gives

\[
\boxed{
\left(\sum_jV_j^{(2)}\right)'
=\frac{M-7}{\epsilon}+O(1).
}
\tag{34}
\]

Hence every fixed `M>7` gives an explicit positive collision spike. This is a useful stress test because it shows that the obstruction is not a delicate high-range effect: the simplest overlapping variance already fails once a neighboring gap carries enough asymmetric mass.

## 7. Exact boundary of the no-go

The finite-range hypothesis is substantive. The proof uses that `AL` has finite support, so a one-sided off-diagonal sign together with zero second moment forces the kernel to vanish. The finding therefore does **not** rule out a genuinely global mean-removal operator whose coupling does not decay to zero at a fixed finite range, nor a scale-dependent family whose control uses additional Xi information to restrict the allowed gap configurations.

It also does not rule out nonlinear functionals. The uncentered carrier of XF-018 is nonlinear in the zero geometry after the conductance is absorbed into the bounded cross-ratio weight, and the span term is not a translation-invariant quadratic convolution on the gap lattice. Signed projective identities, multiscale renormalizations, or exact endpoint flux formulas can therefore escape the theorem's hypothesis.

Most importantly, the conclusion is again **universal rather than Xi-specific**. It says that order, positivity of the conductances, finite-range translation invariance, and quadratic mean removal are insufficient. A candidate may still work for Xi if an unconditional source theorem excludes the large-gap asymmetry used in Section 4 or supplies another signed relation. Such an argument would be genuinely source-facing rather than a formal consequence of the gap ODE.

## 8. Prior art and novelty boundary

The matrix sign mechanism is a discrete higher-order maximum-principle obstruction. The broad literature on biharmonic and graph bi-Laplacian evolutions already shows that composing Laplacian-type operators generally destroys the Markov/maximum-principle sign pattern, with exceptional highly global graph geometries. A targeted search in that literature found the expected neighboring results, so no novelty is claimed for the generic fact that higher-order discrete operators need not be M-matrices.

No external theorem is load-bearing here. The proof needed for the Xi-flow claim is the elementary finite-range moment argument (16)--(22) combined with the exact adjacent-gap singularity from XF-014. The durable contribution is the line-specific identification of the **collision operator `AL`** and the resulting no-go for the exact overlapping-block quadratic mean-removal strategy left open by XF-020--XF-021. Because no external result is required to establish that statement, `SOURCES.md` is unchanged.

## 9. Consequence for `xi_flow`

The broad-buffer program now has a sharper branching point. XF-019--XF-020 already make the far exterior negligible for the collision-safe uncentered carrier, and XF-021 shows that compact centered convex entropies reintroduce a positive collision pole. XF-022 adds that **finite-range quadratic overlap does not repair the problem either**.

The next useful target should therefore be genuinely outside that class. Two concrete possibilities remain mathematically distinct: derive an exact nonlocal span/endpoint-flux identity whose mean removal is global or projective rather than finite-range quadratic, or import Xi-specific aggregate information strong enough to control the asymmetric local gap patterns that make `(ALg)_1` positive. A further search over fixed-length overlapping variances or other finite-range centered quadratic stencils should be treated as closed unless it introduces such additional structure.