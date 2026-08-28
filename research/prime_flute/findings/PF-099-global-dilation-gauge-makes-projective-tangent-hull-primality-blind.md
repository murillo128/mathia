# PF-099 — global dilation gauge makes the projective tangent hull primality-blind

**Status:** `DECISIVE-NEGATIVE / EXACT-DERIVED` for any proposed RH mechanism whose prime-specific content is claimed to reside only in projective gap data, recurrent finite tangents, or the leading distinguished-cuff profile. The exact finite-scale `pi*cot(pi/p)` geometry is not ruled out.

## Claim

Fix an integer `K>=2` and let

\[
q_n:=Kp_n.
\]

Every `q_n` is composite, while

\[
q_{n+1}-q_n=K g_n.
\]

Thus every projective gap vector, every consecutive-gap ratio, every finite multi-gap cross-ratio, and every recurrent isolated tangent pattern of the prime sequence is reproduced by the all-composite sequence `q_n`, up to the common dilation `K`.

For the projective endpoint model `x_n^0=p_n` used in PF-087, this is stronger than equality of tangent data: the entire zero-twist flute attached to `q_n` is exactly Möbius-conjugate to the one attached to `p_n`. Hence every intrinsic spectral or dynamical invariant of that projective flute is identical for the prime-labelled and all-composite-labelled constructions.

Consequently the recurrent projective tangent hull, although spectrally consequential for the exact prime-flute, is **not by itself a primality discriminator**. Any RH-relevant statement depending only on that scale-invariant hull is, at the arithmetic level, a reformulation of the projective prime-gap process rather than a new selector-specific spectral structure.

The exact orthogonal-circle surface escapes this no-go only through the nonprojective finite-scale defect of

\[
V(p)=\pi\cot\frac{\pi}{p},
\]

whose first four-point Möbius-invariant correction is the `P^-4` Schwarzian term of PF-082.

## 1. Exact global conjugacy of the projective flute

For real `a<b`, use the standard zero-twist generator

\[
G(a,b)=\frac1{b-a}
\begin{pmatrix}
a+b&-2ab\\
-2&a+b
\end{pmatrix}.
\]

Let

\[
D_K=
\begin{pmatrix}
\sqrt K&0\\
0&1/\sqrt K
\end{pmatrix},
\]

which acts on the upper half-plane as the hyperbolic isometry `z -> K z`. A direct calculation gives

\[
\boxed{
G(Ka,Kb)=D_KG(a,b)D_K^{-1}.
}
\tag{1}
\]

The same dilation carries every orthogonal semicircle with endpoints `(a,b)` to the corresponding semicircle with endpoints `(Ka,Kb)`. Therefore, for any endpoint sequence `x_n`, scaling all endpoints by `K` conjugates the full Fuchsian construction, including the symmetric side used in the standard zero-twist tight-flute model.

Applying this to `x_n=p_n` gives

\[
\boxed{
X^0_{Kp}\cong X^0_p
}
\tag{2}
\]

as marked hyperbolic surfaces, where the superscript `0` denotes the projective reference of PF-087.

Equation (2) transports, whenever the corresponding objects are defined, the complete Laplace spectrum, essential spectrum, length spectrum, geodesic flow, resonances, scattering data, Patterson--Sullivan data, transfer-operator data, and any Selberg/Ruelle-type invariant intrinsic to the projective surface. This is ordinary Möbius conjugacy, not a new inverse-spectral theorem.

The arithmetic adversary is exact and elementary: because `K>=2`, every label `Kp_n` is composite.

## 2. The whole recurrent tangent hull is cloned

Consider an isolated occurrence of a finite prime pattern

\[
p_{n+j}=P+\eta_j.
\]

The scaled composite sequence has the corresponding block

\[
q_{n+j}=K P+K\eta_j.
\]

All internal and exterior gaps are multiplied by `K`. Hence every projective invariant used by the prime-flute tangent construction is unchanged. In particular,

\[
[d_1:\cdots:d_{r-1}]
=
[Kd_1:\cdots:Kd_{r-1}],
\]

