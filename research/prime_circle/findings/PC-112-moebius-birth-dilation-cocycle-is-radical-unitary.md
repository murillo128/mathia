# PC-112 — Möbius births of the affine dilation cocycle are radical-unitary

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-111 leaves an infinite-scale direct sum/product as one possible way to escape the fact that every fixed affine relative-scale defect is trace class. The most intrinsic exact-order organization of those scales is the same Möbius birth extraction that defines primitive Prime-Circle layers. For the PC-111 dilation cocycle it can be classified exactly.

Let

\[
E_h=D_h-D_1,
\qquad
D_h=U_hD_1U_h^*,
\qquad h>0,
\]

be the trace-class affine-scale cocycle of PC-111, so

\[
E_{hk}=E_h+U_hE_kU_h^*,
\qquad
\operatorname{Tr}E_h=\frac12\log h.
\]

For an integer level `n>1`, define its exact-order/Möbius birth operator by

\[
\boxed{
B_n:=\sum_{d\mid n}\mu(n/d)E_d.
}
\]

Then, writing

\[
R=\operatorname{rad}(n),
\qquad
m=n/R,
\qquad
\alpha_h(T):=U_hTU_h^*,
\]

one has the exact factorization

\[
\boxed{
B_n
=\alpha_m B_R
=\alpha_m\prod_{p\mid R}(\alpha_p-I)D_1.
}
\]

Hence every `B_n` is trace class and is unitarily equivalent to the squarefree-radical block `B_rad(n)`. In particular, along every prime-power tower,

\[
\boxed{
B_{p^k}=\alpha_{p^{k-1}}E_p,
\qquad k\ge1,
}
\]

so **all singular values, eigenvalues, Schatten norms, and the complete Fredholm determinant are independent of the exponent `k`**. The trace is nevertheless the exact common-vertex von Mangoldt weight,

\[
\boxed{
\operatorname{Tr}B_n=\frac12\Lambda(n).
}
\]

Thus the canonical Möbius extraction lifts the scalar von Mangoldt identity to a trace-class operator identity, but repeated prime-power depth contributes only unitary copies of one fixed prime block. The unweighted infinite direct sum/product suggested by PC-111 therefore cannot become a compact Fredholm mechanism: every prime-power ray repeats a nonzero compact block with constant norm forever. Adding a Dirichlet weight restores convergence, but then the operator Dirichlet series factors by the classical reciprocal zeta multiplier and its trace is exactly `-zeta'/2zeta`; no new critical-line mechanism is created.

No historical novelty is claimed for Möbius inversion, the von Mangoldt divisor identity, Dirichlet-series multiplication, trace ideals, or multiplicative dilation dynamics. The durable Prime-Circle content is the exact interaction between those standard operations and the specific geometry-forced PC-111 trace-class dilation cocycle.

## 1. The PC-111 scale family is an additive cocycle for unitary dilation

Put

\[
\alpha_h(T)=U_hTU_h^*.
\]

Because `U_hU_k=U_hk`, the maps `alpha_h` form a commuting multiplicative action. PC-111 gives

\[
D_h=\alpha_h(D_1),
\]

and therefore

\[
\boxed{
E_h=(\alpha_h-I)D_1.
}
\]

The cocycle relation is then simply

\[
E_{hk}
=(\alpha_{hk}-I)D_1
=(\alpha_h-I)D_1+\alpha_h(\alpha_k-I)D_1
=E_h+\alpha_h(E_k).
\]

The important point for the present question is that the scale variable already acts through a **commuting unitary representation**. Möbius birth extraction therefore becomes a finite-difference operation in that representation rather than a new noncommutative refinement law.

## 2. Exact Möbius factorization through the squarefree radical

For `n>1`, insert `E_d=(alpha_d-I)D_1` into the definition of `B_n`:

\[
B_n
=\sum_{d\mid n}\mu(n/d)\alpha_d(D_1)
-\left(\sum_{d\mid n}\mu(n/d)\right)D_1.
\]

The second term vanishes because

\[
\sum_{d\mid n}\mu(n/d)=0.
\]

