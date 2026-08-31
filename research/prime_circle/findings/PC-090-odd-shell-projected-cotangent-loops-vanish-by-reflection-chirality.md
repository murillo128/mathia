# PC-090 — odd shell-projected cotangent loops vanish by reflection chirality

**Status:** `EXACT-DERIVED` + `STRUCTURAL-COLLAPSE` + `DECISIVE-NEGATIVE` for the odd-reflection-parity sector of shell-aware Prime-Circle cotangent words. PC-089 showed that one exact-order intermediate shell between two cotangent propagators collapses to endpoint cyclotomic potentials. The next natural scalar repair is to retain two or more intermediate shells and compose the shell-projected cotangent blocks before taking a cyclic trace or common-anchor return amplitude. On every conjugation-stable roots-of-unity configuration, however, cotangent propagation is reflection-odd while exact-shell projectors are reflection-even. Therefore every such scalar observable of odd total reflection parity vanishes identically.

In particular, the first unweighted higher-memory candidate left open by PC-089 — three cotangent propagators with two intermediate exact-order shells and both endpoints at the common anchor — is exactly zero. The result does **not** kill even-parity shell words, reflection-parity-cancelling geometry-forced weights, non-fixed-endpoint block operators, Hardy higher traces, or the global uniformization/monodromy branch.

## 1. Conjugation gives the cotangent kernel an exact chiral grading

Let `Omega` be any finite subset of the unit circle that is closed under complex conjugation. Include the common anchor `1` when pointed observables are considered. For distinct `z=e^{i theta_z}` and `w=e^{i theta_w}` define

\[
K(z,w)=i\cot\!\left(\frac{\theta_z-\theta_w}{2}\right),
\]

and set `K(z,z)=0`. Let `R` be the permutation involution induced by unit-circle conjugation,

\[
(Rf)(z)=f(\bar z).
\]

Because conjugation sends every angle to its negative modulo `2 pi` and cotangent is odd,

\[
\boxed{K(\bar z,\bar w)=-K(z,w).}
\]

Equivalently, as an operator on functions on `Omega`,

\[
\boxed{RKR=-K.}
\]

Every primitive shell

\[
P_n^*=\{\zeta_n^a:(a,n)=1\}
\]

is conjugation-stable because `a -> -a mod n` preserves coprimality. Hence its exact-shell projector `P_n` commutes with reflection:

\[
\boxed{RP_nR=P_n.}
\]

The common anchor is fixed pointwise,

\[
\boxed{R e_1=e_1.}
\]

This is the multi-shell form of the reflection/chiral symmetry already visible for one primitive cotangent block in PC-045.

## 2. Reflection parity is multiplicative for arbitrary shell words

More generally, let `D_0,...,D_q` be operators on the same finite ambient space that are homogeneous under reflection,

\[
RD_jR=\varepsilon_jD_j,
\qquad \varepsilon_j\in\{+1,-1\}.
\]

Exact-shell projectors have `\varepsilon_j=+1`. Consider a word with `q` cotangent propagators,

\[
W=D_0KD_1K\cdots KD_q.
\]

Repeated use of `RKR=-K` gives the exact grading law

\[
\boxed{
RWR=(-1)^q\left(\prod_{j=0}^q\varepsilon_j\right)W.
}
\]

Let

\[
\eta(W)=(-1)^q\prod_{j=0}^q\varepsilon_j
\]

be its total reflection parity. Since trace is invariant under similarity,

\[
\operatorname{Tr}(W)=\operatorname{Tr}(RWR)=\eta(W)\operatorname{Tr}(W).
\]

Therefore

\[
\boxed{
\eta(W)=-1\quad\Longrightarrow\quad \operatorname{Tr}(W)=0.
}
\]

The same argument is stronger for the pointed geometry. Since `e_1` is fixed by `R`,

\[
\langle e_1,We_1\rangle
=\langle e_1,RWR e_1\rangle
=\eta(W)\langle e_1,We_1\rangle,
\]