and for the canonical tangent separators

\[
\sinh^2\frac{L_j}{4}
=
\frac{d_1+\cdots+d_{j-1}}{d_j}
=
\frac{Kd_1+\cdots+Kd_{j-1}}{Kd_j}.
\tag{3}
\]

Isolation is also preserved: exterior gaps tending to infinity still tend to infinity after multiplication by `K`. Thus the same patterns recur with the same index multiplicities and produce the same pointed finite-area tangents.

This strengthens PF-097. Its finite CRT clone already showed that one tangent is primality-blind; the dilation clone shows that even the **entire ordered recurrent projective tangent process** can be carried by a sequence containing no primes at all.

It also sharpens the interpretation of PF-098. A featureless control that omits a recurrent tangent remains noncompactly different from the prime-flute, exactly as PF-098 proves. But matching the tangent hull is only a necessary condition for a perturbative comparison, not evidence of arithmetic specificity: the all-composite dilation clone matches the hull exactly.

## 3. The leading distinguished cuffs are also dilation-blind

The distinguished prime-flute cuffs satisfy

\[
\ell_n
=2\log\frac{4p_n}{g_{n-1}}+o(1).
\]

For the scaled sequence `q_n=Kp_n`, the corresponding leading expression is

\[
2\log\frac{4Kp_n}{K g_{n-1}}
=
2\log\frac{4p_n}{g_{n-1}}.
\tag{4}
\]

Thus the asymptotic cuff profile used to expose prime-gap fluctuations is exactly scale-invariant at leading order. Relative cuff differences, the tropical pinching hierarchy, the finite tangent barcodes, and the graph/scattering limits built only from those relative quantities are all reproduced by the dilation clone.

This does not invalidate those spectral statements on `X_prime`; it changes their arithmetic interpretation. They are genuine ways in which the hyperbolic surface encodes the gap process, but scale-invariant encoding alone cannot certify that the selected integer labels were prime.

## 4. The exact `cot` surface breaks the gauge only at finite scale

The exact endpoint map is

\[
V(p)=\pi\cot\frac{\pi}{p},
\]

and `V(Kp)` is not a Möbius transform of `V(p)`. Therefore (2) is **not** an isometry statement for the exact orthogonal-circle prime-flute. The surviving arithmetic/geometric question is precisely what the nonprojective defect contributes.

PF-082 gives a sharp intrinsic measurement. Fix offsets

\[
A<B<C<D,
\]

put

\[
Q=(C-A)(D-B),
\]

and let `chi_P` be the exact four-point cross-ratio built from `V(P+A),...,V(P+D)`. Let `chi_P^{(K)}` be the corresponding cross-ratio for the all-composite block

\[
K(P+A),\ldots,K(P+D).
\]

Both have the same projective tangent cross-ratio `chi_0`. Applying PF-082 once at scale `P` and once at scale `KP` with offsets multiplied by `K` gives

\[
\log\frac{\chi_P}{\chi_0}
=-\frac{\pi^2}{3P^4}Q+O(P^{-5}),
\]

\[
\log\frac{\chi_P^{(K)}}{\chi_0}
=-\frac{\pi^2}{3K^2P^4}Q+O(P^{-5}).
\]

Hence

\[
\boxed{
\log\frac{\chi_P}{\chi_P^{(K)}}
=-\frac{\pi^2}{3P^4}
\left(1-K^{-2}\right)Q
+O(P^{-5}).
}
\tag{5}
\]

For the associated exact separating geodesic lengths,

\[
L=4\operatorname{arsinh}\sqrt\chi,
\]

so

\[
\boxed{
L_P-L_P^{(K)}
=-\frac{2\pi^2}{3P^4}
\left(1-K^{-2}\right)Q
\tanh\frac{L_0}{4}
+O(P^{-5}).
}
\tag{6}
\]

Thus the exact surface does distinguish the two samplings, but only after the common projective/tangent geometry has been quotiented out. Equation (5) is the Schwarzian defect, not a new zeta-like object.

