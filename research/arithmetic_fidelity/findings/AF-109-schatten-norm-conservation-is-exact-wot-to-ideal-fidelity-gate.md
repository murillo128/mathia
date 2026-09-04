# AF-109 — Schatten norm conservation is the exact WOT-to-ideal fidelity gate

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-KADEC-KLEE`, `RESOURCE-NORM-FIDELITY`, `SPECTRAL-OBSERVABLE-INSUFFICIENCY`, `NO-NOVELTY-CLAIM`

## Claim

Let `H` be a separable infinite-dimensional complex Hilbert space and let

\[
1\le p<\infty.
\]

AF-108 separated two questions for WOT assemblies in Schatten ideals: a uniform `\mathcal S_p` budget preserves **membership** in the ideal, while scalar observables such as trace or Fredholm determinant may still lose information. The next gate is exact: once the weak operator limit is known, preservation of the full Schatten resource norm is precisely what upgrades weak assembly to convergence in the ideal norm.

### 1. WOT plus Schatten-norm conservation is equivalent to Schatten-norm convergence

Suppose a net `(T_i)` in `\mathcal S_p(H)` satisfies

\[
T_i\longrightarrow T
\quad\text{in WOT in }\mathcal L(H)
\tag{1}
\]

and

\[
\|T_i\|_p\longrightarrow\|T\|_p<\infty.
\tag{2}
\]

Then

\[
\boxed{
\|T_i-T\|_p\longrightarrow0.
}
\tag{3}
\]

Conversely, (3) implies both (1) and (2). Hence, for every finite Schatten class,

\[
\boxed{
T_i\to T\text{ in }\mathcal S_p
\iff
\bigl(T_i\to T\text{ in WOT and }\|T_i\|_p\to\|T\|_p\bigr).
}
\tag{4}
\]

Thus AF-108's WOT membership gate has a sharp second layer:

\[
\boxed{
\text{bounded }\mathcal S_p\text{ budget}
\Rightarrow
\text{category fidelity},
\qquad
\text{exact }\mathcal S_p\text{-norm conservation}
\Rightarrow
\text{full ideal-norm fidelity}.
}
\tag{5}
\]

The second implication is not an arbitrary strengthening of topology. It is the Kadec-Klee/Radon-Riesz phenomenon for Schatten ideals, expressed in the operator topology naturally supplied by the AF-105/AF-106 assembly framework.

### 2. The trace-class positive result of AF-108 is a special case

If `A_i,A\ge0` are trace class, then

\[
\|A_i\|_1=\operatorname{Tr}(A_i),
\qquad
\|A\|_1=\operatorname{Tr}(A).
\tag{6}
\]

Therefore AF-108's implication

\[
A_i\to A\text{ in WOT},
\qquad
\operatorname{Tr}(A_i)\to\operatorname{Tr}(A)
\quad\Longrightarrow\quad
\|A_i-A\|_1\to0
\tag{7}
\]

is exactly the `p=1` case of (4) after positivity converts the scalar trace into the complete `\mathcal S_1` resource norm.

This identifies the real role of positivity in AF-108: it does not merely improve semicontinuity. It makes a scalar observable coincide with the norm that controls the entire trace-class object.

### 3. Trace and the entire Fredholm-determinant function may both survive while operator fidelity fails

Let `(e_n)` be an orthonormal basis and, for `n\ge2`, define the rank-one operator

\[
V_n=|e_n\rangle\langle e_1|.
\tag{8}
\]

Then

\[
V_n\longrightarrow0
\quad\text{in WOT},
\tag{9}
\]

but for every finite `p`,

\[
\|V_n\|_p=1.
\tag{10}
\]

Moreover `V_n^2=0`, so all eigenvalues are zero and

\[
\operatorname{Tr}(V_n)=0=\operatorname{Tr}(0),
\tag{11}
\]

while for every `z\in\mathbb C`,

\[
\det(I+zV_n)=1=\det(I+z\,0).
\tag{12}
\]

Consequently

\[
\boxed{
\text{exact conservation of trace and of the full Fredholm-determinant function}
\not\Rightarrow
\text{trace-norm, or any finite Schatten-norm, fidelity}.
}
\tag{13}
\]

This is stronger than AF-108's escaped-projection example, where trace and determinant visibly failed to converge. Here the scalar spectral observables are **perfectly preserved** and nevertheless miss a unit of singular-value mass moving through orthogonal directions.

The lost datum is therefore not merely a scalar normalization. It is the nonnormal/off-diagonal operator geometry invisible to eigenvalue-only observables.

### 4. The finite-`p` hypothesis is sharp

Equation (4) fails for the operator norm `p=\infty`. Let `Q_n` be the orthogonal projection onto

\[
\operatorname{span}\{e_1,\ldots,e_n\}.
\tag{14}
\]

Then

\[
Q_n\to I_H
\quad\text{strongly, hence in WOT},
\tag{15}
\]

and

\[
\|Q_n\|=1=\|I_H\|
\tag{16}
\]

for every `n`, but

\[
\|Q_n-I_H\|=1.
\tag{17}
\]

Thus norm conservation by itself is not a universal principle for weak operator assembly. The finite Schatten ideals have the required Kadec-Klee geometry; `\mathcal L(H)` with operator norm does not.

## Derivation

### 1. The case `1<p<\infty`: WOT becomes weak `\mathcal S_p` convergence on bounded families

Let `q` be the conjugate exponent. From (2), `(T_i)` is bounded in `\mathcal S_p`, hence also bounded in operator norm.

For every finite-rank `R`, WOT convergence gives

\[
\operatorname{Tr}(R^*T_i)
\longrightarrow
\operatorname{Tr}(R^*T),
\tag{18}
\]

because the trace pairing is a finite linear combination of matrix coefficients.

Finite-rank operators are dense in `\mathcal S_q`, and Schatten Holder gives

\[
|\operatorname{Tr}((R-S)^*T_i)|
\le
\|R-S\|_q\,\|T_i\|_p.
\tag{19}
\]

The uniform `\mathcal S_p` bound therefore extends (18) from finite-rank operators to every `S\in\mathcal S_q`. Using the classical duality

\[
(\mathcal S_q)^*=\mathcal S_p,
\tag{20}
\]

we obtain

\[
T_i\rightharpoonup T
\quad\text{weakly in }\mathcal S_p.
\tag{21}
\]

For `1<p<\infty`, Schatten `p`-classes are uniformly convex. Hence they have the Kadec-Klee/Radon-Riesz property: weak convergence together with convergence of norms implies norm convergence. Equations (2) and (21) give (3).

This also explains why AF-108's uniform budget was already the right resource variable. WOT alone tests finite matrix coefficients, but boundedness in the dual Schatten geometry upgrades those tests to the full Banach-space weak topology; conservation of the norm then closes the remaining gap.

### 2. The trace-class endpoint `p=1`: bounded WOT is weak-star convergence against compact operators

For a uniformly trace-norm-bounded family, WOT convergence determines pairing against every compact operator. Indeed, for finite-rank `R`,

\[
\operatorname{Tr}(R^*T_i)
\to
\operatorname{Tr}(R^*T),
\tag{22}
\]

and finite-rank operators are operator-norm dense in `\mathcal K(H)`. The estimate

\[
|\operatorname{Tr}(K^*(T_i-T))|
\le
\|K\|\,\|T_i-T\|_1
\tag{23}
\]

plus the uniform trace-norm bound lets (22) extend to every `K\in\mathcal K(H)`.

Since

\[
\mathcal K(H)^*=\mathcal S_1(H),
\tag{24}
\]

bounded WOT convergence is exactly weak-star convergence `\sigma(\mathcal S_1,\mathcal K)` on this family. The trace class has the weak-star uniform Kadec-Klee property (Lennard), and more general symmetric-operator-space versions were subsequently developed by Dodds--Dodds--Dowling--Lennard--Sukochev. Therefore weak-star convergence together with

\[
\|T_i\|_1\to\|T\|_1
\tag{25}
\]

forces

\[
\|T_i-T\|_1\to0.
\tag{26}
\]

Barry Simon's classical trace-ideal convergence theorem is an earlier direct source for this type of weak-plus-norm convergence criterion in trace ideals.

### 3. Why the statement holds for nets, not only sequences

The classical Kadec-Klee formulations are often stated sequentially. In the present separable-Hilbert setting the net statement follows without introducing a stronger theorem.

Norm convergence in (2) gives a uniform `\mathcal S_p` bound, hence a uniform operator-norm bound. On operator-norm-bounded subsets of `\mathcal L(H)`, WOT is metrizable when `H` is separable. For `p=1`, the corresponding weak-star topology on bounded subsets of `\mathcal S_1=\mathcal K(H)^*` is also metrizable because `\mathcal K(H)` is separable.

If (3) failed for a net, there would be an `\varepsilon>0` such that arbitrarily far out one could choose an index with

\[
\|T_i-T\|_p\ge\varepsilon.
\tag{27}
\]

Choose successively such indices while also entering the first `n` members of a countable neighborhood base for WOT and making `|\|T_i\|_p-\|T\|_p|<1/n`. This produces a sequence satisfying WOT convergence and norm convergence but violating the sequential Kadec-Klee conclusion, a contradiction.

Thus the assembly statement (4) is valid for the nets naturally used in AF-105--AF-108.

### 4. The nilpotent control separates eigenvalue observables from singular-value mass

For (8), fixed `x,y\in H` satisfy

\[
\langle V_nx,y\rangle
=
\langle x,e_1\rangle\langle e_n,y\rangle
\longrightarrow0,
\tag{28}
\]

so (9) holds.

A rank-one operator `|u\rangle\langle v|` has one nonzero singular value `\|u\|\,\|v\|`. Hence every `V_n` has singular-value list

\[
(1,0,0,\ldots),
\tag{29}
\]

which proves (10) simultaneously for all finite Schatten norms.

For `n\ge2`, `\langle e_1,e_n\rangle=0`, giving

\[
V_n^2
=
|e_n\rangle\langle e_1,e_n\rangle\langle e_1|
=0.
\tag{30}
\]

Thus `V_n` is nilpotent of order two. Its nonzero spectral data vanish completely: trace is zero and the trace-class Fredholm determinant is identically one. Yet its singular-value mass remains exactly one. The example therefore isolates a precise information-loss mechanism:

\[
\boxed{
\text{eigenvalue/spectral scalarization can forget singular-direction geometry even when no scalar drift is visible.}
}
\tag{31}
\]

This distinction disappears on the positive cone because eigenvalues and singular values coincide there, which is why positivity turns trace conservation into trace-norm conservation in AF-108.

## Exact controls and failure modes

### Norm conservation is not the same as a bounded budget

AF-108's bound

\[
\sup_i\|T_i\|_p<\infty
\tag{32}
\]

only prevents the limit from leaving `\mathcal S_p`. It allows a positive amount of ideal mass to disappear under WOT, as the rank-one projections and the present nilpotent sequence show.

Equation (2) is strictly stronger: it states that the amount of `p`-mass in the approximants converges to the amount present in the limit. Kadec-Klee geometry says that, for finite Schatten classes, this scalar resource equality is sufficient to prevent every remaining hidden escape.

### Trace conservation is sufficient only in categories where trace is the norm

For positive trace-class operators,

\[
\operatorname{Tr}(A)=\|A\|_1,
\tag{33}
\]

so trace conservation closes the gap. For general trace-class operators, `\operatorname{Tr}` can vanish on a large subspace and does not control singular values. The `V_n` family proves that exact trace conservation cannot replace trace-norm conservation.

Self-adjointness alone also does not repair this. For example,

\[
D_n=P_{2n}-P_{2n+1}
\tag{34}
\]

is self-adjoint, WOT-null, has trace zero, and satisfies `\|D_n\|_1=2`. Positivity, not merely reality of the spectrum, is the decisive condition in AF-108's trace argument.

### Fredholm determinants are complete only for the eigenvalue product they encode

For trace-class operators, `z\mapsto\det(I+zT)` records the nonzero eigenvalues with algebraic multiplicity through its zeros/product representation. It does not recover nonnormal singular-vector geometry or the full operator up to unitary equivalence.

The nilpotent family makes this failure maximal: every determinant function is exactly the same as that of zero. Therefore determinant convergence, even locally uniform convergence of the entire determinant function, is not a substitute for `\mathcal S_1` convergence unless additional structure independently links eigenvalues to singular values.

### The operator-norm endpoint has different geometry

The projection control (14)--(17) shows that `\mathcal L(H)` does not have the corresponding WOT Kadec-Klee property. Any attempt to extrapolate (4) from finite Schatten ideals to arbitrary operator categories must therefore identify the geometric property that performs the upgrade rather than assuming that "weak convergence + norm conservation" is universal.

### Ideal-norm fidelity still does not imply arithmetic fidelity

Equation (4) is a topology/category theorem. It says that no operator information measured in `\mathcal S_p` norm is lost once WOT convergence and exact resource conservation have been proved. It does **not** establish that the operator itself contains a rational-prime discriminator, that the approximants are canonical, or that the needed norm conservation follows from arithmetic structure.

A Mathia application must derive the Schatten setting and the conservation law intrinsically. Imposing `\|T_i\|_p\to\|T\|_p` merely to force convergence would encode the desired no-loss conclusion into the admissibility assumptions.

## Prior art and novelty assessment

The convergence mechanism is classical. **No theorem-level novelty is claimed.**

- Barry Simon, **“Convergence in trace ideals,”** *Proceedings of the American Mathematical Society* 83(1), 39--43 (1981), DOI `10.1090/S0002-9939-1981-0619977-2`. Role: direct classical trace-ideal convergence source; establishes convergence principles in unitarily invariant/trace-ideal norms and is the nearest early prior art for the present weak-plus-norm formulation.
- C. J. Lennard, **“C1 is uniformly Kadec-Klee,”** *Proceedings of the American Mathematical Society* 109(1), 71--77 (1990). Role: direct prior art for the weak-star uniform Kadec-Klee property at the trace-class endpoint, where `\mathcal S_1=\mathcal K(H)^*`.
- P. G. Dodds, T. K. Dodds, P. N. Dowling, C. J. Lennard, and F. A. Sukochev, **“A uniform Kadec-Klee property for symmetric operator spaces,”** *Mathematical Proceedings of the Cambridge Philosophical Society* 118(3), 487--502 (1995), DOI `10.1017/S0305004100073813`. Role: broader operator-space prior art; in particular it proves uniform Kadec-Klee results for Lorentz-Schatten classes with respect to WOT and places the phenomenon in symmetric operator-space geometry.
- B. Simon, ***Trace Ideals and Their Applications***, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society (2005), DOI `10.1090/surv/120`. Role: standard trace-ideal reference for Schatten duality, trace norm, Fredholm determinants, and convergence theorems.

The durable Arithmetic Fidelity content is therefore not a new Kadec-Klee theorem. It is the exact placement of this classical geometry in the AF-106--AF-108 hierarchy and the paired control showing what the scalar spectral summaries fail to certify: **bounded ideal norm preserves category, conserved ideal norm preserves the full ideal object, while trace and even the complete Fredholm-determinant function can remain unchanged despite total failure of operator fidelity.**

## Consequences for Arithmetic Fidelity

AF-106 through AF-109 now give a four-level assembly audit for operator-valued carriers:

\[
\boxed{
\begin{array}{c}
\text{closure in the supplied assembly topology}
\Rightarrow
\text{stagewise admissibility survives},\\[1mm]
\text{family-level compactness when needed}
\Rightarrow
\text{compact operator category survives},\\[1mm]
\text{uniform finite Schatten budget}
\Rightarrow
\mathcal S_p\text{ membership survives},\\[1mm]
\text{WOT + exact finite Schatten-norm conservation}
\Longleftrightarrow
\mathcal S_p\text{-norm fidelity}.
\end{array}}
\tag{35}
\]

This gives a concrete rule for future spectral/operator RH routes. If a finite-stage construction is assembled only weakly, first ask which operator category is closed under that assembly and what family-level resource prevents escape. If the final claim depends on traces, determinants, or other scalar spectral summaries, do not infer that the underlying operator survived merely because those summaries did. The missing gate may be singular-value/resource conservation rather than another scalar identity.

For positive trace-class carriers, AF-108 already identifies trace tightness as a natural way to derive that conservation. Outside positivity, the next useful question is therefore not "which additional determinant should be computed?" but **what intrinsic structural mechanism prevents singular-value mass and singular directions from escaping while the eigenvalue observables remain unchanged?**