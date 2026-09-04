# AF-106 — Bounded WOT closure is the admissibility assembly gate

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-OPERATOR-TOPOLOGY-MECHANISM`, `CATEGORY-EXPLICIT-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

Let `X` and `K` be Banach spaces, let

\[
J_K:K\to K^{**}
\]

be the canonical embedding, and let

\[
\mathcal A\subseteq \mathcal L(X,K)
\]

be a declared class of admissible repairs: equivariant maps, positive maps, maps satisfying specified linear relations, or any other source-imposed operator constraint.

AF-105 identifies pointwise weak compactness of a bounded repair family as an exact gate forcing a pointwise weak-star bidual limit back into the original target `K`. The next question is whether the **extra admissibility carried by every approximant** also survives that assembly.

For `C\ge 0`, write

\[
\mathcal A_C
:=
\mathcal A\cap C B_{\mathcal L(X,K)},
\tag{1}
\]

and denote weak-operator closure by `\overline{\cdot}^{\rm WOT}`. Then:

### 1. Orbit-compact assembly preserves exactly the bounded WOT closure of the declared constraint

Suppose `(S_i)\subseteq\mathcal A_C` satisfies

\[
J_KS_i x\longrightarrow Ux
\quad\text{weak-star in }K^{**}
\qquad(x\in X),
\tag{2}
\]

and for every `x\in X` the orbit

\[
\{S_i x:i\}
\tag{3}
\]

is relatively weakly compact in `K`.

Then AF-105 gives a unique `S\in\mathcal L(X,K)` such that

\[
U=J_KS,
\qquad
S_i x\to Sx\text{ weakly in }K
\quad(x\in X).
\tag{4}
\]

The second statement is precisely WOT convergence. Therefore

\[
\boxed{
S\in\overline{\mathcal A_C}^{\rm WOT}.
}
\tag{5}
\]

Consequently the correct generic retention condition is not "every finite repair has property `\mathcal A`" but

\[
\boxed{
\mathcal A_C\text{ is WOT-closed for the relevant uniform budget }C.
}
\tag{6}
\]

Whenever (6) holds, every orbit-compact assembly of `C`-bounded admissible repairs remains admissible:

\[
S_i\in\mathcal A_C
\quad\Longrightarrow\quad
S\in\mathcal A_C.
\tag{7}
\]

Thus original-range recovery and admissibility recovery are two distinct gates:

\[
\boxed{
\text{orbit weak compactness}
\Rightarrow
\text{assembly in }K,
\qquad
\text{bounded WOT closure of }\mathcal A
\Rightarrow
\text{assembly still lies in }\mathcal A.
}
\tag{8}
\]

### 2. For reflexive targets, bounded WOT closure is also sharp

If `K` is reflexive, bounded subsets of `K` are relatively weakly compact. Hence for every `C` and every

\[
S\in\overline{\mathcal A_C}^{\rm WOT}
\tag{9}
\]

there is a net `(S_i)\subseteq\mathcal A_C` converging WOT to `S`, and every orbit (3) is automatically relatively weakly compact. Since `K=K^{**}` canonically, this net is an AF-105 admissible assembly with limit `S`.

Therefore, for reflexive `K`, the set of all limits obtainable from `C`-bounded admissible repairs under the AF-105 assembly rule is exactly

\[
\boxed{
\overline{\mathcal A_C}^{\rm WOT}.
}
\tag{10}
\]

So WOT-closedness is not merely a convenient sufficient condition in that regime: it is the exact topological condition preventing a per-repair constraint from disappearing at the limit.

### 3. Equivariance, closed-cone positivity, and fixed linear relations survive automatically

Many structural constraints relevant to Mathia are WOT-closed because they are defined coefficientwise.

If `\rho:G\to\mathcal L(X)` and `\pi:G\to\mathcal L(K)` are bounded representations and

\[
\mathcal A_{\rm eq}
=
\{S:S\rho(g)=\pi(g)S\text{ for every }g\in G\},
\tag{11}
\]

