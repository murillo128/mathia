# PL-382 — Nyman's integer dilation semigroup is the exact non-doubly-commuting boundary of positive-energy Wold regularity

**Evidence:** `LITERATURE+EXACT-DERIVED + DECISIVE-STRUCTURAL-BOUNDARY + PRIOR-ART-REDIRECT`.

**Parent finding:** `PL-381`.

**Related findings:** `PL-017`, `PL-018`, `PL-019`, `PL-380`, `PL-381`.

**Status:** `THE-DOUBLE-COMMUTATIVITY-HYPOTHESIS-IN-PL-381-IS-NOT-A-TECHNICAL-CONVENIENCE: THE-CLASSICAL-NYMAN/BAGCHI-INTEGER-DILATIONS-SIT-ON-THE-OTHER-SIDE-OF-THAT-BOUNDARY. ON-THE-AMBIENT-L2(0,1)-SPACE-THEY-ARE-COMMUTING-PURE-ISOMETRIES-WITH-A-SEMIBOUNDED-SELFADJOINT-GENERATOR-AND-EXACT-LOG-PRIME-COVARIANCE, AND-THEIR-JOINT-WANDERING-SUBSPACE-EVEN-GENERATES, BUT-THEY-FAIL-DOUBLE-COMMUTATIVITY-BECAUSE-ALL-PRIME-DIRECTIONS-ARE-EMBEDDED-IN-ONE-CONTINUOUS-DILATION/TRANSLATION-SEMIGROUP. THE-SAME-INTEGER-OPERATORS-RESTRICT-TO-THE-NYMAN-STEP-SPACE-USED-IN-THE-RH-EQUIVALENT-TOTALITY-PROBLEM-AND-REMAIN-NON-DOUBLY-COMMUTING-THERE. THUS-PL-381-CANNOT-BE-USED-TO-CANONICALIZE-AWAY-THE-NYMAN-ROUTE; THE-SURVIVING-OPERATORIAL-DIFFERENCE-IS-PRECISELY-THE-OVERLAPPING-ONE-DIMENSIONAL-BOUNDARY-GEOMETRY, WHICH-IS-ITSELF-GENERIC-AND-NOT-YET-AN-RH-MECHANISM`.

## Claim

On

\[
\mathcal H=L^2((0,1),dx),
\tag{PL382-1}
\]

define, for every real `r>=1`,

\[
(D_r f)(x)
=
\begin{cases}
\sqrt r\,f(rx),&0<x\le 1/r,\\
0,&1/r<x\le1.
\end{cases}
\tag{PL382-2}
\]

These are the normalized dilation isometries underlying the Nyman--Beurling/Bagchi realization in `PL-017`; for integer `r=n` they are exactly Bagchi's operators `T_n` on the invariant Nyman step space.

Let

\[
(Af)(x)=(-\log x)f(x),
\qquad
U_t=e^{itA}.
\tag{PL382-3}
\]

Then `A` is self-adjoint, nonnegative, and

\[
D_rD_s=D_{rs},
\qquad
U_tD_rU_t^*=r^{it}D_r.
\tag{PL382-4}
\]

Hence the prime operators

\[
V_p:=D_p
\tag{PL382-5}
\]

are commuting isometries satisfying the exact positive-energy covariance

\[
U_tV_pU_t^*=e^{it\log p}V_p
\tag{PL382-6}
\]

with the same weights as `PL-381`. Every `V_p` is pure, and the joint wandering subspace

\[
W:=\bigcap_p\ker V_p^*
\tag{PL382-7}
\]

is generating.

Nevertheless the family is **not doubly commuting**. Already

\[
V_2^*V_3\ne V_3V_2^*.
\tag{PL382-8}
\]

Indeed, for `1<a<b`,

\[
D_a^*D_b=D_{b/a},
\tag{PL382-9}
\]

whereas `D_bD_a^*` is the same rescaled translation only after an additional boundary cutoff. Their difference is an infinite-rank boundary operator.

