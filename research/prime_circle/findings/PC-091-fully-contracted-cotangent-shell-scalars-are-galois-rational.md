# PC-091 — fully contracted cotangent shell scalars are Galois-rational

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `STRUCTURAL-COLLAPSE` + `DECISIVE-BOUNDARY` for finite fully contracted scalar words built from the intrinsic Prime-Circle cotangent kernel and complete exact-order shells. PC-090 left even-reflection-parity shell words open because symmetry no longer forces them to vanish. The surviving scalar sector is nevertheless much smaller than it first appears: every such finite anchored return amplitude or cyclic trace is fixed by the full cyclotomic Galois group and therefore lies in `Q`. Combined with PC-090, every odd cotangent word is zero and every even word is rational.

This does **not** say that the resulting rational numbers are trivial, prime-blind, or incapable of entering a later cross-level construction. Rational arithmetic sequences can carry substantial information, and Lewis--Zagier give an explicit warning that asymptotic determinants of a different rational-cotangent family can encode GRH. The exact no-go is fixed-level and scalar: an unweighted finite exact-shell contraction cannot hide a new cyclotomic phase, nontrivial number-field extension, or higher period merely by increasing the number of remembered shells.

## 1. Finite exact-shell cotangent words

For roots of unity `z=e^{i theta_z}` and `w=e^{i theta_w}`, use the intrinsic oriented cotangent kernel from PC-045--PC-053 and PC-089--PC-090,

\[
K(z,w)=
\begin{cases}
i\cot\!\left(\dfrac{\theta_z-\theta_w}{2}\right),&z\neq w,\\[2mm]
0,&z=w.
\end{cases}
\]

For distinct points this has the algebraic form

\[
\boxed{
K(z,w)=-\frac{z+w}{z-w}.
}
\]

Let

\[
S_j=P_{n_j}^*
\qquad (n_j>1)
\]

be complete primitive/exact-order shells, put `z_0=z_q=1`, and define the `q`-propagator common-anchor return amplitude

\[
\boxed{
L_q(n_1,\ldots,n_{q-1})
=
\sum_{z_1\in S_1}\cdots\sum_{z_{q-1}\in S_{q-1}}
\prod_{j=0}^{q-1}K(z_j,z_{j+1}).
}
\]

The zero-diagonal convention makes this definition valid even if adjacent shell labels coincide. The same argument below applies to cyclic traces

\[
\operatorname{Tr}
\left(P_{n_0}KP_{n_1}K\cdots P_{n_{q-1}}K\right),
\]

where the projectors are realized on any common roots-of-unity ambient set containing the shells.

## 2. Exact Galois fixed-field theorem

Let

\[
M=\operatorname{lcm}(n_1,\ldots,n_{q-1})
\]

and work in the cyclotomic field

\[
E=\mathbb Q(\zeta_M).
\]

Every summand of `L_q` lies in `E`, because the common anchor is rational and `K(z,w)` is a rational function over `Q` in its two root coordinates whenever the points differ.

For `a in U(M)`, let `sigma_a` be the Galois automorphism

\[
\sigma_a(\zeta_M)=\zeta_M^a.
\]

Every primitive shell is stable under this action:

\[
\boxed{
\sigma_a(P_n^*)=P_n^*
\qquad(n\mid M),
}
\]

because exponentiation by a unit modulo `M` preserves exact order. Moreover, for `z != w`,

\[
\begin{aligned}
\sigma_a(K(z,w))
&=
-\frac{\sigma_a(z)+\sigma_a(w)}
{\sigma_a(z)-\sigma_a(w)}\\
&=
K(\sigma_a(z),\sigma_a(w)).
\end{aligned}
\]

If `z=w`, both sides are zero by convention, so the equivariance is global:

\[
\boxed{
\sigma_a(K(z,w))
=
K(\sigma_a(z),\sigma_a(w)).
}
\]

Applying `sigma_a` to `L_q` therefore just permutes the Cartesian product of shell indices:

\[
\begin{aligned}
\sigma_a(L_q)
&=
\sum_{z_1\in S_1,\ldots,z_{q-1}\in S_{q-1}}
\prod_j K(\sigma_a z_j,\sigma_a z_{j+1})\\
&=L_q.
\end{aligned}
\]