Let `R=rad(n)` and `m=n/R`. The only divisors contributing to the Möbius sum are `d=n/e` with `e|R`. Hence

\[
\begin{aligned}
B_n
&=\sum_{e\mid R}\mu(e)\alpha_{mR/e}(D_1)\\
&=\alpha_m
\sum_{e\mid R}\mu(e)\alpha_{R/e}(D_1).
\end{aligned}
\]

Since the `alpha_p` commute, the squarefree sum factors exactly:

\[
\sum_{e\mid R}\mu(e)\alpha_{R/e}
=
\prod_{p\mid R}(\alpha_p-I).
\]

Therefore

\[
\boxed{
B_n
=\alpha_{n/\operatorname{rad}(n)}
\prod_{p\mid\operatorname{rad}(n)}(\alpha_p-I)D_1.
}
\]

For the squarefree level itself,

\[
\boxed{
B_R=\prod_{p\mid R}(\alpha_p-I)D_1,
}
\]

so

\[
\boxed{B_n=\alpha_{n/R}(B_R).}
\]

Because `alpha_h` is unitary conjugation, this proves the complete radical-unitary classification. In particular,

\[
\boxed{
\operatorname{Spec}(B_n)=\operatorname{Spec}(B_R),
\qquad
s_j(B_n)=s_j(B_R),
}
\]

with multiplicity, and for every Schatten exponent `q>=1`,

\[
\boxed{
\|B_n\|_{\mathcal S_q}=\|B_R\|_{\mathcal S_q}.
}
\]

Since each `B_n` is a finite linear combination of the trace-class `E_d`, it lies in `S_1`. Therefore its ordinary Fredholm determinant also depends only on the radical:

\[
\boxed{
\det(I-zB_n)=\det(I-zB_R).
}
\]

This is stronger than a scalar prime-power collapse: the **entire exact-order compact operator shape** forgets every repeated-prime exponent.

## 3. Prime-power births are one fixed block moving by dilation

For `n=p^k`, the divisor Möbius sum has only two nonzero terms:

\[
B_{p^k}=E_{p^k}-E_{p^{k-1}}.
\]

Using the PC-111 cocycle,

\[
E_{p^k}
=E_{p^{k-1}}+\alpha_{p^{k-1}}E_p,
\]

so

\[
\boxed{
B_{p^k}=\alpha_{p^{k-1}}E_p.
}
\]

Thus for every `k>=1`,

\[
\boxed{
\|B_{p^k}\|=\|E_p\|>0,
\qquad
\det(I-zB_{p^k})=\det(I-zE_p).
}
\]

The strict positivity of the norm needs no separate spectral calculation: PC-111 gives

\[
\operatorname{Tr}E_p=\frac12\log p\ne0,
\]

so `E_p` is nonzero.

This is the decisive control on the proposed infinite-scale escape. The exponent coordinate `k` does not generate successively smaller compact corrections, new spectral locations, or a renormalizing hierarchy. It merely translates one fixed trace-class block along the dilation orbit.

## 4. The trace is exactly one half of the von Mangoldt function

Trace is legitimate term by term because `B_n` is a finite sum of trace-class operators. Using PC-111,

\[
\begin{aligned}
\operatorname{Tr}B_n
&=\frac12\sum_{d\mid n}\mu(n/d)\log d\\
&=\boxed{\frac12\Lambda(n)}.
\end{aligned}
\]

The last equality is the classical divisor identity

\[
\Lambda(n)=\sum_{d\mid n}\mu(n/d)\log d.
\]

Consequently

\[
\operatorname{Tr}B_n
=
\begin{cases}
\frac12\log p,&n=p^k,\\
0,&n\text{ has at least two distinct prime factors}.
\end{cases}
\]

This is an exact operator lift of the common-vertex von Mangoldt phenomenon, but it is **not** additional zeta information. The prime-power selector appears because Möbius finite differencing is applied to the logarithmic trace character `Tr E_h=(1/2)log h`.

