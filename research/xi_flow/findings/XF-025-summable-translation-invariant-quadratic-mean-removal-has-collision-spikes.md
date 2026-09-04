# XF-025 — summable translation-invariant quadratic mean removal has unavoidable collision spikes

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `STRUCTURAL/BOUNDARY`. XF-022 ruled out every nonzero **finite-range** symmetric translation-invariant quadratic mean-removal kernel. Its proof used a vanishing second moment for the collision operator `AL`, so a natural escape remained: let the quadratic coupling have a genuinely infinite but summable tail, for example a slowly decaying multiscale convolution obtained by combining block variances across arbitrarily large fixed scales.

That escape also fails. Let

\[
L=(L_d)_{d\in\mathbb Z}\in \ell^1(\mathbb Z)
\]

be real, symmetric, nonzero, and annihilate constants,

\[
L_{-d}=L_d,
\qquad
\sum_dL_d=0.
\]

For compact perturbations `u=g-h` of a constant positive gap background, define

\[
Q_L(g)=\frac12\sum_i u_i(L*u)_i.
\]

If a single gap `g_1=\varepsilon\downarrow0` collapses while all other gaps remain fixed positive, the exact logarithmic-repulsion gap dynamics again has

\[
\boxed{
Q_L'
=\frac{2}{\varepsilon}(ALg)_1+O(1),
}
\]

where

\[
(Av)_i=2v_i-v_{i-1}-v_{i+1}.
\]

The new result is that for every such nonzero summable `L`, the convolution kernel `m` of `M:=AL` has a **positive off-diagonal coefficient**. No moment assumption is needed. Therefore one can choose a positive compact perturbation for which `(ALg)_1>0`, giving

\[
\boxed{
Q_L'\to+\infty.
}
\]

Hence **no nonzero absolutely summable translation-invariant quadratic constant-mode remover is collision-safe from above using only the universal Xi/log-repulsion gap equation**. The finite-range hypothesis of XF-022 is unnecessary once the kernel itself is summable.

This closes fixed decaying multiscale quadratic overlap, including any construction whose effective translation-invariant convolution kernel lies in `\ell^1`. It does not rule out non-summable/global mean removal, configuration- or time-dependent kernels, nonlinear/projective flux identities, or Xi-specific spacing information that excludes the collision witnesses.

## 1. The summable quadratic class

Fix `h>0` and let `L\in\ell^1(\mathbb Z)` satisfy

\[
L_{-d}=L_d\in\mathbb R,
\qquad
\sum_{d\in\mathbb Z}L_d=0,
\qquad
L\not\equiv0.
\tag{1}
\]

For a finitely supported perturbation

\[
u_i:=g_i-h,
\tag{2}
\]

define

\[
\boxed{
Q_L(g)
:=\frac12\sum_i u_i(L*u)_i.
}
\tag{3}
\]

Because `u` is finitely supported and `L\in\ell^1`, the sum is absolutely convergent. Symmetry gives the gradient

\[
\boxed{
p_i:=\frac{\partial Q_L}{\partial g_i}=(L*u)_i=(L*g)_i,}
\tag{4}
\]

where the last equality uses `L*1=0`. The sequence `p` lies in `\ell^1`.

No positivity assumption on `L` is required for the obstruction. In the intended mean-removal applications `L` would normally be positive semidefinite, but allowing indefinite kernels only strengthens the no-go.

## 2. A collapsing gap still probes `AL`

Place the collapsing gap at index `1`,

\[
g_1=\varepsilon\downarrow0,
\tag{5}
\]

and keep all other gaps fixed positive. Write

\[
g_0=a>0,
\qquad
g_2=b>0.
\tag{6}
\]

In the exact real-simple gap equation of XF-014, the only conductances singular in `\varepsilon` are the two adjacent ones,

\[
c_{0,1}=\frac1{a\varepsilon},
\qquad
c_{1,2}=\frac1{\varepsilon b}.
\tag{7}
\]

Exactly as in XF-022, the corresponding pair contributions to `Q_L'` are

\[
\frac{2}{\varepsilon}(p_1-p_0)+O(1)
\tag{8}
\]

and

\[
\frac{2}{\varepsilon}(p_1-p_2)+O(1).
\tag{9}
\]

Hence