then `\mathcal A_{\rm eq}` is WOT-closed: left and right multiplication by a fixed bounded operator are WOT-continuous, so (11) is an intersection of kernels of WOT-continuous linear maps.

Likewise, if `X` and `K` are ordered Banach spaces with norm-closed convex positive cones, then

\[
\mathcal A_+
=
\{S:S(X_+)\subseteq K_+\}
\tag{12}
\]

is WOT-closed. A norm-closed convex cone is weakly closed, and WOT convergence gives `S_i x\to Sx` weakly for each fixed `x\in X_+`.

More generally, any family of fixed affine operator identities such as

\[
A_jSB_j=C_j
\tag{13}
\]

with bounded fixed `A_j,B_j,C_j` defines a WOT-closed admissibility class. The norm ball itself is WOT-closed because

\[
\|S\|
=
\sup_{\|x\|\le1,\ \|k^*\|\le1}
|k^*(Sx)|.
\tag{14}
\]

Hence symmetry, order, normalization, annihilation, and other coefficientwise closed relations can pass through AF-105 assembly without an additional family-level compactness theorem once the original-range gate has already been established.

### 4. Per-operator weak compactness does **not** survive; collective compactness is genuinely stronger

The preceding principle is sharp because important properties are not WOT-closed.

Take

\[
X=K=\ell^1
\]

and let `P_n:\ell^1\to\ell^1` be the coordinate truncation

\[
P_n(x_1,x_2,\ldots)
=(x_1,\ldots,x_n,0,0,\ldots).
\tag{15}
\]

Then:

- `\|P_n\|=1`;
- every `P_n` has finite rank, hence is compact and weakly compact;
- `P_nx\to x` in norm for every `x\in\ell^1`.

Thus each pointwise orbit

\[
\{P_nx:n\ge1\}
\tag{16}
\]

is relatively norm compact, hence relatively weakly compact, and the AF-105 assembly limit is

\[
S=I_{\ell^1}.
\tag{17}
\]

But `I_{\ell^1}` is not weakly compact because `\ell^1` is not reflexive. Therefore

\[
\boxed{
P_n\text{ weakly compact for every }n,
\qquad
P_n\to I_{\ell^1}\text{ SOT (hence WOT)},
\qquad
I_{\ell^1}\text{ not weakly compact}.
}
\tag{18}
\]

So the property "this individual repair is weakly compact" can disappear even under a uniformly bounded **sequence** whose pointwise repair orbits are norm compact.

This also explains why AF-105's stronger collective condition cannot be replaced by per-operator weak compactness. Indeed

\[
\bigcup_n P_n(B_{\ell^1})
\tag{19}
\]

contains every unit vector `e_m`. The space `\ell^1` has the Schur property, so a weakly convergent sequence converges in norm; the sequence `(e_m)` has no norm-convergent subsequence. By Eberlein--Šmulian, (19) is not relatively weakly compact. Thus AF-105's collective compactness gate fails exactly where the weakly compact-operator property is lost.

The same example shows that compactness of each repair separately is not enough either.

## Derivation

### 1. AF-105 converts pointwise weak-star convergence into WOT convergence

Under (2)--(3), AF-105 proves `U=J_KS` and

\[
S_i x\to Sx\quad\text{weakly in }K
\tag{20}
\]

for every `x\in X`. By definition, (20) says

\[
k^*(S_i x)\to k^*(Sx)
\qquad
(x\in X,\ k^*\in K^*),
\tag{21}
\]

which is exactly WOT convergence in `\mathcal L(X,K)`. Since every `S_i` lies in `\mathcal A_C`, (5) follows immediately.

If `\mathcal A_C` is WOT-closed, (7) follows. No stronger topology may be silently substituted: the assembly theorem supplies exactly the scalar matrix coefficients (21).

### 2. Reflexivity turns the closure statement into a converse