Moreover

\[
W=L^2((1/2,1]),
\tag{PL382-10}
\]

and

\[
D_nW=L^2((1/(2n),1/n]).
\tag{PL382-11}
\]

The intervals in (PL382-11) cover `(0,1]`, so `W` generates `H`; but they overlap, for example

\[
D_2W\cap D_3W
=
L^2((1/4,1/3])\ne\{0\}.
\tag{PL382-12}
\]

Thus the implication

\[
\text{commuting isometries}
+
\text{semibounded exact log-prime covariance}
+
\text{generating joint wandering space}
\Longrightarrow
\text{regular orthogonal prime multishift}
\tag{PL382-13}
\]

is false without double commutativity.

This is not an artificial control. The integer operators `D_n` are the same dilation family used in the classical Nyman/Báez-Duarte Hilbert-space route to RH. Their restriction to Bagchi's step space remains non-doubly-commuting. Consequently the double-commuting hypothesis in `PL-381` excludes an already established RH-equivalent representation rather than following from the prime-lattice arithmetic itself.

At the same time, this does **not** produce a new RH mechanism. Under logarithmic coordinates all `D_r` lie on one ordinary one-parameter right-shift semigroup, and the same construction works for arbitrary positive frequency sets. The surviving structure is therefore a precise route boundary: any future use of the Nyman representation must exploit additional target-relative/arithmetic information in its overlapping invariant-subspace geometry, not non-double-commutativity by itself.

## 1. The Nyman dilation family has exact positive-energy covariance

For `r>=1`, a change of variables gives

\[
\|D_rf\|_2^2
=
\int_0^{1/r}r|f(rx)|^2dx
=
\int_0^1|f(u)|^2du,
\tag{PL382-14}
\]

so every `D_r` is an isometry. Direct substitution also gives

\[
D_rD_s=D_{rs}.
\tag{PL382-15}
\]

The operator `A=M_{-\log x}` is self-adjoint on its natural multiplication domain and

\[
\sigma(A)=[0,\infty).
\tag{PL382-16}
\]

Thus it has exactly the positive-energy property used in `PL-381`. Since

\[
(U_tf)(x)=x^{-it}f(x),
\tag{PL382-17}
\]

we obtain, for `x<=1/r`,

\[
\begin{aligned}
(U_tD_rU_t^*f)(x)
&=x^{-it}\sqrt r\,(rx)^{it}f(rx)\\
&=r^{it}(D_rf)(x),
\end{aligned}
\tag{PL382-18}
\]

and both sides vanish for `x>1/r`. Therefore

\[
U_tD_rU_t^*=e^{it\log r}D_r.
\tag{PL382-19}
\]

Restricting to rational primes gives every hypothesis of the first line of `PL-381` except double commutativity.

The representation of the positive exponent semigroup is faithful. If

\[
\alpha\ne\beta
\quad\text{in}\quad
\mathbb N_0^{(\mathcal P)},
\tag{PL382-20}
\]

then unique factorization gives distinct integers

\[
\prod_pp^{\alpha_p}\ne\prod_pp^{\beta_p},
\tag{PL382-21}
\]

and hence distinct dilation parameters. Thus the example does not identify two different integer lattice points algebraically. What it does collapse is their **multidirectional operator geometry**: the entire representation factors through the scalar energy coordinate

\[
\alpha
\longmapsto
\sum_p\alpha_p\log p.
\tag{PL382-22}
\]

That distinction is central below.

## 2. Double commutativity fails by an exact boundary defect

The adjoint of (PL382-2) is

\[
(D_r^*g)(u)=r^{-1/2}g(u/r),
\qquad 0<u\le1.
\tag{PL382-23}
\]

Take `1<a<b`. Then

\[
(D_a^*D_bf)(u)
=
\begin{cases}
\sqrt{b/a}\,f((b/a)u),&u\le a/b,\\
0,&u>a/b,
\end{cases}
\tag{PL382-24}
\]

which is exactly