Thus `L_q` is fixed by every automorphism of `E/Q`. Since the fixed field of the full cyclotomic Galois group is `Q`,

\[
\boxed{
L_q(n_1,\ldots,n_{q-1})\in\mathbb Q.
}
\]

Exactly the same reindexing proves

\[
\boxed{
\operatorname{Tr}
(P_{n_0}KP_{n_1}K\cdots P_{n_{q-1}}K)
\in\mathbb Q.
}
\]

No Fourier transform, character decomposition, limiting process, or analytic continuation is used.

The argument is more general than cotangent: any fully contracted finite scalar network whose vertex sets are complete Galois-stable root sets and whose local weights are rational functions over `Q` is Galois-fixed, provided the chosen expression has no unresolved poles. The cotangent shell words are the canonical Prime-Circle instance.

## 3. Reflection plus Galois classifies the scalar word at number-field level

PC-090 proves that conjugation reflection anticommutes with `K`, commutes with every exact-shell projector, and fixes the anchor. Hence

\[
q\ \text{odd}
\quad\Longrightarrow\quad
L_q=0
\]

and the corresponding odd cyclic traces vanish.

Combining that selection rule with the Galois theorem gives the exact dichotomy

\[
\boxed{
L_q=
\begin{cases}
0,&q\ \text{odd},\\
\text{a rational number},&q\ \text{even}.
\end{cases}
}
\]

The statement is intentionally **not** integrality. Already the two-edge loop through `P_3^*` gives

\[
\boxed{
L_2(3)=\frac23.
}
\]

Indeed `K(1,\zeta_3)=-i/\sqrt3` and `K(\zeta_3,1)=i/\sqrt3`, and the two primitive cubic roots contribute `1/3` each. This is a direct falsification control against accidentally strengthening `Q` to `Z`.

## 4. The first even higher-memory survivor has an explicit one-shell Galois-trace form

PC-090 killed the first three-propagator/two-intermediate-shell loop but left the next even case open. Let `A`, `B`, `C` be complete primitive shells with `A\cap B=B\cap C=\varnothing` (while `A=C` is allowed), and define

\[
k(z)=K(1,z),
\qquad
\sigma_A(z)=\sum_{u\in A}K(z,u).
\]

PC-089 gives, for a primitive shell `A=P_a^*`,