\[
\boxed{
Q_L'
=\frac{2}{\varepsilon}
(2p_1-p_0-p_2)+O(1)
=\frac{2}{\varepsilon}(ALg)_1+O(1).
}
\tag{10}
\]

For the compact perturbations used below, the nonadjacent part is genuinely `O(1)`: `p\in\ell^1`, while the perturbation-induced velocities on an asymptotically arithmetic ordered control decay quadratically with distance. Equivalently, the coefficient of the only possible `1/\varepsilon` pole is local and is exactly (10), regardless of how the bounded remainder is represented.

Thus the finite-range issue in XF-022 was not needed to identify the collision operator. It entered only in the earlier sign proof.

## 3. Fourier sign obstruction without a moment assumption

Let

\[
M:=AL
\tag{11}
\]

and denote its convolution kernel by `m=(m_d)`. Since `A` has finite support and `L\in\ell^1`, also

\[
m\in\ell^1(\mathbb Z).
\tag{12}
\]

Moreover `m` is real and symmetric, and because both factors annihilate constants,

\[
\sum_dm_d=0.
\tag{13}
\]

Suppose for contradiction that every off-diagonal coefficient had the collision-safe sign

\[
m_d\le0
\qquad(d\ne0).
\tag{14}
\]

Set

\[
r_d:=-m_d\ge0
\qquad(d\ge1).
\tag{15}
\]

By symmetry and (13),

\[
m_0=2\sum_{d\ge1}r_d.
\tag{16}
\]

The Fourier symbol of `M` is therefore

\[
\boxed{
\widehat M(\theta)
=2\sum_{d\ge1}r_d(1-\cos d\theta)
\ge0.
}
\tag{17}
\]

The nearest-neighbor Laplacian has symbol

\[
\widehat A(\theta)=2-2\cos\theta.
\tag{18}
\]

For `\theta\ne0` modulo `2\pi`,

\[
\boxed{
\widehat L(\theta)
=\frac{\widehat M(\theta)}{\widehat A(\theta)}.
}
\tag{19}
\]

Because `L\in\ell^1`, its Fourier series is continuous, and (1) gives

\[
\widehat L(0)=0.
\tag{20}
\]

If `M` were nonzero under the sign assumption (14), some `r_{d_*}>0`. Keeping only that one nonnegative term in (17),

\[
\frac{\widehat M(\theta)}{\widehat A(\theta)}
\ge
r_{d_*}
\frac{1-\cos(d_*\theta)}{1-\cos\theta}.
\tag{21}
\]

As `\theta\to0`,

\[
\frac{1-\cos(d_*\theta)}{1-\cos\theta}
\longrightarrow d_*^2,
\tag{22}
\]

so

\[
\liminf_{\theta\to0}
\widehat L(\theta)
\ge r_{d_*}d_*^2>0,
\tag{23}
\]

contradicting continuity and (20).

Thus the only way (14) could hold is `M\equiv0`. But then

\[
\widehat A(\theta)\widehat L(\theta)=0
\tag{24}
\]

for every `\theta`. Since `\widehat A(\theta)>0` away from zero, `\widehat L(\theta)=0` there, and continuity gives `\widehat L(0)=0` as well. Hence `L=0`, again contradicting (1).

Therefore every nonzero summable constant-annihilating symmetric kernel satisfies

\[
\boxed{
\exists d\ne0:\qquad m_d>0.
}
\tag{25}
\]

This is stronger than the second-moment argument of XF-022. It requires neither finite support nor existence of any weighted moment of `L` or `m`.

## 4. A positive off-diagonal coefficient gives a positive collision pole

Because `M` annihilates constants,

\[
(Mg)_1
=\sum_dm_d(g_{1-d}-h).
\tag{26}
\]

Choose `d_*\ne0` with `m_{d_*}>0`. Keep every gap at the background value `h` except

\[
g_1=\varepsilon,
\qquad
g_{1-d_*}=H,
\tag{27}
\]

with `H>h` fixed. Then

\[
(Mg)_1
=m_{d_*}(H-h)+m_0(\varepsilon-h).
\tag{28}
\]

Since `m_{d_*}>0`, choose `H` sufficiently large that the right side has a strictly positive limit as `\varepsilon\downarrow0`. Equation (10) then yields

\[
\boxed{
Q_L'
=\frac{2c_*}{\varepsilon}+O(1)
\longrightarrow+\infty
}
\tag{29}
\]

