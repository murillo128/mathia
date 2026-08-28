# WP-003 — projective Prime-Flute positivity has an all-composite isometric clone

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for any Weil-positivity route whose positive geometric form and finite-place decomposition are claimed to be intrinsic to the **projective** zero-twist Prime-Flute geometry (including its tangent/collar-capacity networks). The result does **not** rule out a mechanism using the exact nonprojective endpoint map `V(p)=pi*cot(pi/p)`, a genuinely geometric way of recovering an absolute arithmetic scale, or other data not preserved by the dilation gauge.

## Claim

Prime Flute currently contains a genuine, independently positive geometric form: the harmonic collar-capacity Dirichlet form of PF-056. However, that form factors through projective gap geometry. PF-099 supplies an exact adversarial control showing that the whole projective flute, and therefore every isometry-functorial positive form on it, is unchanged when the prime endpoint sequence is replaced by the all-composite sequence

\[
q_n=2p_n.
\]

The Riemann Weil finite-place distribution is not invariant under that replacement: it depends on the absolute logarithmic locations and von Mangoldt weights of the rational prime powers. Hence no construction determined only by the projective Prime-Flute isometry class can **canonically** recover the finite-place part of the Weil explicit formula, and an archimedean/global term derived from the same projective geometry cannot repair the missing arithmetic scale.

Equivalently:

\[
\boxed{
\text{intrinsic projective-flute positivity}
\not\Rightarrow
\text{canonical Riemann Weil finite-place positivity}.
}
\]

This is a canonicity obstruction, not a claim that projective prime-gap data contain no information about the primes. The clone is a deterministic recoding of the prime sequence and can still encode prime statistics. What fails is the stronger target of this research line: that the **geometry itself** forces the arithmetic Weil functional without retaining or reinserting an external prime labeling/scale.

---

## 1. Exact isometric all-composite control

Let the projective reference endpoints be

\[
x_n=p_n.
\]

For any `K>0`, the map

\[
D_K:z\mapsto Kz
\]

is an isometry of the upper half-plane. PF-099 proves directly on the standard zero-twist generators that

\[
G(Ka,Kb)=D_KG(a,b)D_K^{-1}.
\]

Therefore scaling every endpoint by `K` conjugates the complete projective Fuchsian construction. In particular, for `K=2`,

\[
\boxed{X_p^0\cong X_{2p}^0.}
\tag{1}
\]

Every integer `2p_n` is composite. For every odd prime `p_n`, it has two distinct prime factors and hence

\[
\Lambda(2p_n)=0.
\tag{2}
\]

The exceptional first label `2\cdot2=4` is also composite but is a prime power, so `Lambda(4)=log 2`; it plays no role in the infinite obstruction.

More importantly than (2), the hyperbolic isometry (1) erases the **absolute endpoint scale**. The same projective surface can be represented by `p_n`, `2p_n`, `Kp_n`, or any common positive dilation. Thus the projective isometry class cannot intrinsically distinguish the normalization in which the selected integer labels are the rational primes.

---

## 2. Functorial positivity is cloned exactly

Let `Q_X` be any quadratic or Hermitian form constructed functorially from the intrinsic hyperbolic geometry of a projective flute `X`. By functoriality under an isometry `U:X->Y`,

\[
Q_Y(Uf)=Q_X(f).
\tag{3}
\]

This is automatic for standard geometric examples such as Dirichlet energy, harmonic capacity, Laplace quadratic forms, Hodge norms, and finite-truncation Dirichlet-to-Neumann/Steklov forms whenever the relevant object is defined canonically. The same statement applies to any other pairing that uses only the intrinsic projective metric and canonical markings preserved by (1).

PF-056 gives a particularly concrete Mathia-native instance. For a prime-derived tangent with consecutive gaps `d_i`, define

\[
R_k=\frac{d_1+\cdots+d_{k-1}}{d_k},
\qquad
L_k=4\operatorname{arsinh}\sqrt{R_k}.
\]

The exact collar conductance is

\[
\kappa(L)=\frac{L}{4\arctan(e^{-L/2})}>0,
\]

