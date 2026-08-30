# PC-073 — bounded-drift scalar dilation covariance still forbids compact resolvent

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the translation-like non-bijective scalar-covariance frontier left open by PC-071 and PC-072 on the compatible Prime-Circle solenoid.

## Claim

PC-064 identifies the compatible all-level Prime-Circle refinement with the arithmetic solenoid

\[
\Sigma_{\mathbb Q}\cong\widehat{\mathbb Q},
\qquad
L^2(\Sigma_{\mathbb Q})
=\overline{\operatorname{span}}\{\chi_q:q\in\mathbb Q\},
\]

and PC-069--PC-072 study the intrinsic Haar-Koopman power dilation

\[
V_m\chi_q=\chi_{mq},\qquad m\ge2.
\]

PC-071 rules out scalar homeomorphic covariance and PC-072 rules out non-bijective laws whose tails are eventually outward in absolute value. A natural remaining repair is a **translation-like but folding** scalar law: a non-injective `\Phi` with uniformly positive drift, so backward spectral chains escape toward `-\infty` rather than being trapped as in PC-072.

That repair also fails for the actual Prime-Circle dilation representation.

Let `\Phi:\mathbb R\to\mathbb R` be a finite-valued real Borel function. Suppose there are constants

\[
0<\delta\le M<\infty
\]

such that either

\[
\boxed{\delta\le \Phi(x)-x\le M\qquad\text{for every }x\in\mathbb R}
\]

or, with the sign reversed,

\[
\boxed{-M\le \Phi(x)-x\le-\delta\qquad\text{for every }x\in\mathbb R.}
\]

Then there is no self-adjoint compact-resolvent operator `H` on either

\[
L^2_0(\Sigma_{\mathbb Q})=\mathbf1^\perp
\]

or the full `L^2(\Sigma_{\mathbb Q})` satisfying, as an equality of self-adjoint operators,

\[
\boxed{V_m^*HV_m=\Phi(H).}
\]

The mechanism is not the bounded-backward-orbit argument of PC-072. Uniform bounded drift instead creates a **bounded spectral transversal**: every eigenspace of `H` is obtained from the finite-dimensional spectral band `E_H([0,M])` by finitely many powers of `V_m` and `V_m^*`. Hence a finite-dimensional subspace is cyclic for the unitary `V_m`. That forces finite unitary spectral multiplicity, contradicting the exact Prime-Circle decomposition of `V_m` into countably infinitely many bilateral rational-character orbits from PC-070.

Thus even a regular non-injective scalar law that looks like translation plus bounded geometric folding cannot support an ordinary compact-resolvent Hilbert--Pólya operator while preserving the intrinsic two-sided solenoid dilation.

## 1. Spectral projections give the exact predecessor decomposition

Assume

\[
V_m^*HV_m=\Phi(H).
\]

For every Borel set `B\subset\mathbb R`, functional calculus gives

\[
V_m^*E_H(B)V_m
=E_{\Phi(H)}(B)
=E_H(\Phi^{-1}(B)).
\]

For one eigenvalue `y` this becomes

\[
V_m^*E_y(H)V_m
=
\bigoplus_{\substack{x\in\operatorname{Spec}_p(H)\\\Phi(x)=y}}
E_x(H).
\]

Equivalently,

\[
\boxed{
E_y(H)
=
V_m
\left(
\bigoplus_{\Phi(x)=y}E_x(H)
\right)
V_m^*.
}
\]

This identity is stronger than the existence-of-a-predecessor statement used in PC-072. It records every preimage eigenspace and is the correct tool when `\Phi` is non-injective.

Forward transport is also exact at the vector level. If `H\psi=x\psi`, then

\[
H(V_m\psi)=\Phi(x)V_m\psi,
\]

so

\[
V_mE_x(H)\subseteq E_{\Phi(x)}(H).
\]

No continuity, monotonicity or injectivity of `\Phi` is being assumed.

## 2. Uniform positive drift produces a finite spectral transversal

It is enough to prove the positive-drift case

\[
\delta\le\Phi(x)-x\le M.
\]

The negative-drift case follows by replacing `H` by `-H` and `\Phi` by

