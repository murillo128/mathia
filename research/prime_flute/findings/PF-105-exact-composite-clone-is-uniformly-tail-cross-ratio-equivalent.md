# PF-105 — the exact all-composite dilation clone is uniformly tail cross-ratio equivalent

**Status:** `DECISIVE-NEGATIVE / EXACT-DERIVED` for RH mechanisms whose claimed prime-specific content lives only in asymptotic tail cross-ratios, canonical multi-gap separator limits, fan-shear tail classes, or pointed/right-limit geometry of the exact prime-flute. This does **not** assert global isospectrality or compact resolvent equivalence of the two infinite surfaces.

## Claim

Let

\[
V(x)=\pi\cot\frac{\pi}{x},\qquad x>2,
\]

and let `X_E` be the exact zero-twist flute with endpoints

\[
x_n^E=V(p_n).
\]

Fix an integer `K>=2`. The labels

\[
q_n=Kp_n
\]

are all composite. Let `X_K` be the exact orthogonal-circle flute with endpoints `V(Kp_n)`. Hyperbolic dilation `z -> z/K` is an isometry, so `X_K` is isometric to the flute with endpoints

\[
x_n^K=W_K(p_n),
\qquad
W_K(x):=\frac1K V(Kx).
\]

Although `X_E` and `X_K` are not globally Möbius-conjugate in general, their **entire marked exact tail cross-ratio geometry becomes uniformly indistinguishable**. If

\[
P\le a<b<c<d
\]

are any four prime labels, with no restriction on how far apart they are, and `chi_E`, `chi_K` are the PF-004 cross-ratios of the corresponding exact endpoints, then

\[
\boxed{
\left|\log\frac{\chi_E}{\chi_K}\right|
\le 2\log V'(P)
=
\frac{2\pi^2}{3P^2}+O(P^{-4}).
}
\tag{1}
\]

For the corresponding canonical separating geodesic lengths

\[
L=4\operatorname{arsinh}\sqrt\chi,
\]

one consequently has the uniform estimate

\[
\boxed{
|L_E-L_K|
\le 4\log V'(P)
=
\frac{4\pi^2}{3P^2}+O(P^{-4}).
}
\tag{2}
\]

Thus every matched canonical multi-gap separator anywhere in the tail beginning at `P` differs by `O(P^-2)`, **uniformly over the size of the gaps and the span of the block**.

There is also a global summability statement in the canonical fan-shear coordinates. If

\[
\Delta_n^E=V(p_{n+1})-V(p_n),
\qquad
\Delta_n^K=W_K(p_{n+1})-W_K(p_n),
\]

and

\[
\sigma_n^E=\log\frac{\Delta_{n+1}^E}{\Delta_n^E},
\qquad
\sigma_n^K=\log\frac{\Delta_{n+1}^K}{\Delta_n^K},
\]

then

\[
\boxed{
\sum_n |\sigma_n^E-\sigma_n^K|<\infty.
}
\tag{3}
\]

Accordingly, the exact cotangent correction does not rescue the asymptotic tangent/right-limit branch from PF-099: the exact prime surface and an all-composite exact clone have the same marked tail cross-ratio and canonical-separator limit data. Any surviving exact-geometry mechanism must accumulate the vanishing defects in a genuinely global way rather than depend only on their tail equivalence class.

## 1. The exact composite clone and its isometric normalization

PF-099 used the projective reference `p_n -> Kp_n`, for which global dilation gives an exact conjugacy. Here both surfaces use the **exact** endpoint law `V`.

The exact composite surface has vertices

\[
V(Kp_n).
\]

Applying the hyperbolic isometry `z -> z/K` sends these vertices to

\[
W_K(p_n)=\frac{V(Kp_n)}K.
\]

Because dilation is Möbius, it preserves the complete orthogonal-circle incidence pattern, all cross-ratios, all hyperbolic translation lengths, and the interior/exterior realization. Hence it is enough to compare the two increasing real functions

\[
V(x)
\quad\text{and}\quad
W_K(x).
\]

Their asymptotic expansions begin

\[
V(x)=x-\frac{\pi^2}{3x}+O(x^{-3}),
\]

\[
W_K(x)=x-\frac{\pi^2}{3K^2x}+O(x^{-3}),
\]

but the proof below does not truncate either function to a finite jet.

## 2. A global secant-distortion bound

Differentiate the exact map. With `y=pi/x`,

\[
\boxed{
V'(x)
=
\frac{\pi^2}{x^2}\csc^2\frac{\pi}{x}
=
\left(\frac{y}{\sin y}\right)^2.
}
\tag{4}
\]

For `x>2`, the function `V'(x)` is strictly decreasing to `1`: `y/sin y` is increasing in `y` because

\[
\sin y-y\cos y>0
\qquad(0<y<\pi/2),
\]