so

\[
\boxed{
\eta(W)=-1\quad\Longrightarrow\quad
\langle e_1,We_1\rangle=0.
}
\]

No Fourier decomposition, Abel limit, asymptotic argument, or arithmetic hypothesis is used. The vanishing is a finite-dimensional symmetry identity.

## 3. Every unweighted odd cotangent loop through exact shells is zero

Take conjugation-stable intermediate exact shells `S_1,...,S_{q-1}` and write `P_{S_j}` for their projectors. The common-anchor return amplitude of a `q`-edge cotangent path is

\[
L_q(S_1,\ldots,S_{q-1})
=
\langle e_1,
K P_{S_1}K P_{S_2}\cdots P_{S_{q-1}}K
e_1\rangle.
\]

Equivalently,

\[
L_q
=
\sum_{x_1\in S_1}\cdots\sum_{x_{q-1}\in S_{q-1}}
K(1,x_1)K(x_1,x_2)\cdots K(x_{q-1},1).
\]

All inserted projectors are reflection-even, so

\[
L_q=(-1)^qL_q.
\]

Hence

\[
\boxed{
q\ \text{odd}\quad\Longrightarrow\quad
L_q(S_1,\ldots,S_{q-1})=0.
}
\]

The first case beyond PC-089 is `q=3`:

\[
\boxed{
\langle e_1,KP_rKP_sKe_1\rangle=0
}
\]

for **every** pair of exact primitive shells `P_r^*`,`P_s^*` in a common ambient roots-of-unity configuration. Thus adding a second remembered intermediate shell does not rescue the most direct scalar pointed cotangent loop. The same obstruction kills `q=5,7,...` no matter how many different exact shells are traversed.

The trace version is identical: every cyclic shell-projected word containing an odd number of cotangent factors and only reflection-even shell projectors has zero trace.

## 4. PC-089 endpoint potentials fit the same grading

The selection rule is not a claim that every word with an odd number of cotangent factors vanishes after arbitrary weights are inserted. Geometry-forced insertions can themselves be reflection-odd.

For a conjugation-stable finite set `B`, PC-089 introduced

\[
\sigma_B(z)=\sum_{u\in B}K(z,u).
\]

Conjugation and the bijection `u -> \bar u` on `B` give

\[
\begin{aligned}
\sigma_B(\bar z)
&=\sum_{u\in B}K(\bar z,u)
=\sum_{v\in B}K(\bar z,\bar v)\\
&=-\sum_{v\in B}K(z,v)
=-\sigma_B(z).
\end{aligned}
\]

Thus multiplication by `sigma_B` is reflection-odd. For a primitive shell,