\[
\Psi(x)=-\Phi(-x),
\]

for which `\delta\le\Psi(x)-x\le M`.

Set

\[
W=\operatorname{Ran}E_H([0,M]).
\]

Because `H` has compact resolvent, `W` is finite-dimensional.

### Negative eigenvalues move forward into `W`

Let `x<0` be an eigenvalue. Its forward orbit satisfies

\[
\Phi^k(x)\ge x+k\delta,
\]

so it eventually becomes nonnegative. Let `N` be the first index with

\[
\Phi^N(x)\ge0.
\]

Then `\Phi^{N-1}(x)<0`, and the upper drift bound gives

\[
0\le\Phi^N(x)
\le\Phi^{N-1}(x)+M
<M.
\]

Thus `\Phi^N(x)\in[0,M]`, and forward spectral transport yields

\[
\boxed{E_x(H)\subseteq V_m^{-N}W.}
\]

So every negative eigenspace is generated from the bounded band by a finite negative power of the dilation.

### Eigenvalues above `M` are recursively generated from `W`

Now let `y>M` be an eigenvalue. Every spectral predecessor `x` with `\Phi(x)=y` satisfies

\[
y-M\le x\le y-\delta.
\]

In particular,

\[
0<x<y.
\]

The interval `[y-M,y-\delta]` is compact, so compact resolvent implies that only finitely many `H`-eigenvalues lie in it. The exact projection identity of Section 1 therefore writes `E_y(H)` as `V_m` applied to a **finite** sum of strictly lower positive eigenspaces.

Apply the same decomposition to every predecessor still above `M`. At each step the spectral value decreases by at least `\delta`, so after finitely many steps every branch reaches `(0,M]`. Consequently

\[
\boxed{
E_y(H)\subseteq
\operatorname{span}\{V_m^kW:0\le k\le N_y\}
}
\]

for some finite `N_y` depending on `y`.

Together with the negative case and the band itself, every eigenspace of `H` lies in the bilateral cyclic span of `W`.

## 3. Compact resolvent therefore forces finite dilation multiplicity

A compact-resolvent self-adjoint operator has a complete orthogonal basis of finite-dimensional eigenspaces. Section 2 shows that every such eigenspace lies in the closed span of the `V_m`-translates of `W`. Therefore

\[
\boxed{
L^2_0(\Sigma_{\mathbb Q})
=
\overline{\operatorname{span}}
\{V_m^kW:k\in\mathbb Z\}
}
\]

in the mean-zero case, and the same statement holds with the full `L^2` when `H` is posed there.

Since `W` is finite-dimensional, this says that `V_m` has a finite set of cyclic generators. Equivalently, its unitary spectral multiplicity is finite, bounded by `\dim W`.

But PC-070 computes the actual Prime-Circle representation exactly. On the nonzero rational characters,

\[
\mathbb Q^\times
=
\bigsqcup_{[q]\in\mathbb Q^\times/m^{\mathbb Z}}
\{m^kq:k\in\mathbb Z\},
\]

and hence

\[
\boxed{
L^2_0(\Sigma_{\mathbb Q})
=
\bigoplus_{[q]\in\mathbb Q^\times/m^{\mathbb Z}}
\overline{\operatorname{span}}
\{\chi_{m^kq}:k\in\mathbb Z\}.
}
\]

Each summand is one bilateral shift, and there are countably infinitely many orbit classes. For example, distinct primes not dividing `m` lie in distinct classes. Thus `V_m` has **countably infinite bilateral-shift multiplicity** on the mean-zero space. Adding the constant character on the full space does not remove that infinite-multiplicity component.

A unitary cannot have both finite and countably infinite spectral multiplicity. Therefore the assumed compact-resolvent `H` cannot exist.

This contradiction is representation-theoretic: bounded drift creates a finite spectral transversal for `H`, while the intrinsic Prime-Circle dilation has no finite transversal in unitary multiplicity.

## 4. This genuinely closes a gap left by PC-071 and PC-072

Consider the explicit continuous law

\[
\boxed{\Phi(x)=x+4+3\sin(2x).}
\]

It satisfies

\[
1\le\Phi(x)-x\le7,
\]