\[
D_a^*D_b=D_{b/a}.
\tag{PL382-25}
\]

By contrast,

\[
(D_bD_a^*f)(u)
=
\begin{cases}
\sqrt{b/a}\,f((b/a)u),&u\le1/b,\\
0,&u>1/b.
\end{cases}
\tag{PL382-26}
\]

Since `1/b<a/b`, (PL382-24) and (PL382-26) differ on the whole interval

\[
(1/b,a/b].
\tag{PL382-27}
\]

Equivalently, if `P_E` denotes multiplication by `1_E`, then

\[
D_bD_a^*
=
P_{(0,1/b]}D_{b/a},
\tag{PL382-28}
\]

and

\[
D_a^*D_b-D_bD_a^*
=
P_{(1/b,a/b]}D_{b/a}.
\tag{PL382-29}
\]

The right side has infinite-dimensional range. Thus the failure of double commutativity is not a compact or trace-class perturbative defect; it is a macroscopic boundary sector created by the one-sided cutoff at `x=1`.

For the prime pair `2,3`, (PL382-29) gives the explicit obstruction

\[
D_2^*D_3-D_3D_2^*
e0.
\tag{PL382-30}
\]

This pinpoints exactly which hypothesis of `PL-381` the dilation model violates.

## 3. Positive energy and a generating wandering space still do not recover the prime Fock geometry

From (PL382-23),

\[
\ker D_p^*
=
L^2((1/p,1]).
\tag{PL382-31}
\]

Because `2` is the smallest prime,

\[
W
=
\bigcap_pL^2((1/p,1])
=
L^2((1/2,1]).
\tag{PL382-32}
\]

For every integer `n>=1`, dilation gives

\[
D_nW=L^2((1/(2n),1/n]).
\tag{PL382-33}
\]

These orbit subspaces generate all of `H`. Indeed, for every `x in (0,1]`, put `y=1/x>=1` and `n=floor(y)`. Then

\[
n\le y<n+1\le2n,
\tag{PL382-34}
\]

so

\[
1/(2n)<x\le1/n.
\tag{PL382-35}
\]

Hence the intervals in (PL382-33) cover `(0,1]`. If a vector were orthogonal to every `D_nW`, it would vanish on every one of these intervals and therefore vanish almost everywhere.

But these orbit subspaces are not mutually orthogonal and are not even pairwise disjoint. For example,

\[
(1/4,1/2]\cap(1/6,1/3]
=(1/4,1/3],
\tag{PL382-36}
\]

which proves (PL382-12).

This is a sharp control on `PL-380`--`PL-381`. A generating joint wandering subspace plus exact positive-energy covariance does **not** by itself produce the orthogonal decomposition

\[
\mathcal H
=\bigoplus_{\alpha}V^\alpha W.
\tag{PL382-37}
\]

Double commutativity is what turns different coordinate histories into orthogonal prime-Fock sectors. Without it, the same lattice can be represented by heavily overlapping translates along a single ordered half-line.

## 4. Logarithmic coordinates reveal the one-dimensional collapse exactly

Define the unitary

\[
(Jf)(y)=e^{-y/2}f(e^{-y}),
\qquad
J:L^2((0,1),dx)\to L^2(\mathbb R_+,dy).
\tag{PL382-38}
\]

Writing `r=e^a`, a direct calculation gives

\[
(JD_{e^a}J^{-1}h)(y)
=
\begin{cases}
h(y-a),&y\ge a,\\
0,&0\le y<a.
\end{cases}
\tag{PL382-39}
\]

This is the standard right-translation isometric semigroup `S_a` on the half-line. At the same time,

\[
JAJ^{-1}=M_y.
\tag{PL382-40}
\]

Thus

\[
V_p
\longleftrightarrow
S_{\log p}.
\tag{PL382-41}
\]

All prime directions are therefore sampled times of **one** strongly continuous one-parameter semigroup. The identity

\[
\log n=\langle v(n),(\log p)_p\rangle
\tag{PL382-42}
\]