for some `c_*>0`.

If `d_*=\pm1`, the large witness gap is one of the two noncollapsing gaps adjacent to `\varepsilon`; the leading law (10) is unchanged because the singular pair calculation does not require `a` or `b` to equal the background, only to remain fixed and positive.

Thus no inequality asserting a universal upper Lyapunov bound for `Q_L` can follow from the positive-conductance gap equation over all positive ordered configurations.

## 5. What fixed multiscale quadratic overlap is now closed

XF-022 already covered a uniform sum of all translates of a block variance at one fixed finite length. A natural next attempt is a positive or signed combination over arbitrarily many fixed lengths,

\[
Q(g)=\sum_{N\ge2}\beta_N\sum_jV_j^{(N)},
\tag{30}
\]

provided the resulting translation-invariant quadratic kernel is absolutely summable and the series defines the corresponding convolution form on compact perturbations.

Whenever those hypotheses hold, the effective kernel is exactly an `L` of the class above. Therefore the infinitely many artificial block boundaries cannot cancel into a collision-safe mean remover merely because the range is unbounded:

\[
\boxed{
L\in\ell^1,\quad L1=0,\quad L\ne0
\quad\Longrightarrow\quad
\text{some positive collision witness has }Q_L'\to+\infty.
}
\tag{31}
\]

The escape from XF-022 is therefore not "use a longer decaying quadratic stencil." To leave the theorem one must lose at least one of its structural hypotheses: summability/decay, translation invariance, fixed coefficients, quadraticity, or source-free universality over positive gap configurations.

## 6. Boundary of the theorem

The `\ell^1` hypothesis is substantive. It gives a continuous Fourier symbol and is exactly what turns constant annihilation into the boundary condition `\widehat L(0)=0`. The argument does **not** rule out genuinely non-summable global projectors or kernels whose effective coupling grows with the observation scale. The literal projection onto the orthogonal complement of the constant mode on a finite block is an example of an operation whose thermodynamic/global limit does not become a fixed summable convolution kernel.

Configuration- or time-dependent kernels are also outside the theorem because their own derivative contributes additional terms that could, in principle, cancel the adjacent pole. Likewise, a nonlinear signed flux identity need not have a convolution gradient at all.

Most importantly, the witness uses only positivity of gaps and the universal adjacent logarithmic-repulsion singularity. It does not prove that the actual Xi zero configuration realizes the required large-gap/collision pattern. An Xi-specific spacing theorem excluding that geometry, or coupling the smallest gap to the multiscale kernel itself, could still rescue a scale-dependent construction.

The finding remains entirely on the real-simple side of a collision. It studies `\varepsilon\downarrow0` and does not continue the ordered zero ODE through the collision time.

## 7. Prior art and novelty boundary

The sign pattern in (17) is the standard symbol of a symmetric translation-invariant Markov/Laplacian generator, and the general principle that higher-order or factored elliptic operators lose maximum-principle structure is classical. A targeted prior-art check across discrete maximum principles, M-matrices, nonlocal/fractional Laplacians, and higher-order Laplacian operators found the expected broad theory but no source whose stated result is the particular `\ell^1` factorization obstruction (19)--(25) in the Xi gap-collision setting.

No novelty claim is based on that absence, and no external theorem is load-bearing: the proof is the elementary Fourier-series argument above combined with the adjacent collision law already derived from XF-014. Accordingly `SOURCES.md` needs no new entry.

The durable contribution is the exact sharpening of XF-022's research boundary: **finite range was not the real reason quadratic overlap failed. Absolute summability plus constant annihilation is already enough to force a positive side lobe in the collision operator `AL`.**

## 8. Consequence for `xi_flow`

After XF-021--XF-025, the broad-buffer program should treat fixed decaying translation-invariant quadratic mean removal as closed, even when it combines infinitely many spatial scales. The collision-safe carrier of XF-018 and the super-mesoscopic far-tail control of XF-019--XF-020 therefore cannot be completed by replacing finite overlap with an `\ell^1` multiscale quadratic convolution.

The surviving mean-removal mechanisms are now genuinely global/non-summable, adaptive/configuration-dependent, nonlinear/projective, or Xi-specific. In particular, an exact endpoint/span flux identity remains conceptually different from the class ruled out here: its coefficients depend on the physical block geometry and need not define a fixed summable convolution on index space.