so PC-073 applies with `\delta=1` and `M=7`.

But this law lies outside both preceding no-go theorems.

- It is **not injective**: `\Phi'(x)=1+6\cos(2x)` is negative on nonempty intervals and positive on others, so `\Phi` is not monotone and hence not a homeomorphism. PC-071 does not apply.
- On the negative tail, `\Phi(x)=x+O(1)` with positive drift, so for all sufficiently negative `x` one has `|\Phi(x)|<|x|`. The eventual absolute-outward hypothesis of PC-072 therefore fails.

This is exactly the natural remaining scalar geometry: a translation-like law with bounded nonlinear folding. It is not being excluded by relabeling one of the previous proofs.

The affine choice `\Phi(x)=x+d` is recovered as the special constant-drift case already handled by PC-070. PC-073 shows that the obstruction is stable under arbitrary bounded, possibly discontinuous and non-injective perturbations of that drift, provided the drift keeps one strict sign and stays uniformly away from both zero and infinity.

## 5. The bounded-drift hypothesis has a real boundary

It would be false to conclude that **every** Borel scalar law is incompatible with compact resolvent for a unitary of infinite bilateral multiplicity. An explicit manufactured control shows why the Prime-Circle mandate's arbitrary-spectral-wrapper warning remains essential.

Let

\[
\mathcal K=
\bigoplus_{j\ge1}\ell^2(\mathbb Z),
\qquad
S e_{j,k}=e_{j,k+1},
\]

and put `\alpha_j=2^{-j}`. Define distinct real numbers

\[
\lambda_{j,k}=
\begin{cases}
-j^2-\alpha_j+k,&k<0,\\
+j^2+\alpha_j+k,&k\ge0.
\end{cases}
\]

For every bounded interval only finitely many `\lambda_{j,k}` occur, so the diagonal self-adjoint operator

\[
He_{j,k}=\lambda_{j,k}e_{j,k}
\]

has compact resolvent.

Define a Borel function on its discrete spectrum by

\[
\Phi(\lambda_{j,k})=\lambda_{j,k+1}
\]

and extend `\Phi` arbitrarily, for example by zero, off that spectrum. Then

\[
\boxed{S^*HS=\Phi(H)}
\]

exactly, even though `S` has countably infinite bilateral multiplicity.

The price is visible at the transition `k=-1\to0`:

\[
\lambda_{j,0}-\lambda_{j,-1}
=2j^2+2\alpha_j+1
\longrightarrow\infty.
\]

There is no bounded common spectral transversal and no geometrically regular scalar drift. The function was written **after** choosing the desired discrete spectrum and simply encodes the shift orbit labels. Since the mean-zero Prime-Circle `V_m` is itself a countable direct sum of bilateral shifts, the same artificial wrapper can be transferred to that representation by a unitary identification.

This control proves two things at once:

1. the bounded-drift assumption in PC-073 is doing genuine mathematical work;
2. dropping all regularity and allowing a spectrum-specific Borel `\Phi` does not produce a meaningful RH mechanism—it permits the spectrum to be manufactured first and the covariance law fitted afterward.

## 6. Prior-art and novelty audit

No historical novelty is claimed for the abstract ingredients.

- Borel functional calculus and the spectral-projection identity under unitary conjugacy are standard spectral theory.
- Compact resolvent gives discrete real spectrum, finite-dimensional eigenspaces and finite-rank spectral projections on bounded intervals.
- Finite cyclic generating sets and unitary spectral multiplicity are standard consequences of the spectral theorem; PC-070 already uses the equivalent bilateral-shift multiplicity formulation.
- PC-070 also records the unitary time-operator/additive-covariance literature, including Funakawa--Matsuzawa--Sasaki--Suzuki--Teranishi, and demonstrates that additive covariance itself is classical and can coexist with discrete spectrum for finite-multiplicity shift dynamics.

Targeted searches for compact-resolvent relations of the form `U^*HU=\Phi(H)`, nonlinear/unitary covariance, bounded drift in scalar functional calculus, and finite cyclic multiplicity did not locate this exact arithmetic-solenoid statement. That absence is not a novelty proof and is not used as evidence of historical priority.

The durable contribution is the project-specific frontier closure