The distinction matters. The full block `B_n` can be nonzero even when its trace vanishes, so this theorem does not reduce every mixed-prime operator to the scalar `Lambda(n)`. What it does prove is that the only scalar trace character created by this canonical multiscale birth operation is precisely the already-known von Mangoldt one.

## 5. The unweighted prime-power direct sum is bounded but never compact

Fix one prime `p` and consider the most direct infinite exact-order accumulation along its refinement ray,

\[
\mathfrak B_p:=\bigoplus_{k\ge1}B_{p^k}.
\]

Every block is unitarily equivalent to `E_p`, so

\[
\|\mathfrak B_p\|=\|E_p\|<\infty.
\]

However a direct sum of compact operators can be compact only if the block operator norms tend to zero. Here

\[
\boxed{
\|B_{p^k}\|=\|E_p\|>0
\quad\text{for every }k.
}
\]

Therefore

\[
\boxed{
\mathfrak B_p\text{ is bounded and noncompact.}
}
\]

Any unweighted direct sum over all Prime-Circle levels contains this prime-power ray as a reducing direct-sum component, so it cannot be a compact Hilbert--Polya/Fredholm operator either.

The determinant obstruction is equally explicit. Let

\[
F_p(z):=\det(I-zE_p).
\]

For the first `K` prime-power birth blocks,

\[
\det\!\left(I-z\bigoplus_{k=1}^K B_{p^k}\right)
=F_p(z)^K.
\]

Since

\[
F_p'(0)=-\operatorname{Tr}E_p=-\frac12\log p\ne0,
\]

the sequence `F_p(z)^K` cannot converge locally uniformly near `z=0` to a nonzero entire determinant normalized by value `1` at the origin. Its derivative at zero already diverges linearly with `K`.

Thus the literal unweighted infinite product left open by PC-111 fails before any question about zeta-zero placement arises.

## 6. Dirichlet weighting restores convergence only by the classical zeta transform

The previous obstruction naturally suggests damping the levels. The PC-111 proof in fact gives enough trace-norm control to classify the standard Dirichlet choice.

For `h>=1`, the proof of PC-111 decomposes `E_h` into:

- a difference of two unitary conjugates of the fixed trace-class off-origin operator from PC-110;
- a difference of two normalized rank-one cell terms;
- the positive Carleman annulus `P_(1,h) C P_(1,h)`, whose trace norm is `(1/2)log h`;
- two Carleman cross terms between `(0,1)` and `(1,h)`.

The cross-term nuclear norms are uniformly bounded in `h`. Indeed, with the Laplace vectors `e_t(x)=e^{-tx}` used in PC-111,

\[
\|P_{(1,h)}e_t\|
\le
\|P_{(1,\infty)}e_t\|
=\frac{e^{-t}}{\sqrt{2t}},
\]

while

\[
\|P_{(0,1)}e_t\|
=\sqrt{\frac{1-e^{-2t}}{2t}}.
\]

Their product is `O(t^{-1/2})` at zero and `O(e^{-t}/t)` at infinity, hence integrable independently of `h`. Therefore

\[
\boxed{
\|E_h\|_1=O(1+|\log h|).
}
\]

For every `sigma>1`, both trace-class Dirichlet series

\[
\mathcal E(s)=\sum_{n\ge1}\frac{E_n}{n^s},
\qquad
\mathcal B(s)=\sum_{n\ge2}\frac{B_n}{n^s}
\]

converge absolutely in `S_1`, uniformly on closed half-planes `Re(s)>=1+epsilon`. Since `B=mu*E` as an operator-valued Dirichlet convolution,

\[
\boxed{
\mathcal B(s)=\frac1{\zeta(s)}\mathcal E(s),
\qquad \Re s>1.
}
\]

Taking traces gives