\[
\boxed{
\sigma_A(z)
=
\varphi(a)-2z\frac{\Phi_a'(z)}{\Phi_a(z)},
\qquad z\notin A,
}
\]

and cyclotomic reciprocity gives `sigma_A(1)=0`.

For `z in B`, the PC-089 three-point identity yields

\[
\begin{aligned}
T_A(z)
&:=
\sum_{u\in A}K(1,u)K(u,z)\\
&=
-k(z)\sigma_A(z)-|A|.
\end{aligned}
\]

Contracting the two sides of the four-edge loop through the middle shell `B` therefore gives

\[
\boxed{
L_4(A,B,C)
=
\sum_{z\in B}
\bigl(k(z)\sigma_A(z)+|A|\bigr)
\bigl(k(z)\sigma_C(z)+|C|\bigr).
}
\]

Thus the first even-parity higher-memory scalar left by PC-090 is not an irreducible three-shell period. It is a **single Galois trace over the central primitive shell** of a rational function generated by the anchor cotangent profile and cyclotomic logarithmic derivatives.

When `A=C`, Hermiticity makes the control especially transparent:

\[
\boxed{
L_4(A,B,A)
=
\|P_B K P_A K e_1\|^2
\in\mathbb Q_{\ge0}.
}
\]

The value can be arithmetically nontrivial; the theorem only identifies its fixed field and its endpoint/cyclotomic algebraic provenance.

## 5. Matched controls and the precise obstruction

The rationality proof does not use primality of any shell order. It uses only:

1. a finite Galois extension generated by the chosen roots;
2. stability of every summed vertex set under the Galois action;
3. a scalar obtained by summing all internal indices;
4. local weights defined over `Q`.

Therefore the same conclusion holds for full regular polygons, unions of divisor shells, composite primitive shells, and any other Galois-stable finite root configuration. At the level of mechanism,

\[
\boxed{
\text{complete Galois-stable shells}
\to
\text{finite rational-function contraction}
\to
\mathbb Q
}
\]

is not a prime-specific phenomenon.

This closes one specific escape hatch from PC-089/PC-090: adding finitely many unweighted exact-shell memories cannot create a new fixed-level cyclotomic phase or higher period after **full scalar contraction**. A reflection-odd rational-function insertion can make an odd-parity expression nonzero, but once all complete shells are summed the same Galois argument still puts that scalar in `Q`.

The obstruction does **not** apply to:

- non-scalar block/tensor data retained before complete contraction;
- infinite-dimensional Hardy/Hankel operators such as PC-075--PC-086;
- analytic operations involving logarithms, boundary limits, or other functions not rational over `Q`;
- global uniformization/monodromy data;
- or cross-level sequences, Gram constructions, asymptotic determinants, and Dirichlet/Mellin transforms built from the resulting rational numbers.

Those boundaries are essential. Rationality is a fixed-level field statement, not an RH impossibility theorem.

## 6. Prior-art and novelty audit

No historical novelty is claimed for the fixed-field argument.

- Cyclotomic Galois theory makes `Q` the fixed field of `Gal(Q(zeta_M)/Q)` and makes each exact-order root set a Galois orbit/stable set. The proof above is the elementary trace/invariance consequence.
- Kurt Girstmair, *Cotangent power sums and character coordinates* (2025), explicitly treats `i cot(pi k/n)` as cyclotomic-field data and organizes its Galois orbit by character coordinates, Gauss sums, and generalized Bernoulli values. This is direct prior-art warning against interpreting finite cotangent Galois data as a new analytic spectrum.
- Matthias Beck, *Dedekind cotangent sums* (2003), places broad finite products of cotangent derivatives at rational arguments inside the established generalized Dedekind-sum framework.
- John Lewis and Don Zagier, *Cotangent sums, quantum modular forms, and the generalized Riemann hypothesis* (2019), provide the critical counter-warning: a different **cross-scale/asymptotic** family of rational-cotangent matrices can encode a GRH criterion. Hence the present theorem must not be promoted into a blanket no-go for rational cotangent data.

These sources are already anchored in `research/prime_circle/SOURCES.md`. The durable contribution here is the Prime-Circle-specific research boundary obtained by combining its complete primitive-shell summation with the rational cotangent kernel: the entire finite fully contracted scalar shell-word family is Galois-rational, and the odd half is identically zero by PC-090.

## 7. Exact falsification tests

The claim is finite and has several direct checks.

1. Verify
   \[
   K(z,w)=-(z+w)/(z-w)
   \]
   for distinct roots and the equivariance `sigma(K)=K(sigma z,sigma w)`.
2. For any shell order `n|M`, verify that `z -> z^a`, `(a,M)=1`, preserves exact order `n`.
3. Compute any finite shell loop in `Q(zeta_M)` and apply all `a in U(M)`; every automorphism must leave the scalar unchanged.
4. Check the non-integral control `L_2(3)=2/3`.
5. For the first even higher-memory case, compare the direct four-edge sum with
   \[
   \sum_{z\in B}
   (k\sigma_A+|A|)(k\sigma_C+|C|).
   \]
6. For odd `q`, independently recover zero from PC-090 reflection chirality.

A counterexample to Galois invariance of a complete-shell scalar would refute the theorem. A nonzero odd word would instead refute the PC-090 reflection hypothesis or reveal that an inserted weight breaks its parity assumptions.

## 8. Consequence for the surviving shell-cocycle clue

The accepted `CLUE-preimage-tube-fiber-sector-cocycle` had already been narrowed by PC-087--PC-090 to higher-memory, even-parity, shell-aware constructions. The present result narrows the scalar part further:

\[
\boxed{
\text{finite fully contracted exact-shell cotangent word}
\Longrightarrow
\begin{cases}
0,&\text{odd reflection parity},\\
\mathbb Q,&\text{even cotangent length}.
\end{cases}
}
\]

Accordingly, a genuinely new fixed-level carrier must retain non-scalar relational data before contraction or leave the finite rational-function shell algebra. A cross-level organization of the rational scalars remains logically open and must be judged separately against Lewis--Zagier/Dedekind-Vasyunin prior art. PC-091 supplies no spectral parameter, functional equation, gamma factor, or critical-line selector.