and the canonical trial-space energy is

\[
\boxed{
\mathcal E(c)
=\sum_{e=(i,i+1)}\kappa(L_e)|c_{i+1}-c_i|^2
\ge 0.
}
\tag{4}
\]

Under `p_n -> 2p_n`, every gap becomes `2d_i`, so every ratio `R_k` is unchanged. Hence every `L_k`, every `kappa(L_k)`, every collar mass, and the whole generalized graph form are identical:

\[
\boxed{
\mathcal E_{p}(c)=\mathcal E_{2p}(c).
}
\tag{5}
\]

Equation (5) is exact, not asymptotic. It shows that Prime Flute really does possess independent geometric positivity, but that this particular positivity cannot know whether its endpoint labels were primes or the all-composite dilation clone.

---

## 3. The Weil finite-place distribution needs the missing absolute scale

Up to the usual sign/convention choices in the explicit formula, the finite arithmetic distribution is built from atoms

\[
\frac{\Lambda(n)}{\sqrt n}
\quad\text{at}\quad
\pm\log n.
\tag{6}
\]

Equivalently, decomposing by prime rays gives coefficients involving

\[
(\log p)p^{-k/2}
\quad\text{at}\quad
k\log p,
\qquad k\ge1.
\tag{7}
\]

These data are **not projectively scale invariant**. Replacing an endpoint label `p` by `2p` changes the logarithmic location from `log p` to `log p+log 2`, changes any absolute `p^{-k/2}` scale, and for odd `p` changes the von Mangoldt selector from `Lambda(p)=log p` to `Lambda(2p)=0`.

A compactly supported test function can separate an atom at `log p` from one at `log(2p)`, so the two labeled finite-place distributions are genuinely different. Yet by (1) every intrinsic projective geometric construction sees exactly the same surface.

Therefore there is no isometry-invariant rule

\[
X^0\longmapsto \mu_{\mathrm{finite}}(X^0)
\]

which, **from the projective geometry alone**, canonically decides that the correct arithmetic interpretation of (1) is the prime labeling rather than the dilation clone.

One can of course attach the original numbers `p_n` as extra marks and then reconstruct (6)-(7). But that is precisely the move excluded by the target question: the arithmetic scale has then been retained externally rather than forced by the positive geometry.

---

## 4. Adding a projective archimedean term does not break the gauge

Suppose a proposed global construction supplements a finite-place positive form with a boundary, cusp, curvature, scattering, cohomological, or other archimedean/global counterterm, but every ingredient is still functorially determined by the same projective hyperbolic surface.

The isometry (1) transports **all** such intrinsic ingredients simultaneously. Hence the complete geometric object is still unable to distinguish the prime normalization from the `2p_n` normalization.

This does not prove that two externally labeled explicit-formula expressions can never have the same numerical value for some specially transformed test functions. The narrower and relevant statement is structural: the projective geometry itself does not provide the datum needed to identify the Riemann finite-place decomposition in the first place. A later cancellation with an archimedean term cannot manufacture a selector/absolute scale that no projective ingredient contains.

Thus a successful local-to-global Weil bridge must break the dilation gauge **before** claiming arithmetic matching.

---

## 5. Exact matched-control failure

This is stronger than an asymptotic universality objection.

The control

\[
\{p_n\}
\longrightarrow
\{2p_n\}
\]

preserves, exactly:

- the complete projective zero-twist hyperbolic surface up to isometry;
- all projective cross-ratios and finite tangent surfaces;
- all intrinsic spectra, scattering data, capacities, Dirichlet energies, and boundary responses defined from that projective surface;
- the PF-056 positive collar-capacity network.

But it replaces the distinguished integer sequence by an all-composite one and removes the von Mangoldt weight at `2p` for every odd prime `p`.

So any purported projective-flute positivity mechanism that is presented as intrinsically generating the Riemann arithmetic place structure fails an exact matched control.