\[
\boxed{
\operatorname{Tr}\mathcal B(s)
=\frac12\sum_{n\ge2}\frac{\Lambda(n)}{n^s}
=-\frac12\frac{\zeta'(s)}{\zeta(s)},
\qquad \Re s>1.
}
\]

This is exactly the collapse the Prime-Circle mandate warns against. The reciprocal zeta factor enters because Möbius inversion is Dirichlet convolution, while the logarithmic derivative enters because the trace character is `log h`. Neither the functional equation, the gamma factor, the line `Re(s)=1/2`, nor an intrinsic analytic continuation of this operator series has been derived.

A weight such as `n^{-s}` can therefore make the multiscale family summable, but it does so by introducing the standard Dirichlet spectral parameter and immediately recovering the classical zeta transform. That is a valid transform of the data, not a new RH mechanism.

## 7. Prior-art and novelty audit

The arithmetic identities in Sections 2, 4, and 6 are classical and already anchored in `research/prime_circle/SOURCES.md`: Möbius inversion, the standard Dirichlet series for `mu`, and the von Mangoldt/logarithmic-derivative identity. PC-055 already establishes a closely related warning in the coefficient-Hilbert setting: completing a Möbius basis transform turns it into multiplication by reciprocal zeta and produces only standard Euler-product thresholds.

The scaling-semigroup warning is older and broader. PC-010 identifies the abstract Prime-Circle root/refinement tower with the Bost--Connes cyclotomic system; its literature audit already places positive-integer scaling, cyclotomy, and zeta partition functions firmly in classical noncommutative arithmetic dynamics. The present result therefore does not claim novelty for obtaining `log p`, `Lambda`, or `zeta` from a multiplicative dilation action.

PC-078 is also an important internal control but not a duplicate. There the single-conductor Hardy operator at repeated-prime depth is a signed tensor inflation of its squarefree-radical level. Here the object is the **continuum affine-scale trace-class cocycle of PC-111**, and the exact-order Möbius extraction produces unitary conjugates of radical blocks rather than finite tensor copies. The shared lesson is nevertheless consistent: repeated-prime depth is not producing a new operator shape.

Directed novelty searches across dilation-cocycle, Bost--Connes/scaling, trace-formula, and operator-valued Möbius formulations found broad established machinery connecting multiplicative scaling and zeta. Nothing found supports a historical novelty claim for the standard ingredients above. The line-specific result retained here is the exact radical-unitary factorization and the resulting noncompactness/divergence of the canonical unweighted multiscale birth tower built from the PC-111 geometric defect.

## 8. Falsification surface and remaining boundary

The claim has direct exact failure points:

1. `E_h` must satisfy both `E_h=(alpha_h-I)D_1` and the PC-111 cocycle;
2. Möbius support for `n=m rad(n)` must reduce to divisors `m f` with `f|rad(n)`;
3. the commuting dilation action must factor the squarefree finite difference as `prod_(p|rad(n))(alpha_p-I)`;
4. unitary conjugation must preserve the full spectrum, singular values, Schatten norms, and Fredholm determinant;
5. the trace calculation must reproduce the classical divisor identity for `Lambda(n)`;
6. the trace-norm bound from the PC-111 Carleman decomposition must be `O(1+log n)`, ensuring the stated `Re(s)>1` Bochner convergence.

Each step follows directly from the persisted PC-111 operator identities plus standard Möbius arithmetic. No numerical experiment or analytic continuation is used.

The result closes only the **canonical Möbius exact-order organization of fixed affine scales**, including its unweighted direct sum/product and its ordinary Dirichlet damping. It does not rule out:

- a genuinely joint cross-conductor operator formed before the PC-109 single-conductor universalization;
- a geometry-forced non-affine or multiscale recentering whose operator shape is not a dilation conjugate of `D_1`;
- weights or couplings derived independently from embedded chord/old-new geometry rather than imposed as a Dirichlet parameter;
- nonlinear cross-level constructions outside direct sums/products of the `E_h`/`B_n` blocks;
- the nonlinear uniformization/monodromy branch rooted at PC-017.

But any surviving infinite-scale repair now has a sharper burden. It must do more than accumulate the PC-111 affine defects across primitive levels: **Möbius birth extraction makes repeated prime powers spectrally identical up to unitary dilation, the unweighted tower is noncompact, and the standard summable repair immediately classicalizes to reciprocal zeta and `-zeta'/zeta`.**