is not only an eigenvalue formula here; it is the map that collapses the whole exponent cone onto the translation parameter of the ambient flow.

This explains simultaneously why the representation is faithful on the ordinary integers and why it is not a coordinate-separated multishift. The map `n -> log n` is injective, but the images of different prime directions live on the same one-dimensional ordered geometry. Their boundary ranges are nested/overlapping rather than Nica-independent.

The right-shift semigroup itself is classical operator theory. Modern treatments of isometric semigroups routinely use (PL382-39) as the standard pure model; for example Gallardo-Gutiérrez and Partington, “C0-semigroups of 2-isometries and Dirichlet spaces,” *Revista Matemática Iberoamericana* 34 (2018), explicitly use the same right-shift semigroup on `L^2(R_+)`. No novelty is claimed for this model or its Wold theory.

## 5. The same non-double-commuting operators occur in the RH-equivalent Nyman route

`PL-017` records Bagchi's integer operators on the Nyman step space `M`:

\[
(T_mf)(x)
=
\begin{cases}
\sqrt m\,f(mx),&x\le1/m,\\
0,&x>1/m.
\end{cases}
\tag{PL382-43}
\]

Thus

\[
T_m=D_m|_M.
\tag{PL382-44}
\]

The restriction remains non-doubly-commuting. Let

\[
h=\sqrt2\,1_{(1/2,1]}\in M.
\tag{PL382-45}
\]

Since every vector in the range of `T_2` is supported in `(0,1/2]`,

\[
T_2^*h=0,
\qquad
T_3T_2^*h=0.
\tag{PL382-46}
\]

On the other hand,

\[
T_2h=2\,1_{(1/4,1/2]},
\qquad
T_3h=\sqrt6\,1_{(1/6,1/3]},
\tag{PL382-47}
\]

so

\[
\langle T_2^*T_3h,h\rangle
=
\langle T_3h,T_2h\rangle
=
2\sqrt6\,| (1/4,1/3] |
=
\frac{\sqrt6}{6}
\ne0.
\tag{PL382-48}
\]

Therefore

\[
T_2^*T_3\ne T_3T_2^*
\quad\text{on }M.
\tag{PL382-49}
\]

This matters because Bagchi's invariant Nyman subspace and the Báez-Duarte totality criterion use precisely these integer dilations. The non-double-commuting geometry is therefore present in an existing RH-equivalent formulation, not merely in an unrelated counterexample invented to falsify `PL-381`.

There is one important boundary condition. The multiplication group `U_t=x^{-it}` from (PL382-17) does **not** preserve the step space `M` for nonzero `t`; multiplying a step function by `x^{-it}` destroys stepwise constancy. Hence one must not claim that the restricted triple `(M,A,{T_p})` itself satisfies all hypotheses of `PL-381` except double commutativity. The exact positive-energy covariance belongs to the ambient `L^2(0,1)` extension, while the RH totality problem lives in the invariant step subspace for the integer semigroup. What survives on `M` exactly is the same multiplicative isometry family and its failure of double commutativity.

That distinction is enough for the route boundary: the operator family relevant to Nyman is excluded by the double-commuting axiom before one even asks whether its special invariant subspace is total.

## 6. The model is generic, so non-double-commutativity alone is not arithmetic rigidity

The construction does not need rational primes. Given any positive weights `{lambda_j}`, define

\[
V_j:=D_{e^{\lambda_j}}.
\tag{PL382-50}
\]

Then

\[
U_tV_jU_t^*=e^{it\lambda_j}V_j
\tag{PL382-51}
\]

and the `V_j` commute because they all belong to the same dilation semigroup. If the weights are integer-linearly independent, the resulting representation of the free positive exponent monoid is faithful, just as for `{log p}`.

Thus even the conjunction

\[
\text{faithful exponent-semigroup representation}
+
\text{semibounded exact covariance}
+
\text{pure isometries}
+
\text{one-parameter embedding}
\tag{PL382-52}
\]