Assume `K` reflexive and (9). By the definition of topological closure there is a net `(S_i)\subseteq\mathcal A_C` converging WOT to `S`. For each fixed `x`,

\[
\|S_i x\|\le C\|x\|,
\tag{22}
\]

so the orbit is bounded. Reflexivity makes every bounded subset of `K` relatively weakly compact. Therefore the net satisfies the AF-105 orbit condition automatically, proving (10).

The fixed budget in (9) is essential. An unrestricted closure may be witnessed by a net with no common operator-norm bound; Arithmetic Fidelity must keep the resource category explicit rather than infer bounded accessibility from bare topological closure.

### 3. Coefficientwise constraints are WOT-closed

For equivariance, fix `g\in G`, `x\in X`, and `k^*\in K^*`. If `S_i\to S` WOT and each `S_i` satisfies (11), then

\[
\begin{aligned}
k^*(S\rho(g)x)
&=\lim_i k^*(S_i\rho(g)x)\\
&=\lim_i k^*(\pi(g)S_i x)\\
&=\lim_i \pi(g)^*k^*(S_i x)\\
&=k^*(\pi(g)Sx).
\end{aligned}
\tag{23}
\]

Since `k^*` is arbitrary, `S\rho(g)=\pi(g)S`.

For positivity, if `x\in X_+`, then every `S_i x\in K_+`. A norm-closed convex subset of a Banach space is weakly closed by Hahn--Banach separation, so the weak limit `Sx` also lies in `K_+`.

The same matrix-coefficient argument proves closure of (13), while (14) expresses the radius constraint as an intersection of WOT-closed scalar inequalities.

### 4. The `\ell^1` control separates pointwise from collective coherence

Equation (15) gives finite-rank contractions and

\[
\|P_nx-x\|_1
=\sum_{j>n}|x_j|	o0.
\tag{24}
\]

Hence (16) is a convergent sequence together with finitely many initial terms, so its norm closure is compact. The limit operator is the identity.

A bounded operator `T:X\to Y` is weakly compact exactly when `T(B_X)` is relatively weakly compact. For `T=I_X`, this is equivalent to weak compactness of `B_X`, hence to reflexivity of `X`. Since `\ell^1` is nonreflexive, (18) follows.

Finally `e_m\in P_m(B_{\ell^1})`, so all unit vectors occur in (19). Schur's theorem and Eberlein--Šmulian rule out relative weak compactness of that union. The loss in (18) is therefore not a defect in AF-105: it is exactly the distinction between pointwise orbit coherence and coherence of the entire repaired unit ball.

## Exact controls and failure modes

### WOT-closedness is category-relative, not an intrinsic virtue

Equation (6) does not say WOT is always the "right" topology. WOT appears because AF-105's assembly conclusion is pointwise weak convergence. A different assembly mechanism may induce a different closure topology and therefore a different survival criterion.

The rule is structural: **a constraint on approximants survives only if it is closed in the topology actually supplied by the assembly theorem**, unless some additional theorem upgrades the convergence.

### Uniform budget must remain visible

The relevant object is `\overline{\mathcal A_C}^{\rm WOT}` for a declared finite `C`, not an unbudgeted WOT closure. Nets used merely to witness unrestricted closure can hide arbitrarily large norms outside every chosen tail. Such a closure statement would not certify AF-100/AF-105 bounded accessibility.

### Pointwise admissibility and collective admissibility are different data

The `\ell^1` example shows that requiring every `S_i` to be weakly compact is a property of individual members and is too weak. AF-105's condition

\[
\bigcup_iS_i(B_X)\text{ relatively weakly compact}
\tag{25}
\]

is a property of the **whole family**. It carries cross-index coherence that no statement of the form `S_i\in\mathcal A` for each `i` can replace when `\mathcal A` is not WOT-closed.

This is directly analogous to the line's earlier finite-versus-uniform and local-versus-global separations: a good property at every finite stage need not be closed under the declared global assembly operation.