PF-101 gives a complementary finite-scale warning: even after the exact cotangent geometry breaks the global dilation gauge, any mechanism visible only in a fixed finite asymptotic endpoint jet can be reproduced by a matched smooth control. The surviving gate is therefore narrower than merely saying “use the cotangent correction.”

---

## 6. The canonical symplectic/intersection escape also degenerates at zero twist

PF-058 and PF-059 provide a second, independent obstruction inside the same branch.

On finite truncations, the zero-twist Prime Flute lies on the Lagrangian fixed locus of its reflection:

\[
\omega_{WP}|_{\tau=0}=0.
\]

Moreover, every reflection-invariant cuff or multi-gap separating length has zero mutual Weil-Petersson/Goldman Poisson bracket at the actual zero-twist point. Hence replacing the positive Dirichlet/capacity form by the most obvious canonical first-order symplectic/intersection structure does not solve the problem:

```text
projective Dirichlet/capacity positivity
    -> nontrivial and genuinely positive
    -> but exactly dilation-clone blind

WP/Goldman first-order intersection structure at zero twist
    -> canonical
    -> but vanishes on the reflection-invariant arithmetic length sector
```

Second variations, Hessians, or other positive metrics are not ruled out by the Lagrangian statement. However, if they are constructed solely from the projective isometry class, they still satisfy the clone obstruction of Sections 1-4. To escape both negatives they must use a canonically forced nonprojective datum.

---

## 7. Relation to WP-001 and WP-002

The first three Weil-positivity findings now isolate three different failure modes:

1. **WP-001:** Prime Circle has the correct prime-power kernel scale, but the actual finite-place Weil block is indefinite; local ray positivity cannot equal the Weil summand.
2. **WP-002:** the Prime-Circle uniformization defect admits natural positive norms, but their support vanishes exactly where the Weil finite arithmetic measure is nonzero.
3. **WP-003:** Prime Flute has a bona fide nontrivial geometric Dirichlet/capacity positivity, but its projective form lacks the absolute arithmetic scale and is exactly reproduced by an all-composite isometric control.

So the obstruction is not merely “Mathia has not yet found a positive form.” It already has positive forms. The harder requirement is to make positivity, arithmetic support/scale, and the archimedean completion arise from the **same canonical structure**.

---

## 8. Prior-art / novelty audit

No novelty is claimed for the general ingredients:

- hyperbolic dilation is a Möbius isometry;
- Dirichlet energy, harmonic capacity, Laplace/DtN forms, and intrinsic pairings are transported by isometries;
- the finite-place Weil explicit formula uses the classical von Mangoldt prime-power distribution;
- Weil/Bombieri positivity criteria are classical;
- the Lagrangian zero-twist and Goldman/WP facts used above are classical Teichmüller/character-variety geometry.

The program-specific inputs are PF-056's exact prime-gap collar-capacity form and PF-099's global all-composite dilation clone. Directed searches for combinations of Weil positivity, hyperbolic collar capacity, prime-gap/Fuchsian geometry, and Möbius-dilation prime/composite controls found the classical components but no prior treatment of this particular obstruction.

The durable contribution is therefore a **negative consequence for Mathia**, not a new theorem about hyperbolic surfaces: a positive form that factors through the projective Prime-Flute cannot be promoted to the desired intrinsic Weil-positive geometry merely because its Dirichlet theorem proves nonnegativity.

---

## 9. Surviving gate

A Prime-Flute route remains viable only if it supplies, from geometry rather than from retained labels, a datum that simultaneously:

1. breaks the global projective dilation gauge;
2. survives the PF-101 matched-smooth-control test rather than depending on a fixed finite endpoint jet;
3. generates the prime-power logarithmic scale and weights without inserting them by hand;
4. supplies or forces the archimedean/pole counterterms in the same construction;
5. has positivity from an independent geometric theorem, not from RH or zero data.

The most plausible surviving part of Prime Flute is therefore not its projective tangent/capacity sector by itself, but some genuinely global/nonperturbative use of the exact endpoint geometry

\[
V(p)=\pi\cot\frac{\pi}{p}
\]

coupled to a canonical positive global construction. No such bridge is established here.