is generic. It does not know that the weights came from rational primes, nor does it produce analytic continuation or a zeta zero divisor.

The rational-prime specialization becomes RH-relevant only after one adds the distinguished Nyman target/subspace and the Mellin identity involving `zeta`, as in `PL-017`--`PL-020`. This is exactly the kind of extra target-relative analytic information required by the line mandate.

## 7. Prior-art and novelty audit

The ingredients are classical.

- Nyman's 1950 thesis is explicitly built around a one-dimensional translation group and semigroup in function spaces.
- Bagchi's 2006 survey, already source 14 in `research/prime_lattice/SOURCES.md`, defines the normalized integer isometries used in (PL382-43), proves their multiplicative law, and uses them in the RH-equivalent totality formulation recorded in `PL-017`.
- The right-translation semigroup (PL382-39) is a standard pure isometric semigroup model; the cited 2018 paper of Gallardo-Gutiérrez--Partington is a modern explicit reference.
- `PL-380` and `PL-381` already prove the regular multishift conclusion under double commutativity and identify the positive-energy mechanism that globalizes the countable Wold structure.

The exact calculations (PL382-23)--(PL382-36) are elementary consequences of the dilation formula. A targeted literature/repository audit found no basis for claiming novelty for right-shift semigroups, Nyman dilations, or the general fact that commuting isometries need not doubly commute.

The durable new value for this line is therefore **not a theorem-novelty claim**. It is the matched-control consequence for the current frontier: the most important RH-equivalent prime-dilation realization is an explicit sharp witness that `PL-381` cannot drop double commutativity, even though the ambient representation has the exact same semibounded `log p` covariance and a generating joint wandering space.

## 8. Audit and falsification tests

The finding is falsified or materially narrowed if any of the following fails:

1. the operators (PL382-2) are not isometries or fail `D_rD_s=D_rs`;
2. `A=M_{-log x}` is not semibounded/self-adjoint or fails the covariance (PL382-19);
3. the adjoint formula (PL382-23) or the explicit non-double-commutation calculation (PL382-24)--(PL382-30) is wrong;
4. the joint wandering space is not (PL382-32), or its integer translates fail to generate `L^2(0,1)`;
5. Bagchi's integer operators differ from (PL382-43), so the connection to `PL-017` is false;
6. the restricted Nyman operators actually satisfy `T_2^*T_3=T_3T_2^*`, contradicting the explicit positive inner product in (PL382-48).

All six are direct calculations or literature-level definitions. What remains open is not whether the boundary exists, but whether the **overlap structure together with the distinguished Nyman target** admits a new arithmetic rigidity principle strong enough to force totality.

## Consequence for `prime_lattice`

`PL-379` showed that countably many abstract doubly commuting isometries can have diffuse Wold behavior. `PL-381` then showed that semibounded locally finite positive covariance kills that diffuse pathology and forces the regular prime multishift. The present finding identifies the exact hypothesis separating that rigidity from the classical RH-equivalent dilation route:

\[
\text{double commutativity / Nica independence}.
\tag{PL382-53}
\]

On the double-commuting side, positive energy separates prime directions into orthogonal Fock sectors and leaves only the generic `log n` Hamiltonian plus a prime-independent internal sector. On the Nyman side, the same integer semigroup is embedded in one ordered continuous dilation flow; prime-direction ranges overlap, adjoints fail to commute across coordinates, and the hard RH statement remains a target-relative totality problem.

This materially redirects the next operator-theoretic search. It is no longer useful to ask whether semibounded `log p` covariance by itself canonicalizes every one-sided prime representation: it does not. A viable continuation should instead ask whether the **non-double-commuting boundary overlaps of the Nyman dilation family, together with its distinguished invariant subspace/target and Mellin continuation, impose a rigidity not shared by arbitrary one-parameter shift samples**. Any claim using only the overlap algebra without that target-relative arithmetic input will fail the generic-weight control in Section 6.