At the level of individual distinguished cuffs the exact `cot` correction appears earlier. Writing `h_n=log(cot(pi/p_n)/cot(pi/p_{n-1}))` and using `ell'(h)=-1/sinh(h/2)`, the prime number theorem implication `g_{n-1}/p_n ->0` gives

\[
\boxed{
\ell_n^{(K)}-\ell_n
=
\frac{4\pi^2}{3}
\left(1-K^{-2}\right)p_n^{-2}
+o(p_n^{-2}).
}
\tag{7}
\]

The leading term in (7) is universal: the gap cancels. Multi-gap projective information first distinguishes the exact samplings through the intrinsic `P^-4` cross-ratio correction (5).

## 5. Consequence for the RH search

PF-034/PF-043/PF-045/PF-046 and their later spectral descendants remain valid statements about the actual prime-flute. Recurrent tangents can create essential spectrum, localized resonances, wave barcodes, and multiscale scattering structure.

PF-099 rules out a stronger interpretation that had remained open after PF-097/PF-098:

\[
\boxed{
\text{recurrent projective tangent hull}
\not\Rightarrow
\text{intrinsic primality-specific spectral structure}.
}
\tag{8}
\]

The obstruction is a global gauge, not merely a finite-pattern counterexample. Every construction depending only on data invariant under

\[
(p_n,g_n)\mapsto(Kp_n,Kg_n)
\]

has an all-composite clone.

This does **not** prove that scale-invariant gap statistics cannot have consequences equivalent to RH: the cloned sequence `Kp_n` is itself a deterministic recoding of the primes and therefore still carries their distributional information. The narrower decisive conclusion is that such a relation would not be a new spectral selection principle created by the hyperbolic geometry; it would be a geometric encoding of the original projective gap process.

Accordingly, a surviving prime-flute mechanism that aims to add genuinely new arithmetic structure must use information that the dilation gauge does not preserve, most naturally the exact finite-scale `V(p)` defect, or else an external arithmetic condition not recoverable from projective gap geometry alone.

## 6. Interior/exterior duality

The argument respects the interior/exterior duality. Dilation is a Möbius isometry of the upper half-plane, all tangent quantities in (3) are cross-ratios, and the exact finite-scale distinction in (5)--(6) is itself Möbius invariant. Passing to the dual orthogonal-circle realization therefore changes neither the no-go nor the surviving Schwarzian defect.

## 7. Prior-art and novelty audit

No novelty is claimed for the ingredients:

- dilation `z -> Kz` is a standard element of `PSL_2(R)` and conjugates scaled Fuchsian configurations;
- cross-ratios and hyperbolic translation lengths are Möbius invariant;
- multiplying an integer sequence by an integer `K>=2` makes every selected label composite;
- the exact `P^-4` Schwarzian/cross-ratio expansion is PF-082.

Arredondo--Morales--Ramírez Maluendas provide the standard positive-sequence/Fuchsian realization of zero-twist tight flutes used by the branch. Directed searches for prime-gap Fuchsian surfaces, scaled prime endpoint flutes, Möbius-conjugate prime/composite hyperbolic constructions, and Selberg/spectral interpretations of such a dilation found no prior work containing this program-specific composition.

The durable contribution is therefore an **impossibility principle for this research line**, not a new theorem about Möbius geometry:

\[
\boxed{
\text{projective spectral completeness}
\text{ cannot become primality specificity while global dilation is a gauge.}
}
\]

## 8. Audit / formalizable core

The decisive core is finite and directly checkable:

1. prove (1) by matrix multiplication;
2. prove that `q_n=Kp_n` is composite and that its gaps are `Kg_n`;
3. prove invariance of every finite gap cross-ratio under common scaling;
4. combine PF-082 at scales `P` and `KP` to obtain (5)--(6).

A counterexample to PF-099 would have to exhibit a purported projective/tangent-hull invariant of the construction which changes under the exact conjugacy (1), or show that the claimed invariant uses nonprojective finite-scale data after all.