\[
\boxed{
\text{Prime-Circle infinite-multiplicity two-sided dilation}
+\text{ uniformly signed bounded scalar drift}
+\text{ ordinary compact resolvent}
\quad\text{are incompatible}.}
\]

The theorem is therefore classified as an exact negative derived from standard functional analysis plus the exact Prime-Circle representation already established in PC-064/PC-070, not as a claim that its abstract lemmas are new.

## 7. Consequence for the RH/operator branch

PC-071 and PC-072 had left open non-bijective laws whose backward chains can escape every compact interval. PC-073 shows that **translation-like escape by itself is not enough**. If the escape occurs through a bounded one-signed drift, compact resolvent forces a finite spectral fundamental region and therefore finite unitary multiplicity, which the compatible Prime-Circle solenoid does not possess.

The regular scalar-functional-calculus frontier is consequently much narrower. A surviving construction would have to use at least one of the following genuinely different ingredients:

- an unbounded-jump or otherwise non-uniform scalar law derived independently from Prime-Circle geometry rather than fitted to a target spectrum;
- operator-valued or matrix covariance instead of `\Phi(H)`;
- a one-sided semigroup/isometry rather than the two-sided solenoid automorphism;
- a semifinite or other spectral framework not requiring ordinary compact resolvent;
- symmetry breaking by the common anchor, old/new decomposition, chord geometry or cross-level couplings before the abstract solenoid quotient;
- nonlinear determinant/transfer data not reducible to scalar functional calculus of one self-adjoint operator;
- or the global primitive-root uniformization/accessory branch of PC-017.

In particular, replacing the additive law `H+dI` by a bounded nonlinear periodic modulation of it does not create a new RH spectral mechanism. The arithmetic representation obstruction survives the folding.

## 8. Exact audit tests

This finding has direct falsifiers.

1. From `V_m^*HV_m=\Phi(H)`, verify
   \[
   V_m^*E_H(B)V_m=E_H(\Phi^{-1}(B))
   \]
   for every Borel `B`.
2. Under `\delta\le\Phi(x)-x\le M`, verify that every negative spectral point enters `[0,M]` under a finite forward iterate.
3. For every `y>M`, verify that each spectral predecessor belongs to `[y-M,y-\delta]`, hence is positive and strictly smaller than `y`.
4. Use compact resolvent to check that each predecessor set in item 3 is finite, and recurse until every branch reaches `(0,M]`.
5. Conclude that `W=E_H([0,M])\mathcal H` is finite-dimensional and that `\overline{\operatorname{span}}\{V_m^kW:k\in\mathbb Z\}` contains every `H`-eigenspace.
6. Compare item 5 with PC-070's decomposition of `V_m` into the countably many orbit blocks `m^\mathbb Zq` and verify the finite-versus-infinite spectral-multiplicity contradiction.
7. Check the control `\Phi(x)=x+4+3\sin(2x)`: it has drift in `[1,7]`, is non-injective, and fails PC-072's absolute-outward condition on the negative tail.
8. Check the manufactured wrapper of Section 5 directly: its diagonal spectrum is locally finite, `S^*HS=\Phi(H)`, and the single transition jump on orbit `j` grows like `2j^2`, so the bounded-drift theorem correctly does not apply.

Any failure of items 1--6 would invalidate the no-go. Items 7--8 test that PC-073 closes a genuine gap without silently claiming an impossible universal theorem for arbitrary scalar wrappers.

## 9. Dependencies and scope

This finding depends on:

- PC-064 for the compatible solenoid `\Sigma_{\mathbb Q}` and rational-character basis;
- PC-069 for the intrinsic two-sided dilation action;
- PC-070 for the exact countably-infinite bilateral-orbit multiplicity and the additive-covariance boundary;
- PC-071 for the homeomorphic scalar-law no-go;
- PC-072 for the eventually outward non-bijective scalar-law no-go.

It does not modify or rely on `prime_flute`, and it does not claim a zeta-zero realization. It is a negative result inside the canonical `prime_circle` scale/refinement/operator program: another broad and geometrically natural scalar attempt to turn intrinsic dilation into a compact-resolvent spectral law is ruled out exactly.