\[
\sigma_r(z)=\varphi(r)-2z\frac{\Phi_r'(z)}{\Phi_r(z)}
\]

has exactly this parity. Consequently an odd number of `K` factors can survive when accompanied by an odd number of reflection-odd insertions: the correct invariant is **total reflection parity**, not path length alone.

This also explains why PC-089's endpoint-potential reduction is compatible with the present obstruction rather than superseded by it.

## 5. Matched controls show that the vanishing is not prime-specific

The proof used only three facts:

1. the point set is closed under conjugation;
2. the cotangent kernel changes sign under simultaneous conjugation of both endpoints;
3. the common anchor `1` is fixed.

None of these facts distinguishes a rational-prime birth shell. They hold for primitive shells of composite order, full regular polygons, unions of divisor shells, and arbitrary matched finite root sets closed under conjugation.

Therefore the entire odd-reflection-parity scalar sector obeys the same vanishing law on prime and non-prime controls:

\[
\boxed{
\text{odd reflection parity}
\Longrightarrow
\text{zero cyclic trace and zero common-anchor return amplitude}.
}
\]

Such observables cannot by themselves be a prime discriminator, and a nonzero numerical signal from an allegedly unweighted odd shell loop would indicate a broken conjugation pairing, a non-intrinsic orientation choice, or an implementation error rather than new arithmetic.

## 6. Novelty and prior-art audit

The underlying symmetry is classical and is **not** a novelty claim. PC-045 already derived the single-shell form

\[
P H_nP^{-1}=-H_n
\]

for reflection on the oriented primitive cotangent block and used it to obtain the paired `lambda <-> -lambda` spectrum. The present result extends that same exact grading through arbitrary exact-shell projectors and turns it into a selection rule for multi-level cyclic and pointed words.

The surrounding cotangent-matrix and cotangent-sum technology is also established prior art. The line's existing `SOURCES.md` records, among others:

- Kurt Girstmair, *Cotangent power sums and character coordinates* (2025), for character coordinates of cyclotomic cotangent data;
- Wiktor Ejsmont and Franz Lehner, *The Trace Method for Cotangent Sums* (2021), for finite self-adjoint cotangent matrices and trace/power-sum methods;
- Matthias Beck, *Dedekind cotangent sums* (2003), for generalized cotangent-sum structure;
- John Lewis and Don Zagier, *Cotangent sums, quantum modular forms, and the generalized Riemann hypothesis* (2019), as a critical boundary showing that different cross-scale cotangent constructions can encode genuine GRH criteria.

No historical novelty is claimed for anticommutation with an involution or for the consequent vanishing of odd traces. The durable Prime-Circle contribution is the exact **research no-go**: the first higher-memory scalar shell repair left open by PC-089, and in fact the whole odd-parity shell-word family, is killed before any zeta mechanism can appear.

## 7. Boundary of the obstruction

This result deliberately leaves several structurally different directions open.

- **Even-parity shell words** such as four-propagator pointed loops are not forced to vanish.
- Reflection-odd geometry-forced weights can cancel the cotangent parity and produce nonzero scalar observables.
- **Non-fixed endpoint blocks** can transform into their reflected partners rather than vanish.
- A genuinely different multioperator tensor need not be homogeneous under this `Z_2` grading.
- The Hardy higher-trace sector of PC-082--PC-086 uses a different analytic operator structure and is not ruled out here.
- Global uniformization/monodromy data are outside this finite cotangent-word argument.

For the accepted preimage-tube/fiber-sector clue, the next viable cotangent repair must therefore live in an **even total reflection-parity sector** or introduce a geometry-forced coupling not reducible to these shell-projected cotangent words. Merely increasing an unweighted pointed path from one intermediate shell to two, four, or any other number that leaves an odd number of propagators cannot work.

## 8. Exact checks

The derivation has several independent finite checks.

1. **Shell closure.** If `(a,n)=1`, then `(-a,n)=1`, so every `P_n^*` is paired exactly by conjugation.
2. **Kernel parity.** Direct substitution into `i cot((theta_z-theta_w)/2)` gives `K(\bar z,\bar w)=-K(z,w)`.
3. **Pointed invariance.** The anchor `1` is fixed by conjugation, so an odd operator cannot have a nonzero anchor diagonal matrix element.
4. **Finite trace.** All spaces are finite; `Tr(RWR)=Tr(W)` is exact and needs no regularization.
5. **Numerical stress controls.** Direct finite sums for three-edge anchored loops on several prime/composite shell pairs, and five-edge loops on several four-shell sequences, vanish to floating-point roundoff. These computations are checks only; the operator proof is exact.

## 9. Consequence

PC-089 left multi-shell relational memory as a plausible escape from the one-intermediate-shell cyclotomic collapse. PC-090 shows that this escape already has a hard parity wall:

\[
\boxed{
\text{conjugation-stable exact shells}
\to
\text{shell-projected cotangent word}
\to
\text{odd total reflection parity}
\to
0.
}
\]

The important surviving question is narrower: whether an **even-parity**, genuinely shell-aware or multioperator observable retains arithmetic information that is not classical cotangent/cyclotomic data and that differs under a matched non-prime control. PC-090 supplies no such positive mechanism and introduces no spectral parameter, functional equation, gamma factor, or critical-line selector.