and `y=pi/x` decreases with `x`.

Also

\[
W_K'(x)=V'(Kx).
\]

Therefore, pointwise for `x>2`,

\[
1<W_K'(x)\le V'(x).
\tag{5}
\]

For any interval `P<=a<b`, define the exact secant-distortion ratio

\[
R_K(a,b)
:=
\frac{V(b)-V(a)}{W_K(b)-W_K(a)}.
\]

Using the integral form of the increments and (5),

\[
V(b)-V(a)=\int_a^b V'(t)\,dt,
\qquad
W_K(b)-W_K(a)=\int_a^b V'(Kt)\,dt.
\]

The numerator integrand dominates the denominator integrand, while on the whole interval

\[
V'(t)\le V'(P),
\qquad
V'(Kt)>1.
\]

Hence the decisive uniform estimate is

\[
\boxed{
1\le R_K(a,b)\le V'(P)
\qquad
\text{for every }P\le a<b,
}
\tag{6}
\]

independently of the length of the interval.

Finally,

\[
\log V'(P)
=2\log\frac{\pi/P}{\sin(\pi/P)}
=
\frac{\pi^2}{3P^2}+O(P^{-4}).
\tag{7}
\]

No prime-gap estimate enters (6)--(7).

## 3. Uniform exact cross-ratio equivalence on the whole tail

PF-004 uses, for ordered endpoints `a<b<c<d`,

\[
\chi(a,b,c,d)
=
\frac{(c-b)(d-a)}{(b-a)(d-c)}.
\]

Apply this once to `V(a),V(b),V(c),V(d)` and once to `W_K(a),W_K(b),W_K(c),W_K(d)`. Equation (6) gives

\[
\frac{\chi_E}{\chi_K}
=
\frac{R_K(b,c)R_K(a,d)}{R_K(a,b)R_K(c,d)}.
\tag{8}
\]

Every `log R_K` lies in `[0,log V'(P)]`. The sum of the two numerator logs and the sum of the two denominator logs both lie in `[0,2 log V'(P)]`. Therefore

\[
\boxed{
\left|\log\frac{\chi_E}{\chi_K}\right|
\le 2\log V'(P),
}
\]

which is (1).

The important quantifier is the uniformity: `a,b,c,d` may separate as `P` grows, and the gaps may be tiny, huge, or hierarchically different. The bound depends only on the left edge `P` of the tail.

Thus if `\mathcal C_P^E` denotes the marked family of all PF-004 cross-ratios whose four prime labels are at least `P`, and `\mathcal C_P^K` is the corresponding family for the exact composite clone, the matching has logarithmic distortion

\[
\sup_{\text{matched }\chi}
|\log\chi_E-\log\chi_K|
=O(P^{-2})\to0.
\tag{9}
\]

This is stronger than saying that every **fixed** finite tangent has the same projective limit. It controls all four-point configurations in the tail at once.

## 4. Uniform canonical separator equivalence

For the PF-004 separator,

\[
L(\chi)=4\operatorname{arsinh}\sqrt\chi.
\]

Differentiating with respect to `log chi`,

\[
\frac{dL}{d\log\chi}
=
2\sqrt{\frac{\chi}{1+\chi}}
\le2.
\tag{10}
\]

So `L` is globally `2`-Lipschitz in the logarithmic cross-ratio coordinate. Combining (1) and (10) gives

\[
|L_E-L_K|
\le2\left|\log\frac{\chi_E}{\chi_K}\right|
\le4\log V'(P),
\]

which proves (2).

The bound remains valid even when `chi` itself tends to `0` or `infinity`. Hence pinching regimes, long-separator regimes, and mixed hierarchical blocks do not evade the comparison.

A direct consequence is that every limit set built from **matched canonical separator lengths escaping to infinity** is identical for the exact prime surface and the exact all-composite clone. In particular, the exact `pi*cot(pi/p)` correction cannot create a different pointed finite-window tangent hull from the one seen by the clone.

## 5. The exact fan-shear deformation is absolutely summable

For consecutive primes put

\[
r_n
:=
\log\frac{\Delta_n^E}{\Delta_n^K}
=
\log R_K(p_n,p_{n+1}).
\]

From (6),

\[
0\le r_n\le\log V'(p_n)=O(p_n^{-2}).
\tag{11}
\]

Since `sum_p p^-2` converges,

\[
\boxed{
\sum_n r_n<\infty.
}
\tag{12}
\]

The canonical fan shears satisfy

\[
\sigma_n^E-\sigma_n^K
=
\left(\log\Delta_{n+1}^E-\log\Delta_{n+1}^K\right)
-
\left(\log\Delta_n^E-\log\Delta_n^K\right)
=
r_{n+1}-r_n.
\tag{13}
\]

Therefore

