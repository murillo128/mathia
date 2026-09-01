# WP-094 — Exact cover covariance collapses positive block-Toeplitz forms to the singular endpoint anchor

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + INFINITE-RANGE-CLASSIFICATION + BLOCK-TOEPLITZ + CLASSICAL-HERGLOTZ + MATCHED-CONTROL`.

`WP-093` classifies the fixed-finite-band positive forms satisfying the exact Mathia cover law

\[
W_n^*AW_n=nA,
\]

and leaves a genuine nonlocal loophole: an infinite-range positive kernel might retain enough cross-scale structure to escape the weighted-Dirichlet/Cesaro classification. The most canonical stationary version of that loophole can be closed completely.

Let `K` be a finite-dimensional Hilbert space and let `q_A` be any positive Hermitian **block-Toeplitz** quadratic form on `c_00(N_0;K)`,

\[
q_A(x)=\sum_{j,k\ge0}\langle x_j,A_{j-k}x_k\rangle_K,
\qquad
A_{-m}=A_m^*.
\tag{1}
\]

No finite bandwidth, decay, bounded-operator assumption, Markov property, or place-additive decomposition is imposed. Assume only exact degree-one covariance for the normalized cover/refinement isometries

\[
W_ne_k=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r}:
\qquad
q_A(W_nx)=nq_A(x)
\quad(n\ge1).
\tag{2}
\]

Then positivity and the single case `n=2` already force

\[
\boxed{
q_A(x)=\left\langle R\sum_{j\ge0}x_j,\sum_{j\ge0}x_j\right\rangle_K
}
\tag{3}
\]

for one positive operator `R>=0` on `K`. Equivalently,

\[
\boxed{A_m=R\quad\text{for every }m\in\mathbb Z.}
\tag{4}
\]

Conversely every form (3) satisfies (2) for every integer cover degree. Thus the whole positive finite-dimensional block-Toeplitz exact-cover-covariant cone is exactly the cone of positive endpoint-evaluation forms at `z=1`.

This survivor is singular in the ambient Hardy/`ell^2` topology. Every nonzero form (3) is **not closable** on `ell^2(N_0;K)`. Consequently

\[
\boxed{
\text{positive + block-Toeplitz + exact cover covariance + closable}
\Longrightarrow q_A=0.
}
\tag{5}
\]

So merely replacing the finite-range kernel of `WP-093` by an arbitrary stationary infinite-range positive kernel cannot produce a global Weil geometry. Exact cover covariance pushes the entire Toeplitz spectral measure onto the distinguished boundary point, reproducing the singular boundary-anchor phenomenon already encountered elsewhere in the line rather than a finite-energy global pairing.

## 1. The block-Toeplitz hypothesis is the stationary nonlocal escape

For `x=(x_0,x_1,...)` of finite support write the `K`-valued analytic polynomial

\[
f_x(z)=\sum_{j\ge0}x_jz^j.
\tag{6}
\]

The Toeplitz condition in (1) means that the interaction depends only on coefficient separation `j-k`. It is therefore the natural Hardy-shift-stationary class of infinite-range kernels. This is deliberately different from rotation-invariant Hilbert metrics such as those classified in `WP-071`, which are diagonal in the monomial basis. Here every distance `|j-k|` may interact, with arbitrary matrix-valued coefficients.

The normalized Mathia cover map has the polynomial form

\[
(W_nf)(z)
=\frac1{\sqrt n}D_n(z)f(z^n),
\qquad
D_n(z)=1+z+\cdots+z^{n-1}.
\tag{7}
\]

The question is whether a positive stationary nonlocal form can obey the same exact scale law as the positive finite-band geometry of `WP-093` while retaining nontrivial spectral support around the circle.

It cannot.

## 2. Positivity gives a classical Herglotz representation

Because every finite block Toeplitz matrix extracted from (1) is positive semidefinite, the operator-valued trigonometric moment/Herglotz theorem gives a finite positive operator-valued measure `M` on the unit circle `T` such that

\[
A_m=\int_{\mathbb T}z^{-m}\,dM(z)
\tag{8}
\]

(up to the harmless Fourier-sign convention), and

\[
\boxed{
q_A(x)=\int_{\mathbb T}
\langle dM(z)f_x(z),f_x(z)\rangle_K.
}
\tag{9}
\]

For finite-dimensional `K` this can also be obtained by applying the scalar Herglotz theorem to

\[
\mu_v(E)=\langle M(E)v,v\rangle
\]

and recovering the mixed matrix coefficients by polarization.

Nothing arithmetic has entered here. This is standard harmonic analysis: scalar positive-definite sequences on `Z` are Fourier coefficients of positive measures on `T`, with block/operator-valued Toeplitz positivity giving the corresponding matrix-valued version. The new question is what the specific Mathia cover covariance does to that positive measure.

## 3. The two-fold cover is already extremal

Take the constant polynomial

\[
f(z)=v,
\qquad v\in K.
\tag{10}
\]

For `n=2`, equation (7) gives

\[
W_2v=\frac{1+z}{\sqrt2}v.
\tag{11}
\]

Apply exact covariance (2) to this one vector. With the positive scalar measure

\[
\mu_v(E)=\langle M(E)v,v\rangle,
\tag{12}
\]

we obtain

\[
\frac12\int_{\mathbb T}|1+z|^2\,d\mu_v(z)
=2\mu_v(\mathbb T).
\tag{13}
\]

Equivalently,

\[
\int_{\mathbb T}
\bigl(4-|1+z|^2\bigr)\,d\mu_v(z)=0.
\tag{14}
\]

On the unit circle there is the exact identity

\[
4-|1+z|^2
=|1-z|^2\ge0,
\tag{15}
\]

and equality holds only at `z=1`. Since `mu_v` is positive, (14) forces

\[
\boxed{\operatorname{supp}\mu_v\subseteq\{1\}.}
\tag{16}
\]

This holds for every `v in K`. Hence for every Borel set `E` disjoint from `1`,

\[
\langle M(E)v,v\rangle=0
\quad\text{for all }v.
\]

Positivity and polarization imply `M(E)=0`. Therefore the full operator-valued measure is supported at the single point `1`:

\[
\boxed{M=R\,\delta_1,\qquad R=M(\mathbb T)\succeq0.}
\tag{17}
\]

Substitution in (8)--(9) immediately gives (3)--(4).

The mechanism is worth isolating. The critical cover scaling asks the constant vector to attain the **maximum possible Dirichlet-kernel amplification**. For `n=2`,

\[
|D_2(z)|=|1+z|\le2,
\]

and positivity prevents cancellation between points where the inequality is strict. Exact saturation therefore concentrates the entire stationary positive geometry at the unique maximizer `z=1`.

No large-`n` asymptotic, regularization, analytic continuation, or spectral approximation is involved.

## 4. Converse: endpoint evaluation is exactly cover covariant

For completeness, take any `R>=0` and define (3). Since

\[
D_n(1)=n,
\]

equation (7) gives

\[
(W_nf)(1)=\sqrt n\,f(1).
\tag{18}
\]

Therefore

\[
\begin{aligned}
q_R(W_nx)
&=\langle R(W_nf_x)(1),(W_nf_x)(1)\rangle\\
&=n\langle Rf_x(1),f_x(1)\rangle\\
&=nq_R(x).
\end{aligned}
\tag{19}
\]

Thus there is no missing Toeplitz branch hidden by the proof: (17) gives the **complete positive cone** under the stated hypotheses.

The scalar case is simply

\[
q(x)=r\left|\sum_jx_j\right|^2,
\qquad r\ge0.
\tag{20}
\]

A finite internal fibre changes only the positive matrix `R`; it cannot create another circle frequency or a nontrivial scale response.

## 5. Every nonzero survivor is nonclosable on the ambient Hilbert space

The endpoint form (3) is densely defined on `c_00(N_0;K)`, but it does not define a closable positive energy in the ambient `ell^2` topology unless `R=0`.

Assume `R!=0` and choose `v in K` with

\[
\langle Rv,v\rangle>0.
\tag{21}
\]

For `N>=1`, define

\[
x^{(N)}_j=
\begin{cases}
v/N,&0\le j<N,\\0,&j\ge N.
\end{cases}
\tag{22}
\]

Then

\[
\|x^{(N)}\|_{\ell^2(K)}^2
=\frac{\|v\|^2}{N}
\longrightarrow0,
\tag{23}
\]

while

\[
\sum_jx^{(N)}_j=v
\]

for every `N`, so

\[
q_R(x^{(N)})=\langle Rv,v\rangle>0.
\tag{24}
\]

Moreover every pair has the same endpoint sum, hence

\[
q_R(x^{(N)}-x^{(M)})=0.
\tag{25}
\]

Thus `x^(N)->0` in the ambient Hilbert space and is Cauchy in form seminorm, but its form energy does not tend to zero. This violates the standard closability criterion for positive quadratic forms. Hence

\[
\boxed{R\ne0\Longrightarrow q_R\text{ is not closable on }\ell^2(\mathbb N_0;K).}
\tag{26}
\]

Combining the classification with (26) proves (5).

## 6. Matched controls identify exactly what has been lost

### 6.1 `WP-093` escapes only by breaking Toeplitz stationarity

The critical positive survivor of `WP-093` is

\[
G=T^*T,
\qquad
(Tx)_j=(j+1)(x_{j+1}-x_j),
\tag{27}
\]

with energy

\[
\sum_{j\ge0}(j+1)^2|x_{j+1}-x_j|^2.
\]

Its coefficients depend strongly on absolute position `j`; it is not Toeplitz. There is therefore no contradiction between `WP-093` and the present theorem. Instead the two results give a sharp structural split:

\[
\boxed{
\begin{array}{ll}
\text{fixed finite range, position-dependent} &\Rightarrow\text{nontrivial closable weighted Dirichlet cone},\\
\text{arbitrary infinite range, Toeplitz stationary} &\Rightarrow\text{endpoint delta, nonclosable if nonzero}.
\end{array}}
\tag{28}
\]

So adding long-range couplings while preserving coefficient-shift stationarity is not the missing ingredient.

### 6.2 This is stronger than the Markov-symbol obstruction of `WP-039` in a different direction

`WP-039` assumes a translation-invariant **Markov/Dirichlet** form on a compact abelian group and rules out exact Mangoldt support because the zero set of a conditionally negative-definite Fourier symbol is a subgroup.

Here there is no Markov property and no attempt to prescribe Mangoldt support to a Fourier symbol. The argument classifies every positive Toeplitz form obeying the cover covariance before any arithmetic scalarization is attempted. Its conclusion is therefore independent of the subgroup-zero-set obstruction.

### 6.3 This is not the rotation-invariant renorming theorem of `WP-071`

`WP-071` assumes a positive rotation-invariant Hilbert completion, which makes monomials orthogonal, and proves that bounded boundary evaluation is incompatible with retaining a cyclotomic shell function. The present form has the opposite matrix geometry: Toeplitz stationarity allows all off-diagonal coefficient couplings but exact cover covariance itself collapses them to boundary evaluation.

The two obstructions meet at the same singular object from different hypotheses. `WP-071` says the Mangoldt boundary anchor cannot become bounded while preserving the shell inside a rotation-invariant Hilbert metric; the present theorem says a stationary positive exact-cover form has **no choice but** to become that boundary anchor, and then proves directly that it is nonclosable.

### 6.4 All-integer control

The endpoint form satisfies (19) for every integer `n>=1`. Nothing recognizes primes, prime powers, or the arithmetic of `Q`. Replacing prime-labelled covers by arbitrary composite cover degrees leaves both positivity and covariance unchanged.

Thus even before the nonclosability obstruction, the surviving stationary cone is an arithmetically universal cover geometry rather than a Riemann-specific finite-prime mechanism.

## 7. It supplies neither the finite Weil selector nor the archimedean completion

The form (3) has only one scalar geometric location, `z=1`. Its cover response is exactly the homogeneous factor `n` from (19). There is no intrinsic mechanism selecting prime powers, no `Lambda(n)` coefficient, and no place where the completed-zeta Gamma factor or the polar/global counterterms arise.

One can of course apply an external logarithm to the known scale factor and manufacture `log n`, or apply Möbius inversion to manufacture prime-power support. Those are precisely the post-hoc nonlinear/arithmetic operations excluded by the research mandate unless another Mathia structure forces them while preserving an independent sign theorem.

Likewise, the singularity of endpoint evaluation is not a useful source of positivity by itself. `WP-068`, `WP-069`, and `WP-071` already isolate the difficulty of turning the exact Mangoldt boundary readout into a bounded finite-energy anchor. The present theorem shows that stationary infinite-range cover positivity runs directly into the same boundary rather than bypassing it.

## 8. Prior-art and novelty audit

The representation step is classical. Herglotz's theorem characterizes positive-definite sequences on `Z` as Fourier coefficients of finite positive measures on the circle; standard references include Yitzhak Katznelson, *An Introduction to Harmonic Analysis*, 3rd ed., Cambridge University Press (2004), DOI `10.1017/CBO9781139165372`, and the general locally compact abelian formulation in Walter Rudin, *Fourier Analysis on Groups*.

Block Toeplitz positivity is likewise standard operator-system territory. Douglas Farenick, *The operator system of Toeplitz matrices*, Trans. Amer. Math. Soc. Ser. B 8 (2021), 999–1023, DOI `10.1090/btran/83`, develops modern positive/block-Toeplitz structure. Christopher Deninger, *Invariant measures on the circle and functional equations*, arXiv:`1111.6416`, is a nearby but different comparison: multiplication-map invariance of circle measures produces functional equations for Herglotz transforms.

A directed search over positive Toeplitz forms, block/operator-valued Herglotz representations, Hardy weighted-composition/refinement operators, multiplication-map invariant measures, and Dirichlet-kernel transfer identities found abundant classical machinery for the ingredients but no source asserting the Mathia-specific implication

\[
q(W_nx)=nq(x)
\quad+\quad
q\text{ positive Toeplitz}
\quad\Longrightarrow\quad
M=R\delta_1.
\]

No novelty is claimed for Herglotz theory, Toeplitz positivity, Dirichlet-kernel extremality, or the closability criterion. The durable Mathia result is the exact classification produced by applying those classical tools to the normalized cover isometries of this research line.

## 9. Boundary of the no-go and falsification test

The theorem uses four hypotheses:

1. a scalar or finite-dimensional block coefficient space `K`;
2. Toeplitz dependence `A_{jk}=A_{j-k}`;
3. positivity on all finitely supported vectors;
4. exact cover covariance `q(W_nx)=nq(x)`, in fact only for `n=2` for the forward classification.

A single positive block-Toeplitz form satisfying the `n=2` law whose Herglotz measure has support away from `1` would falsify the classification. Equation (14)--(16) shows why such a counterexample cannot exist under these hypotheses.

The result does **not** classify:

- position-dependent infinite-range kernels;
- degree-dependent or noncoherent kernel families;
- genuinely nonseparable couplings in which prime labels act before reduction to one stationary coefficient direction;
- infinite-dimensional internal sectors requiring additional domain/operator-valued-measure hypotheses;
- constructions that are not positive before a later canonical compression or quotient;
- nonlinear volume/rank mechanisms such as `WP-030`.

In particular, no conclusion is claimed for a nonlocal kernel `A_{jk}` carrying arithmetic information through the absolute positions `(j,k)` rather than through their difference alone.

## Research consequence

`WP-093` left two broad ways to escape its finite-range classification: increase interaction range, or add genuinely nonseparable arithmetic/global structure. The present result eliminates the first option whenever the long-range extension remains Hardy-shift stationary:

\[
\boxed{
\text{arbitrary Toeplitz range}
+\text{ positivity}
+\text{ exact Mathia cover covariance}
\Longrightarrow
\text{singular endpoint evaluation}.
}
\tag{29}
\]

A viable infinite-range continuation must therefore break Toeplitz stationarity in an **intrinsically forced** way. It must use absolute scale/position, prime-sensitive incidence, a genuinely transforming global sector, or another nonseparable structure before positivity/scalarization, while still surviving the all-integer/generalized-prime controls and independently generating the finite-prime, archimedean, and polar pieces of the Weil form.

Merely adding a stationary long-range positive kernel does not move the frontier.