### Positivity does not imply canonicity

Although positivity survives WOT assembly, it need not select a unique repair. AF-080 already shows that positivity of a projection alone can leave a nontrivial shear family, while the stronger two-sided order condition selects a band projection. AF-106 concerns **survival of a declared property**, not uniqueness or naturality of the resulting repair.

### No arithmetic specificity follows

Equivariance, positivity, and WOT closure are generic categorical properties. They do not distinguish rational primes from matched controls. In a later arithmetic application the admissibility class must first be derived intrinsically from the prime construction; AF-106 only states which such constraints are stable under an AF-105-type assembly.

## Prior art and novelty assessment

The mathematical ingredients are classical operator-topology and Banach-space facts. **No theorem-level novelty is claimed.** WOT is by definition coefficientwise weak convergence; weakly closed convex cones preserve positivity under weak limits; reflexive spaces turn bounded sets into relatively weakly compact sets; weak compactness of the identity characterizes reflexivity; `\ell^1` has the Schur property; and Eberlein--Šmulian identifies weak compactness with weak sequential compactness in Banach spaces.

- John B. Conway, ***A Course in Functional Analysis***, Graduate Texts in Mathematics 96, Springer, 2nd ed. (1990; later Springer electronic reprint), DOI `10.1007/978-1-4757-4383-8`. Role: standard reference for locally convex/weak topologies and operator-topology closure arguments.
- Robert E. Megginson, ***An Introduction to Banach Space Theory***, Graduate Texts in Mathematics 183, Springer (1998), ISBN `0-387-98431-3`. Role: standard Banach-space source for reflexivity, weak compactness, canonical bidual embeddings, Goldstine, Eberlein--Šmulian, and the Schur property of `\ell^1`.
- Charalambos D. Aliprantis and Owen Burkinshaw, ***Positive Operators***, Springer (2006 reprint of the 1985 monograph), DOI `10.1007/978-1-4020-5008-4`. Role: authoritative background for ordered Banach spaces/Banach lattices and positive operators; positivity is an established closed-cone operator constraint, not a new Arithmetic Fidelity construction.
- Joseph Diestel, ***Sequences and Series in Banach Spaces***, Graduate Texts in Mathematics 92, Springer (1984), DOI `10.1007/978-1-4612-5200-9`. Role: classical weak-sequential compactness and Schur-property background used in the `\ell^1` control.

A targeted prior-art search across WOT/SOT closure, weakly compact operator ideals, positive operators, reflexivity, and weakly compact families did not reveal a new operator-theory theorem here. The durable Arithmetic Fidelity content is the exact two-gate translation forced by AF-105 and the sharp `\ell^1` control: original-target assembly does **not** automatically preserve all structure carried stagewise; coefficientwise WOT-closed constraints survive, while nonclosed compactness properties require genuinely collective coherence.

## Consequences for Arithmetic Fidelity

AF-105 answered **where the assembled map lands**. AF-106 answers a different question: **which properties of the approximating repairs survive once it lands there**.

The resulting audit is:

\[
\boxed{
\begin{array}{c}
\text{bounded finite repairs in }\mathcal A\\
+\ \text{pointwise weak compactness}\\
\Downarrow\\
\text{original-range limit }S\in\overline{\mathcal A_C}^{\rm WOT}.
\end{array}
}
\tag{26}
\]

If the source-imposed admissibility class is boundedly WOT-closed, the property survives automatically. If it is not, stagewise membership carries no such guarantee; one needs a stronger family-level invariant, convergence upgrade, or compactness principle.

This separates two kinds of structure that had been bundled together in the current frontier. Symmetry/order/linear identities are often **closure constraints**. Weak compactness, compactness, and similar global properties can be **coherence constraints** that are invisible from membership of each approximant separately. A later prime-specific repair theorem must identify which kind of constraint it needs before treating a coherent limit as preserving the arithmetic mechanism.