\[
\sum_n|\sigma_n^E-\sigma_n^K|
\le
\sum_n(r_{n+1}+r_n)
<\infty,
\]

proving (3).

This is an exact discrete statement about the two sampled endpoint meshes. It does not use an off-prime differential profile as extra geometry; derivatives are only a proof device for the secant bounds.

## 6. What this rules out, and what remains open

PF-099 showed that the **projective** prime tangent hull has an exact all-composite dilation clone. PF-101 showed that finite asymptotic jets of the exact endpoint map do not provide a distinguished scattering scale. PF-104 showed that the continuous interpolation between sampled prime vertices is not intrinsic.

PF-105 closes a different escape: retaining the **full exact sampled cotangent values** does not separate the prime surface from the composite dilation clone at the level of asymptotic marked cross-ratio or canonical-separator geometry. The distinction is nonzero at every finite scale, but it vanishes uniformly in the tail.

Consequently the following route cannot supply a primality-specific spectral mechanism merely by passing to an asymptotic class:

\[
\boxed{
\text{exact tail endpoint geometry}
\to
\text{tail cross-ratio / separator limits}
\to
\text{right-limit or tangent spectral invariant}
\to
\text{primality specificity}.
}
\tag{14}
\]

Any invariant continuous under the uniform tail distortion (9) sees the same asymptotic data on the prime-labelled surface and on the exact all-composite clone.

This result deliberately **does not** claim any of the following:

- that the two infinite Laplacians are unitarily equivalent;
- that their resolvent or heat-semigroup difference is compact or trace class;
- that their complete primitive length spectra agree;
- that a nonlocal determinant or scattering phase cannot accumulate the summable local defects into a finite global quantity.

Those stronger conclusions require operator-theoretic hypotheses not established here, especially because the prime-flute has unbounded distinguished cuffs and collapsing separator geometry.

The remaining exact-geometry route is therefore narrower: it must exploit a genuinely global accumulation or organization of the vanishing exact defects, not just their tail limit, pointed tangent hull, or asymptotic cross-ratio class.

There is also the same arithmetic caveat as PF-099. The composite sequence `Kp_n` is a deterministic recoding of the primes, so this does not prove that its geometry is arithmetically independent of RH. The decisive statement is about **geometric discrimination**: asymptotic exact tail geometry does not know whether the sampled integer labels themselves were prime.

## 7. Interior/exterior duality

The construction and the obstruction preserve the ambient interior/exterior duality. The passage from `V(Kp_n)` to `W_K(p_n)` is a hyperbolic Möbius dilation. Cross-ratios and the PF-004 translation lengths are Möbius invariant, and the orthogonal circles are transported exactly under the same dilation.

Thus neither realization of the prime-circle-derived flute supplies a second channel that escapes (1)--(3).

## 8. Prior art and novelty audit

The analytic ingredients are classical:

- `V'(x)=((pi/x)/sin(pi/x))^2` and its monotonicity are elementary calculus;
- cross-ratios are Möbius invariant and control the PF-004 hyperbolic separator;
- small tail cross-ratio distortion is standard language in universal/asymptotic Teichmüller theory;
- Firat Yaşar, *Infinite-dimensional Teichmüller spaces* (arXiv:2104.00289), studies asymptotically isometric infinite-type hyperbolic structures and gives Fenchel--Nielsen criteria under an **upper-bounded** base-surface hypothesis.

That theorem is **not invoked here**: the prime-flute's distinguished cuffs tend to infinity, so its natural pants decomposition is not upper bounded. The exact bounds (1)--(3) are proved directly and require no Teichmüller-space existence theorem.

Directed searches for prime-gap/cotangent tight flutes, exact prime/composite dilation clones, and asymptotic cross-ratio equivalence of such Fuchsian constructions did not locate this specialization. No novelty is claimed for cross-ratio distortion theory itself. The durable program-specific contribution is the explicit all-composite control showing that even the full exact sampled cotangent geometry becomes asymptotically indistinguishable in the strongest canonical four-point sector available in this construction.

## 9. Audit / falsification core

The decisive finite checks are:

1. verify (4) and that `V'` decreases to `1`;
2. verify the pointwise comparison `V'(x)>=V'(Kx)>1`;
3. integrate it to obtain the span-independent secant bound (6);
4. substitute the four secant ratios into the exact PF-004 cross-ratio to obtain (1);
5. use (10) to obtain the uniform separator bound (2);
6. apply (6) to consecutive prime intervals and sum `O(p_n^-2)` to obtain (3).

A counterexample to the stated no-go would have to exhibit a proposed **tail-limit** invariant of the canonical exact endpoint/cross-ratio/separator geometry which changes despite the uniform matched distortion tending to zero, or show that the candidate actually depends on a nonlocal accumulation not covered by the tail-equivalence claim.